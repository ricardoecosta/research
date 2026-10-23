# Loop scoreboard

The stopping rule is P_cum ≥ 5, meaning pursue verdicts at medium+ confidence. The stall rule pauses the loop after 2 consecutive iterations with P = 0. Definitions are in `LOOP.md` §1–2.

| Iter | Sources | Leads into kill-check | P (new pursue, med+) | P_cum | M (maybe) | Survivor rate | Novelty vs ledger | Kill-check precision | Codex / Claude / box / Grok Bot web checks | Wall-clock | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v8 (baseline) | 435 Koerner transcripts + 20 scouts | n/a: no kill-check stage; 35 validated | 0 | 0 | 2 (low) | 2/35 = 5.7% | 0 new survivors vs v7 | n/a | ~1,200 / 364 / 127 transcripts / 35 | ~7 h, incl. ~3 h of rate-limit stalls | Stall counter: 1 of 2 |
