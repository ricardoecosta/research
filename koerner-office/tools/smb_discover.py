#!/usr/bin/env python3
"""SMB discovery: build company lists (name, website, sector, country, source) for doc-heavy B2B
makers/exporters from free public sources. Collects NO contact data (no emails/phones/people).
Respects robots.txt, 1 request/sec per host. Instagram is deliberately not used (ToS).

Sources (each a public member/exporter directory or open data):
  UK  BEAMA member directory (electrical, rendered + 'load more'), LIA list (local csv), OSM
  PT  APCOR directory (cork), APICER members (ceramics), OSM
  ES  ASCER/Tile of Spain members (ceramics), ANFALUM member pages (lighting), OSM
Usage: smb_discover.py -o companies.csv [--sources a,b] [--osm]
"""
import argparse, csv, json, os, re, sys, time, urllib.parse, urllib.request, urllib.robotparser
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh) Chrome/126 smb-discover/0.1 (research; non-commercial; contact: ricardo)"
SKIP = re.compile(r"(facebook|instagram|twitter|x\.com|linkedin|youtube|youtu\.be|pinterest|tiktok|vimeo|google|"
                  r"gstatic|bit\.ly|wa\.me|whatsapp|apple\.com|microsoft|wordpress\.org|w3\.org|schema\.org|"
                  r"cookie|onetrust|pixl8|readymembership|gov\.|europa\.eu|issuu|flickr|jquery|cloudflare|"
                  r"bootstrapcdn|fontawesome|hotjar|doubleclick|hubspot|mailchimp|addtoany|sharethis|viriato|gmpg|browsehappy|wpml|elementor|wp\.com|creativecommons|openstreetmap)", re.I)
_last, _robots = {}, {}

def allowed(url):
    host = urllib.parse.urlsplit(url).netloc
    if host not in _robots:
        rp = urllib.robotparser.RobotFileParser()
        try:
            rp.parse(fetch(f"https://{host}/robots.txt", check=False).splitlines())
        except urllib.error.HTTPError as e:
            rp.parse(['User-agent: *', 'Disallow: /'] if e.code in (401, 403) else [])
        except Exception:
            rp.parse([])
        _robots[host] = rp
    return _robots[host].can_fetch(UA, url)

def fetch(url, check=True, data=None, timeout=60):
    if check and not allowed(url):
        raise PermissionError(f"robots.txt disallows {url}")
    host = urllib.parse.urlsplit(url).netloc
    wait = 1.0 - (time.time() - _last.get(host, 0))
    if wait > 0: time.sleep(wait)
    _last[host] = time.time()
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")

def render(url, click=None, max_clicks=40):
    """Rendered HTML for JS directories; optionally keep clicking a 'load more' selector."""
    if not allowed(url): raise PermissionError(f"robots.txt disallows {url}")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(user_agent=UA)
        pg.goto(url, wait_until="domcontentloaded", timeout=45000); pg.wait_for_timeout(3000)
        for _ in range(max_clicks if click else 0):
            loc = pg.locator(click)
            if not loc.count() or not loc.first.is_visible(): break
            loc.first.click(); pg.wait_for_timeout(1500)
        html = pg.content(); b.close()
    return html

def site_links(html, own_host):
    """External company websites in a directory page: hrefs + bare 'www.x.tld' text (never emails)."""
    found = re.findall(r'href=["\'](https?://[^"\'\s>]+)', html, re.I)
    found += ["http://" + w for w in re.findall(r'(?<![@\w./])(www\.[a-z0-9-]+(?:\.[a-z0-9-]+)+)', html, re.I)]
    out = {}
    for u in found:
        host = urllib.parse.urlsplit(u).netloc.lower().split(":")[0]
        if not host or own_host in host or SKIP.search(host) or "@" in u: continue
        if re.search(r"\.(png|jpe?g|svg|css|js|pdf)$", host): continue
        key = re.sub(r"^www\.", "", host)
        if "." not in key or key.startswith(("http", "www")): continue
        out.setdefault(key, f"https://{host}")
    return out

def name_of(domain):
    return re.sub(r"\.(co|com|org)?\.?(uk|pt|es|com|eu|net)$", "", domain).replace("-", " ").title()

def rows(domains, country, sector, source):
    return [dict(name=name_of(d), url=u, domain=d, country=country, sector=sector, source=source)
            for d, u in domains.items()]

# ---------- sources ----------
def src_beama():
    u = "https://www.beama.org.uk/about-beama/member-directory.html"
    return rows(site_links(render(u, click="a.generic-load-more-link"), "beama.org.uk"), "UK", "electrical", "BEAMA")

