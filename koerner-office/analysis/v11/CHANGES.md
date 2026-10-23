# v11 method changes (REBUILT 23 Oct 2026, 23:15 BST)

**Why the rebuild:** Ricardo approved it after forum research into how people actually find profitable ideas with AI. The key lesson: **AI should collect, cluster and count real evidence of paid demand. It should not generate or judge ideas.** v8–v10 spent most of their tokens on generating and judging, and found 0 pursue. The earlier v11 draft (time-to-moat plus a 90-day buy track, paused at 22:26 with no leads) is folded into this rebuild.

| # | Change | What it replaces | How RETRO_v11 judges it |
|---|---|---|---|
| 1 | **Evidence first (build track).** Harvest cheaply, mostly without the LLM: Hacker News (Algolia API), Reddit (public search RSS), and 1–2★ reviews of PAID tools (Shopify App Store, WordPress.org, Apple App Store). The LLM, at Codex low or medium, only labels, clusters and counts. A cluster reaches the kill-check only if it has **≥30 distinct complainers in the last 6 months** (or a documented lower bar, with the actual count recorded) **AND proof that someone already pays for a fix**. Then comes the time-to-moat check (agents build it in ≤3 months, a rival needs ≥3 months, nobody owns it), plus the single xhigh kill-check with a dated-launch search. | LLM-generated leads (v9 and v10 harvests) | Clusters reaching the bar, survivors, and P from this track. LLM calls per lead compared with v10. |
| 2 | **The buy track is the main track.** Listings from Flippa (and similar sites) at $20k–$150k, with verified revenue, traffic mostly organic or from app stores rather than owner outreach, low owner involvement, no customer concentration, and the owner's current hours stated. The LLM turns each listing into a **checklist table (stated / missing / looks off) plus 5 follow-up questions for the seller**. It doesn't pick winners. A listing **passes** if it clears the checklist and has a plausible 90-day handover to agents (≤5 h/week after the handover). | The LLM ranking and judging of listings in v10 | Checklist pass rate and P from this track. |
| 3 | **A real-money test instead of more rounds.** Compounding assets are favoured, for example agent-run curated data or directory sites where people pay to be listed (OpenAlternative-style). Every pursue or maybe gets a concrete **≤£50 test plan**: a pre-sale page or a small ad test, with a success threshold. **Nothing is spent and nobody is contacted. The plans are only written.** | Running more research rounds to settle maybes | Whether the plans can be run as written, and their cost. |

Everything else stays **locked**:
- market scope: any country
- agent-automatable, and interesting to Ricardo
- no selling to local businesses
- no face or personal brand
- no unlawful or cold outreach
- ≤5 h/week, measured after the handover for a bought business
- dedupe against `loop/SEEN.csv`
- one xhigh kill-check

**Infrastructure:** the harvesters in `scripts/v11/harvest_evidence.py` and `harvest_listings.py` are plain HTTP and don't call the LLM.

**Blocked sources (403 from Ricardo's Mac, 23 Oct 23:05):**
- Reddit JSON (the search RSS works)
- Upwork search and RSS
- G2 and Capterra
- the Flippa API, which needs auth (the public search HTML works)
- pullpush.io, which is rate-limited for agents

No Apify connector or token is available. For paying proof, the Upwork job-post signal is replaced by paid rivals, paid workarounds and reviews of paid tools.
