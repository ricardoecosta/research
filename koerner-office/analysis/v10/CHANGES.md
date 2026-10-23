# v10 method changes

**Iteration start:** 23 Oct 2026, 19:10 BST. Direction chosen by Ricardo after the v9 stall: the NEW APPROACH with the SAME constraints. There's no loosening on cold email or hours. Changes come from `RETRO_v9.md` §5; max 3 per `LOOP.md` §3.

| # | Change | Expected effect | How we'll judge it (RETRO_v10) |
|---|---|---|---|
| 1 | **Defensible-asset gate first.** Every lead must name a real moat: compiled data, a maintained rules engine, a network effect or switching costs. Score `defensible_asset` 0–10; "none" or under 4 is a kill. | Stops "uncopied gap" leads that were copied in weeks in v8 and v9. | How many validated candidates are later killed on copy-speed (target 0); P. |
| 2 | **Buy-instead-of-build track.** Software businesses listed for sale are judged as acquisitions on verified revenue, churn, owner hours ≤5 h/week, price vs profit and account transferability. They are not treated as ideas to copy. | An existing customer base is the moat that a gap lacks. | Buy-track survivor rate and P vs the build track. |
| 3 | **One xhigh kill-check with a dated-launch search.** The medium pass is dropped. Each lead needs a dated search for competing launches in the last 6 months and a platform-owner/partner check. Kill if 2+ rivals launched in the last 6 months, or if the revenue story is more than 18 months old. | v9 medium flipped 28/77 verdicts, and 4/8 xhigh survivors still died on copy-speed. | Shadow precision (Claude); validation kills on K2/K3. |

**Scope change (Ricardo, 23 Oct 19:10): any country market.** Target customers and markets can be in any country (US, EU, global). Sources, moat ideas (data or rules engines for any jurisdiction) and acquisition listings are all global. Ricardo is UK-based, so his own UK compliance still applies. Outreach must be lawful both in his jurisdiction and the recipient's: UK PECR, EU ePrivacy/GDPR, US CAN-SPAM and TCPA. This is a constraint clarification and doesn't count toward the 3.

**Infrastructure fixes (don't count toward the 3):**
- The evidence/score schema no longer defaults `automation_share_pct` to 0. It must be an estimated integer with a reason, or null with the label "unverified". The scorer must estimate it and never copy a placeholder.
- The kill-check shadow re-judge runs on Claude, a different model family.
- The runner kills only the PIDs it started.
