# Loop scoreboard

The stopping rule is P_cum ≥ 5, meaning pursue verdicts at medium+ confidence. The stall rule pauses the loop after 2 consecutive iterations with P = 0. Definitions are in `LOOP.md` §1–2.

| Iter | Sources | Leads into kill-check | P (new pursue, med+) | P_cum | M (maybe) | Survivor rate | Novelty vs ledger | Kill-check precision | Codex / Claude / box / Grok Bot web checks | Wall-clock | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v8 (baseline) | 435 Koerner transcripts + 20 scouts | n/a: no kill-check stage; 35 validated | 0 | 0 | 2 (low) | 2/35 = 5.7% | 0 new survivors vs v7 | n/a | ~1,200 / 364 / 127 transcripts / 35 | ~7 h, incl. ~3 h of rate-limit stalls | Stall counter: 1 of 2 |
| v9 | S1 UK regulation calendar (23), S2 decaying paid apps (20), S3 acquisition listings (20), S4 paid-tool complaints (14) | 77 (23 survived xhigh kill-check; top 8 validated) | 0 | 0 | 0 | 0/77 = 0% (kill-check survivors 23/77 = 30%) | 77/78 = 99% (1 ledger dupe dropped) | Medium pass: 2/10 shadow wrong kills → safeguard fired, full xhigh re-run (28/77 verdicts flipped). xhigh pass: 4 of 8 it passed were then killed at validation on K2/K3 (copy-speed / platform) | ~100 Codex (29 medium, 65 xhigh, ~6 aborted/test) / 8 Claude / 0 box / 0 Grok Bot web checks | ~1 h 5 min of run time (16:30–17:35 BST, plus a ~20 min interruption); first verdict 17:27 (57 min) | **Stall rule triggered (2 of 2): loop paused for Ricardo.** All 8 kills; 4 on copy-speed/platform. |
