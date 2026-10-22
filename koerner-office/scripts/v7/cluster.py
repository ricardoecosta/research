#!/usr/bin/env python3
"""Deduplicate and cluster all idea mentions (ideas_flat.jsonl) into canonical ideas with Claude.
Pass A: per category (chunks of <=260), Pass B: cross-category merge of cluster labels.
Writes analysis/v7/clusters/{passA_*.json, passB.json, membership.json}."""
import concurrent.futures as cf, json, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import *

CDIR = V7 / "clusters"; CDIR.mkdir(exist_ok=True)
MODEL = sys.argv[1] if len(sys.argv) > 1 else "opus"
SYS_A = """You deduplicate business-idea mentions extracted from many podcast transcripts into canonical ideas.
Two mentions belong to the same canonical idea when a founder would run essentially the same business: same core offer to the same kind of customer with the same way of making money. Variations in niche (e.g. different city, slightly different customer sub-segment) stay together when the playbook is the same; split when the delivery or revenue model is materially different (e.g. 'done-for-you agency' vs 'self-serve SaaS' for the same problem are DIFFERENT ideas; 'vending machines' vs 'claw machines' can be one idea 'vending/amusement machines on location' only if the playbook is the same).
Be careful: prefer precise clusters of 1-15 members over giant vague buckets. Every input index must appear in exactly one cluster.
OUTPUT JSON only: {"clusters":[{"name":"short canonical idea name","description":"one sentence: offer, customer, revenue model","members":[indices]}]}"""
SYS_B = """You merge duplicate canonical business-idea clusters produced separately per category. Input: clusters with id, category, name, description, size.
Merge clusters that are the SAME business (same offer, customer, revenue model) even if they were filed under different categories. Do not merge merely related ideas.
OUTPUT JSON only: {"merges":[{"keep":"id","merge":["id",...],"name":"final name","description":"final one sentence"}]} (only list groups that change; clusters not listed stay as they are)."""


def call(prompt, system, tag):
    p = CDIR / f"{tag}.json"
    if p.exists():
        return json.loads(p.read_text())
    for attempt in range(2):
        res = run_claude(prompt, system, model=MODEL)
        try:
            data = parse_json_text(res["result"])
            log_cost("cluster", tag, MODEL, res, "ok")
            p.write_text(json.dumps(data, ensure_ascii=False, indent=1))
            return data
        except Exception as e:
            log_cost("cluster", tag, MODEL, res, "fail")
    raise RuntimeError(f"cluster call failed: {tag}")


def main():
    flat = [json.loads(l) for l in open(V7 / "ideas_flat.jsonl")]
    bycat = defaultdict(list)
    for i, x in enumerate(flat):
        bycat[x["category"]].append(i)
    jobs = []
    for cat, idxs in sorted(bycat.items()):
        n = max(1, -(-len(idxs) // 260))
        size = -(-len(idxs) // n)
        for c in range(n):
            chunk = idxs[c * size:(c + 1) * size]
            lines = [f"{i} | {flat[i]['name']} — {flat[i]['one_liner']} | customer: {flat[i]['customer'][:100]} | model: {flat[i]['business_model'][:80]}" for i in chunk]
            jobs.append((f"passA_{cat}_{c}", cat, chunk, "CATEGORY: " + cat + "\n\n" + "\n".join(lines)))
    clusters = []
    with cf.ThreadPoolExecutor(4) as ex:
        futs = {ex.submit(call, j[3], SYS_A, j[0]): j for j in jobs}
        for f in cf.as_completed(futs):
            tag, cat, chunk, _ = futs[f]
            data = f.result(); seen = set()
            for k, c in enumerate(data["clusters"]):
                mem = [m for m in c["members"] if m in chunk and m not in seen]
                seen.update(mem)
                if mem:
                    clusters.append({"id": f"{tag}_{k}", "category": cat, "name": c["name"], "description": c["description"], "members": mem})
            for m in set(chunk) - seen:  # anything the model dropped becomes a singleton
                clusters.append({"id": f"{tag}_s{m}", "category": cat, "name": flat[m]["name"], "description": flat[m]["one_liner"], "members": [m]})
            print(tag, len(chunk), "->", len(data["clusters"]), flush=True)
    clusters.sort(key=lambda c: c["id"])
    # Pass B over labels, chunked by size to keep prompts manageable
    lines = [f"{c['id']} | {c['category']} | {c['name']} — {c['description']} | n={len(c['members'])}" for c in clusters]
    merged = call("CLUSTERS:\n" + "\n".join(lines), SYS_B, "passB")
    byid = {c["id"]: c for c in clusters}
    for g in merged.get("merges", []):
        k = byid.get(g["keep"])
        if not k:
            continue
        for mid in g["merge"]:
            if mid in byid and mid != g["keep"]:
                k["members"] += byid.pop(mid)["members"]
        k["name"], k["description"] = g.get("name", k["name"]), g.get("description", k["description"])
    final = sorted(byid.values(), key=lambda c: -len(c["members"]))
    for n, c in enumerate(final, 1):
        c["cid"] = f"C{n:04d}"
        c["member_keys"] = [flat[m]["key"] for m in c["members"]]
    (CDIR / "membership.json").write_text(json.dumps(final, ensure_ascii=False, indent=1))
    print(len(flat), "mentions ->", len(clusters), "pass A ->", len(final), "final clusters")


if __name__ == "__main__":
    guarded(main)
