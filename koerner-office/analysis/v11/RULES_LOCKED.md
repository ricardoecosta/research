# v11 rules (locked 23 Oct 2026, 22:27 BST, before any lead generation)

These rules can't change mid-run (METHOD EFFICIENCY rule 2). Market scope: **any country**. Ricardo is a UK-based founder, so channels must be lawful both in the UK and in the recipient's jurisdiction.

## Hard constraints (failing any one means kill)
1. **Agent-runnable at steady state.** Agents must handle at least 50% of all the work, including sales, support and admin. Ricardo's time must be ≤5 h/week, measured **after** the 90-day handover for bought businesses; more during the handover is fine.
2. **No selling to local businesses.**
3. **No face or personal brand needed.** This includes a seller-dependent brand.
4. **No cold or unlawful outreach.** Fine channels: SEO, app stores, marketplaces, integrations, paid ads, partnerships, and the existing customer base.
5. **Interesting:** a software, digital or data product. No physical goods, and no services Ricardo has to deliver himself.

## Kill-check: a single Codex xhigh pass with live web; every kill cites a URL
- **K0, build track (time to moat):** kill if any of these fails:
  - (a) agents can build the defensible asset within 3 months (compiled data, a maintained rules engine, a network or switching costs)
  - (b) a rival would need 3+ months to copy it
  - (c) nobody already owns that asset

  Record each part as yes or no with its reason.
- **K0, buy track:** the existing paying customer base, integrations or data must give real switching costs. Rate it 0–10; under 4 is a kill.
- **K1:** the hard rules above.
- **K2 copy-speed:** a dated search for competing launches since 23 Apr 2026. Two or more is a kill. For the buy track this applies to the listed product's niche.
- **K3:** the platform owner or an official partner already serves the need.
- **K4:** 5+ maintained incumbents at or below the price floor, with no wedge.
- **K5:** the only payment evidence is older than 18 months (before 23 Apr 2025), or comes from a self-described failure.
- **K6:** the demand is dead.

**Buy-track checklist** (used instead of K4; K2 still applies):
- **B1, verified revenue only.** It needs a marketplace "verified" badge, a Stripe/ProfitWell connection or verified P&L. Unverified is a **kill**.
- **B2, floor:** ≥$1k/month revenue, with profit greater than 0.
- **B3, price:** asking price between $20k and $150k, and at most 5× annual profit. Above 6× is a kill. Outside the band is a kill.
- **B4, hours after the handover:** a credible 90-day handover-to-agents plan must reach ≤5 h/week. Kill if the work is inherently human: enterprise sales, account management, bespoke dev, regulated advice.
- **B5, transferability:** the domain, code, app store or marketplace accounts and payment processor must be transferable. Kill if it depends on the seller personally.
- **B6, durability:** no revenue decline over 30%, no platform-ban risk and no heavy churn evidence.

**Demand-first leads (D)** carry verified revenue of at least $1k/month, dated within the last 18 months. Treat each as buy if it is for sale, otherwise as build-adjacent: the lead is a *different* product in the same niche, and must pass build K0.

Unverifiable facts are marked `unverified` and never invented. If there's no evidenced kill, the lead survives, except for **B1 and K0, which are strict.**

## Shadow check
10 random kills (seed 11) are re-judged by Claude Opus with live web. If 2 or more of the 10 were wrong, re-run the kill-check for all kills on Claude within budget.

## Scoring (METHOD step 8)
Separate scores:
- success in 12 months (/10)
- agent-runnability at steady state (/10)
- fit (/10)
- automation share % at steady state (an estimated integer with a reason)
- moat (/10)

Also record:
- `track`
- `claim_event_date`
- `copy_speed`
- for the buy track: `listing_url`, `price`, `verified_revenue_profit`, `multiple` and `handover_plan`, a 90-day plan in 3–6 steps

Hard-rule fails are dropped. The top 8 or fewer go forward, ranked by success, then moat, then fit, and **reserving at least 4 slots for the buy track** if that many survive.

## Validation (METHOD step 10)
Claude Opus high with live web. Fallbacks: Codex xhigh, then pi, then Grok Bot. Each verdict is pursue, maybe or kill, with confidence (low, medium or high) and URLs.

**Pursue at medium or higher requires:**
- live revenue or demand dated within 18 months (verified for the buy track)
- a lawful channel
- copy-speed passing on re-check
- for build: the time-to-moat parts confirmed
- for buy: a price that makes sense against verified profit, plus a credible handover plan and a defined due-diligence step
- a first step taking a day or less

## Sources (≤100 leads, ~60% buy)
- **A1** Acquire.com
- **A2** Flippa verified listings
- **A3** Empire Flippers, FE International, Quiet Light, Microns, Tiny, IndieMaker and others
- **D1** demand-first, verified-revenue boards (TrustMRR, Indie Hackers verified)
- **G1** build ideas meeting time-to-moat

Dedupe against `loop/SEEN.csv` at a fuzzy match of 88 or more.

## Budget
- ≤5 h wall-clock (until about 03:25 BST)
- Codex ≤250 calls
- Claude ≤30
- box ≤50
- Grok Bot web checks ≤40
