#!/usr/bin/env python3
"""v8 steps 8-9: dossiers for every cluster, Codex xhigh scoring (4 separate scores + flags), staleness,
automation distribution, and the top slice for step 10 (not a shortlist). Requires the completeness gate.
Writes analysis/v8/clusters/dossiers.json, scores/*.json, ideas_scored.{json,csv}, AUTOMATION_DISTRIBUTION.md, TOP_SLICE.md."""
import collections, concurrent.futures as cf, csv, json, statistics as st, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common8 import *

LOGF = WORK / "score.log"
SC = V8 / "scores"; SC.mkdir(parents=True, exist_ok=True)
JSYS = """You are a rigorous venture analyst. You do not run commands or browse; everything is below. Score business-idea clusters (aggregated from podcast transcripts; all money figures are speaker CLAIMS, quotes marked unverified are excluded) for Ricardo:
technical, UK-based (London/Bromley), solo, part-time (at most ~5 h/week for the business), small test budget (~GBP 300), wants high automation by an AI-agent team (he approves things), and ideas he would enjoy. HARD CONSTRAINTS he set: no selling to local businesses; nothing needing his face or personal brand; UK PECR (no cold SMS/WhatsApp/DMs to individuals or sole traders; cold email only to limited companies).
Score each cluster with a short reason per score. Keep the scores separate.
- success_12m (0-10): realistic odds of meaningful revenue (say GBP 1k+/month) within 12 months for Ricardo in the UK, given evidence strength (distinct videos, first-hand claims), competition and AI commoditisation in late 2026, capital and regulation.
- agent_runnability (0-10): how much of the day-to-day an AI-agent team can run (acquisition, onboarding, delivery, billing, support). Physical-world work and in-person sales score low.
- fit (0-10): fit with Ricardo's skills, interests, hours and hard constraints (breaking a hard constraint caps fit at 3).
- automation_share (0-100): realistic % of ALL work automated, including sales, support and admin, not just the core product. Be strict; earlier low-effort passes overestimated by 15-40 points.
- hours_per_week: Ricardo's realistic weekly hours once running.
- flags: sells_to_local_businesses, needs_face_or_personal_brand, uk_legal_risk (acquisition relies on PECR-banned channels), physical_world (booleans) and uk_legal_reason.
- staleness_note: if the evidence is old (stale=true) or rests on specific tools/prices/platforms, say what must be rechecked.
Mark your own estimates [E].
OUTPUT JSON only: {"scores":[{"cid":"...","success_12m":n,"success_why":"...","agent_runnability":n,"agent_why":"...","fit":n,"fit_why":"...","automation_share":n,"automation_why":"...","hours_per_week":n,"sells_to_local_businesses":bool,"needs_face_or_personal_brand":bool,"uk_legal_risk":bool,"uk_legal_reason":"... or null","physical_world":bool,"staleness_note":"...","one_line":"..."}]}"""


def qstatus():
    p = V8 / "qc" / "quote_status.json"
    return json.loads(p.read_text()) if p.exists() else {}


def build():
    flat = {json.loads(l)["key"]: json.loads(l) for l in open(V8 / "ideas_flat.jsonl")}
    cl = json.loads((V8 / "clusters" / "membership.json").read_text())
    qs = qstatus()
    ev_ok = lambda key, path: qs.get(f"{key}|{path}", {}).get("status", "unchecked") in ("verified", "batch_certified")
    out = []
    for c in cl:
        mem = [flat[k] for k in c["member_keys"] if k in flat]
        vids = sorted({m["video_id"] for m in mem}); dates = sorted(m["publish_date"] for m in mem)
        firsts, seen = [], set()
        for m in sorted(mem, key=lambda m: (m["depth"] != "deep", m["publish_date"]), reverse=False):
            if m["video_id"] not in seen: firsts.append(m); seen.add(m["video_id"])
        ex = []
        for m in firsts[:6]:
            sp = m.get("stated_problem")
            ex.append(dict(video=m["video_id"], date=m["publish_date"], evidence_quality=m.get("evidence_quality"),
                           stated_problem=(sp.get("quote") if isinstance(sp, dict) and ev_ok(m["key"], "stated_problem") else None),
                           customer=m["idea"].get("customer"), offer=m["idea"].get("offer"), revenue_model=m["idea"].get("revenue_model"),
                           channels=[f"{a.get('channel')}: {str(a.get('details'))[:120]}" for a in (m.get("acquisition_channels") or [])][:4],
                           delivery=str(m.get("delivery"))[:200],
                           claims=[dict(claim=q.get("claim"), first_hand=q.get("first_hand"), hypothetical=q.get("hypothetical"))
                                   for k, q in enumerate(m.get("claims") or []) if ev_ok(m["key"], f"claims[{k}]")][:4]))
        spec = collections.Counter(s for m in mem for kk in ("tools", "platforms", "prices") for s in (m.get("specifics") or {}).get(kk, []) or [])
        fh_vids = {m["video_id"] for m in mem for k, q in enumerate(m.get("claims") or []) if q.get("first_hand") and not q.get("hypothetical") and ev_ok(m["key"], f"claims[{k}]")}
        tri = [m.get("automation_share_e") for m in mem if isinstance(m.get("automation_share_e"), (int, float))]
        d = dict(cid=c["cid"], name=c["name"], description=c["description"], category=c["category"], n_videos=c["n_videos"],
                 n_mentions=c["n_mentions"], single_video=c["single_video"], videos=vids, channels=sorted({m["channel"] or "" for m in mem}),
                 oldest=dates[0] if dates else None, newest=dates[-1] if dates else None,
                 stale=all(m["publish_date"] < STALE_BEFORE for m in mem), recheck_specifics=any(m.get("specifics_flag") for m in mem),
                 specifics_top=[s for s, _ in spec.most_common(8)], n_first_hand_claim_videos=len(fh_vids),
                 miner_flags=dict(uk_legal_risk=sum(bool((m.get("uk_legal_risk") or {}).get("flag")) for m in mem),
                                  local=sum(bool(m.get("sells_to_local_businesses")) for m in mem),
                                  face=sum(bool(m.get("needs_face_or_personal_brand")) for m in mem),
                                  physical=sum(bool(m.get("physical_world")) for m in mem), n=len(mem)),
                 uk_legal_reasons=list({(m.get("uk_legal_risk") or {}).get("reason") for m in mem if (m.get("uk_legal_risk") or {}).get("flag")})[:3],
                 triage_automation_median=(st.median(tri) if tri else None), examples=ex, member_keys=c["member_keys"])
        out.append(d)
    return out


