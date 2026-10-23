#!/usr/bin/env python3
"""v8 step 7: flatten mined ideas, cluster with Codex xhigh (pass A per category, pass B cross-category merge).
Support = distinct videos. Requires the completeness gate. Writes analysis/v8/ideas_flat.jsonl,
ideas_feature_requests.jsonl, clusters/*.json, clusters/membership.json."""
import collections, concurrent.futures as cf, json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common8 import *

LOGF = WORK / "cluster.log"
CD = V8 / "clusters"; CD.mkdir(parents=True, exist_ok=True)
SYS_A = """You deduplicate business-idea mentions extracted from many podcast transcripts into canonical ideas. You do not run commands; everything is below.
Two mentions belong to the same canonical idea when a founder would run essentially the same business: same core offer, same kind of customer, same way of making money. Niche variations stay together when the playbook is the same; split when delivery or revenue model differ materially (done-for-you agency vs self-serve SaaS for the same problem are DIFFERENT ideas).
Each line ends with its source video tag [v:ID]. Prefer precise clusters of 1-15 members over vague buckets. Every input index must appear in exactly one cluster.
OUTPUT JSON only: {"clusters":[{"name":"short canonical idea name","description":"one sentence: offer, customer, revenue model","members":[indices]}]}"""
SYS_B = """You merge duplicate canonical business-idea clusters produced separately per category. You do not run commands. Input lines: id | category | name - description | videos=<distinct source videos>.
Merge clusters that are the SAME business (same offer, customer, revenue model) even if filed under different categories. Do not merge merely related ideas.
OUTPUT JSON only: {"merges":[{"keep":"id","merge":["id",...],"name":"final name","description":"final one sentence"}]} (only groups that change)."""


def call(tag, prompt):
    p = CD / f"{tag}.json"
    if p.exists(): return json.loads(p.read_text())
    data, runner, secs = call_llm(prompt, "xhigh", LOGF, tag)
    data["_runner"] = runner; p.write_text(json.dumps(data, ensure_ascii=False, indent=1)); log(LOGF, f"{tag} ok {runner} {secs:.0f}s")
    return data


def flatten():
    flat, fr = [], []
    for p in sorted((V8 / "mined").glob("*.json")):
        r = json.loads(p.read_text())
        for i in r["ideas"]:
            x = {**i, **dict(key=i["idea_id"], video_id=r["id"], record_id=i["record_id"], channel=r.get("channel"), title=r.get("title"),
                     publish_date=r["publish_date"], evidence_quality=r.get("evidence_quality"), miner=r["miner"])}
            (fr if i.get("feature_request") else flat).append(x)
    with open(V8 / "ideas_flat.jsonl", "w") as f:
        for x in flat: f.write(json.dumps(x, ensure_ascii=False) + "\n")
    with open(V8 / "ideas_feature_requests.jsonl", "w") as f:
        for x in fr: f.write(json.dumps(x, ensure_ascii=False) + "\n")
    return flat, fr


def main():
    if subprocess.run([sys.executable, str(Path(__file__).parent / "gate.py")]).returncode != 0:
        print("GATE CLOSED: refusing to cluster"); sys.exit(2)
    flat, fr = flatten()
    bycat = collections.defaultdict(list)
    for k, x in enumerate(flat): bycat[x["idea"]["category"]].append(k)
    jobs = []
    for cat, idxs in sorted(bycat.items()):
        n = max(1, -(-len(idxs) // 250)); size = -(-len(idxs) // n)
        for c in range(n):
            ch = idxs[c * size:(c + 1) * size]
            lines = [f"{k} | {flat[k]['idea']['name']} - {flat[k]['idea'].get('one_liner', '')} | customer: {str(flat[k]['idea'].get('customer', ''))[:100]} | model: {str(flat[k]['idea'].get('revenue_model', ''))[:80]} [v:{flat[k]['video_id']}]" for k in ch]
            jobs.append((f"passA_{cat}_{c}", cat, ch, SYS_A + "\n\nCATEGORY: " + cat + "\n\n" + "\n".join(lines)))
    clusters = []
    with cf.ThreadPoolExecutor(6) as ex:
        futs = {ex.submit(call, j[0], j[3]): j for j in jobs}
        for f in cf.as_completed(futs):
            tag, cat, ch, _ = futs[f]; data = f.result(); seen = set()
            for k, c in enumerate(data.get("clusters", [])):
                mem = [m for m in c.get("members", []) if m in ch and m not in seen]; seen.update(mem)
                if mem: clusters.append(dict(id=f"{tag}_{k}", category=cat, name=c["name"], description=c.get("description", ""), members=mem))
            for m in set(ch) - seen:
                clusters.append(dict(id=f"{tag}_s{m}", category=cat, name=flat[m]["idea"]["name"], description=flat[m]["idea"].get("one_liner", ""), members=[m]))
    clusters.sort(key=lambda c: c["id"])
    byid = {c["id"]: c for c in clusters}
    lines = [f"{c['id']} | {c['category']} | {c['name']} - {c['description']} | videos={len({flat[m]['video_id'] for m in c['members']})}" for c in clusters]
    # pass B in chunks of 700 labels sorted by name so near-duplicates share a chunk
    order = sorted(range(len(lines)), key=lambda k: clusters[k]["name"].lower())
    chunks = [order[i:i + 700] for i in range(0, len(order), 700)]
    with cf.ThreadPoolExecutor(4) as ex:
        res = list(ex.map(lambda t: call(f"passB_{t[0]}", SYS_B + "\n\nCLUSTERS:\n" + "\n".join(lines[k] for k in t[1])), enumerate(chunks)))
    for data in res:
        for g in data.get("merges", []):
            kp = byid.get(g.get("keep"))
            if not kp: continue
            for mid in g.get("merge", []):
                if mid in byid and mid != g["keep"]: kp["members"] += byid.pop(mid)["members"]
            kp["name"], kp["description"] = g.get("name", kp["name"]), g.get("description", kp["description"])
    for c in byid.values():
        vids = {flat[m]["video_id"] for m in c["members"]}
        c["n_videos"], c["n_mentions"], c["single_video"] = len(vids), len(c["members"]), len(vids) == 1
        c["member_keys"] = [flat[m]["key"] for m in c["members"]]
    final = sorted(byid.values(), key=lambda c: (-c["n_videos"], -c["n_mentions"], c["id"]))
    for n, c in enumerate(final, 1): c["cid"] = f"C{n:04d}"
    (CD / "membership.json").write_text(json.dumps(final, ensure_ascii=False, indent=1))
    msg = f"{len(flat)} ideas (+{len(fr)} feature requests) from {len({x['video_id'] for x in flat})} videos -> {len(clusters)} pass A -> {len(final)} clusters; single-video {sum(c['single_video'] for c in final)}"
    log(LOGF, msg)


if __name__ == "__main__":
    main()
