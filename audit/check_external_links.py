"""Read-only accessibility audit of public external links; no note edits."""
from __future__ import annotations
import argparse
import collections
import concurrent.futures
import datetime
import html
import ipaddress
import json
import os
import pathlib
import re
import socket
import ssl
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'audit/external-links.json'
TIMEOUT = 15
MAX_READ = 16384
WORKERS = 16
HOST_GAP = 0.4
CHECK_DATE = datetime.datetime.now().astimezone().date().isoformat()
OPENER = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl.create_default_context()))

def write_report(value):
    temporary = OUT.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.replace(temporary,OUT)

def markdown_lines(text):
    """Skip fenced/indented code and inline code; preserve source line numbers."""
    fence = None
    for n, line in enumerate(text.splitlines(), 1):
        f = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if f:
            marker = f.group(1)[0]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        indented_code = (line.startswith('    ') or line.startswith('\t')) and not re.match(r'^\s+(?:[-*+]\s|\d+[.)]\s|>)', line)
        if fence or indented_code:
            continue
        line = re.sub(r'`+[^`]*`+', '', line)
        yield n, line

def clean_url(raw):
    raw = html.unescape(raw.strip())
    depth = 0
    for j, char in enumerate(raw):
        if char == '(':
            depth += 1
        elif char == ')':
            if depth == 0:
                raw = raw[:j]
                break
            depth -= 1
    raw = raw.rstrip('.,;:!?。；，、*_')
    while raw.endswith(')') and raw.count(')') > raw.count('('):
        raw = raw[:-1]
    raw = raw.rstrip('}）')
    parts = urllib.parse.urlsplit(raw)
    host = (parts.hostname or '').lower()
    if parts.scheme not in ('http','https') or not host:
        return None, 'malformed'
    if parts.username or parts.password:
        return None, 'credentials_or_secret'
    sensitive = {'token','access_token','api_key','apikey','password','secret','signature','sig'}
    if sensitive.intersection(k.lower() for k,v in urllib.parse.parse_qsl(parts.query)):
        return None, 'credentials_or_secret'
    if host in {'example.com','example.org','example.net','localhost'} or any(host.endswith('.'+h) for h in ('example.com','example.org','example.net','example','localhost')):
        return None, 'example_or_local'
    try:
        if not ipaddress.ip_address(host).is_global:
            return None, 'example_or_local'
    except ValueError:
        pass
    if any(c in raw for c in ('{','}','<','>')):
        return None, 'placeholder'
    # Fragment anchors are not sent in HTTP requests; one network check covers all.
    parts = parts._replace(scheme=parts.scheme.lower(), netloc=parts.netloc.lower(), fragment='')
    return urllib.parse.urlunsplit(parts), None

def inventory():
    files = sorted((ROOT/'notes').rglob('*.md')) + [ROOT/'README.md', ROOT/'Home.md'] + sorted((ROOT/'canvas').glob('*.canvas'))
    refs = collections.defaultdict(list)
    excluded = []
    pattern = re.compile(r'https?://[^\s<>"\]\x60]+')
    for p in files:
        if not p.is_file():
            continue
        source = p.relative_to(ROOT).as_posix()
        content = p.read_text(encoding='utf-8-sig')
        if p.suffix == '.canvas':
            obj = json.loads(content)
            segments = []
            for node in obj.get('nodes',[]):
                for key in ('text','url'):
                    if isinstance(node.get(key),str):
                        segments.extend((f'node:{node.get("id")}/{key}:{line}',text) for line,text in markdown_lines(node[key]))
        else:
            segments = markdown_lines(content)
        for location, line in segments:
            for m in pattern.finditer(line):
                raw = m.group(0).rstrip("'")
                url, reason = clean_url(raw)
                ref = {'file':source, 'location':location}
                if reason:
                    excluded.append({'url':'[redacted]' if reason=='credentials_or_secret' else raw,'reason':reason, 'reference':ref})
                    continue
                if ref not in refs[url]:
                    refs[url].append(ref)
    return dict(sorted(refs.items())), excluded, [p.relative_to(ROOT).as_posix() for p in files if p.is_file()]

host_guard = threading.Lock()
host_next = {}
def throttle(url):
    host = urllib.parse.urlsplit(url).hostname
    with host_guard:
        now = time.monotonic()
        allowed = max(now, host_next.get(host, now))
        host_next[host] = allowed + HOST_GAP
    pause = allowed - now
    if pause > 0:
        time.sleep(pause)

def classify_http(code):
    if 200 <= code < 300: return 'accessible'
    if code == 403: return 'forbidden_403'
    if code == 404: return 'not_found_404'
    if code == 410: return 'gone_410'
    if code == 429: return 'rate_limited_429'
    if code == 401: return 'authentication_401'
    if 500 <= code < 600: return 'server_error'
    if 300 <= code < 400: return 'redirect_unresolved'
    return 'http_error'

