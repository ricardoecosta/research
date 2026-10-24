"""details/*.json + xdetail_raw_*.txt + resources.json -> ../details.json (id -> {d, res}). URLs from the LLM are kept
only if they appear verbatim in the cited files; file paths only if they exist."""
import json, glob, re, sys
from pathlib import Path
here = Path(__file__).parent; H = here.parents[3]  # ~/hustling
sys.path.insert(0, str(here.parents[1] / "scripts/common")); from runner import parse_json_text
res = json.load(open(here/"resources.json"))
D = {}
for f in sorted(glob.glob(str(here/"details/batch_*.json"))):
    for r in json.load(open(f))["records"]: D[r.pop("id")] = r
dropped = kept = 0
for f in sorted(glob.glob(str(here/"xdetail_raw_*.txt"))):
    txt = open(f).read()
    try: data = parse_json_text(txt)
    except Exception:
        txt = re.sub(r'"\}\]\}\],"', '"]}],"', txt); data = json.JSONDecoder().raw_decode(txt[txt.find("{"):])[0]
    for r in data.get("records", []):
        i = r.pop("id"); urls = r.pop("urls", []) or []; files = r.pop("files", []) or []
        okf = []
        for p in files:
            p = re.sub(r"\s*§.*$", "", str(p)).strip()
            pp = H/p if not p.startswith("~") else Path(p).expanduser()
            if pp.exists(): okf.append(p)
        corpus = "".join(open(H/p, errors="ignore").read() for p in okf if (H/p).is_file())
        R = res.setdefault(i, {"youtube": [], "links": [], "files": []})
        for p in okf:
            rel = p[len("research/"):] if p.startswith("research/") else ("../" + p if p.startswith("playbooks/") else p)
            if rel not in R["files"]: R["files"].append(rel)
        have = {x["url"] for x in R["links"]} | {x["url"] for x in R["youtube"]}
        for u in urls:
            url = str(u.get("url", "")).strip()
            if not url or url in have: continue
            if url not in corpus: dropped += 1; continue
            kept += 1; have.add(url)
            if "youtube.com/watch" in url or "youtu.be/" in url:
                ts = re.search(r"[?&]t=(\d+)", url); R["youtube"].append({"url": re.sub(r"[?&]t=\d+s?", "", url), "label": u.get("label") or url, "kind": "youtube", "ts": ts.group(1) if ts else None})
            else:
                R["links"].append({"url": url, "label": u.get("label") or url.split("/")[2], "kind": "flippa" if "flippa.com" in url else "acquire" if "acquire.com" in url else "web"})
        D.setdefault(i, r)
opps = json.load(open(here.parent/"opportunities.json"))["opportunities"]
SRC = {b["id"]: b["src"] for b in map(json.loads, open(here/"raw_bundles.jsonl")) if not b["x"]}
stripped = 0
for i, d in D.items():  # keep a kill code only if the source text actually uses it
    if i not in SRC: continue
    for rd in d.get("rounds") or []:
        keep = [c for c in rd.get("codes") or [] if c == "too many missing" or re.search(r"\b" + re.escape(c) + r"\b", SRC[i])]
        stripped += len(rd.get("codes") or []) - len(keep); rd["codes"] = keep
print("codes stripped (not in source):", stripped)
for o in opps:  # fallback: every record links at least its main source file
    R = res.setdefault(o["id"], {"youtube": [], "links": [], "files": []})
    if not R.get("files"):
        f = re.sub(r"\s*§.*$", "", str(o.get("source_file") or "")).strip()
        R["files"] = [f[len("research/"):] if f.startswith("research/") else f] if f else (["koerner-office/analysis/proven_models/PROVEN_MODELS.md"] if o["id"].startswith("X-pm-") else [])
out = {o["id"]: {"d": D.get(o["id"], {}), "res": res.get(o["id"], {})} for o in opps}
json.dump(out, open(here.parent/"details.json", "w"), ensure_ascii=False)
missing = [o["id"] for o in opps if not D.get(o["id"])]
print("details for", len(opps) - len(missing), "/", len(opps), "| missing:", missing[:10], "| extra urls kept", kept, "dropped (not verbatim)", dropped)
