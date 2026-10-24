"""tagged/*.json + extras.json -> ../opportunities.json (deduped), then inject into ../index.html."""
import json, csv, re, difflib, glob
from pathlib import Path
here = Path(__file__).parent; A = here.parents[1] / "analysis"
seen = {r["key"]: r for r in csv.DictReader(open(A/"loop/SEEN.csv"))}
recs = []
for f in sorted(glob.glob(str(here/"tagged/batch_*.json"))):
    for r in json.load(open(f))["records"]:
        s = seen.get(r["id"], {})
        r["source_round"] = s.get("first_seen"); r["source_file"] = "research/koerner-office/" + s.get("evidence", "")
        r["ledger"] = {"source": s.get("source"), "verdict": s.get("verdict"), "confidence": s.get("confidence"), "reason": s.get("reason")}
        recs.append(r)
extras = json.load(open(here/"extras.json"))["records"]
patch = json.load(open(here/"patch.json"))
P = {p["id"]: p for p in patch["patch"]}
P["X-amazon-author-review-saas-acquisition"]["same_as"] = ["V11-B-14387997"]  # manual fix (spot-check)
for x in extras: x.update({k: v for k, v in P.get(x["id"], {}).items() if k != "id"})
extras += [dict(n, same_as=n.get("same_as") or []) for n in patch["new"]]
byid = {r["id"]: r for r in recs}
for x in extras:
    x.setdefault("dupes", [])
    for k in x.get("same_as") or []:
        if k in byid:
            old = byid.pop(k); x["dupes"].append(f"{k} ({old['name']})")
            x["verdicts"] = (old.get("verdicts") or []) + (x.get("verdicts") or [])
    x.pop("same_as", None)
recs = list(byid.values())
# fuzzy within-ledger dedupe (same opportunity re-seen in a later round)
norm = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower())
out = []
for r in recs:
    hit = next((o for o in out if difflib.SequenceMatcher(None, norm(o["name"]), norm(r["name"])).ratio() >= 0.9), None)
    if hit:
        hit.setdefault("dupes", []).append(f"{r['id']} ({r['name']})"); hit["verdicts"] += r.get("verdicts") or []
    else: out.append(r)
out += extras
from enforce import enforce
nfix = sum(enforce(r, r.get("ledger") or {}) for r in out)
print("deterministic overrides:", nfix)
for r in out:
    for k, c in (r.get("c") or {}).items():
        if not isinstance(c, dict): r["c"][k] = c = {"s": "unknown", "v": None, "r": ""}
        c.setdefault("f", r.get("source_file"))
        if isinstance(c.get("v"), str) and re.fullmatch(r"-?\d+(\.\d+)?", c["v"].strip()): c["v"] = float(c["v"])
        if c.get("s") not in ("pass", "soft", "hard", "unknown"):
            v = c.get("v")
            c["s"] = {"none": "pass", "lawful_cold": "soft", "unlawful_cold": "hard"}.get(v, "unknown") if k == "outreach" else ("unknown" if v is None else "soft")
    # buy-track budget: asking price in £ if missing
meta = json.load(open(here/"meta.json"))
meta["subtitle"] = f"{len(out)} opportunities consolidated from v1–v11 reports, proven models, backlog, SMB AI-gap notes and playbooks · built {meta['built']}"
data = {"meta": meta, "opportunities": out}
(here.parent/"opportunities.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
tpl = (here/"template.html").read_text()
(here.parent/"index.html").write_text(tpl.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print(len(recs), "ledger after id-merge;", len(out), "total;", len(extras), "extras")
