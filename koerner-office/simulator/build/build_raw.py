"""Deterministic join: one raw source bundle per opportunity -> raw_bundles.jsonl
(full source text for the LLM detail pass) + resources.json (every URL + repo paths, no LLM)."""
import csv, json, re, difflib
from pathlib import Path
here = Path(__file__).parent; R = here.parents[2]; A = R/"koerner-office/analysis"
def jl(p): return [json.loads(l) for l in open(p) if l.strip()]
opps = json.load(open(here.parent/"opportunities.json"))["opportunities"]
seen = {r["key"]: r for r in csv.DictReader(open(A/"loop/SEEN.csv"))}
v8 = {r["cid"]: r for r in json.load(open(A/"v8/ideas_scored.json"))}
v8top = {r["cid"]: r for r in json.load(open(A/"v8/top_slice.json"))}
scouts = jl(A/"v8/scouts/scouts.jsonl")
vids = {}
for f in ("videos.csv", "videos_v2.csv"):
    for r in csv.DictReader(open(R/"koerner-office/data"/f)): vids[r["id"]] = r
V = {}
for v in ("v9", "v10"):
    V[v] = dict(leads={r["id"]: r for r in jl(A/v/"leads.jsonl")}, kc={r["id"]: r for r in json.load(open(A/v/"killcheck.json"))["xhigh"]},
                val={r["id"]: r for r in json.load(open(A/v/"validation.json"))},
                scores={m.group(1): m.group(0) for m in re.finditer(r"^\| (L\d+) \|.*$", open(A/v/"SCORES.md").read(), re.M)},
                ev={p.stem: json.load(open(p)) for p in (A/v/"evidence").glob("L*.json")})
chk = json.load(open(A/"v11/checklists.json")); v11val = json.load(open(A/"v11/validation.json"))
te = json.load(open(A/"v11/track_e.json")); te_counts = {c["cluster"]: c for c in te["counts"]["clusters"]}
v8val = open(A/"v8/VALIDATION.md").read()
def fuzzy(name, items, key, th=0.6):
    best, bs = None, 0
    for it in items:
        s = difflib.SequenceMatcher(None, name.lower(), str(it.get(key, "")).lower()).ratio()
        if s > bs: best, bs = it, s
    return best if bs > th else None
def section(text, needle, n=3500):
    i = text.find(needle)
    if i < 0: return ""
    if needle.startswith("#"):  # a heading: take just that section
        e = text.find("\n#", i + len(needle)); return text[i: e if e > 0 else i + n][:n]
    j = text.rfind("\n#", 0, i); j = j if j >= 0 and i - j < 1500 else i - 200
    return text[max(0, j): i + n]
URL = re.compile(r"https?://[^\s\"'<>\)\]\\,;]+")
def ids_of(r):  # ledger keys merged into this record
    out = [r["id"]] + [d.split(" ")[0] for d in r.get("dupes") or []]
    return [k for k in out if k in seen]