def dossier_text(d):
    return json.dumps({k: d[k] for k in ("cid", "name", "description", "category", "n_videos", "single_video", "channels", "oldest", "newest",
                                         "stale", "recheck_specifics", "specifics_top", "n_first_hand_claim_videos", "miner_flags", "uk_legal_reasons", "examples")}, ensure_ascii=False)


def judge(tag, batch):
    p = SC / f"{tag}.json"
    if p.exists(): return json.loads(p.read_text())
    prompt = JSYS + "\n\nCLUSTER DOSSIERS:\n" + "\n\n".join(dossier_text(d) for d in batch) + "\n\nScore every dossier now (JSON only)."
    data, runner, secs = call_llm(prompt, "xhigh", LOGF, tag)
    data["_runner"] = runner; p.write_text(json.dumps(data, ensure_ascii=False, indent=1)); log(LOGF, f"{tag} ok {runner} {secs:.0f}s n={len(data.get('scores', []))}")
    return data


def passes(d):
    s = d.get("score") or {}
    why = []
    if (s.get("automation_share") or 0) < 50: why.append("automation<50%")
    if (s.get("hours_per_week") or 99) > 5: why.append("hours>5")
    if s.get("sells_to_local_businesses"): why.append("sells to local businesses")
    if s.get("needs_face_or_personal_brand"): why.append("needs face/personal brand")
    if s.get("uk_legal_risk"): why.append("UK legal risk (PECR)")
    return why


