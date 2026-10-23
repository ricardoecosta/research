# Retrospective: v11 (rebuilt, evidence-first)

**Written:** 24 Oct 2026, ~00:20 BST, by Grok Bot.
**Evidence:**
- `v11/TRACK_E.md` and `track_e.json`, `CHECKLISTS.md`, `VALIDATION.md`, `TEST_PLANS.md`
- `/tmp/loop/v11/` logs on Ricardo's Mac
- `proven_models/PROVEN_MODELS.md` (separate pass, `4485ba6`)

## 1. Outcome

**P = 0, M = 1 (medium). P_cum = 0.** That makes three iterations in a row with P = 0, so **the stall rule triggers and the loop is paused** for Ricardo.

| Track | In | Passed gate | Validated | Pursue / maybe / kill |
|---|---|---|---|---|
| E, evidence-first (build) | 1,869 snippets → 445 clusters → 25 at the ≥10 bar (only 3 at ≥30) | 0 of 25 passed the kill-check (K0 21, K2 4) | 0 | n/a |
| B, buy (main) | 177 listings → 100 in band | 5 of 100 passed the checklist | 5 | 0 / 1 / 4 |

**The maybe:** Internet Web Browser for Google TV (https://flippa.com/12008497).
- **Price:** $117.8k, about 1.8× profit.
- **Revenue:** ~€4.9k/mo, Flippa-vetted but not data-connected.
- **Owner time:** 0–1 h/month.
- **Unknowns:** churn, trend, and whether revenue is gross or net of the Play fee.
- **Next step:** a ≤£10 due-diligence test, an NDA plus a Play Console screenshare. It needs Ricardo's Flippa account, so it wasn't run.

**The 4 kills:**
- COPA: ad-dependent, 7% margin, 40% churn.
- Kliptok: inconsistent figures, and its Sora API was shut down.
- AI chatbot: revenue down 35%.
- Amazon-author review exchange: Amazon ban risk, and the numbers don't reconcile.

## 2. Did the 3 rebuild changes help?

| Change | Verdict | Evidence |
|---|---|---|
| 1. Evidence first, with the LLM only clustering and counting | **Cheap and honest, but no signal yet.** | Harvest cost 0 LLM calls, and labelling and clustering took 36 cheap calls. Only 3 clusters reached 30 complainers. The labels were product-agnostic, so they merged into generic clusters ("use reliable apps", "avoid subscriptions") that describe complaints about specific apps, not a shared unmet job. That made every fix copyable or owned (K0). Reddit (429 from both networks), Upwork and G2/Capterra (403) were blocked, which left the corpus skewed to App Store reviews. |
| 2. Buy track as main, with a checklist and a mechanical pass | **Best signal of the round.** | It produced the only survivor. The checklist was cheap (100 Codex medium calls, about 3 min) and caught real problems: inconsistent figures, decline, platform-ban risk. The limit is Flippa hiding financials, traffic and seller notes behind a login, so many rows came back "missing" (20 listings had no hard fail but more than 3 rows missing). |
| 3. A real-money test instead of more rounds | **Plans written, none run** (by design). | `TEST_PLANS.md` has the maybe's DD test plus the 3 proven-model tests. |

**Cost:** 145 Codex calls (mostly low and medium) and 15 Claude, against 64 Codex and 13 Claude in v10. There were more calls but far fewer xhigh ones (9 vs 56), and no limits or runner switches.

## 3. The bigger lesson (with PROVEN_MODELS.md)

- `PROVEN_MODELS.md` shows that the v8 corpus contains **proven, repeatable models** with many operators: niche apps (13 operators), SEO directories (5), and faceless video pages (5).
- v8–v11 killed them as "copied" or "crowded". **For a proven model, crowding is the expected state, not a defect.**
- The K0/K2 gates are the right test for a *gap* idea and the wrong one for a *proven model*.
- After 4 rounds and about 330 checked leads with P = 0, more desk research has a low expected value. A £50 market test gives real data.

## 4. Proposed changes for v12 (max 3)

1. **Proven-model track, judged by a test rather than desk gates.** For models with ≥5 independent operators (apps, directories, faceless video), drop K0 and K2. A candidate becomes "pursue" only through a passed ≤£50 test against pre-set thresholds. The iteration unit becomes **a test**, not a research round.
2. **Gated listing data for the buy track.** With Ricardo's OK, he creates free Flippa and Acquire buyer accounts and signs NDAs himself, so the checklist reads the full financials and the "missing" rows can be resolved. Add Acquire and Microns once there's access. The mechanical pass rule stays.
3. **Product-specific evidence clusters.** Keep the paid tool's name in each label (cluster by tool + job). Count "paying users of tool X want Y" to find replacement or alternative products for a named paid tool. Add sources that aren't blocked: Chrome Web Store reviews, Trustpilot (if fetchable), and HN "Ask HN" threads.

**Decision for Ricardo (stall rule):**
- (a) Run the £50 tests instead of v12.
- (b) v12 with the changes above.
- (c) Both: tests now, and v12 only for the buy track.
