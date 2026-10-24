#!/usr/bin/env python3
"""SMB AI-gap scan (exploration only): how doc-heavy is a company's public site, and does it
already have chat or an AI bot? Stdlib only. Reads public homepage + robots-allowed sitemaps.
Collects NO contact data. Usage: smb_ai_gap_scan.py input.csv(name,url) -o out.csv"""
import urllib.error, csv, re, sys, gzip, io, math, argparse, urllib.request, urllib.robotparser
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); import smb_playbook_score as PB
src = (Path(__file__).parent/'chat_widget_scanner.py').read_text()
ns = {}; exec(src[src.index('SIGNATURES:'):src.index('FORM_HINTS')], ns)
SIG = {k: ns['SIGNATURES'][k] for k in ('chat', 'ai_bot')}
SIG['helpdesk'] = {"Zendesk": [r"\.zendesk\.com", r"zdassets\.com"], "Freshdesk": [r"\.freshdesk\.com", r"freshworks\.com/widget"],
    "Help Scout": [r"beacon-v2\.helpscout\.net", r"helpscoutdocs\.com"], "HelpJuice": [r"helpjuice\.com"],
    "Intercom Help Center": [r"intercom\.help"], "Document360": [r"document360\.io"], "Gorgias": [r"gorgias\.chat", r"gorgias\.io"],
    "Salesforce/Service Cloud": [r"embeddedservice", r"embeddedMessaging", r"salesforceliveagent", r"my\.site\.com"], "Kayako": [r"kayako\.com"]}
SIG['ai_bot'].update({"Intercom Fin": [r"\bfin\b.*intercom|intercom.*\bfin\b"], "Tidio Lyro": [r"lyro"], "Zendesk AI agent": [r"ultimate\.ai"],
    "Ada": [r"static\.ada\.support", r"ada\.support/embed"], "Forethought": [r"forethought\.ai"], "Kore.ai": [r"kore\.ai"],
    "Chatbot.com": [r"cdn\.chatbot\.com"], "Yellow.ai": [r"cloud\.yellow\.ai"], "Sobot/other": [r"sobot\.io"]})
SIG['chat']['LiveChat'] = SIG['chat']['LiveChat'] + [r"connect\.livechatinc\.com"]
AI_CAPABLE = {"Intercom", "Tidio", "Drift", "Zendesk/Zopim", "Freshchat", "HubSpot chat", "Zoho SalesIQ", "Zendesk", "Freshdesk", "Gorgias"}
CAREERS = re.compile(r"(career|jobs|vacanc|join-us|work-with-us|recruit|carreira|emprego|recrutamento|trabalhe|empleo|trabaja|unete|bolsa-de-trabajo)", re.I)
SUPPORT_JOB = re.compile(r"(customer (support|service)|technical support|support (engineer|specialist|advisor|executive)|helpdesk|help desk|"
                         r"apoio ao cliente|assist[eê]ncia t[eé]cnica|suporte t[eé]cnico|atenci[oó]n al cliente|soporte t[eé]cnico|asistencia t[eé]cnica|servicio t[eé]cnico)", re.I)
TECHSUP = re.compile(r"(technical-support|tech-support|/support|customer-service|assistencia-tecnica|apoio-ao-cliente|apoio-tecnico|suporte|"
                     r"asistencia-tecnica|servicio-tecnico|atencion-al-cliente|soporte|/sat\b|/sav\b|aftersales|after-sales|pos-venda|postventa)", re.I)
HELPSUB = re.compile(r"^https?://(help|support|docs|kb|knowledge|ayuda|ajuda|soporte|suporte)\.", re.I)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36 smb-ai-gap-scan/0.1 (research; contact: ricardo)"
DOC = re.compile(r"(\.pdf\b|faq|support|help|download|manual|datasheet|data-sheet|spec-?sheet|installation|instructions|"
                 r"documentation|knowledge|technical|resources|guide|"
                 r"manuais|instru[cç][oõ]es|instalac|perguntas|suporte|ajuda|transfer[eê]ncias|documenta[cç]|cat[aá]logo|"
                 r"instrucciones|preguntas|soporte|ayuda|descargas|documentaci|montaje|garant|certificad|"
                 r"declaration-of-performance|/dop|ficha)", re.I)
DS = re.compile(r"(datasheet|data-sheet|spec-?sheet|technical-data|ficha[-_ ]?t[eé]cnica|fichas?-tecnicas?|ficha-producto|"
                r"/tds|_tds|-tds|product-data|hoja-tecnica|ficha_tecnica)", re.I)
