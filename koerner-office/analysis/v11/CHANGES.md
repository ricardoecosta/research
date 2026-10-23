# v11 method changes

**Iteration start:** 23 Oct 2026, 22:25 BST. Ricardo chose to run v11 with the proposed changes from `RETRO_v10.md` §5. All other rules stay locked. The changes are capped at 3 per `LOOP.md` §3.

| # | Change | Expected effect | How we'll judge it (RETRO_v11) |
|---|---|---|---|
| 1 | **Time-to-moat replaces the evidenced-moat gate on the build track.** A build lead passes K0 only if all three hold: (a) AI agents can build the defensible asset within 3 months; (b) a rival would need 3+ months to copy it once it exists; (c) nobody owns that asset yet. If any one fails, the lead is killed. | Stops the v10 contradiction, where every build idea died because its moat was "prospective". | Build-track survivors past scoring; validation kills on copy-speed or ownership. |
| 2 | **Buy track judged on a 90-day handover-to-agents plan.** Price band is $20k–$150k, and only revenue verified by a marketplace badge, Stripe connection or P&L verification counts. The ≤5 h/week limit applies at steady state after the 90-day handover; more hours during the handover are allowed. Automation is also scored at steady state. **This track gets more weight: about 60% of leads.** | Real businesses with customers (an installed base is the moat) can now pass if agents can take over their support and ops. | Buy-track P and survivor rate vs build. |
| 3 | **Demand-first source.** Small products with **verified revenue of at least $1k/month, dated within the last 18 months**, from Stripe-verified boards (e.g. TrustMRR), Indie Hackers verified revenue, and verified listings. They are used either as buy leads (if for sale) or as proof that an adjacent build-track niche pays. | Every lead starts with proof that someone pays. | Share of survivors from the demand-first source. |

**Unchanged and still locked:**
- market scope is any country
- automatable by agents
- interesting to Ricardo
- no selling to local businesses
- no face or personal brand
- no cold or unlawful outreach
- a single xhigh kill-check with a dated-launch search
- dedupe against `loop/SEEN.csv`
- a Claude shadow check on kills
