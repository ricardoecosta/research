"""Join every SEEN.csv row with its structured source records -> contexts.jsonl (one compact context per opportunity)."""
import csv, json, re, difflib
from pathlib import Path
A = Path(__file__).resolve().parents[2] / "analysis"
def jl(p): return [json.loads(l) for l in open(p) if l.strip()]
def short(x, n=2200):
    s = json.dumps(x, ensure_ascii=False) if not isinstance(x, str) else x
    return s[:n]
seen = list(csv.DictReader(open(A/"loop/SEEN.csv")))
v8 = {r["cid"]: r for r in csv.DictReader(open(A/"v8/ideas_scored.csv"))}
v8top = {r["cid"]: r for r in json.load(open(A/"v8/ideas_scored.json"))}
scouts = jl(A/"v8/scouts/scouts.jsonl")
def by_id(lst): return {r.get("id"): r for r in lst}
R = {}
for v in ("v9", "v10"):
    kc = json.load(open(A/v/"killcheck.json"))
    R[v] = dict(leads=by_id(jl(A/v/"leads.jsonl")), kc=by_id(kc["xhigh"]), val=by_id(json.load(open(A/v/"validation.json"))),
               scores={m.group(1): m.group(0) for m in re.finditer(r"^\| (L\d+) \|.*$", open(A/v/"SCORES.md").read(), re.M)})
chk = json.load(open(A/"v11/checklists.json"))
te = json.load(open(A/"v11/track_e.json")); te_kc = te["killcheck"]; te_counts = {c["cluster"]: c for c in te["counts"]["clusters"]}
v11val = json.load(open(A/"v11/validation.json"))
def fuzzy(name, items, key):
    best, bs = None, 0
    for it in items:
        s = difflib.SequenceMatcher(None, name.lower(), str(it.get(key, "")).lower()).ratio()
        if s > bs: best, bs = it, s
    return best if bs > 0.6 else None
def grep(path, needle, n=1800):
    try: t = open(A.parent/path).read()
    except Exception: return ""
    i = t.find(needle)
    if i < 0: i = t.lower().find(needle.lower()[:30])
    return t[max(0, i-100): i+n] if i >= 0 else ""
out = []
for r in seen:
    k, ctx = r["key"], {}
    if re.fullmatch(r"C\d+", k):
        x = v8.get(k, {}); ctx["v8_scored"] = {c: x.get(c) for c in ("category","n_videos","success_12m","agent_runnability","fit","automation_share","hours_per_week","local","face","uk_legal_risk","physical","stale","newest","fails","one_line")}
        if k in v8top: ctx["v8_top"] = {"description": v8top[k].get("description"), "score_why": {z: (v8top[k].get("score") or {}).get(z) for z in ("success_why","fit_why","automation_why","uk_legal_reason")}, "examples": [{"date": ex.get("date"), "q": ex.get("evidence_quality"), "customer": ex.get("customer"), "channels": ex.get("channels"), "claims": [c.get("claim") for c in (ex.get("claims") or []) if c.get("first_hand") or "$" in str(c.get("claim"))][:3]} for ex in (v8top[k].get("examples") or [])[:2]]}
    elif k.startswith("SC"):
        ctx["scout"] = fuzzy(r["name"], scouts, "name")
    m = re.match(r"V(9|10)-(L\d+)", k)
    if m:
        v, lid = "v"+m.group(1), m.group(2)
        ctx.update(lead=R[v]["leads"].get(lid), killcheck=R[v]["kc"].get(lid), score_row=R[v]["scores"].get(lid), validation=R[v]["val"].get(lid))
    if k.startswith("V11-B"):
        c = fuzzy(r["name"], chk, "name")
        if c: ctx["checklist"] = {kk: c.get(kk) for kk in ("name","category","asking_price_usd","monthly_revenue_usd","monthly_profit_usd","verification","rows","pass","hard_fails")}
        ctx["validation"] = fuzzy(r["name"], v11val, "name")
    if k.startswith("V11-E"):
        c = fuzzy(r["name"], te_kc, "cluster") or fuzzy(r["name"], te_kc, "product")
        if c: ctx["killcheck"] = {kk: c.get(kk) for kk in ("cluster","product","verdict","kill_rule","time_to_moat","launches_last_6m","incumbents","reason")}; ctx["counts"] = {kk: te_counts.get(c["cluster"], {}).get(kk) for kk in ("complainers","paying_proof")}
    ctx = {a: b for a, b in ctx.items() if b}
    if not ctx: ctx["excerpt"] = grep(r["evidence"], r["name"])
    out.append({"id": k, "seen": r, "context": short(ctx, 3500)})
with open(Path(__file__).parent/"contexts.jsonl", "w") as f:
    for o in out: f.write(json.dumps(o, ensure_ascii=False) + "\n")
print(len(out), sum(1 for o in out if '"excerpt"' in o["context"]), "excerpt-only")