def main():
    if subprocess.run([sys.executable, str(Path(__file__).parent / "gate.py")]).returncode != 0:
        print("GATE CLOSED: refusing to score/rank"); sys.exit(2)
    cat = build()
    (V8 / "clusters" / "dossiers.json").write_text(json.dumps(cat, ensure_ascii=False, indent=1))
    batches = [cat[i:i + 8] for i in range(0, len(cat), 8)]
    log(LOGF, f"START scoring {len(cat)} clusters in {len(batches)} batches")
    with cf.ThreadPoolExecutor(6) as ex:
        futs = [ex.submit(judge, f"judge_{k:04d}", b) for k, b in enumerate(batches)]
        for f in cf.as_completed(futs):
            try: f.result()
            except Exception as e: log(LOGF, f"judge batch failed: {e}")
    js = {}
    for p in sorted(SC.glob("judge_*.json")):
        for s in json.loads(p.read_text()).get("scores", []): js[s.get("cid")] = s
    missing = [d["cid"] for d in cat if d["cid"] not in js]
    if missing:  # one retry pass for clusters the judge skipped
        for k in range(0, len(missing), 8):
            b = [d for d in cat if d["cid"] in set(missing[k:k + 8])]
            try:
                for s in judge(f"judge_retry_{k:04d}", b).get("scores", []): js[s.get("cid")] = s
            except Exception as e: log(LOGF, f"retry failed {e}")
    for d in cat:
        d["score"] = js.get(d["cid"]); d["fails"] = passes(d) if d["score"] else ["unscored"]
    scored = [d for d in cat if d["score"]]
    (V8 / "ideas_scored.json").write_text(json.dumps(cat, ensure_ascii=False, indent=1))
    with open(V8 / "ideas_scored.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["cid", "name", "category", "n_videos", "single_video", "success_12m", "agent_runnability", "fit", "automation_share", "hours_per_week",
                    "local", "face", "uk_legal_risk", "physical", "stale", "recheck_specifics", "newest", "fails", "one_line", "videos"])
        for d in cat:
            s = d["score"] or {}
            w.writerow([d["cid"], d["name"], d["category"], d["n_videos"], d["single_video"], s.get("success_12m"), s.get("agent_runnability"), s.get("fit"),
                        s.get("automation_share"), s.get("hours_per_week"), s.get("sells_to_local_businesses"), s.get("needs_face_or_personal_brand"),
                        s.get("uk_legal_risk"), s.get("physical_world"), d["stale"], d["recheck_specifics"], d["newest"], "; ".join(d["fails"]), s.get("one_line"), " ".join(d["videos"])])
    # step 9: automation distribution
    au = [d["score"]["automation_share"] for d in scored if isinstance(d["score"].get("automation_share"), (int, float))]
    flat = [json.loads(l) for l in open(V8 / "ideas_flat.jsonl")]
    tri = [x["automation_share_e"] for x in flat if isinstance(x.get("automation_share_e"), (int, float))]
    def hist(xs):
        b = collections.Counter(min(int(x // 10) * 10, 90) for x in xs)
        return "\n".join(f"| {k}-{k + 9}% | {b.get(k, 0)} |" for k in range(0, 100, 10))
    thr = lambda xs: " | ".join(f">={t}%: {sum(x >= t for x in xs)}" for t in (40, 50, 60, 70))
    fails = collections.Counter(f for d in scored for f in d["fails"])
    dist = (f"# Automation distribution (step 9)\n\n## Scored clusters (Codex xhigh judge), n={len(au)}\n\nMedian {st.median(au) if au else 'n/a'}%. {thr(au)}\n\n| bin | clusters |\n|---|---|\n{hist(au)}\n\n"
            f"## Miner triage estimates across all {len(tri)} mined ideas (triage only, not used to rank)\n\nMedian {st.median(tri) if tri else 'n/a'}%. {thr(tri)}\n\n| bin | ideas |\n|---|---|\n{hist(tri)}\n\n"
            f"## Which constraint does the killing (scored clusters; a cluster can fail several)\n\n" + "\n".join(f"- {k}: {v}" for k, v in fails.most_common()) +
            f"\n- pass all hard constraints: {sum(not d['fails'] for d in scored)}\n")
    (V8 / "AUTOMATION_DISTRIBUTION.md").write_text(dist)
    # top slice
    key = lambda d: (-d["score"]["success_12m"], -d["score"]["fit"], -d["score"]["agent_runnability"], -d["n_videos"])
    ok = sorted([d for d in scored if not d["fails"]], key=key)
    top = ok[:15]
    cited = sorted(scored, key=lambda d: (-d["n_videos"], -d["n_mentions"]))[:5]
    extra = [d for d in cited if d not in top]
    def row(n, d, tag):
        s = d["score"]
        flags = ", ".join(x for x in [("STALE" if d["stale"] else ""), ("recheck specifics: " + ", ".join(d["specifics_top"][:4]) if d["recheck_specifics"] else ""), ("single video" if d["single_video"] else "")] if x)
        return f"| {n} | {d['cid']} | {d['name']} | {tag} | {s['success_12m']} | {s['agent_runnability']} | {s['fit']} | {s['automation_share']}% | {s['hours_per_week']} | {d['n_videos']} | {'; '.join(d['fails']) or 'passes'} | {flags} |"
    rows = [row(n, d, "rank") for n, d in enumerate(top, 1)] + [row(f"M{n}", d, "most-cited") for n, d in enumerate(extra, 1)]
    md = ("# v8 top slice, ready for high-effort validation (step 10)\n\nNot a shortlist. Nothing here is validated yet. Scores are Codex gpt-6-luna xhigh judge scores, kept separate.\n"
          "Order among clusters passing the hard constraints: success, then fit, then agent-runnability, then distinct videos. Most-cited clusters are added regardless of rank (step 11).\n\n"
          "| # | cid | cluster | why in slice | success /10 | agent /10 | fit /10 | automation | h/week | videos | constraints | staleness / recheck |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n" + "\n".join(rows) +
          f"\n\n{len(scored)} clusters scored; {len(ok)} pass all hard constraints.\n\n## Reasons\n\n" +
          "\n".join(f"- **{d['cid']} {d['name']}**: {d['score'].get('one_line')} Success: {d['score'].get('success_why')} Staleness: {d['score'].get('staleness_note')}" for d in top + extra))
    (V8 / "TOP_SLICE.md").write_text(md)
    (V8 / "top_slice.json").write_text(json.dumps(top + extra, ensure_ascii=False, indent=1))
    log(LOGF, f"END scored={len(scored)}/{len(cat)} pass={len(ok)} slice={len(top) + len(extra)}")


if __name__ == "__main__":
    main()