def src_lia():
    p = Path.home() / "hustling/data/prospects-starter.csv"
    out = []
    for r in csv.DictReader(open(p)):
        d = re.sub(r"^www\.", "", urllib.parse.urlsplit(r["website"]).netloc.lower())
        out.append(dict(name=r["company"], url=r["website"], domain=d, country="UK", sector="lighting", source="LIA"))
    return out

def src_apcor():
    return rows(site_links(fetch("https://apcor.pt/pt/diretorio"), "apcor.pt"), "PT", "cork", "APCOR")

def src_apicer():
    return rows(site_links(fetch("https://www.apicer.pt/apicer/pt"), "apicer.pt"), "PT", "ceramics", "APICER")

def src_tileofspain():
    return rows(site_links(fetch("https://tileofspain.com/nosotros/"), "tileofspain.com"), "ES", "ceramics", "ASCER/TileOfSpain")

def src_anfalum(max_id=140):
    out, miss = {}, 0
    for i in range(1, max_id):
        try:
            html = fetch(f"https://www.anfalum.com/organization/{i}/")
        except Exception:
            continue
        m = re.search(r"Web\s*(?:</[^>]+>\s*)*(?:<[^>]+>\s*)*(https?://[^\s<\"']+|www\.[^\s<\"']+)", html)
        if m:
            u = m.group(1) if m.group(1).startswith("http") else "https://" + m.group(1)
            out.update(site_links(f'href="{u}"', "anfalum.com"))
    return rows(out, "ES", "lighting", "ANFALUM")

OSM_KW = {"lighting": "lighting|luminaire|iluminação|iluminacion|iluminación",
          "electrical": "electrical|switchgear|cable|eléctric|elétric|electric",
          "ceramics": "ceramic|cerâmica|cerámica|azulejo|tiles",
          "cork": "cork|cortiça|corcho",
          "machinery": "machinery|engineering|maquinaria|máquinas|metalomecânica|metalurgica",
          "construction products": "precast|insulation|isolamento|aislamiento|roofing|cladding|brick|tijolo|ladrillo"}
OSM_ENDPOINTS = ["https://overpass-api.de/api/interpreter", "https://overpass.private.coffee/api/interpreter"]

def src_osm(countries=("GB", "PT", "ES")):
    out = []
    for cc in countries:
        for sector, kw in OSM_KW.items():
            q = (f'[out:json][timeout:90];area["ISO3166-1"="{cc}"][admin_level=2]->.a;'
                 f'(nwr["website"]["name"~"{kw}",i]["shop"!~"."]["amenity"!~"."](area.a););out tags;')
            for ep in OSM_ENDPOINTS:
                try:
                    d = json.loads(fetch(ep, check=False, data=urllib.parse.urlencode({"data": q}).encode(), timeout=120))
                    break
                except Exception as e:
                    print(f"  osm {cc}/{sector} {ep}: {type(e).__name__}", file=sys.stderr); time.sleep(10); d = None
            for el in (d or {}).get("elements", []):
                t = el.get("tags", {}); w = t.get("website", "")
                if not w.startswith("http"): w = "https://" + w
                host = urllib.parse.urlsplit(w).netloc.lower()
                if not host or SKIP.search(host): continue
                out.append(dict(name=t.get("name", host), url=w, domain=re.sub(r"^www\.", "", host),
                                country={"GB": "UK"}.get(cc, cc), sector=sector, source="OSM"))
            time.sleep(5)
    return out

SOURCES = dict(beama=src_beama, lia=src_lia, apcor=src_apcor, apicer=src_apicer,
               tileofspain=src_tileofspain, anfalum=src_anfalum, osm=src_osm)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("-o", required=True)
    ap.add_argument("--sources", default="beama,lia,apcor,apicer,tileofspain,anfalum,osm"); a = ap.parse_args()
    allrows, seen = [], set()
    for s in a.sources.split(","):
        try:
            got = SOURCES[s]()
        except Exception as e:
            print(f"{s}: FAILED {type(e).__name__}: {e}", file=sys.stderr); continue
        new = [r for r in got if r["domain"] not in seen]; seen |= {r["domain"] for r in new}
        print(f"{s}: {len(got)} found, {len(new)} new", file=sys.stderr); allrows += new
    with open(a.o, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "url", "domain", "country", "sector", "source"])
        w.writeheader(); w.writerows(allrows)
    print(f"{len(allrows)} companies -> {a.o}")
