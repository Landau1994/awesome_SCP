# Knowledge Base Link Completion and Core Fact-Checking Report

Audit cutoff: **2026-10-20**. Revisions were made directly in the existing knowledge base. No changes were committed, pushed or published to GitHub.

## Coverage and Completion

The register includes **341 existing notes** and **28 new notes**, for a total of **369 notes**. README, Home and three canvases were also checked. Per-file audit records cover **369/369 notes (100%)**. This means that every note was inspected and recorded; it does not mean that every statement has been substantiated.

| Category | Existing | New | Audit records |
|---|---:|---:|---:|
| Concepts | 90 | 0 | 90 |
| Methods | 78 | 8 | 86 |
| Tools | 116 | 20 | 136 |
| Literature | 44 | 0 | 44 |
| Reviews | 2 | 0 | 2 |
| Databases | 7 | 0 | 7 |
| Applications | 3 | 0 | 3 |
| Researcher index | 1 | 0 | 1 |
| Total | 341 | 28 | 369 |

- **Verified within the recorded core scope: 195 notes**.
- **Partially verified: 153 notes**.
- **Compatibility pages checked: 19 notes**.
- **Insufficient evidence for identity or core claims: 2 notes**.

"Verified within the recorded core scope" covers only the definitions, bibliographic details or conclusions specified in the record. "Partially verified" retains explicit limitations concerning full-text details, versions, performance or experimental conditions. Bibliographic metadata and public abstracts were checked for the literature and review notes; checking a public abstract was not represented as a sentence-by-sentence review of the full text. Software packages were not individually installed and run, and experiments or training results were not reproduced.

Per-note entry point: [Audit register](note-register.md). Complete records are divided into [concepts, databases, applications and indexes](root-audit.json), [methods](methods-audit.json), [tools](tools-audit.json), and [literature and reviews](literature-audit.json). The [file inventory](file-inventory.json) identifies existing and new notes, current URLs and audit-record paths.

## Links and Structure

- All **117 blank `url` fields** identified in the initial inspection have been addressed. No blank `url` fields remain in the notes.
- The **29 missing internal target names** identified initially were resolved by adding **28 entity notes**. Two CRISPRa names refer to the same note, and references now use an explicit target.
- `g:Profiler` uses the Windows-compatible filename `gProfiler.md`; the page title and display text retain `g:Profiler`.
- The previously empty **MsImpute.md** was rebuilt with the package's purpose, missingness assumptions, input format, sources and related notes.
- **10 filenames** were corrected, including the 2022 year for AlphaPeptDeep, the 2025 year for OpenSpec, the 2026 year for Proteoform medicine, and clear spelling or truncation errors. Previous names were retained as aliases. See [renames.json](renames.json) for the mapping.
- Compatibility pages and short notes were retained. Template, empty and ambiguous aliases were cleaned up, and internal links and canvas paths were updated. See [structural-changes.json](structural-changes.json) for the operation log.
- **hEF** and **Leading Scientists** have no `url` field. The former cannot be uniquely identified and is explicitly left unresolved; the latter retains its original index format, with reliable sources in the body. Neither is a remaining blank URL field.

Templates, chat histories, application settings and code examples unrelated to fact-checking were outside the content-revision scope. Necessary corrections were made to canvas content that directly affected references or interpretation, including incorrect software-installation targets and statistical labels.

## Main Content Corrections

