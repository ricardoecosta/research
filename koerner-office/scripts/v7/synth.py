#!/usr/bin/env python3
"""Cross-transcript learnings synthesis -> analysis/v7/SYNTHESIS.md (+ synthesis/*.md parts)."""
import concurrent.futures as cf, json, sys
from collections import defaultdict, Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import *

SD = V7 / "synthesis"; SD.mkdir(exist_ok=True)
MODEL = sys.argv[1] if len(sys.argv) > 1 else "opus"
SYS = """You synthesise learnings mined from hundreds of business/side-hustle podcast transcripts for Ricardo, a technical UK (London/Bromley) solo part-timer who wants businesses AI agents can run.
Each input line ends with the source video id in square brackets. Write a Markdown section (start at heading level ###, no top-level title) that:
- groups the inputs into recurring principles/patterns, ordered by how many DISTINCT videos support each (state the count, e.g. "(14 videos)");
- for each: a bold one-line principle, 1-3 sentences of specifics (concrete numbers only if they appear in the inputs, labelled as claims), and the supporting video ids in backticks (list up to 12, all real ids from the input);
- notes contradictions/counter-evidence and UK caveats (e.g. PECR cold-outreach rules, US-only platforms) where relevant;
- ends with a short "What this means for an agent-run UK business" paragraph.
Do not invent facts, numbers or video ids. Skip generic platitudes unless strongly recurring. Aim for 8-20 patterns."""


def call(tag, title, lines):
    p = SD / f"{tag}.md"
    if p.exists():
        return p.read_text()
    prompt = f"TOPIC: {title}\nINPUT ({len(lines)} items):\n" + "\n".join(lines) + "\n\nWrite the section now."
    res = run_claude(prompt, SYS, model=MODEL)
    if res.get("is_error"):
        log_cost("synth", tag, MODEL, res, "fail"); raise RuntimeError(tag)
    log_cost("synth", tag, MODEL, res, "ok")
    p.write_text(res["result"].strip() + "\n")
    return p.read_text()


def main():
    recs = [json.loads(l) for l in open(V7 / "learnings.jsonl")]
    groups = defaultdict(list)
    for r in recs:
        vid = r["video"]["id"]
        for l in r.get("lessons", []):
            groups[("lessons_" + l["theme"], "Lessons: " + l["theme"].replace("_", " "))].append(f"- {l['lesson']} [{vid}]")
        for w in r.get("warnings", []):
            groups[("failure_modes", "Common failure modes, mistakes and warnings")].append(f"- {w['warning']} [{vid}]")
        for i in r.get("ideas", []):
            if i["depth"] == "mention":
                continue
            for c in i["acquisition_channels"]:
                groups[("acquisition", "Customer-acquisition channels that worked (or failed), by channel")].append(
                    f"- {c['channel']}: {c['details'][:220]} (idea: {i['name'][:60]}) [{vid}]")
            pp = "; ".join(f"{p.get('currency') or ''}{p.get('amount')} {p.get('unit') or ''}" for p in i["pricing"]["price_points"][:4])
            groups[("pricing", "Pricing patterns and price points")].append(
                f"- {i['category']} | {i['name'][:60]} | model: {i['pricing']['model'][:120]} | {pp} | {(i['pricing'].get('notes') or '')[:150]} [{vid}]")
        for t in r.get("tactics", []):
            area = t.get("area") or "other"
            groups[("tactics_" + area, "Reusable tactics: " + area)].append(f"- {t['name']}: " + " > ".join(s[:120] for s in t["steps"][:6]) + f" [{vid}]")
    jobs = []
    for (tag, title), lines in groups.items():
        if len(lines) < 8:
            continue
        # chunk very large groups
        CH = 900
        if len(lines) > CH:
            for k in range(0, len(lines), CH):
                jobs.append((f"{tag}_{k // CH}", title + f" (part {k // CH + 1})", lines[k:k + CH]))
        else:
            jobs.append((tag, title, lines))
    print(len(jobs), "synthesis calls:", [(j[0], len(j[2])) for j in jobs], flush=True)
    with cf.ThreadPoolExecutor(4) as ex:
        out = dict(zip([j[0] for j in jobs], ex.map(lambda j: call(*j), jobs)))
    print("done", len(out))


if __name__ == "__main__":
    guarded(main)
