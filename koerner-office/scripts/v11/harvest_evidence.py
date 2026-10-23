"""v11 Track E harvest: no LLM. HN Algolia + Reddit search RSS + 1-2 star reviews of paid tools (Shopify, WordPress.org, Apple).
Output: analysis/v11/evidence_raw.jsonl  {src, author, date, url, text, tool}"""
import html, json, re, time, datetime as dt, urllib.parse as up, urllib.request as ur, xml.etree.ElementTree as ET
from pathlib import Path
V = Path(__file__).resolve().parents[2] / "analysis/v11"; OUT = V / "evidence_raw.jsonl"
SINCE = dt.datetime(2026, 4, 23, tzinfo=dt.timezone.utc); UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/130 Safari/537.36"
LOG = Path("/tmp/loop/v11/harvest_evidence.log")
def log(m):
    print(m, flush=True); open(LOG, "a").write(f"{dt.datetime.now():%H:%M:%S} {m}\n")
RL = {"n": 0}
def get(url, tries=2):
    for t in range(tries):
        try:
            with ur.urlopen(ur.Request(url, headers={"User-Agent": UA}), timeout=25) as r: RL["n"] = 0; return r.read().decode("utf-8", "replace")
        except Exception as e:
            if "429" in str(e):
                RL["n"] += 1; log(f"429 {url[:80]}")
                if RL["n"] >= 3: return None
                time.sleep(15)
            elif t == tries - 1: log(f"FAIL {url[:100]} {e}"); return None
            else: time.sleep(3)
    return None
def strip(h): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h or ""))).strip()

PHRASES = ["\"I would pay for\"", "\"I'd pay for\"", "\"is there a tool\"", "\"is there an app\"", "\"is there a service\"", "\"looking for a tool\"",
           "\"we pay someone to\"", "\"hired someone to\"", "\"manually every week\"", "\"manually every month\"", "\"copy and paste\" spreadsheet",
           "\"data entry\" hours", "\"waste hours\"", "\"so tedious\"", "\"wish there was\"", "\"why is there no\"", "\"switched from\" because", "\"cancelled my subscription\""]
recs = []
def add(src, author, date, url, text, tool=None):
    if date and date < SINCE: return
    recs.append({"src": src, "author": f"{src.split(':')[0]}:{author}", "date": date.isoformat()[:10] if date else None, "url": url, "text": text[:1200], "tool": tool})

# HN
ts = int(SINCE.timestamp())
for q in PHRASES:
    for page in range(3):
        u = f"https://hn.algolia.com/api/v1/search_by_date?query={up.quote(q)}&tags=(comment,story)&numericFilters=created_at_i>{ts}&hitsPerPage=100&page={page}"
        t = get(u)
        if not t: break
        hits = json.loads(t).get("hits", [])
        for h in hits:
            add("hn", h.get("author"), dt.datetime.fromtimestamp(h["created_at_i"], dt.timezone.utc), f"https://news.ycombinator.com/item?id={h['objectID']}",
                strip(h.get("comment_text") or ((h.get("title") or "") + " " + (h.get("story_text") or ""))))
        if len(hits) < 100: break
log(f"hn: {len(recs)}")

# Reddit search RSS (global + business subs)
n0 = len(recs); ns = {"a": "http://www.w3.org/2005/Atom"}
SUBS = [None, "smallbusiness", "Entrepreneur", "SaaS", "ecommerce", "shopify", "accounting", "Bookkeeping", "realtors", "sysadmin", "msp", "marketing", "freelance", "agency", "projectmanagement", "nonprofit", "PropertyManagement", "Etsy", "AmazonSeller", "legaltech"]
import itertools, os
REDDIT_OFF = os.environ.get("NO_REDDIT") == "1"
for sub, q in ([] if REDDIT_OFF else itertools.product(SUBS[:10], PHRASES[:8])):
    if RL["n"] >= 3: log("reddit circuit breaker: 3 consecutive 429s, stopping reddit"); break
    if True:
        base = f"https://www.reddit.com/r/{sub}/search.rss?restrict_sr=1&" if sub else "https://www.reddit.com/search.rss?"
        t = get(base + f"q={up.quote(q)}&sort=new&t=year&limit=100"); time.sleep(4)
        if not t: continue
        try: root = ET.fromstring(t)
        except Exception: continue
        for e in root.findall("a:entry", ns):
            a = e.find("a:author/a:name", ns); d = e.find("a:updated", ns) or e.find("a:published", ns)
            try: date = dt.datetime.fromisoformat(d.text.replace("Z", "+00:00"))
            except Exception: date = None
            add("reddit" + (f":{sub}" if sub else ""), (a.text if a is not None else "?").replace("/u/", ""), date, e.find("a:link", ns).get("href"),
                strip((e.find("a:title", ns).text or "") + " " + (e.find("a:content", ns).text or "")))
log(f"reddit: {len(recs) - n0}"); RL["n"] = 0