| Issue | Revision and evidence |
|---|---|
| PepPre described as a routine preprocessing or imputation tool | Corrected to a tool for precursor detection, scoring and ranking in mass spectra; it supports downstream peptide identification through isotopic-cluster decomposition. [Official description](https://peppre.ctarn.io/) |
| MassNet raw and processed data volumes conflated | Distinguished approximately 30 TB of raw DDA data from the 4.45 TB processed corpus. The 82% figure is the average run-level reduction in MSDT file size relative to the combined spectra and search-result files. Performance gains are limited to the relevant benchmarks, and cross-dataset transfer limitations were added. [Original paper](https://www.nature.com/articles/s41592-026-03247-y) |
| Incorrect aPCA expansion, Gps1 species context and central-dogma definition | Corrected aPCA to abundance protein-fragment complementation assay; restored Gps1 to the mouse COP9-subunit context; distinguished sequence-information transfer from quantitative RNA–protein relationships in the central-dogma note. [aPCA source](https://www.nature.com/articles/s41586-024-08370-4), [central dogma](https://doi.org/10.1038/227561a0) |
| nDIA/Chip-Tip conditions and single-cell performance conflated | Distinguished the 2024 bulk nDIA study from the 2025 Chip-Tip study. The 5,204-protein figure is the median number identified per single cell in the reported HeLa benchmark using Orbitrap Astral at 40 samples per day; it is not a general capability claim. [Chip-Tip](https://doi.org/10.1038/s41592-024-02558-2) |
| Generalized performance claims for nanoPOTS, plexDIA and nPOP | Distinguished small cell pools from single cells; limited the approximately 98% completeness claim for plexDIA to the same multiplexed set; clarified that nPOP depth depends on the accompanying acquisition and analysis workflow. Relevant primary sources were added to the method notes. |
| Confused descriptions of pSCoPE, REAP-seq, Spatial CITE-seq, DVP/scDVP and related methods | Corrected purposes, original references and conditions of use. pSCoPE is no longer presented as a validation method covering only a small panel, and results from multiple sectioned cells are no longer presented as measurements of an intact single cell. |
| Mismatched references for SPDB, SingPro and CPTAC | Corrected SPDB to 10.1093/nar/gkad1018, SingPro to 10.1093/nar/gkad830, and the historical CPTAC portal paper to 10.1021/pr501254j. Database statistics now specify the date and the inclusion of multiple measurement technologies; unsupported comparative rankings were removed. |
| Confused attribution among MSKCC, cBioPortal, TCGA and CPTAC | Distinguished institutions, assays, platforms and programs. The 18,227 samples in a multi-source training corpus are no longer attributed entirely to TCGA. PDC is the primary access point following retirement of the historical CPTAC portal. |
| Template errors in software references, installation instructions and platform support | Corrected references for cTP-net, sciPENN, DO-MS and other tools. SCeptre now points to the official bfurtwa repository, and instructions to install the unrelated PyPI package of the same name were removed. SCPDA was moved to the Python category, and AlphaPept was corrected to an identification and quantification framework. |
| Unsupported template parameters and incorrect hardware inputs/outputs | Removed 51 unsupported template parameter tables and 47 installation/usage templates without substantive instructions from the tool notes. Hardware inputs are no longer described as raw software files, and enrichment-tool inputs are no longer described as spectra. Qualifications concerning version-dependent capabilities were retained. |
| Absolute comparisons in reviews | Removed claims that single-cell MS has no Poisson noise, DIA detects all ions, and all clinical assays require absolute quantification. Depth, cellular protein mass and clinical advantages are qualified by the relevant experiment and application. [Primary study of ion-sampling quantification](https://doi.org/10.1038/s41467-021-23667-y) |
| Overgeneralized inferences in application notes | Clarified that 3,042 proteins is the total across the 1,490-cell SCoPE2 matrix. Pseudotime is not longitudinal tracking, and abundance does not automatically establish activity. Claims of universally detecting rare cells below 1% abundance and of demonstrated diagnostic superiority were removed. |
| Publication years, preprints and indexes | Distinguished online-publication years, volume years and preprint versions. Separate pages for preprints and published articles were retained. The 2024 scp-workflow reference in README was corrected to a Methods in Molecular Biology book chapter. |

These corrections were propagated to repeated statements in the relevant notes, README, Home or canvases. The per-note records define the precise scope of each change.

## Key Unresolved Items

| Item | Missing evidence or limitation |
|---|---|
| [hEF](../notes/concepts/hEF.md) | The abbreviation, cell identity and original source cannot be uniquely confirmed. No URL was guessed, and hEF was not equated with hFF. |
| [ORBIT](../notes/tools/ORBIT.md) | Only the brain-development study context is retained. A standalone implementation, official repository and platform remain unconfirmed. |
| [MetaMorpheus-TC](../notes/tools/MetaMorpheus-TC.md) | The name appears in a review, but a dedicated release or standalone implementation remains unconfirmed. |
| [PSEA-Quant](../notes/tools/PSEA-quant.md) | The original paper and function were confirmed; the current availability of the historical Web/Java service was not. |
| [hi12](../notes/concepts/hi12.md) | The 2021 and 2025 sources report different cell-bank identifiers for the parental hFF cells. They were not assumed to refer to the same cell stock. |
| AST/GSC/MAC/MIC | Cell-population meanings were specified according to the associated SoftHybrid study, but the complete original sample table remains to be checked. |
| Exact numerical and mechanistic claims in some literature notes | Cell counts, classification accuracies, performance multiples, figures/tables and specific mechanisms not substantiated by public abstracts are listed as unresolved in the per-note records. Verification-scope statements were added to the relevant notes. |
| Software and method version details | Some release dependencies, instrument support, parameter syntax and performance extrapolations remain only partially verified. Source-page accessibility must not be equated with empirical testing. |

## External-Link Access

See [external-links.json](external-links.json) for batch access results, redirects, response status, source files and retry history. HTTP success means only that a response was received, not that the cited content is correct. Access denials, timeouts, TLS errors and candidate 404s are recorded separately.

The scan covered **454 unique external URLs in 374 files**. Final statuses are listed below. Earlier successful-access records came from [root-source-access.json](root-source-access.json); they were not misrepresented as newly obtained HTTP 200 responses in this pass.

| Status | Count |
|---|---:|
| Response obtained in this pass | 340 |
| 403 access denied | 37 |
| Reused successful-access record from earlier in this audit | 49 |
| 429 rate limit | 13 |
| Verification/blocking page, including 2xx responses | 12 |
| Server error | 1 |
| TLS connection error | 2 |

Links returning 404 on both requests: **0**. URLs, source files and specific statuses were retained for restricted or temporarily unsuccessful requests; these outcomes do not establish that a link is broken.

Link-identity and content checks prioritized developer documentation, official repositories, product pages, Crossref records, public PubMed abstracts and original papers. Accessibility and content accuracy are recorded separately. For example, the old SPDB/SingPro DOIs resolved successfully but were still corrected because they cited the wrong works.

## Validation and Workspace Preservation

Final structural results are in [validation.json](validation.json), with the checker in [check_vault.py](check_vault.py). Checks cover YAML/JSON parsing, internal targets, relative Markdown links, heading/block anchors, aliases, 24 canvas file references, and canvas nodes/edges. The final structural check reported 0 errors and 0 warnings. An additional check of 83 tables and 64 code blocks found no column-count or closure problems, and the Git diff whitespace check passed. Structural checks do not replace page-by-page rendering in Obsidian or establish scientific validity.

The file-inventory comparison confirmed that all 311 originally tracked notes and 30 originally untracked notes correspond to current files. Apart from 10 mapped renames, no originally tracked note is missing without explanation. No broad staging, reversion or cleanup of user files was performed, and the staging area is empty. Out-of-scope Git differences still include the pre-existing change to `.obsidian/graph.json`; that configuration was not edited during this audit.

**Limitation of the preservation check:** The initial complete workspace snapshot was stored in a session temporary directory and became inaccessible after an execution-environment change. A complete byte-for-byte or hash comparison against the initial dirty workspace therefore cannot be claimed. The current checks use the file inventory, Git diff, modification scope and rename mapping. The original per-page states of 5 initially blank URLs among the pre-existing untracked tool notes could not be fully recovered and were not inferred from current content. See [workspace-preservation.json](workspace-preservation.json).

This report retains that limitation alongside gaps in scientific evidence. Claims lacking sufficient evidence have not been presented as confirmed facts.
