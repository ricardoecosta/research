#!/usr/bin/env python3
"""Aggregate clusters into the idea catalogue and score them.
Stage 1 (python): dossiers + preliminary scores for every cluster.
Stage 2 (Claude): judge a shortlist (automation parts, UK-legal acquisition, realism, market headroom).
Writes analysis/v7/ideas_catalogue.{json,md}, scores/*.json, ideas_scored.csv."""
import concurrent.futures as cf, csv, json, statistics as st, sys
from collections import Counter, defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import *

SC = V7 / "scores"; SC.mkdir(exist_ok=True)
PARTS = ["acquisition", "onboarding", "delivery", "billing", "support"]
W = {"acquisition": .30, "onboarding": .15, "delivery": .25, "billing": .10, "support": .20}
EV = {"A": 5, "B": 4, "C": 2.5, "D": 1}
MODEL = "opus"


def src_score(n):
    return 1 if n <= 1 else 2 if n == 2 else 3 if n <= 4 else 4 if n <= 7 else 5


def build():
    recs = {json.loads(l)["video"]["id"]: json.loads(l) for l in open(V7 / "learnings.jsonl")}
    clusters = json.loads((V7 / "clusters" / "membership.json").read_text())
    cat = []
    for c in clusters:
        mem = []
        for k in c["member_keys"]:
            vid, lid = k.split(":")
            r = recs[vid]
            i = next(x for x in r["ideas"] if x["local_id"] == lid)
            mem.append((r, i))
        vids = sorted({r["video"]["id"] for r, _ in mem})
        chans = sorted({r["video"]["channel"] for r, _ in mem})
        subst = [(r, i) for r, i in mem if i["depth"] != "mention"]
        best = max([EV.get((r.get("evidence_quality") or {}).get("rating"), 1) for r, _ in subst] or [1])
        claims = []
        for r, i in mem:
            for m in r["metric_claims"]:
                if m.get("idea_local_id") == i["local_id"]:
                    claims.append({"video": r["video"]["id"], "claim": m["claim"], "first_hand": m["first_hand"],
                                   "hypothetical": m.get("hypothetical"), "quote": m["quote"]["text"], "verified": m["quote"].get("verified")})
        fh = [x for x in claims if x["first_hand"] and not x.get("hypothetical")]
        E = min(5, best + (0.5 if len(fh) >= 2 else 0)) if subst else 1
        S = src_score(len(vids))
        med = lambda xs: round(st.median(xs), 1) if xs else None
        pool = subst or mem
        auto = {p: med([i["automation"][p]["score_e"] for _, i in pool]) for p in PARTS}
        uk = med([i["uk_applicability"]["score_e"] for _, i in pool])
        auto_pct = round(100 * sum(W[p] * auto[p] / 5 for p in PARTS))
        acq = Counter(ch["channel"] for _, i in mem for ch in i["acquisition_channels"])
        d = {"cid": c["cid"], "name": c["name"], "description": c["description"], "category": c["category"],
             "n_videos": len(vids), "n_channels": len(chans), "videos": vids, "channels": chans,
             "depth": dict(Counter(i["depth"] for _, i in mem)), "best_evidence": best,
             "E_evidence": E, "S_sources": S, "auto_parts_extractor_median": auto, "auto_pct_prelim": auto_pct,
             "uk_extractor_median": uk, "acquisition_channels": dict(acq.most_common()),
             "claims": claims[:40], "n_first_hand_claims": len(fh),
             "members": [{"key": f"{r['video']['id']}:{i['local_id']}", "name": i["name"], "depth": i["depth"],
                          "evidence": (r.get("evidence_quality") or {}).get("rating"), "title": r["video"]["title"],
                          "channel": r["video"]["channel"]} for r, i in mem],
             "detail": [{"video": r["video"]["id"], "customer": i["customer"], "offer": i["offer"], "pricing": i["pricing"],
                         "acquisition": [f"{x['channel']}: {x['details']}" for x in i["acquisition_channels"]],
                         "delivery": i["delivery"], "startup_cost": i["startup_cost"], "tools": i["tools"],
                         "risks": i["risks"], "uk_notes": i["uk_applicability"]["notes"],
                         "auto_how": {p: i["automation"][p]["how"] for p in PARTS}} for r, i in (subst or mem)[:8]]}
        d["prelim_success"] = round(100 * (0.30 * E + 0.20 * S + 0.30 * (uk or 0) + 0.20 * 3) / 5)
        cat.append(d)
    return cat


JSYS = """You are a rigorous venture analyst scoring business ideas for Ricardo: a technical, UK-based (Bromley, London) solo part-timer with a toddler (~6-8 h/week), budget for a test of ~£300, who wants a business an AI-agent team can run with him only approving things.
For each idea dossier (aggregated from podcast transcripts; all money figures are speaker CLAIMS), score with justification:
- automation, five parts 0-5 each: acquisition, onboarding, delivery, billing, support. 0 = a human every time; 3 = agents do most with routine human checks; 5 = unattended software. Physical-world work caps delivery at 0-1. ACQUISITION MUST BE UK-LEGAL: UK PECR bans unsolicited marketing SMS/WhatsApp/social DMs/emails to individuals and sole traders without consent (cold email to limited companies is allowed; cold calls need TPS/CTPS screening and a human). If the idea only works via in-person or cold outreach to consumers/sole traders, acquisition <= 1. Inbound channels (SEO, app stores, marketplaces like Etsy/Apify/Shopify, paid ads, content, affiliates) can score high; note platform-dependence.
- legal_acquisition: "inbound_ok" | "b2b_cold_email_ok" | "needs_human_outreach" | "doubtful".
- R_realism 0-5: realistic for this person in the UK (capital, hours, skills, regulation, UK market/demand, AI substitutes).
- M_headroom 0-5: market and competition headroom in 2026 (saturation, AI commoditisation, platform risk).
- E_adjust: -1, 0 or +1 adjustment to the computed evidence score if the claims look inflated, promotional, hypothetical (-1) or unusually well-corroborated (+1).
- one_line: why it is or is not attractive for an agent-run UK business. Mark your own estimates [E].
OUTPUT JSON only: {"scores":[{"cid":"...","automation":{"acquisition":{"score":n,"why":"..."},"onboarding":{...},"delivery":{...},"billing":{...},"support":{...}},"legal_acquisition":"...","R_realism":n,"R_why":"...","M_headroom":n,"M_why":"...","E_adjust":n,"one_line":"..."}]}"""