bundles, resources = [], {}
for r in opps:
    src, files, yt = {}, set(), []
    for k in ids_of(r):
        s = seen[k]; files.add("koerner-office/" + s["evidence"]); src[f"ledger {k}"] = s
        if re.fullmatch(r"C\d+", k) and k in v8:
            x = v8[k]; files.add("koerner-office/analysis/v8/ideas_scored.csv")
            src[f"v8 cluster {k}"] = {kk: x.get(kk) for kk in ("description","category","n_videos","oldest","newest","stale","specifics_top","uk_legal_reasons","score","fails")}
            src[f"v8 cluster {k}"]["examples"] = [{kk: e.get(kk) for kk in ("video","date","evidence_quality","stated_problem","customer","offer","revenue_model","channels","delivery","claims")} for e in (x.get("examples") or [])[:4]]
            for vid in x.get("videos") or []:
                m = vids.get(vid, {}); yt.append({"url": f"https://www.youtube.com/watch?v={vid}", "label": (m.get("title") or vid) + (f" ({m.get('channel')})" if m.get("channel") else ""), "kind": "youtube", "ts": None})
            if k in v8top: src[f"v8 top slice {k}"] = {kk: v8top[k].get(kk) for kk in ("description","specifics_top")}
            sec = section(v8val, f"### {k}:", 3000) or section(v8val, k)
            if sec: src["v8 VALIDATION.md"] = sec; files.add("koerner-office/analysis/v8/VALIDATION.md")
        if k.startswith("SC"):
            sc = scouts[int(k[2:]) - 1]  # scouts.jsonl is in SC01..SC20 order (checked against SEEN.csv)
            if sc: src["v8 scout"] = sc; files.add("koerner-office/analysis/v8/scouts/scouts.jsonl")
            sec = section(v8val, f"### {k}:", 2500)
            if sec: src["v8 VALIDATION.md"] = sec; files.add("koerner-office/analysis/v8/VALIDATION.md")
        m = re.match(r"V(9|10)-(L\d+)", k)
        if m:
            v, lid = "v" + m.group(1), m.group(2); D = V[v]
            for lab, dd, f in (("lead", D["leads"], "leads.jsonl"), ("kill-check", D["kc"], "killcheck.json"), ("validation", D["val"], "validation.json"), ("deep evidence", D["ev"], f"evidence/{lid}.json")):
                if lid in dd: src[f"{v} {lab}"] = dd[lid]; files.add(f"koerner-office/analysis/{v}/{f}")
            if lid in D["scores"]: src[f"{v} SCORES.md row"] = D["scores"][lid]; files.add(f"koerner-office/analysis/{v}/SCORES.md")
        if k.startswith("V11-B"):
            lid = k.split("-")[-1]
            c = next((x for x in chk if lid in x["url"]), None) or fuzzy(s["name"], chk, "name")
            if c: src["v11 checklist"] = c; files.add("koerner-office/analysis/v11/checklists.json")
            vv = next((x for x in v11val if lid in str(x.get("key", ""))), None)
            if vv: src["v11 validation"] = vv; files.add("koerner-office/analysis/v11/validation.json"); files.add("koerner-office/analysis/v11/VALIDATION.md")
        if k.startswith("V11-E"):
            c = fuzzy(s["name"], te["killcheck"], "cluster") or fuzzy(s["name"], te["killcheck"], "product")
            if c:
                src["v11 Track E kill-check"] = c; files.add("koerner-office/analysis/v11/track_e.json")
                cnt = te_counts.get(c["cluster"], {}); src["v11 Track E evidence counts"] = {kk: cnt.get(kk) for kk in ("complainers","snippets","paying_proof","sources","examples")}
    for f in str(r.get("source_file") or "").split(";"):
        f = re.sub(r"\s*§.*$", "", f.strip())
        if f: files.add(re.sub(r"^research/", "", f) if f.startswith("research/") else ("../" + f if f.startswith("playbooks/") else f))
    blob = json.dumps(src, ensure_ascii=False)
    urls, seen_u = [], set()
    for u in URL.findall(blob):
        u = u.rstrip(".:")
        if u in seen_u or "youtube.com/watch" in u: continue
        seen_u.add(u); urls.append({"url": u, "label": re.sub(r"^www\.", "", u.split("/")[2]), "kind": "flippa" if "flippa.com" in u else "acquire" if "acquire.com" in u else "web"})
    files = sorted(f for f in files if f and not f.endswith("/"))
    resources[r["id"]] = {"youtube": yt, "links": urls, "files": files}
    bundles.append({"id": r["id"], "name": r["name"], "x": r["id"].startswith("X-"), "source_file": r.get("source_file"), "src": blob[:14000]})
with open(here/"raw_bundles.jsonl", "w") as f:
    for b in bundles: f.write(json.dumps(b, ensure_ascii=False) + "\n")
json.dump(resources, open(here/"resources.json", "w"), ensure_ascii=False)
import collections
print(len(bundles), "bundles;", sum(len(b["src"]) for b in bundles) // 1000, "k chars;", collections.Counter(len(b["src"]) // 3000 * 3000 for b in bundles))
print("with youtube", sum(1 for v in resources.values() if v["youtube"]), "with links", sum(1 for v in resources.values() if v["links"]), "total links", sum(len(v["links"]) for v in resources.values()))