FAQ = re.compile(r"(faq|support|help|knowledge|perguntas|frequentes|suporte|ajuda|preguntas|frecuentes|soporte|ayuda|atencion-al-cliente|apoio)", re.I)
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
    res = dict(name=name, url=url, country=row.get('country',''), sector=row.get('sector',''), source=row.get('source',''), status='', chat='', ai_bot='', homepage_pdf_links=0, homepage_doc_links=0,
               sitemap_urls=0, sitemap_doc_urls=0, sitemap_pdf_urls=0, sitemap_product_urls=0, datasheet_links=0, pdf_links=0, faq_or_support_page='no', help_centre='no', tech_support_page='no', support_email_present='no', phone_present='no', careers_page='no', support_hiring='no', helpdesk='', chat_type='none', size_band='unknown', ticket_volume='unknown', doc_heavy='no', render_status='', chat_render='', ai_bot_render='', helpdesk_render='', gap='', fit_score=0,
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
        res['datasheet_links'] = sum(1 for u in list(links) + urls if DS.search(u))
        res['pdf_links'] = res['homepage_pdf_links'] + res['sitemap_pdf_urls']
        if any(FAQ.search(l) for l in doclinks + urls): res['faq_or_support_page'] = 'yes'
        docs = res['sitemap_doc_urls'] + res['homepage_doc_links'] + res['homepage_pdf_links']
        s = min(40, 10 * math.log10(1 + docs))            # documentation depth
        s += min(20, 6 * math.log10(1 + res['sitemap_product_urls']))  # catalogue size
        s += 15 if res['faq_or_support_page'] == 'yes' else 0          # questions already being asked
        s += 0 if res['ai_bot'] else (10 if res['chat'] else 25)       # gap: no AI bot (human chat = partial)
        res['ai_gap_score'] = round(s)
        res['doc_heavy'] = 'yes' if (docs >= 25 or res['pdf_links'] >= 10 or res['datasheet_links'] >= 5) else 'no'
        # support-function signals: booleans only, no contact data stored
        res['support_email_present'] = 'yes' if re.search(r"(mailto:)?\b(support|technical|tech|service|help|helpdesk|suporte|soporte|apoio|sat|sav|asistencia|assistencia|aftersales)@", html, re.I) else 'no'
        res['phone_present'] = 'yes' if re.search(r'href=["\']tel:', html, re.I) else 'no'
        res['tech_support_page'] = 'yes' if any(TECHSUP.search(l) for l in list(links) + urls) else 'no'
        res['help_centre'] = 'yes' if (res['helpdesk'] or any(HELPSUB.search(l) for l in links)) else 'no'
        car = next((l for l in links if CAREERS.search(l) and urlparse(l).netloc.endswith(urlparse(final).netloc.replace('www.', ''))), None)
        if car:
            res['careers_page'] = 'yes'
            try:
                if rp.can_fetch(UA, car): res['support_hiring'] = 'yes' if SUPPORT_JOB.search(get(car, n=1_500_000)[1]) else 'no'
            except Exception: pass
        res.update(PB.page_signals(html, links, urls))
        classify(res); res['fit_score'] = fit(res)
        if not urls: res['note'] = 'no sitemap found; doc depth from homepage only'
    except Exception as e:
        res['status'] = 'error'; res['note'] = str(e)[:120]
    return res
CONSENT = re.compile(r"^\s*(accept( all)?( cookies)?|allow all|agree|i agree|ok|aceitar( todos| tudo)?|aceptar( todas| todo)?|permitir todos|consent)\s*$", re.I)
def classify(res):
    vendors = set(filter(None, (res['chat'] + ';' + res['helpdesk']).split(';')))
    if res['ai_bot']: res['chat_type'] = 'ai_agent'
    elif vendors & AI_CAPABLE: res['chat_type'] = 'ai_capable_vendor (AI add-on unknown)'
    elif 'Custom/unknown' in res['chat']: res['chat_type'] = 'custom_chat (AI unknown)'
    elif res['chat']: res['chat_type'] = 'live_chat_non_ai'
    elif res['helpdesk']: res['chat_type'] = 'ticket_helpdesk_only'
    else: res['chat_type'] = 'none'
def fit(res):
    """Manual §3.2 proxy: knowledge complexity + support team + tech signal. Ticket volume unknown."""
    docs = res['sitemap_doc_urls'] + res['homepage_doc_links'] + res['homepage_pdf_links']
    f = min(30, 9 * math.log10(1 + docs + 2 * res['datasheet_links']))           # knowledge complexity
    f += min(10, 4 * math.log10(1 + res['sitemap_product_urls']))                   # catalogue breadth
    f += 5 * (res['faq_or_support_page'] == 'yes') + 5 * (res['help_centre'] == 'yes')
    f += 6 * (res['tech_support_page'] == 'yes') + 4 * (res['support_email_present'] == 'yes') + 2 * (res['phone_present'] == 'yes')
    f += 10 * (res['support_hiring'] == 'yes')                                       # existing/growing support team
    f += {'none': 22, 'live_chat_non_ai': 25, 'ticket_helpdesk_only': 25}.get(res['chat_type'], 12 if res['chat_type'].startswith(('ai_capable', 'custom')) else 0)
    return round(f)
def score(res):
    docs = res['sitemap_doc_urls'] + res['homepage_doc_links'] + res['homepage_pdf_links']
    s = min(40, 10 * math.log10(1 + docs)) + min(20, 6 * math.log10(1 + res['sitemap_product_urls']))
    s += 15 if res['faq_or_support_page'] == 'yes' else 0
    s += 0 if res['ai_bot'] else (10 if res['chat'] else 25)
    return round(s)
async def _render_one(browser, res, sem):
    async with sem:
        ctx = await browser.new_context(user_agent=UA.replace(' smb-ai-gap-scan/0.1 (research; contact: ricardo)', ''), viewport={'width': 1366, 'height': 900})
        pg = await ctx.new_page(); reqs = []
        pg.on('request', lambda q: reqs.append(q.url))
        try:
            await pg.goto(res['url'], wait_until='domcontentloaded', timeout=30000)
            await pg.wait_for_timeout(2500)
            try:  # accept cookie banner so consent-gated chat widgets load (no form submission)
                btn = pg.get_by_role('button', name=CONSENT)
                if await btn.count(): await btn.first.click(timeout=2000)
            except Exception: pass
            await pg.wait_for_timeout(6000)
            blob = (await pg.content()) + '\n' + '\n'.join(reqs) + '\n' + '\n'.join(f.url for f in pg.frames)
            for cat, tools in SIG.items():
                res[cat + '_render'] = ';'.join(k for k, pats in tools.items() if any(re.search(p, blob, re.I) for p in pats))
            dom = await pg.evaluate("""() => [...document.querySelectorAll('[id*=chat i],[class*=chat-launcher i],[class*=chat-widget i],[class*=chatbot i],button,[aria-label*=chat i]')]
                .filter(e => /chat|chatbot|assistente|asistente|virtual assistant/i.test((e.id||'')+' '+(e.className||'')+' '+(e.getAttribute('aria-label')||'')+' '+(e.tagName=='BUTTON'?e.innerText:'')))
                .map(e => (e.id||'')+' '+String(e.className||'')+' '+(e.getAttribute('aria-label')||'')).slice(0,5)""")
            dom = [d for d in (dom or []) if not re.search(r"snapchat|joinchat|chaty|wa-?fab|whatsapp", d, re.I)]  # WhatsApp buttons / trackers are not chat
            if dom and not res['chat_render'] and not res['ai_bot_render']:
                if any(re.search(r"chatbot|ai-?chat|assistant|asistente|assistente|avatar|push-to-talk", d, re.I) for d in dom):
                    res['ai_bot_render'] = 'Custom AI chatbot (DOM)'
                else:
                    res['chat_render'] = 'Custom/unknown chat widget'
            res['render_status'] = 'ok'
        except Exception as e:
            res['render_status'] = 'error:' + type(e).__name__
        finally:
            await ctx.close()
def render_pass(results, conc=6):
    import asyncio
    from playwright.async_api import async_playwright
    async def go():
        async with async_playwright() as p:
            b = await p.chromium.launch(); sem = asyncio.Semaphore(conc)
            await asyncio.gather(*[_render_one(b, r, sem) for r in results if r['status'] == 'ok'])
            await b.close()
    asyncio.run(go())
    for r in results:  # merge static + rendered detections, rescore
        r['chat'] = ';'.join(sorted(set(filter(None, (r['chat'] + ';' + r['chat_render']).split(';')))))
        r['ai_bot'] = ';'.join(sorted(set(filter(None, (r['ai_bot'] + ';' + r['ai_bot_render']).split(';')))))
        r['helpdesk'] = ';'.join(sorted(set(filter(None, (r['helpdesk'] + ';' + r['helpdesk_render']).split(';')))))
        if r['status'] == 'ok': r['ai_gap_score'] = score(r); classify(r); r['fit_score'] = fit(r)
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('inp'); ap.add_argument('-o', required=True)
    ap.add_argument('--render', action='store_true', help='headless Chrome pass for JS-injected chat widgets'); a = ap.parse_args()
    rows = [r for r in csv.DictReader(open(a.inp)) if r.get('url')]
    with ThreadPoolExecutor(8) as ex: out = list(ex.map(scan, rows))
    if a.render: render_pass(out)
    for r in out:
        if r['status'] == 'ok':
            r['gap'] = 'yes' if r['doc_heavy'] == 'yes' and r['chat_type'] in ('none', 'live_chat_non_ai', 'ticket_helpdesk_only') and (not a.render or r['render_status'] == 'ok') else 'no'
    PB.rescore(out)
    out.sort(key=lambda r: (-(r.get('manual50_est') or 0) if isinstance(r.get('manual50_est'), int) else 0, -r['fit_score']))
    with open(a.o, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(dict.fromkeys(k for r in out for k in r))); w.writeheader(); w.writerows(out)
    print(f"{len(out)} sites -> {a.o}")
