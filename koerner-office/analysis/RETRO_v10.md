# Retrospective: v10

**Written:** 23 Oct 2026, ~20:00 BST, by Grok Bot.
**Evidence:** `v10/leads.jsonl`, `KILLCHECK.md` and `killcheck.json`, `evidence/*.json`, `SCORES.md`, `VALIDATION.md`, plus `/tmp/loop/v10/run.log` and `calls.jsonl` on Ricardo's Mac.
**Direction:** chosen by Ricardo after the v9 stall. The new approach keeps the same constraints. Market scope changed to **any country** at 19:10 BST.

## 1. Outcome

**P = 0, M = 0. P_cum = 0.** v9 also had P = 0, so the **stall rule triggers again and the loop is paused** until Ricardo answers (§5).

| Stage | Build track | Buy track | Total |
|---|---|---|---|
| Leads into the kill-check | 54 | 34 | 88 |
| Survived the single xhigh kill-check | 16 | 9 | 25 |
| Passed hard rules at scoring | 0 | 0 | 0 |
| Validated (scorer audit of 3 near-misses) | 2 | 1 | 3 → 3 kills |

**Where the leads died:**
- **Kill-check (63 kills):** K0 moat 25, K2 copy-speed 14, K3 platform 12, K1 3, K6 3, buy-checklist B3/B5/B6 5, K4 1.
- **Scoring (25 kills):** K0 moat under 4/10 once deep evidence was in: 19. K1 automation 30–45% (buy listings): 4. K2: 2.
- **Best success score:** 2/10.

## 2. Did the 3 v10 changes help?

| Change | Verdict | Evidence |
|---|---|---|
| 1. Defensible-asset gate | **It did what it was built for, but it is mis-specified for the build track.** | It killed 44 of 88 leads. The commonest reason was "the moat is prospective, not evidenced" (e.g. L045, L029, L042). A *build* idea's moat is always prospective on day 1, so the gate rejects every build lead by construction. Where a real compiled-data moat existed, it was already owned: CompanyStack, Recalls API, The Hive Index, LBNL/i2X and Interconnection.fyi. |
| 2. Buy-instead-of-build | **Right frame, wrong price band and wrong automation test.** | Listings with real moats and revenue, such as L058, a French public-sector CMMS with 80–90 clients at about 3.35× profit, fail ≤5 h/week and ≥50% automation *as currently run*. Cheap listings (<$40k) have no moat, and stated revenue is almost never verified. |
| 3. Single xhigh kill-check with dated launches | **Helped.** | The Claude shadow found 0/10 wrong kills (v9 medium: 2/10). Copy-speed kills at validation fell from 4/8 in v9 to 1/3. It was also cheaper than v9's two passes: 30 calls, ~14 min. |
| Infra: automation-share fix | **Fixed.** | All 25 scored rows have an argued, estimated automation share (30–70%). There are no placeholder zeros. |
| Scope: any country | **Widened the pool without changing the result.** | Global rules-engine niches (EU e-invoicing, VAT, PPWR/EPR) all had 2026 launches or enterprise incumbents. For example, L030 had 3 launches between Jul and Sep 2026. |

## 3. Signal vs noise

- **Signal:**
  - The single xhigh kill-check, with Claude as shadow.
  - Claude validation.
  - The moat question itself, which explained why every v7–v9 gap was copied.
- **Noise:**
  - Moat-first ideation (G1–G4). The model produced plausible moats on paper that the evidence stage then marked "not evidenced".
  - Large listings in A3 ($220k–$2.6m) are far outside a sensible price band and mostly need staff.
- **Structural finding across v7–v10:** 200 leads web-checked in v8–v10 (35 + 77 + 88), 48 given deep evidence, 46 validated, 0 pursue. A tension runs through the constraints. **What is defensible needs either time to compile (data, network) or people (an installed customer base with support and sales). What is fully agent-runnable from day one is copyable within weeks.**

## 4. Cost and time

- **Runners:** Codex `gpt-6-luna` 64 calls (56 xhigh, 2 high, 6 medium); Claude Opus 5.5 13 calls (10 shadow, 3 validation); pi 0; Grok Bot box 0; Grok Bot web checks 0.
- **No rate limits hit,** so there were no runner switches. Every call stayed on its first-choice runner.
- **Time:** wall-clock about 50 min. All within budget.
- **Process management:** only PIDs started by this run were managed. Its PID file is `/tmp/loop/v10/pid`. Nothing was pkilled.

## 5. Proposed changes for v11 (max 3), and the stall decision for Ricardo

1. **Make K0 measure "time-to-moat" for the build track.** Kill unless (a) agents can compile the asset within 3 months, *and* (b) a rival would need 3 months or more to replicate it once it exists, *and* (c) nobody already owns that asset. Keep the strict "evidenced moat" test for the buy track only.
2. **Judge the buy track on a post-takeover agent plan, inside a sensible price band.**
   - Price band: $20k–$150k, with revenue verified (Stripe or marketplace-verified).
   - Score *steady-state* automation and hours after a written 90-day plan that hands support and onboarding to agents.
   - The ≤5 h/week constraint still applies at steady state. The plan must show how it is reached, or the lead is killed.
3. **Demand-first sourcing.** Seed leads from **verified-revenue** small products dated ≤18 months with ≥$1k MRR: TrustMRR and other Stripe-verified boards, Acquire "verified" badges, Indie Hackers verified revenue. Then ask what moat each has, or which adjacent niche could be built with time-to-moat. Generating moat ideas first and looking for demand second didn't work.

**Question for Ricardo:**
- After four iterations (v7–v10), the evidence says the hard constraints *as a set* exclude almost everything that is both defensible and runnable by agents from day one.
- Option (a): v11 with the 3 changes above. Change 2 is the most promising, because it keeps the ≤5 h/week rule at steady state while letting a bought business get there.
- Option (b): stop the loop and take the best near-miss forward as a manual experiment.
