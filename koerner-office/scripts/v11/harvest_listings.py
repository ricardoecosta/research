"""v11 Track B harvest: no LLM. Flippa public search (SaaS + apps, $20k-$150k) -> card text + listing page text.
Output: analysis/v11/listings_raw.jsonl {id,url,card,page}"""
import html, json, re, time, csv, urllib.request as ur
from pathlib import Path
V = Path(__file__).resolve().parents[2] / "analysis/v11"; OUT = V / "listings_raw.jsonl"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/130 Safari/537.36"
def get(u):
    for t in range(3):
        try:
            with ur.urlopen(ur.Request(u, headers={"User-Agent": UA}), timeout=30) as r: return r.read().decode("utf-8", "replace")
        except Exception as e:
            time.sleep(5 * (t + 1)); err = e
    print("FAIL", u, err); return None
def strip(h):
    h = re.sub(r"<(script|style)\b[^>]*>.*?</(script|style)>", " ", h or "", flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]*>", " ", h))).strip()
def window(t):
    i = min([j for j in (t.find("Site Age"), t.find("Asking Price"), t.find("About the Business")) if j >= 0] or [0])
    return t[max(0, i - 1500): i + 8000]
seen_names = " ".join(r["name"].lower() for r in csv.DictReader(open(V.parent / "loop/SEEN.csv")))
cards = {}
for ptype in ["saas", "app", "plugin"]:
    for page in range(1, 7):
        u = f"https://flippa.com/search?filter%5Bproperty_type%5D%5B%5D={ptype}&filter%5Bprice%5D%5Bmin%5D=20000&filter%5Bprice%5D%5Bmax%5D=150000&filter%5Bstatus%5D=open&page={page}"
        t = get(u); time.sleep(1.5)
        if not t: break
        blocks = re.findall(r'<li id="listing-(\d+)"(.*?)</li>\s*(?=<li id="listing-|</ul>)', t, re.S)
        if not blocks: break
        new = 0
        for lid, b in blocks:
            if lid in cards: continue
            m = re.search(r'href="(https://flippa.com/' + lid + r'-[^"]+)"', b)
            cards[lid] = {"id": lid, "type": ptype, "url": m.group(1) if m else f"https://flippa.com/{lid}", "card": strip(b)[:1500]}; new += 1
        print(ptype, page, len(blocks), new, flush=True)
        if new == 0: break
print("cards", len(cards))
out = []
for lid, c in cards.items():
    t = get(c["url"]); time.sleep(1.2)
    c["page"] = window(strip(t)) if t else None
    out.append(c)
with open(OUT, "w") as f:
    for c in out: f.write(json.dumps(c, ensure_ascii=False) + "\n")
print("saved", len(out))
