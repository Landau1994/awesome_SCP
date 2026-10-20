#!/usr/bin/env python3
"""Read-only content validation; writes only the requested JSON report.

Run from any directory: python audit/check_vault.py
Requires Python 3.10+ and PyYAML. Exit 0 = no errors, 1 = findings, 2 = setup error.

Scope/heuristics:
* Scan notes/**/*.md, README.md, Home.md and canvas/**/*.canvas. Templates,
  configuration, chats, audit reports and code examples are not content inputs.
  Excluded content can still be a legitimate explicitly linked local file.
* This is a local structural check, NOT scientific fact checking or HTTP probing.
  No network request is made; 403/429/CAPTCHA/unavailable sites are never classified
  as dead links. Source reachability and evidence quality need separate review.
* Markdown parsing is deliberately dependency-light, not a complete CommonMark or
  Obsidian renderer. It masks fenced/inline code, HTML/Obsidian comments and YAML;
  handles inline links (balanced parentheses), reference links, ATX/setext headings,
  duplicate GitHub-style slugs, HTML anchors and Obsidian block IDs. Plugin-generated
  headings, transclusion-generated headings, HTML-only links and exotic syntax are
  outside scope. Indented blocks are masked only outside an active list context.
* Wikilinks prefer exact paths, then exact basenames, then case-insensitive names,
  then unique aliases. An alias-only link is counted separately: Obsidian's alias
  autocomplete normally writes [[canonical filename|alias]], so explicit canonical
  targets remain preferable. Exact-filename compatibility pages take precedence
  over other notes' same aliases and are not called alias ambiguities.
* Anchor matching accepts literal Obsidian headings and GitHub-like slugs. For
  nested Obsidian heading references, the final heading is checked, not ancestry.
  Unicode slug behavior can differ among renderers; warnings need human review.
* Audit coverage is read from audit/*-audit.json, using lists or notes/records/entries
  arrays. Temporary source caches are not final per-note audit records. A recorded
  status does not by itself prove that a note's scientific claims were verified.
* A missing url field is not an empty url field. Existing notes without frontmatter
  or without url are recorded under metadata_gaps for review, not made errors;
  malformed YAML and an explicitly present but empty url remain errors.
* Links to audit/ are skipped by default while reports are being generated. Pass
  --include-audit-links for the final run. No other local missing link is skipped.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import html
import json
import posixpath
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Install it in the Python environment used to run this script.")


class UniqueYamlLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys instead of silently keeping the last value."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise yaml.constructor.ConstructorError(
                "mapping", node.start_mark, f"duplicate key: {key}", key_node.start_mark
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYamlLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def unique_json(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def blank(text):
    return re.sub(r"[^\n]", " ", text)


def mask_code(text, inline=True):
    """Preserve offsets/line numbers while hiding non-content syntax."""
    text = re.sub(r"(?s)<!--.*?-->|%%.*?%%", lambda m: blank(m[0]), text)
    lines, fence, list_context = [], None, False
    for line in text.splitlines(keepends=True):
        probe = re.sub(r"^\s{0,3}(?:>\s?)+", "", line)
        mark = re.match(r"^ {0,3}(`{3,}|~{3,})", probe)
        if fence:
            lines.append(blank(line))
            if mark and mark[1][0] == fence[0] and len(mark[1]) >= fence[1]:
                fence = None
            continue
        if mark:
            fence = (mark[1][0], len(mark[1]))
            lines.append(blank(line))
            continue
        if re.match(r"^ {0,3}(?:[-+*]|\d+[.)])\s", probe):
            list_context = True
        elif probe.strip() and not probe.startswith((" ", "\t")):
            list_context = False
        if not list_context and re.match(r"^(?: {4}|\t)", probe):
            lines.append(blank(line))
        else:
            lines.append(line)
    text = "".join(lines)
    if inline:
        text = re.sub(r"(?<!\\)(`+)(?!`)([\s\S]*?)(?<!`)\1(?!`)", lambda m: blank(m[0]), text)
    return text


def visible_heading(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[\[([^]|]+)\|([^]]+)\]\]", r"\2", text)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(re.sub(r"[*_`~]", "", text)).strip()


def slug(text):
    text = visible_heading(text).lower()
    text = "".join(c for c in text if c in "-_ " or unicodedata.category(c)[0] in "LN" or unicodedata.category(c)[0] == "M")
    return text.replace(" ", "-")


def anchors(body):
    clean = mask_code(body, inline=False)
    headings, slugs, seen = set(), set(), Counter()
    lines = clean.splitlines()
    for i, line in enumerate(lines):
        atx = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        heading = atx[1] if atx else None
        if heading is None and i + 1 < len(lines) and line.strip() and re.match(r"^\s{0,3}(?:=+|-+)\s*$", lines[i + 1]):
            heading = line.strip()
        if heading is not None:
            headings.add(visible_heading(heading).casefold())
            key = slug(heading)
            slugs.add(key if seen[key] == 0 else f"{key}-{seen[key]}")
            seen[key] += 1
    slugs.update(re.findall(r"<(?:a|\w+)\b[^>]*\b(?:id|name)=[\"']([^\"']+)[\"']", clean, re.I))
    blocks = set(re.findall(r"(?:^|\s)\^([A-Za-z0-9-]+)\s*$", clean, re.M))
    return headings, slugs, blocks


def destination(value):
    value = value.strip()
    if value.startswith("<"):
        end = value.find(">")
        return value[1:end] if end >= 0 else value[1:]
    # A quoted trailing title is metadata, not part of the path. Unescaped spaces
    # in local paths are accepted because Obsidian commonly emits/reads them.
    value = re.sub(r"\s+[\"'].*[\"']\s*$", "", value)
    value = re.sub(r"\\([\\()<>\[\] ])", r"\1", value)
    return value.strip()


def markdown_links(text):
    """Yield (offset, destination) for inline and defined reference links."""
    definitions = {}
    def_spans = []
    for m in re.finditer(r"(?m)^ {0,3}\[([^]\n]+)\]:\s*(.*)$", text):
        definitions[" ".join(m[1].split()).casefold()] = destination(m[2])
        def_spans.append(m.span())
        yield m.start(), definitions[" ".join(m[1].split()).casefold()]
    work = text
    for start, end in reversed(def_spans):
        work = work[:start] + blank(work[start:end]) + work[end:]
    occupied = []
    for m in re.finditer(r"(?<!\\)\]\(", work):
        start, i, depth, angle = m.start(), m.end(), 1, False
        begin = i
        while i < len(work) and depth:
            char = work[i]
            if char == "\\":
                i += 2
                continue
            if char == "<" and i == begin:
                angle = True
            elif char == ">" and angle:
                angle = False
            elif not angle and char == "(":
                depth += 1
            elif not angle and char == ")":
                depth -= 1
            i += 1
        if depth == 0:
            occupied.append((start, i))
            yield start, destination(work[begin:i - 1])
    for m in re.finditer(r"(?<![\\\[])\[([^]\n]+)\](?:\[([^]\n]*)\])?", work):
        if m.end() < len(work) and work[m.end()] == "(":
            continue
        if any(a <= m.start() < b for a, b in occupied):
            continue
        key = " ".join((m[2] or m[1]).split()).casefold()
        # Undefined explicit reference links are diagnosed, but free-standing
        # bracketed prose/citations are not presumed to be shortcut links.
        if key in definitions:
            continue  # Destination was already checked at its definition.
        if m[2] is not None:
            yield m.start(), "__UNDEFINED_REFERENCE__:" + key


class Validator:
    def __init__(self, root, include_audit=False):
        self.root, self.include_audit = root, include_audit
        self.issues, self.stats = [], Counter()
        self.texts, self.frontmatter, self.anchor_cache = {}, {}, {}
        self.paths, self.folded, self.basenames, self.folded_basenames = {}, defaultdict(list), defaultdict(list), defaultdict(list)
        self.aliases = defaultdict(set)
        self.alias_locations = defaultdict(list)
        self.shadowed_aliases = []
        self.alias_only_links, self.metadata_gaps = [], []
        self.stats.update(empty_url_fields=0, missing_url_fields=0, notes_without_frontmatter=0)
        self.note_paths = sorted(p.relative_to(root).as_posix() for p in (root / "notes").rglob("*.md"))
        self.markdown_paths = self.note_paths + [p for p in ("README.md", "Home.md") if (root / p).is_file()]
        self.canvas_paths = sorted(p.relative_to(root).as_posix() for p in (root / "canvas").rglob("*.canvas"))
        for p in root.rglob("*"):
            rel = p.relative_to(root)
            if not p.is_file() or any(x.startswith(".") for x in rel.parts) or rel.parts[0] in ("copilot", "__pycache__"):
                continue
            key = rel.as_posix()
            self.paths[key] = p
            self.folded[key.casefold()].append(key)
            if p.suffix.lower() in (".md", ".canvas", ".base"):
                for name in {p.name, p.stem}:
                    self.basenames[name].append(key)
                    self.folded_basenames[name.casefold()].append(key)

    def issue(self, kind, source, message, severity="error", line=None, **extra):
        row = {"kind": kind, "severity": severity, "source": source, "message": message}
        if line is not None:
            row["line"] = line
        row.update(extra)
        self.issues.append(row)

    def read(self, path):
        if path not in self.texts:
            try:
                self.texts[path] = (self.root / path).read_text(encoding="utf-8-sig")
            except (OSError, UnicodeError) as exc:
                self.issue("read_error", path, str(exc))
                self.texts[path] = ""
        return self.texts[path]

    def load_markdown(self, path, audit_content=True):
        text = self.read(path)
        if path in self.frontmatter:
            return self.frontmatter[path]
        body, metadata = text, {}
        match = re.match(r"\A---\s*\n([\s\S]*?)\n(?:---|\.\.\.)\s*(?:\n|$)", text)
        if match:
            body = blank(match[0]) + text[match.end():]
            try:
                metadata = yaml.load(match[1], Loader=UniqueYamlLoader) or {}
                if not isinstance(metadata, dict):
                    raise ValueError("Frontmatter must be a mapping")
            except (yaml.YAMLError, ValueError, TypeError) as exc:
                if audit_content:
                    self.issue("yaml_parse", path, str(exc), line=1)
                metadata = {}
        elif audit_content and path.startswith("notes/"):
            if re.match(r"\A---\s*\n", text):
                self.issue("yaml_parse", path, "Frontmatter opening delimiter has no closing delimiter.", line=1)
            else:
                self.stats["notes_without_frontmatter"] += 1
                self.metadata_gaps.append({"path": path, "kind": "frontmatter_absent", "note": "Existing Markdown without frontmatter is permitted; body sources and audit coverage are checked separately."})
        if audit_content and path.startswith("notes/"):
            if not text.strip():
                self.issue("empty_note", path, "Note is empty.", line=1)
            if "url" not in metadata:
                self.stats["missing_url_fields"] += 1
                self.metadata_gaps.append({"path": path, "kind": "url_field_absent", "note": "No frontmatter url field; this is distinct from an explicitly blank URL."})
            elif not str(metadata["url"] or "").strip():
                self.stats["empty_url_fields"] += 1
                self.issue("empty_url", path, "Frontmatter url field is explicitly blank.", line=1)
            elif not isinstance(metadata["url"], str):
                self.issue("url_type", path, "Frontmatter url must be a string.", line=1)
            aliases = metadata.get("aliases", []) or []
            if isinstance(aliases, str):
                aliases = [aliases]
            if not isinstance(aliases, list) or any(not isinstance(a, str) for a in aliases):
                self.issue("aliases_type", path, "Aliases must be a string or list of strings.", line=1)
            else:
                for alias in set(aliases):
                    if alias.strip():
                        self.aliases[alias.casefold()].add(path)
                        self.alias_locations[alias.casefold()].append({"path": path, "alias": alias})
        self.frontmatter[path] = (metadata, body)
        return metadata, body

    def choose(self, candidates, source, target, line, kind, exact=True):
        candidates = sorted(set(candidates))
        if not candidates:
            return None
        if len(candidates) > 1:
            self.issue("ambiguous_" + kind, source, "More than one local target matches.", line=line, target=target, candidates=candidates)
            return False
        if not exact:
            self.issue("case_mismatch", source, "Target resolves only with case-insensitive matching.", "warning", line, target=target, resolved=candidates[0])
        return candidates[0]

    def resolve(self, source, target, line, wiki=False, canvas=False):
        target = unquote(target).replace("\\", "/")
        if re.match(r"^[A-Za-z]:/", target):
            self.issue("outside_vault", source, "Absolute filesystem target is outside this vault-relative check.", "warning", line, target=target)
            return None
        if not self.include_audit and (target.startswith("audit/") or "/audit/" in target or target.startswith("../audit/")):
            self.stats["audit_links_skipped"] += 1
            return None
        source_dir = posixpath.dirname(source)
        options = [target.lstrip("/") if target.startswith("/") or canvas else posixpath.normpath(posixpath.join(source_dir, target))]
        if wiki:
            options = [target.lstrip("/"), *options]
            if not target.lower().endswith((".md", ".canvas", ".base")):
                options += [p + ".md" for p in list(options)]
        options = list(dict.fromkeys(options))
        options = [p for p in options if not (p == ".." or p.startswith("../") or re.match(r"^[A-Za-z]:/", p))]
        if not options:
            self.issue("outside_vault", source, "Local target leaves the vault root; not checked.", "warning", line, target=target)
            return None
        # A literal path is preferred before an Obsidian shortest-path/basename.
        exact = [p for p in options if p in self.paths]
        if exact:
            return self.choose(exact[:1], source, target, line, "path")
        if wiki and "/" not in target:
            result = self.choose(self.basenames.get(target, []), source, target, line, "basename")
            if result is not None:
                return result
        if wiki and "/" in target:
            suffix = [p for p in self.paths if any(p.endswith("/" + opt) for opt in options)]
            result = self.choose(suffix, source, target, line, "path")
            if result is not None:
                return result
        folded = [p for opt in options for p in self.folded.get(opt.casefold(), [])]
        if not folded and wiki and "/" not in target:
            folded = self.folded_basenames.get(target.casefold(), [])
        if not folded and wiki and "/" in target:
            folded = [p for p in self.paths if any(p.casefold().endswith("/" + opt.casefold()) for opt in options)]
        result = self.choose(folded, source, target, line, "path", exact=False)
        if result is not None:
            return result
        if wiki and "/" not in target:
            result = self.choose(self.aliases.get(target.casefold(), []), source, target, line, "alias")
            if result:
                self.stats["wikilinks_resolved_by_alias_only"] += 1
                self.alias_only_links.append({"source": source, "line": line, "target": target, "resolved": result})
            if result is not None:
                return result
        self.issue("missing_" + ("canvas_file" if canvas else "wikilink" if wiki else "markdown_target"), source, "Local target does not exist.", line=line, target=target)
        return None

    def check_anchor(self, target, fragment, source, line, wiki=False):
        if not target or not fragment or not target.lower().endswith(".md"):
            return
        self.stats["anchors_checked"] += 1
        if target not in self.anchor_cache:
            self.anchor_cache[target] = anchors(self.load_markdown(target, audit_content=False)[1])
        headings, slugs, blocks = self.anchor_cache[target]
        fragment = unquote(fragment).strip()
        if fragment.startswith("^"):
            exists = fragment[1:] in blocks
        else:
            last = fragment.rsplit("#", 1)[-1] if wiki else fragment
            exists = last in slugs or visible_heading(last).casefold() in headings
        if not exists:
            self.issue("missing_anchor", source, "Local heading or block anchor was not found.", "warning", line, target=target, fragment=fragment)

    def scan_text(self, source, body, node=None):
        first_issue = len(self.issues)
        text = mask_code(body)
        for match in re.finditer(r"(?<!\\)!?\[\[([^]\n]*)\]\]", text):
            raw = match[1].replace("\\|", "|")
            target_fragment = raw.split("|", 1)[0].strip()
            target, _, fragment = target_fragment.partition("#")
            line = text[:match.start()].count("\n") + 1
            self.stats["wikilinks_checked"] += 1
            if not target and not fragment:
                self.issue("empty_wikilink", source, "Wikilink has no target or anchor.", line=line, node=node)
                continue
            resolved = self.resolve(source, target, line, wiki=True) if target else source
            self.check_anchor(resolved, fragment, source, line, wiki=True)
        # Prevent wikilink display portions from being interpreted as Markdown.
        text = re.sub(r"!?\[\[[^]\n]*\]\]", lambda m: blank(m[0]), text)
        for offset, value in markdown_links(text):
            line = text[:offset].count("\n") + 1
            if value.startswith("__UNDEFINED_REFERENCE__:"):
                self.issue("undefined_markdown_reference", source, "Reference link has no definition.", "warning", line, target=value.split(":", 1)[1], node=node)
                continue
            if not value:
                self.issue("empty_markdown_link", source, "Markdown link has an empty destination.", line=line, node=node)
                continue
            # Any URI scheme/protocol-relative destination is external to this
            # local checker. A Windows drive is handled by resolve instead.
            if (re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", value) and not re.match(r"^[A-Za-z]:[/\\]", value)) or value.startswith("//"):
                self.stats["external_links_not_probed"] += 1
                continue
            target, _, fragment = value.partition("#")
            target = target.split("?", 1)[0]
            self.stats["markdown_local_links_checked"] += 1
            resolved = self.resolve(source, target, line) if target else source
            self.check_anchor(resolved, fragment, source, line)
        if node is not None:
            for row in self.issues[first_issue:]:
                row["node"] = node
                row["line_context"] = "canvas node text, not JSON source line"

    def scan_canvas(self, path):
        try:
            data = json.loads(self.read(path), object_pairs_hook=unique_json)
        except (ValueError, TypeError) as exc:
            self.issue("canvas_json", path, str(exc))
            return
        if not isinstance(data, dict) or not isinstance(data.get("nodes"), list) or not isinstance(data.get("edges"), list):
            self.issue("canvas_schema", path, "Canvas requires nodes and edges arrays.")
            return
        ids = Counter()
        for node in data["nodes"]:
            if not isinstance(node, dict) or not isinstance(node.get("id"), str):
                self.issue("canvas_node_schema", path, "Node must be an object with a string id.")
                continue
            ids[node["id"]] += 1
            kind = node.get("type")
            if kind not in ("text", "file", "link", "group"):
                self.issue("canvas_node_type", path, "Unknown canvas node type.", node=node["id"], value=kind)
            if kind == "file":
                self.stats["canvas_file_links_checked"] += 1
                value = node.get("file")
                if not isinstance(value, str) or not value.strip():
                    self.issue("canvas_empty_file", path, "File node has no target.", node=node["id"])
                else:
                    first_issue = len(self.issues)
                    resolved = self.resolve(path, value, None, canvas=True)
                    self.check_anchor(resolved, str(node.get("subpath", "")).lstrip("#"), path, None, wiki=True)
                    for row in self.issues[first_issue:]:
                        row["node"] = node["id"]
            if kind == "text" and isinstance(node.get("text"), str):
                self.scan_text(path, node["text"], node=node["id"])
        for node_id, count in ids.items():
            if count > 1:
                self.issue("canvas_duplicate_node_id", path, "Node id is duplicated.", node=node_id)
        edge_ids = Counter()
        for edge in data["edges"]:
            if not isinstance(edge, dict) or not isinstance(edge.get("id"), str):
                self.issue("canvas_edge_schema", path, "Edge must be an object with a string id.")
                continue
            edge_ids[edge["id"]] += 1
            for field in ("fromNode", "toNode"):
                if edge.get(field) not in ids:
                    self.issue("canvas_edge_missing_node", path, "Edge endpoint does not reference an existing node.", edge=edge["id"], field=field, target=edge.get(field))
        for edge_id, count in edge_ids.items():
            if count > 1:
                self.issue("canvas_duplicate_edge_id", path, "Edge id is duplicated.", edge=edge_id)

    def scan_aliases(self):
        for key, paths in sorted(self.aliases.items()):
            if len(paths) <= 1:
                continue
            names = sorted(set(self.folded_basenames.get(key, [])))
            if len(names) == 1:
                self.shadowed_aliases.append({"alias_key": key, "preferred_filename": names[0], "alias_owners": sorted(paths)})
            else:
                self.issue("ambiguous_alias", "notes/", "Alias is shared and has no unique filename taking precedence.", "warning", alias_key=key, candidates=sorted(paths), spelling=self.alias_locations[key])
        # Case-colliding filenames are portability hazards even when links use
        # distinct exact spellings; report each stem group once.
        for key, paths in sorted(self.folded_basenames.items()):
            paths = sorted(set(paths))
            if len(paths) > 1 and not key.endswith((".md", ".canvas", ".base")):
                self.issue("duplicate_basename", "notes/", "Multiple local files share a case-insensitive basename.", "warning", basename=key, candidates=paths)

    def audit_coverage(self):
        coverage, statuses, report_files = defaultdict(list), Counter(), []
        note_statuses, extra_statuses = Counter(), Counter()
        for file in sorted((self.root / "audit").glob("*-audit.json")):
            path = file.relative_to(self.root).as_posix()
            report_files.append(path)
            try:
                data = json.loads(file.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_json)
            except (OSError, ValueError) as exc:
                self.issue("audit_json", path, str(exc))
                continue
            if isinstance(data, list):
                records = data
            elif isinstance(data, dict):
                records = next((data[k] for k in ("notes", "records", "entries") if isinstance(data.get(k), list)), None)
            else:
                records = None
            if records is None:
                self.issue("audit_report_pending", path, "No final per-note audit array; this may still be a source cache.", "warning")
                continue
            for i, row in enumerate(records):
                if not isinstance(row, dict) or not isinstance(row.get("path"), str):
                    self.issue("audit_record_schema", path, "Audit record requires a string path.", record=i)
                    continue
                target = row["path"].replace("\\", "/")
                coverage[target].append(path)
                statuses[str(row.get("status", "missing"))] += 1
                target_statuses = note_statuses if target in self.note_paths else extra_statuses
                target_statuses[str(row.get("status", "missing"))] += 1
                missing = [k for k in ("status", "checked", "changes", "sources", "unresolved") if k not in row]
                if missing:
                    self.issue("audit_record_schema", path, "Audit record is missing required fields.", target=target, missing=missing)
                if row.get("status") not in ("verified", "partial", "unverified", "compatibility"):
                    self.issue("audit_status", path, "Unsupported audit status.", target=target, value=row.get("status"))
                if target not in self.paths:
                    self.issue("audit_stale_path", path, "Audit record points to a nonexistent file.", target=target)
        for path in self.note_paths:
            if path not in coverage:
                self.issue("audit_missing_coverage", path, "No final audit record covers this note.")
            elif len(coverage[path]) > 1:
                self.issue("audit_duplicate_coverage", path, "More than one audit record covers this note.", "warning", reports=coverage[path])
        return {
            "reports": report_files,
            "covered_notes": sum(p in coverage for p in self.note_paths),
            "total_notes": len(self.note_paths),
            "record_status_counts": dict(statuses),
            "note_status_counts": dict(note_statuses),
            "index_and_canvas_status_counts": dict(extra_statuses),
        }

    def run(self):
        for path in self.markdown_paths:
            self.load_markdown(path)
        self.scan_aliases()
        for path in self.markdown_paths:
            self.scan_text(path, self.frontmatter[path][1])
        for path in self.canvas_paths:
            self.scan_canvas(path)
        coverage = self.audit_coverage()
        self.issues.sort(key=lambda x: (x["source"], x.get("line") or 0, x["kind"]))
        severity = Counter(i["severity"] for i in self.issues)
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "root": str(self.root),
            "scope": {"note_count": len(self.note_paths), "markdown_count": len(self.markdown_paths), "canvas_count": len(self.canvas_paths), "audit_links_included": self.include_audit, "network_requests": 0},
            "summary": {"errors": severity["error"], "warnings": severity["warning"], "issue_counts": dict(Counter(i["kind"] for i in self.issues)), **dict(self.stats)},
            "audit_coverage": coverage,
            "filename_precedence_aliases": self.shadowed_aliases,
            "alias_only_links": self.alias_only_links,
            "metadata_gaps": self.metadata_gaps,
            "issues": self.issues,
            "limitations": ["Local structural validation only; external URLs were not probed.", "Markdown/Obsidian anchor parsing is heuristic; see the script docstring.", "Audit status is reported as supplied, not independently certified by this script."]
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Defaults to ROOT/audit/validation.json")
    parser.add_argument("--include-audit-links", action="store_true")
    parser.add_argument("--strict", action="store_true", help="Return exit 1 for warnings as well as errors")
    args = parser.parse_args()
    root = args.root.resolve()
    if not (root / "notes").is_dir():
        parser.error("--root must identify the vault containing notes/")
    output = args.output or root / "audit" / "validation.json"
    report = Validator(root, args.include_audit_links).run()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps({"report": str(output), "scope": report["scope"], "summary": report["summary"], "audit_coverage": report["audit_coverage"]}, ensure_ascii=False, indent=2))
    return int(bool(report["summary"]["errors"] or (args.strict and report["summary"]["warnings"])))


if __name__ == "__main__":
    raise SystemExit(main())
