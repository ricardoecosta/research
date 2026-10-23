# v9 method changes

**Iteration start:** 23 Oct 2026, 16:30 BST. Chosen from `RETRO_v8.md` §6 (★ items), max 3 per `LOOP.md` §3.

| # | Change | Expected effect | How we'll judge it (RETRO_v9) |
|---|---|---|---|
| 1 | **Validation-first ordering.** Every lead gets a cheap web kill-check (Codex medium + live web search, URL per kill) before deep evidence, scoring or validation. 10 kills are shadow-re-judged at xhigh. | Deep effort only on ~10–15 survivors; far lower compute than v8. | Survivor rate, kill-check precision (shadow), Codex/Claude calls vs budget. |
| 2 | **New sources** replace the 435 retired transcripts: S1 UK regulation calendar (Nov 2026–2028), S2 decaying paid apps/plugins, S3 acquisition listings, S4 paying-user complaints about UK tools. | Leads with built-in timing (S1), proof of payment (S2–S4). | Survivor rate and P by source. |
| 3 | **Copy-speed and claim-age as hard filters.** Kill if ≥2 rivals launched in last 6 months, or platform owner / official partner serves the need. Revenue events >18 months old (or self-described failures) get zero weight; `claim_event_date` recorded. | Stops the v8 failure where every gap was already copied and old anecdotes topped the ranking. | How many kills each filter made; whether any validated pursue later fails on copy-speed. |

**Infrastructure (doesn't count toward the 3):** `scripts/common/runner.py` gains a `web=True` option (Codex `web_search="live"`, Claude `--allowedTools WebSearch WebFetch`) and a per-call runner `order`, so harvest/kill-check/validation can use live web search through the same fail-over chain.