def request_once(url, attempt):
    throttle(url)
    started=time.monotonic()
    rec={'attempt':attempt,'checked_on':CHECK_DATE,'http_status':None,'status':None,'final_url':url,'title':None,'error':None,'content_type':None,'bytes_read':0}
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; PublicLinkAudit/1.0)','Accept':'text/html,application/xhtml+xml,application/json;q=0.8,*/*;q=0.5'})
    try:
        with OPENER.open(req, timeout=TIMEOUT) as response:
            code=response.status;rec.update(http_status=code,status=classify_http(code),final_url=response.geturl(),content_type=response.headers.get('Content-Type',''))
            ctype=rec['content_type'].lower()
            if 'html' in ctype:
                raw=response.read(MAX_READ);rec['bytes_read']=len(raw)
                encoding=response.headers.get_content_charset() or 'utf-8'
                try:text=raw.decode(encoding,errors='replace')
                except LookupError:text=raw.decode('utf-8',errors='replace')
                m=re.search(r'<title\b[^>]*>(.*?)</title\s*>',text,re.I|re.S)
                if m:rec['title']=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',m.group(1)))).strip()[:500]
                # A 2xx response can be a challenge or error page; preserve status and flag it.
                title=(rec['title'] or '').lower()
                if any(t in title for t in ['just a moment','checking your browser','access denied','robot check','verify you are human','attention required','enable javascript']):
                    rec['status']='access_challenge'
                elif any(t in title for t in ['page not found','404 not found','404 -','error 404']):
                    rec['status']='suspected_soft_404'
            # PDFs, archives and other binary bodies are never downloaded.
    except urllib.error.HTTPError as e:
        rec.update(http_status=e.code,status=classify_http(e.code),final_url=e.geturl(),error=f'HTTP {e.code}: {e.reason}',content_type=e.headers.get('Content-Type','') if e.headers else None)
        e.close()
    except (socket.timeout,TimeoutError) as e:
        rec.update(status='timeout',error=f'{type(e).__name__}: {e}')
    except ssl.SSLError as e:
        rec.update(status='tls_error',error=f'{type(e).__name__}: {e}')
    except urllib.error.URLError as e:
        reason=e.reason
        if isinstance(reason,(ssl.SSLError,ssl.CertificateError)) or 'CERTIFICATE_VERIFY_FAILED' in str(reason):status='tls_error'
        elif isinstance(reason,(socket.timeout,TimeoutError)) or 'timed out' in str(reason).lower():status='timeout'
        elif isinstance(reason,socket.gaierror):status='dns_error'
        else:status='network_error'
        rec.update(status=status,error=str(e))
    except Exception as e:
        rec.update(status='request_error',error=f'{type(e).__name__}: {e}')
    rec['elapsed_seconds']=round(time.monotonic()-started,2)
    return rec

def run(urls,attempt,callback=None):
    results={}
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures={pool.submit(request_once,url,attempt):url for url in urls}
        for future in concurrent.futures.as_completed(futures):
            url=futures[future];results[url]=future.result()
            if callback:
                callback(url,results[url])
            if len(results)%25==0 or len(results)==len(urls):
                print(json.dumps({'pass':attempt,'completed':len(results),'total':len(urls),'statuses':dict(collections.Counter(r['status'] for r in results.values()))}),flush=True)
    return results

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--inventory-only',action='store_true');args=parser.parse_args()
    refs,excluded,files=inventory()
    print(json.dumps({'files':len(files),'unique_urls':len(refs),'excluded':len(excluded),'top_hosts':collections.Counter(urllib.parse.urlsplit(u).hostname for u in refs).most_common(15)}),flush=True)
    if args.inventory_only:return
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    all_records={}
    if OUT.exists():
        previous=json.loads(OUT.read_text(encoding='utf-8'))
        if previous.get('checked_on')==CHECK_DATE:
            for record in previous.get('links',[]):
                if record['url'] in refs:
                    record['references']=refs[record['url']]
                    all_records[record['url']]=record
    cache_path=ROOT/'audit/root-source-access.json'
    cache_is_current = cache_path.exists() and datetime.datetime.fromtimestamp(cache_path.stat().st_mtime).astimezone().date().isoformat() == CHECK_DATE
    if cache_is_current:
        cache=json.loads(cache_path.read_text(encoding='utf-8-sig'))
        for key,entry in cache.items():
            url,_=clean_url(entry.get('url',''))
            if url in refs and url not in all_records and entry.get('access')=='retrieved':
                all_records[url]={'url':url,'status':'cached_retrieved','http_status':None,'final_url':entry.get('final_url',url),'title':entry.get('title'),'error':None,'content_type':None,'bytes_read':None,'checked_on':CHECK_DATE,'provenance':'audit/root-source-access.json','cache_key':key,'cache_note':'Earlier successful retrieval recorded in this session; original HTTP code was not retained, so no HTTP 200 is inferred.','references':refs[url],'attempts':[],'confirmed_404':False}
    def checkpoint():
        write_report({'checked_on':CHECK_DATE,'complete':False,'started_utc':start,'scope':files,'summary':{'unique_urls':len(refs),'recorded':len(all_records)},'links':list(all_records.values())})
    def save_result(url,result):
        attempts=all_records.get(url,{}).get('attempts',[])+[result]
        record={'url':url,**{k:result[k] for k in ['status','http_status','final_url','title','error','content_type','bytes_read','checked_on']},'provenance':'fresh_public_http_get','references':refs[url],'attempts':attempts}
        record['confirmed_404']=len(attempts)>1 and all(a['http_status']==404 for a in attempts)
        all_records[url]=record
        # Persist each result so cancellation/restart never loses per-URL evidence.
        checkpoint()
        if record['confirmed_404']:
            print(json.dumps({'confirmed_404':url,'final_url':record['final_url']}),flush=True)
    fresh=[u for u in refs if u not in all_records]
    print(json.dumps({'retained_records':len(all_records),'fresh_requests':len(fresh)}),flush=True)
    run(fresh,1,save_result)
    retry_statuses={'not_found_404','timeout','rate_limited_429','server_error','network_error','tls_error','dns_error','request_error','redirect_unresolved','suspected_soft_404','http_error'}
    retries=[u for u,r in all_records.items() if r['status'] in retry_statuses and len(r.get('attempts',[]))<2]
    # Explicit access denials (403/401) and challenge pages are recorded, not retried.
    print(json.dumps({'retry_count':len(retries)}),flush=True)
    run(retries,2,save_result)
    records=[all_records[u] for u in refs]
    summary={'files_scanned':len(files),'unique_urls':len(records),'recorded_http_attempts':sum(len(r['attempts']) for r in records),'status_counts':dict(collections.Counter(r['status'] for r in records)),'http_status_counts':dict(collections.Counter(str(r['http_status']) for r in records)),'confirmed_404_count':sum(r['confirmed_404'] for r in records),'recovered_on_retry':sum(len(r['attempts'])>1 and r['status']=='accessible' for r in records)}
    result={'checked_on':CHECK_DATE,'complete':True,'started_utc':start,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':files,'method':{'request':'GET with response close after at most 16384 HTML bytes; no binary downloads','concurrency':WORKERS,'timeout_seconds':TIMEOUT,'per_host_spacing_seconds':HOST_GAP,'failure_rechecks':1,'not_retried':['forbidden_403','authentication_401','access_challenge'],'cached_records_reused':sum(r['status']=='cached_retrieved' for r in records)},'limitations':['HTTP accessibility is not factual verification, endorsement, or confirmation of full-text access.','403, 429, timeouts, TLS and network errors are separate categories and do not establish that a link is invalid.','An HTTP 404 is called confirmed only if both requests returned 404; links are never deleted or changed by this script.','Fenced/indented code, inline code, placeholder/example/local URLs and credential-bearing URLs are excluded. HTML fragment identifiers are removed for request deduplication.','Only up to 16 KiB of an HTML response is read for a title; no experimental procedure/full-text content is extracted or retained. Binary bodies are not downloaded.','The timeout is a socket-operation timeout; a redirect chain can take longer than 15 seconds. Some 2xx responses may still be soft errors or access challenges undetectable from the HTML title.','An initial non-checkpointed run was stopped after reporting 125 aggregate completions to fix two Markdown extraction errors and narrow retries. Its per-URL results were not retained, and its requests are not included in recorded_http_attempts.','cached_retrieved records reuse the explicitly named preceding source-access audit; they are not presented as fresh HTTP 200 responses.'],'summary':summary,'confirmed_404':[{'url':r['url'],'final_url':r['final_url'],'references':r['references']} for r in records if r['confirmed_404']],'excluded':excluded,'links':records}
    if CHECK_DATE != '2026-10-20':
        result['limitations'] = [note for note in result['limitations'] if not note.startswith('An initial non-checkpointed run')]
    write_report(result)
    print(json.dumps({'output':OUT.relative_to(ROOT).as_posix(),'summary':summary,'confirmed_404':[r['url'] for r in records if r['confirmed_404']]}),flush=True)

if __name__=='__main__':main()
