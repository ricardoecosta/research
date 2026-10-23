#!/usr/bin/env python3
"""v8 step 6: sampled quote verification per miner (rapidfuzz, 90/100), escalation, citation-line check,
plus shadow comparison (sampled vs full) on the first batch. Writes analysis/v8/qc/quote_*.
Usage: verify.py            (sampled run over all mined files)
       verify.py --full ID,ID  (full check of the given idea ids; used for the top slice)"""
import collections, csv, json, random, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common8 import *
from rapidfuzz import fuzz

QC = V8 / "qc"; QC.mkdir(parents=True, exist_ok=True)
_cache = {}


def tx(vid):
    if vid not in _cache:
        meta, body, rows = numbered(vid, load_dates())
        _cache[vid] = (norm(body), {r["line"]: norm(r["text"]) for r in rows})
    return _cache[vid]


def score(text, hay):
    frags = [norm(f) for f in re.split(r"\.\.\.|\u2026", text or "") if len(norm(f)) >= 12] or [norm(text or "")]
    return min(fuzz.partial_ratio(f, hay) for f in frags) if frags and frags[0] else 0


def quotes_of(rec):
    for i in rec["ideas"]:
        sp = i.get("stated_problem")
        if isinstance(sp, dict) and sp.get("quote"): yield i["idea_id"], "stated_problem", sp
        for k, q in enumerate(i.get("key_quotes") or []):
            if q.get("quote"): yield i["idea_id"], f"key_quotes[{k}]", q
        for k, q in enumerate(i.get("claims") or []):
            if q.get("quote"): yield i["idea_id"], f"claims[{k}]", q


def check(vid, q):
    body, lines = tx(vid)
    s = score(q["quote"], body)
    try: ln = int(q.get("line"))
    except Exception: ln = None
    win = " ".join(lines.get(l, "") for l in range(ln - 2, ln + 3)) if ln else ""
    ls = score(q["quote"], win) if win else 0
    return round(s, 1), s >= 90, (ls >= 90) if s >= 90 else None


def load():
    recs = [json.loads(p.read_text()) for p in sorted((V8 / "mined").glob("*.json"))]
    return sorted(recs, key=lambda r: (r["miner"].split(":")[0], r["mined_at"], r["id"]))


def main_sampled():
    recs = load()
    bym = collections.defaultdict(list)
    for r in recs: bym[r["miner"].split(":")[0] + (":" + r["miner"].split(":")[1] if ":" in r["miner"] else "")].append(r)
    rng = random.Random(8)
    status, rows, summ = {}, [], []
    for miner, rs in bym.items():
        for b in range(0, len(rs), 25):
            batch = rs[b:b + 25]; bid = f"{miner}#b{b // 25:02d}"
            allq = [(r["id"], iid, path, q) for r in batch for iid, path, q in quotes_of(r)]
            samp = allq if len(allq) <= 40 else rng.sample(allq, 40)
            res = [(x, *check(x[0], x[3])) for x in samp]
            rate = sum(ok for _, _, ok, _ in res) / max(len(res), 1)
            escalated = rate < 0.95
            if escalated:
                res = [(x, *check(x[0], x[3])) for x in allq]
            checked = {(x[1], x[2]) for x, *_ in res}
            for x, sc, ok, lok in res:
                status[f"{x[1]}|{x[2]}"] = dict(status="verified" if ok else "unverified", score=sc, line_ok=lok, batch=bid)
                rows.append([bid, x[0], x[1], x[2], sc, ok, lok, x[3]["quote"][:160]])
            for vid, iid, path, q in allq:
                if (iid, path) not in checked:
                    status[f"{iid}|{path}"] = dict(status="batch_certified" if not escalated else "unverified", score=None, line_ok=None, batch=bid)
            n_ok = sum(ok for _, _, ok, _ in res); n_line_bad = sum(1 for _, _, ok, lok in res if ok and lok is False)
            summ.append(dict(batch=bid, transcripts=len(batch), quotes_total=len(allq), sampled=len(samp), checked=len(res),
                             pass_rate=round(100 * n_ok / max(len(res), 1), 1), sample_rate=round(100 * rate, 1),
                             escalated=escalated, citation_line_misses=n_line_bad))
    with open(QC / "quote_checks.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["batch", "video", "idea_id", "field", "score", "verified", "cited_line_ok", "quote"]); w.writerows(rows)
    (QC / "quote_status.json").write_text(json.dumps(status, indent=0))
    with open(QC / "quote_batches.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summ[0])); w.writeheader(); w.writerows(summ)
    tot_c = sum(s["checked"] for s in summ); tot_ok = sum(round(s["pass_rate"] * s["checked"] / 100) for s in summ)
    # shadow: first batch of the first miner, full vs sampled
    m0 = next(iter(bym)); first = bym[m0][:25]
    allq = [(r["id"], iid, path, q) for r in first for iid, path, q in quotes_of(r)]
    full = [check(x[0], x[3])[1] for x in allq]
    full_rate = 100 * sum(full) / max(len(full), 1)
    s0 = summ[0]["sample_rate"]
    dec = "KEEP sampling" if abs(full_rate - s0) <= 2 else "REVERT to full checks"
    (QC / "shadow_quotes.md").write_text(
        f"# Shadow comparison: sampled vs full quote check\n\nBatch {summ[0]['batch']} ({len(first)} transcripts, {len(allq)} quotes).\n\n"
        f"- Sampled ({summ[0]['sampled']} quotes): {s0}% pass\n- Full ({len(full)} quotes): {full_rate:.1f}% pass\n\n"
        f"Rule: revert to full checks if the rates differ by more than 2 points.\n\n**Decision: {dec}.**\n")
    lines = ["# Quote verification (step 6, sampled)", "", f"Checked {tot_c} quotes across {len(summ)} miner batches; pass rate {100 * tot_ok / max(tot_c, 1):.1f}% at 90/100.",
             f"Escalated batches: {sum(s['escalated'] for s in summ)}. Citation-line misses among passing quotes: {sum(s['citation_line_misses'] for s in summ)}.",
             f"Shadow (sampled vs full, first batch): {s0}% vs {full_rate:.1f}% -> {dec}.", "", "| batch | transcripts | quotes | checked | pass % | escalated | line misses |", "|---|---|---|---|---|---|---|"]
    lines += [f"| {s['batch']} | {s['transcripts']} | {s['quotes_total']} | {s['checked']} | {s['pass_rate']} | {s['escalated']} | {s['citation_line_misses']} |" for s in summ]
    (QC / "QUOTE_VERIFICATION.md").write_text("\n".join(lines)); print("\n".join(lines[:6]))


def main_full(ids):
    ids = set(ids); recs = load(); out = {}
    for r in recs:
        for iid, path, q in quotes_of(r):
            if iid in ids:
                sc, ok, lok = check(r["id"], q); out[f"{iid}|{path}"] = dict(status="verified" if ok else "unverified", score=sc, line_ok=lok, batch="topslice_full")
    return out


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].startswith("--full"):
        ids = sys.argv[1].split("=", 1)[1].split(",") if "=" in sys.argv[1] else sys.argv[2].split(",")
        print(json.dumps(main_full(ids), indent=1))
    else:
        main_sampled()
