# v10 rules (locked 23 Oct 2026, 19:12 BST, before any lead generation)

Changing any rule below mid-run is not allowed (METHOD EFFICIENCY rule 2).

## Market scope
**Any country market.** Customers can be in the US, EU, UK or anywhere else. Ricardo is a UK-based founder (Bromley), so UK law applies to him. Any acquisition or outreach channel must be lawful in both his jurisdiction and the recipient's.

## Hard constraints (failing any = kill)
1. **Agent-runnable:** at least 50% of the total work is automatable, including sales, support and admin. Ricardo's time is at most 5 h/week at steady state, including for a bought business.
2. **Not selling to local businesses:** no local-trade or high-street sales motion. National or global online self-serve SMB sales are fine.
3. **No face or personal brand** needed to acquire customers.
4. **No acquisition reliant on unlawful or cold outreach:** no cold SMS, WhatsApp, DM or calls, and no cold email. Self-serve marketplaces, SEO, app stores, integrations and paid ads are fine.
5. **Interesting to Ricardo:** a software, digital or data product. No physical goods, and no services he has to deliver.

## Kill-check: one pass at Codex xhigh with live web. Each kill cites a URL.
- **K0 moat gate (new):** the lead must name a defensible asset that would take a competitor months, not weeks, to copy:
  - (a) compiled or proprietary data assembled from many sources, or a dataset that compounds with use
  - (b) a maintained rules engine for regulation, tax or compliance in a jurisdiction
  - (c) a network effect or two-sided marketplace
  - (d) real switching costs: stored customer data, integrations, workflows

  Rate `defensible_asset` 0–10. **Under 4, or "none", is a kill.** A UI, a prompt, or "first to market" is not a moat.
- **K1 hard rules** (above).
- **K2 copy-speed:** a dated search for competing launches since 23 Apr 2026 is required. Two or more launched means kill. Record the names and dates found.
- **K3 platform ownership:** kill if the platform owner or an official partner already serves the need, free or bundled.
- **K4 incumbents:** kill if there are 5 or more maintained, well-reviewed incumbents at or below the plausible price floor and no evident wedge.
- **K5 claim age:** kill as unproven if the only payment evidence is an event older than 18 months (before 23 Apr 2025) or a self-described failure.
- **K6 dead demand:** kill if the need, regulation or platform has been withdrawn or delayed beyond 2028, or the users are gone.

**Buy track (acquisition listings), checklist instead of K2/K4:**
- **B1 revenue:** stated TTM revenue or profit, and whether it is verified (Stripe/marketplace-verified badge, screenshots). Unverified counts against, but isn't an automatic kill.
- **B2 floor:** at least $500/month profit, or at least $1k MRR.
- **B3 price:** asking price at most about 4× annual profit. More than 6× is a kill.
- **B4 owner hours:** at most 5 h/week stated. If not stated, mark unverified.
- **B5 transferability:** app store accounts, marketplace listings and payment accounts can be transferred. Kill if the business relies on the seller personally (face, brand, consulting).
- **B6 durability:** no evidence of fast churn, platform-ban risk or a revenue decline over 30%.
- K0 still applies, but an established paying customer base with switching costs counts as (d).
- K1 and K5 apply as normal.

Unverifiable facts are marked `unverified`, never invented. If a lead has no evidenced kill but its moat is unclear, **K0 kills** (strict). Otherwise the benefit of the doubt goes to *survive*.

## Shadow check
10 kills sampled at random (seed 10) are re-judged by Claude Opus with live web. If 2 or more of the 10 were wrong kills, re-run the kill-check on Claude for all kills it can cover within budget, and record that.

## Scoring (METHOD step 8)
Five separate scores:
- success in 12 months /10
- agent-runnability /10
- fit /10
- automation share %, an **estimated integer with a reason**. 0 is allowed only when it is argued.
- defensible asset /10

Also record:
- `claim_event_date`
- `copy_speed` (launches in the last 6 months)
- `track` (build or buy)

Revenue claims whose event is more than 18 months old get zero weight. The top 8 or fewer are chosen by success, with ties broken by moat, then fit.

## Validation (METHOD step 10)
Validation runs on Claude Opus high with live web. If Claude is blocked it falls back to Codex xhigh, then pi, then Grok Bot. The verdict is pursue, maybe or kill, with confidence low, medium or high and cited URLs.

**Pursue at medium confidence or higher requires:**
- live demand or revenue evidence dated within 18 months
- a reachable lawful channel
- copy-speed passing on re-check
- the moat confirmed
- a first test of a day or less, or for the buy track, a defined due-diligence step

Any maybe whose deciding test is desk-only and takes a day or less gets that test inside v10.

## Sources and caps (100 leads or fewer into the kill-check)
**Build track (moat-first), about 60:**
- G1 compiled-data products (any country)
- G2 maintained rules engines for tax, regulation or compliance (any jurisdiction)
- G3 network effects and two-sided marketplaces runnable by agents
- G4 switching-cost B2B tools in niches where incumbents are decaying

**Buy track, about 40:**
- A1 Acquire.com
- A2 Flippa, Microns, SideProjectors, Tiny, Empire Flippers and similar

All sources are global. Leads matching `loop/SEEN.csv` (key or name fuzzy match of 88 or more) are dropped unless their `recheck_after` date has passed.

## Budget (LOOP.md §4)
- Wall-clock: 5 h or less (by about 00:10 BST)
- Codex: 250 calls or fewer
- Claude: 30 calls or fewer
- Box prompts: 50 or fewer
- Grok Bot web checks: 40 or fewer
