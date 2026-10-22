#!/usr/bin/env python3
"""Build the consolidated dataset (learnings.jsonl), flat idea table (ideas_flat.jsonl/csv),
and the browsable INDEX.md from analysis/v7/transcripts/*.json."""
import csv, json, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import *

AUTO_W = {"acquisition": .30, "onboarding": .15, "delivery": .25, "billing": .10, "support": .20}


def auto_pct(a):
    try:
        return round(100 * sum(AUTO_W[k] * a[k]["score_e"] / 5 for k in AUTO_W))
    except Exception:
        return None


def main():
    recs = [json.loads(p.read_text()) for p in sorted(OUT.glob("*.json"))]
    recs.sort(key=lambda r: (r["video"].get("upload_date") or "0000", r["video"]["id"]), reverse=True)
    with open(V7 / "learnings.jsonl", "w") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    flat = []
    for r in recs:
        v = r["video"]
        for i in r.get("ideas", []):
            flat.append({"key": f"{v['id']}:{i['local_id']}", "video_id": v["id"], "channel": v["channel"],
                         "upload_date": v.get("upload_date"), "evidence": (r.get("evidence_quality") or {}).get("rating"),
                         "name": i["name"], "one_liner": i["one_liner"], "category": i["category"],
                         "business_model": i["business_model"], "customer": i["customer"], "depth": i["depth"],
                         "is_primary": i["is_primary"], "auto_pct_e": auto_pct(i["automation"]),
                         **{f"auto_{k}": i["automation"][k]["score_e"] for k in AUTO_W},
                         "uk_e": i["uk_applicability"]["score_e"],
                         "channels": "|".join(c["channel"] for c in i["acquisition_channels"])})
    with open(V7 / "ideas_flat.jsonl", "w") as f:
        for x in flat:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    with open(V7 / "ideas_flat.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(flat[0].keys())); w.writeheader(); w.writerows(flat)
    # INDEX
    nq = sum(r["extraction"]["quote_verification"]["quotes"] or 0 for r in recs)
    nv = sum(r["extraction"]["quote_verification"]["verified"] or 0 for r in recs)
    ev = Counter((r.get("evidence_quality") or {}).get("rating") for r in recs)
    ch = Counter(r["video"]["channel"] for r in recs)
    L = ["# v7 transcript learnings: index\n",
         f"{len(recs)} transcripts mined · {len(flat)} idea mentions · {sum(len(r['metric_claims']) for r in recs)} metric claims · "
         f"{sum(len(r['lessons']) for r in recs)} lessons · {sum(len(r['tactics']) for r in recs)} tactics · quotes verified verbatim {nv}/{nq} ({100*nv/max(nq,1):.1f}%) · "
         f"reviewed by Opus: {sum(1 for r in recs if r['extraction'].get('reviewed_by'))}\n",
         "Evidence quality: " + ", ".join(f"{k}: {ev[k]}" for k in "ABCD") + "  ",
         "(A = first-hand operator with specific numbers; B = first-hand but vague; C = second-hand/listicle/promotional; D = speculative or poor transcript)\n",
         "Channels: " + ", ".join(f"{k} ({n})" for k, n in ch.most_common()) + "\n",
         "Each row links to the readable note (`transcripts/<id>.md`); the structured record is `transcripts/<id>.json` (schema: `schema/transcript_learnings.schema.json`).\n",
         "| Uploaded | Channel | Title | Ideas (deep/moderate/mention) | Top idea | Ev. | Quotes ✓ | Note |", "|---|---|---|---|---|---|---|---|"]
    for r in recs:
        v = r["video"]; ideas = r.get("ideas", [])
        d = Counter(i["depth"] for i in ideas)
        prim = next((i["name"] for i in ideas if i.get("is_primary")), ideas[0]["name"] if ideas else "—")
        qv = r["extraction"]["quote_verification"]
        t = v["title"].replace("|", "/")
        L.append(f"| {v.get('upload_date') or '?'} | {v['channel']} | [{t}]({v['url']}) | {len(ideas)} ({d['deep']}/{d['moderate']}/{d['mention']}) | "
                 f"{prim.replace('|','/')} | {(r.get('evidence_quality') or {}).get('rating')} | {qv['verified']}/{qv['quotes']} | [note](transcripts/{v['id']}.md) |")
    (V7 / "INDEX.md").write_text("\n".join(L) + "\n")
    print(len(recs), "records,", len(flat), "ideas")


if __name__ == "__main__":
    main()