# Apple App Store 1-2 star reviews of paid/subscription apps (US store), recent pages
n0 = len(recs)
APPS = {"QuickBooks": 584606479, "FreshBooks": 1052387489, "Xero": 441880705, "Wave": 882059622, "Expensify": 471713959, "Shopify": 371294472, "Squarespace": 1004009340,
        "Canva": 897446215, "Notion": 1232780281, "Todoist": 572688855, "Evernote": 281796108, "Dropbox": 327630330, "DocuSign": 474990205, "Jobber": 1001941412,
        "HoneyBook": 1050185225, "Monday": 1290128888, "Asana": 489969512, "Trello": 461504587, "Zoho Books": 1110524922, "Gusto": 1490470693}
for name, aid in APPS.items():
    for page in (1, 2, 3):
        t = get(f"https://itunes.apple.com/us/rss/customerreviews/page={page}/id={aid}/sortby=mostrecent/json")
        if not t: break
        try: ents = json.loads(t)["feed"].get("entry", [])
        except Exception: break
        for e in ents if isinstance(ents, list) else [ents]:
            if "im:rating" not in e: continue
            if int(e["im:rating"]["label"]) > 2: continue
            date = dt.datetime.fromisoformat(e["updated"]["label"]) if "updated" in e else None
            add("appstore", e["author"]["name"]["label"], date, e["author"]["uri"]["label"], f"[{name}] {e['title']['label']}. {e['content']['label']}", name)
log(f"appstore: {len(recs) - n0}")

# WordPress.org 1-star reviews of freemium plugins with paid pro versions
n0 = len(recs)
PLUG = ["woocommerce", "elementor", "wordpress-seo", "wpforms-lite", "updraftplus", "wp-mail-smtp", "jetpack", "really-simple-ssl", "all-in-one-seo-pack", "mailchimp-for-wp",
        "the-events-calendar", "wp-rocket", "litespeed-cache", "woocommerce-payments", "complianz-gdpr", "redirection", "duplicator", "wordfence", "contact-form-7", "smash-balloon-social-photo-feed"]
for p in PLUG:
    for stars in (1, 2):
        t = get(f"https://wordpress.org/support/plugin/{p}/reviews/?filter={stars}")
        if not t: continue
        for m in re.finditer(r'<li[^>]*class="[^"]*bbp-body[^"]*"[^>]*>(.*?)</li>\s*</ul>', t, re.S) or []:
            pass
        for row in re.findall(r'<ul id="bbp-topic-\d+".*?</ul>', t, re.S):
            title = re.search(r'class="bbp-topic-permalink" href="([^"]+)"[^>]*>(.*?)</a>', row, re.S)
            auth = re.search(r'bbp-author-name">([^<]+)<', row); fresh = re.search(r'title="([A-Z][a-z]+ \d{1,2}, \d{4})', row)
            date = None
            if fresh:
                try: date = dt.datetime.strptime(fresh.group(1), "%B %d, %Y").replace(tzinfo=dt.timezone.utc)
                except Exception: pass
            if title: add("wporg", auth.group(1) if auth else "?", date, title.group(1), f"[{p} {stars}*] {strip(title.group(2))}", p)
log(f"wporg: {len(recs) - n0}")

# Shopify App Store 1-2 star reviews of paid apps
n0 = len(recs)
SAPPS = ["klaviyo-email-marketing", "judgeme", "loox", "privy", "recharge", "gorgias", "shipstation", "smile-io", "yotpo-social-reviews", "omnisend", "aftership",
         "pagefly", "shogun", "bold-subscriptions", "tidio-chat", "vitals", "matrixify", "printful", "zipify-pages", "rebuy"]
for a in SAPPS:
    for r_ in (1, 2):
        t = get(f"https://apps.shopify.com/{a}/reviews?ratings%5B%5D={r_}&sort_by=newest")
        if not t: continue
        for blk in re.findall(r'data-merchant-review(.*?)</div>\s*</div>\s*</div>\s*</div>', t, re.S):
            txt = strip(blk); dm = re.search(r'([A-Z][a-z]+ \d{1,2}, \d{4})', txt); date = None
            if dm:
                try: date = dt.datetime.strptime(dm.group(1), "%B %d, %Y").replace(tzinfo=dt.timezone.utc)
                except Exception: pass
            au = re.search(r'tw-text-heading-xs[^>]*>\s*([^<]{2,80})<', blk)
            add("shopify", (au.group(1).strip() if au else f"anon{hash(txt)%10**6}"), date, f"https://apps.shopify.com/{a}/reviews", f"[{a} {r_}*] {txt}", a)
log(f"shopify: {len(recs) - n0}")

seen = set(); out = []
for r in recs:
    k = (r["author"], r["url"], r["text"][:80])
    if k in seen: continue
    seen.add(k); out.append(r)
with open(OUT, "w") as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False) + "\n")
log(f"total unique {len(out)} -> {OUT}")
