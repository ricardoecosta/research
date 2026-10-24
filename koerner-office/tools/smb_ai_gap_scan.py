#!/usr/bin/env python3
"""SMB AI-gap scan (exploration only): how doc-heavy is a company's public site, and does it
already have chat or an AI bot? Stdlib only. Reads public homepage + robots-allowed sitemaps.
Collects NO contact data. Usage: smb_ai_gap_scan.py input.csv(name,url) -o out.csv"""
import urllib.error, csv, re, sys, gzip, io, math, argparse, urllib.request, urllib.robotparser
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
src = (Path(__file__).parent/'chat_widget_scanner.py').read_text()
ns = {}; exec(src[src.index('SIGNATURES:'):src.index('FORM_HINTS')], ns)
SIG = {k: ns['SIGNATURES'][k] for k in ('chat', 'ai_bot')}
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36 smb-ai-gap-scan/0.1 (research; contact: ricardo)"
DOC = re.compile(r"(\.pdf\b|faq|support|help|download|manual|datasheet|data-sheet|spec-?sheet|installation|instructions|documentation|knowledge|technical|resources|guide)", re.I)
PROD = re.compile(r"/products?/|/product-|/shop/|/range/|/catalog", re.I)
def get(url, n=3_000_000, t=15):
    r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=t)
    b = r.read(n)
    if url.endswith('.gz') or b[:2] == b'\x1f\x8b':
        b = gzip.decompress(b)
    return r.geturl(), b.decode('utf-8', 'replace')
def sitemap_urls(base, rp, cap=20000):
    out, todo, seen = [], [], set()
    try:
        todo = [u for u in (rp.site_maps() or [])]
    except Exception: pass
    todo = todo or [urljoin(base, '/sitemap.xml'), urljoin(base, '/sitemap_index.xml')]
    fetched = 0
    while todo and len(out) < cap and fetched < 25:
        sm = todo.pop(0)
        if sm in seen or not rp.can_fetch(UA, sm): continue
        seen.add(sm)
        try: _, x = get(sm); fetched += 1
        except Exception: continue
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", x)
        if '<sitemapindex' in x: todo += locs
        else: out += locs
    return out[:cap]
def scan(row):
    name, url = row['name'], row['url']
    res = dict(name=name, url=url, status='', chat='', ai_bot='', homepage_pdf_links=0, homepage_doc_links=0,
               sitemap_urls=0, sitemap_doc_urls=0, sitemap_pdf_urls=0, sitemap_product_urls=0, faq_or_support_page='no',
               ai_gap_score=0, note='')
    try:
        rp = urllib.robotparser.RobotFileParser()
        try:
            _, txt = get(urljoin(url, '/robots.txt'), n=500_000); rp.parse(txt.splitlines())
        except urllib.error.HTTPError as e:
            rp.parse(['User-agent: *', 'Disallow: /'] if e.code in (401, 403) else [])
        except Exception:
            rp.parse([])
        if not rp.can_fetch(UA, url): res['status'] = 'robots-disallow'; return res
        final, html = get(url)
        res['status'] = 'ok'
        for cat, tools in SIG.items():
            res[cat] = ';'.join(k for k, pats in tools.items() if any(re.search(p, html, re.I) for p in pats))
        links = set(urljoin(final, h) for h in re.findall(r'href=["\']([^"\'#]+)', html, re.I))
        res['homepage_pdf_links'] = sum(1 for l in links if '.pdf' in l.lower())
        doclinks = [l for l in links if DOC.search(l)]
        res['homepage_doc_links'] = len(doclinks)
        urls = sitemap_urls(final, rp)
        res['sitemap_urls'] = len(urls)
        res['sitemap_doc_urls'] = sum(1 for u in urls if DOC.search(u))
        res['sitemap_pdf_urls'] = sum(1 for u in urls if '.pdf' in u.lower())
        res['sitemap_product_urls'] = sum(1 for u in urls if PROD.search(u))
        if any(re.search(r"faq|support|help|knowledge", l, re.I) for l in doclinks + urls): res['faq_or_support_page'] = 'yes'
        docs = res['sitemap_doc_urls'] + res['homepage_doc_links'] + res['homepage_pdf_links']
        s = min(40, 10 * math.log10(1 + docs))            # documentation depth
        s += min(20, 6 * math.log10(1 + res['sitemap_product_urls']))  # catalogue size
        s += 15 if res['faq_or_support_page'] == 'yes' else 0          # questions already being asked
        s += 0 if res['ai_bot'] else (10 if res['chat'] else 25)       # gap: no AI bot (human chat = partial)
        res['ai_gap_score'] = round(s)
        if not urls: res['note'] = 'no sitemap found; doc depth from homepage only'
    except Exception as e:
        res['status'] = 'error'; res['note'] = str(e)[:120]
    return res
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('inp'); ap.add_argument('-o', required=True); a = ap.parse_args()
    rows = [r for r in csv.DictReader(open(a.inp)) if r.get('url')]
    with ThreadPoolExecutor(6) as ex: out = list(ex.map(scan, rows))
    out.sort(key=lambda r: -r['ai_gap_score'])
    with open(a.o, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    print(f"{len(out)} sites -> {a.o}")
