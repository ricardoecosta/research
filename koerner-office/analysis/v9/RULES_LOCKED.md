# v9 rules (locked 23 Oct 2026, 16:35 BST, before any lead generation)

Changing any rule below mid-run is not allowed (METHOD EFFICIENCY rule 2).

## Hard constraints (fail any = kill)
1. **Agent-runnable:** ≥50% of total work (incl. sales, support, admin) automatable; ≤5 h/week of Ricardo's time at steady state.
2. **Not selling to local businesses** (no local-trade or high-street sales motion; national/online SMB self-serve is fine).
3. **No face or personal brand** needed to acquire customers.
4. **No acquisition reliant on PECR-banned channels** (cold SMS/WhatsApp/DM/email to individuals or sole traders). Self-serve marketplaces, SEO, app stores, paid ads are fine.
5. **Interesting to Ricardo:** software/digital/data product (not physical goods, not services he must deliver).

## Kill-check filters (v9 changes 1 + 3), each kill cites a URL
- **K1 hard rules** (above).
- **K2 copy-speed:** ≥2 competing products launched in the last 6 months (since 23 Apr 2026) → kill.
- **K3 platform ownership:** platform owner or an official partner already serves the need (free or bundled) → kill.
- **K4 incumbents:** ≥5 established, maintained, well-reviewed incumbents at or below the plausible price floor and no evident UK/niche wedge → kill.
- **K5 claim age:** a lead whose *only* evidence of payment is a revenue/traction event older than 18 months (before 23 Apr 2025) or self-described failure → kill as unproven.
- **K6 dead demand:** the regulation/platform/need has been withdrawn, delayed beyond 2028, or the user base is gone.
- Unverifiable facts are marked `unverified`, never invented. A lead that can't be checked survives only if no kill rule is evidenced (benefit of the doubt goes to *survive*, so the deep stage decides).

## Shadow check
10 kills sampled at random (seed 9) are re-judged at Codex xhigh with web. If ≥2 of 10 are wrong kills, re-run the whole kill-check at xhigh.

## Scoring (METHOD step 8, plus v9 fields)
Four separate scores: success in 12 months /10, agent-runnability /10, fit /10, automation share %. Plus `claim_event_date`, `copy_speed` (launches in last 6 months), `defensible_asset` (note only; not scored in v9). Revenue claims with event >18 months old get zero weight. Top ≤8 by success, ties broken by fit then runnability.

## Validation (METHOD step 10)
Claude Opus high with live web; Grok Bot if Claude is blocked. Verdict pursue/maybe/kill with confidence low/medium/high and cited URLs. **Pursue at medium+** requires: live demand evidence dated ≤18 months, a reachable lawful channel, copy-speed pass re-checked, and a ≤1-day first test. Any maybe whose deciding test is desk-only and ≤1 day gets that test inside v9.

## Sources and caps
S1 UK regulation calendar 20–25; S2 decaying paid products 20–30; S3 acquisition listings 15–20; S4 paid-tool complaints 10–15. Total ≤100 leads into kill-check. Leads matching `loop/SEEN.csv` (key or name fuzzy ≥88) are dropped unless `recheck_after` has passed.

## Budget (LOOP.md §4)
Wall-clock ≤5 h (lock → scoreboard, i.e. by ~21:35 BST); Codex ≤250 calls; Claude ≤30; box prompts ≤50; Grok Bot web checks ≤40.
