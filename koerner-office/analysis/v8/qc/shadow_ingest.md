# Shadow comparison: ingest at medium vs xhigh

Batch: first 10 transcripts. Rule (RULES_LOCKED): revert if medium finds >10% fewer records in total, or misses an xhigh record in 2+ transcripts.

| video | records medium | records xhigh | xhigh records missed by medium | removed lines medium/xhigh | business lines removed by medium only |
|---|---|---|---|---|---|
| -AVFpzAfjW0 | 3 | 2 | 0 | 81/77 | 9 |
| -B8E6i1JKfU | 19 | 14 | 0 | 43/19 | 1 |
| -Gw8jMFGmbE | 4 | 2 | 0 | 15/19 | 0 |
| -S2DPfEDRU4 | 4 | 5 | 0 | 31/156 | 0 |
| -VdiyFruaJg | 5 | 9 | 0 | 0/1 | 0 |
| -Whqjr6ZnmY | 13 | 13 | 1 | 30/51 | 0 |
| -kwF1zol2gQ | 14 | 15 | 0 | 67/30 | 29 |
| 0SB3OUrElys | 4 | 4 | 0 | 412/126 | 277 |
| 0aLYK6tBoJo | 5 | 4 | 0 | 591/81 | 510 |

Totals: medium 71 records, xhigh 68; transcripts where medium missed a record: 1.

- -Whqjr6ZnmY: medium missed ['AI tools built inside an existing company to solve its probl']
- Record-count rule: passes. But medium removed 826 lines that xhigh kept inside business records; in 2 transcripts (0SB3OUrElys, 0aLYK6tBoJo) it removed 100+ business lines (e.g. 510 of 1,005 lines in 0aLYK6tBoJo), which would hide business content from mining. One medium call (03DjE7j0Suw) also hung for 8+ minutes and was killed. Under the METHOD.md safeguard ('if the cheaper path starts missing things, revert immediately') this is missing things, so ingest runs at xhigh for all 435. The 10 xhigh shadow outputs are used as the real ingest records.

**Decision: REVERT to xhigh.**