def dossier_text(d):
    det = d["detail"][:4]
    claims = [c for c in d["claims"] if c["first_hand"]][:6] or d["claims"][:4]
    return json.dumps({"cid": d["cid"], "name": d["name"], "description": d["description"], "category": d["category"],
                       "n_videos": d["n_videos"], "channels": d["channels"], "evidence_score_computed": d["E_evidence"],
                       "acquisition_channels_seen": d["acquisition_channels"],
                       "claims": [{"claim": c["claim"], "first_hand": c["first_hand"], "hypothetical": c["hypothetical"]} for c in claims],
                       "examples": [{k: (v if k not in ("pricing",) else {"model": v.get("model"), "points": v.get("price_points", [])[:3]}) for k, v in x.items() if k != "auto_how"} for x in det],
                       "extractor_automation_median": d["auto_parts_extractor_median"], "extractor_uk_median": d["uk_extractor_median"]},
                      ensure_ascii=False)


def judge(batch, tag):
    p = SC / f"{tag}.json"
    if p.exists():
        return json.loads(p.read_text())
    prompt = "IDEA DOSSIERS:\n" + "\n\n".join(dossier_text(d) for d in batch) + "\n\nScore every dossier now (JSON only)."
    for _ in range(2):
        res = run_claude(prompt, JSYS, model=MODEL)
        try:
            data = parse_json_text(res["result"]); log_cost("score", tag, MODEL, res, "ok")
            p.write_text(json.dumps(data, ensure_ascii=False, indent=1)); return data
        except Exception:
            log_cost("score", tag, MODEL, res, "fail")
    return {"scores": []}


def finalize_scores(cat):
    js = {}
    for p in SC.glob("judge_*.json"):
        for s in json.loads(p.read_text()).get("scores", []):
            js[s["cid"]] = s
    for d in cat:
        s = js.get(d["cid"])
        if s:
            parts = {k: s["automation"][k]["score"] for k in PARTS}
            d["judge"] = s
            d["automation_pct"] = round(100 * sum(W[k] * parts[k] / 5 for k in PARTS))
            E = max(1, min(5, d["E_evidence"] + s.get("E_adjust", 0)))
            d["success"] = round(100 * (0.30 * E + 0.20 * d["S_sources"] + 0.30 * s["R_realism"] + 0.20 * s["M_headroom"]) / 5)
            d["combined"] = round(0.55 * d["success"] + 0.45 * d["automation_pct"], 1)
            d["scored_by"] = "judge"
        else:
            d["automation_pct"] = d["auto_pct_prelim"]; d["success"] = d["prelim_success"]
            d["combined"] = round(0.55 * d["success"] + 0.45 * d["automation_pct"], 1); d["scored_by"] = "prelim"
    cat.sort(key=lambda d: (-(d["scored_by"] == "judge"), -d["combined"]))
    return cat


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    cat = build()
    (V7 / "clusters" / "dossiers.json").write_text(json.dumps(cat, ensure_ascii=False, indent=1))
    short = [d for d in cat if d["auto_pct_prelim"] >= 50 and (d["n_videos"] >= 2 or d["E_evidence"] >= 4)]
    short.sort(key=lambda d: -(d["auto_pct_prelim"] + d["prelim_success"]))
    print(len(cat), "clusters;", len(short), "shortlisted for judging", flush=True)
    if stage in ("all", "judge"):
        batches = [short[i:i + 8] for i in range(0, len(short), 8)]
        with cf.ThreadPoolExecutor(4) as ex:
            list(ex.map(lambda b: judge(b[1], f"judge_{b[0]:03d}"), enumerate(batches)))
    cat = finalize_scores(cat)
    (V7 / "ideas_scored.json").write_text(json.dumps(cat, ensure_ascii=False, indent=1))
    with open(V7 / "ideas_scored.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "cid", "name", "category", "combined", "success", "automation_pct", "scored_by", "n_videos", "n_channels",
                    "E", "S", "R", "M", "legal_acquisition", "acq", "onb", "del", "bill", "sup", "videos"])
        for n, d in enumerate(cat, 1):
            j = d.get("judge") or {}
            a = {k: (j.get("automation", {}).get(k, {}).get("score") if j else d["auto_parts_extractor_median"][k]) for k in PARTS}
            w.writerow([n, d["cid"], d["name"], d["category"], d["combined"], d["success"], d["automation_pct"], d["scored_by"],
                        d["n_videos"], d["n_channels"], d["E_evidence"], d["S_sources"], j.get("R_realism"), j.get("M_headroom"),
                        j.get("legal_acquisition"), *[a[k] for k in PARTS], " ".join(d["videos"])])
    print("scored", sum(1 for d in cat if d["scored_by"] == "judge"))


if __name__ == "__main__":
    guarded(main)
