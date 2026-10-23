# v11 status: PAUSED

**Paused:** 23 Oct 2026, 22:26 BST, at Ricardo's request, pending a method review.

| Stage | State |
|---|---|
| 0. Rules locked (`RULES_LOCKED.md`, `CHANGES.md`, METHOD/LOOP updates) | Done, commit `1317504` |
| 1. Harvest (A1, A2, A3, D1, G1) | Started at 22:25:53. All 5 Codex calls were stopped in flight. **No leads saved.** |
| 2–6 | Not started |

**Resume:** run `cd koerner-office/scripts/v11 && /tmp/v7venv/bin/python v11.py harvest killcheck shadow evidence score validate`. If the method review changes any rule, update `RULES_LOCKED.md` first.

**Cost so far:** 5 Codex calls started at high effort, cut off after about 30 s. No Claude calls.
