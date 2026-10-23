# Retrospective: v1 → v8 research workflow

**Written:** 23 Oct 2026, ~16:40 BST, by Grok Bot.
**Evidence:**
- git history of `ricardoecosta/research`: 73 commits, 21 Oct 17:26 → 23 Oct 16:18
- `/tmp/v8` logs: `run.log`, `mine.log`, `score.out`, `commits.txt`
- `v8/ideas_flat.jsonl`, `v8/ideas_scored.csv`, `v8/AUTOMATION_DISTRIBUTION.md`, `v8/VALIDATION.md`, including the "Loose ends closed" section in `682273f`
- `v7/IDEAS_WORTH_PURSUING.md`

**Success** here means a candidate that passes validation with **verdict "pursue" at medium+ confidence** and is worth a real, cheap test. By that measure, **v1–v8 produced zero successes**.

---

## 1. What happened, version by version

| Version | When (BST) | What it did | Outcome |
|---|---|---|---|
| v1–v5 | 21 Oct 17:26 → 22 Oct 00:42 | Collected Koerner Office transcripts: 271, then 316, then 435. Mined them, ranked 192 → 207 → 227 → 344 ideas, and wrote playbooks. | Rankings with no web validation. |
| v6 | 22 Oct 00:22 → 01:47 | Chose a "UK trades tools hub" and a Bromley missed-call AI plan. Scanned 29 local trade websites. | Later ruled out: it sells to local businesses. |
| v7 | 22 Oct 01:58 → 23 Oct 00:35 (~22.5 h) | Structured extraction of all 435 transcripts (Grok Bot box first, then Codex). Opus QC, clustering and scoring, TOP10, red team, low- and then high-effort validation, hidden gems, benchmarks. | Best ideas scored ≤4/10 for success. "Start now" picks: a Shopify add-on and an iOS app. The **Shopify gap scan then found no term that passed.** |
| v8 | 23 Oct 09:25 → 16:16 (~7 h) | Wrote METHOD.md. Locked the rules, ran 20 market scouts, re-ingested and re-mined the same 435 transcripts with stricter structure, then clustered, scored, and validated 35 candidates. | **0 pursue, 2 maybe (low), 33 kill.** Both maybes were already on v7's list: the vault app (v7 #3) and the UK directory/calculator idea (v7 #4). |

**Headline:** v8 re-mined the same corpus with a better method and found nothing new that survived. Better processing can't add information that the source doesn't contain.

## 2. Yield funnel (v8)

| Stage | Count | Ratio |
|---|---|---|
| Transcripts | 435 | |
| Mined (1 quarantined) | 434 | 99.8% |
| Business records after splitting | 5,185 | |
| Ideas mined | 4,344 (4,334 in the flat file) | ~10 per transcript |
| … of which **passing mentions** (`depth=mention`) | 3,404 | **79%** (only 794 were "deep") |
| … of which need physical-world work | 2,435 | 56% |
| Passed the first filter into clustering | 2,645 | 61% |
| Clusters | 2,491 | |
| … backed by a **single video** | 2,054 | **82%** |
| Clusters passing all hard constraints | 195 | 7.8% of clusters |
| … of which single-video | 176 | **90% of passers** |
| … scoring ≥4/10 for success | 8 | 0.3% of clusters |
| Top slice validated (15 ranked + 5 most-cited) | 20 | |
| Scout leads validated | 20 | |
| **Validation survivors (maybe)** | 2 | 5.7% of the 35 validated |
| **Pursue at medium+** | **0** | 0% |

**What did the killing (scored clusters; a cluster can fail several):**

| Constraint failed | Clusters |
|---|---|
| Hours > 5 per week | 2,141 |
| Automation < 50% | 2,042 |
| Sells to local businesses | 514 |
| Needs a face or personal brand | 283 |
| UK PECR risk | 128 |

At validation, the **moat / copy-speed check** killed nearly everything that had survived the rules.

## 3. Where effort went vs where value came from

| Activity | Effort | Value produced |
|---|---|---|
| Transcript mining. v7: ~11 h of extraction, with Codex in batches and ~70 transcripts on the Grok Bot box. v8: ~4.5 h of ingest and mining, ~3,254 ideas on Codex, 364 on Claude, 716 on the Grok Bot box. | **Most of the compute and wall-clock.** Re-mining the same 435 videos twice. | Low. The v8 mining added 0 new survivors over v7. Its main value was negative knowledge: what YouTube side-hustle content is made of. |
| Clustering and scoring. v8: 312 Codex xhigh judge calls, ~55 min, plus a crash and a restart. | Medium | Low to negative. The scorer put a 2005 anecdote at #1, along with a self-described failure (C2253). |
| Market scouts (v8: 20 records in about one stage) | **Small** | **High.** These gave specific, checkable leads. Copy-speed was found here, and two v7 gaps (Gift Aid, FreeAgent) had already closed. |
| Live web validation (v8: 35 candidates, ~2 h, done by Grok Bot) | Medium | **Highest per hour.** Every decisive fact came from here: competitors launched in 2026, platform-owned integrations, GOV.UK dates, store rules. |
| Rate-limit stalls (v8) | **~3 h of wall-clock lost or degraded.** Codex was blocked 11:50 → 14:34 BST, and Claude 12:35 → 17:20 BST. The runner backed off instead of failing over; Grok Bot box mining bridged the gap from ~12:45 to 13:58, and clustering waited ~36 min for Codex. | None |

**Conclusion:** value per unit of effort ran **validation > scouts ≫ scoring > mining**. The pipeline spent its effort in the reverse order.

## 4. Failure modes, with evidence

1. **The source doesn't fit the brief.** YouTube "side hustle" content skews to physical, local or audience-dependent businesses: 56% of ideas need physical work, and 514 clusters sell to local businesses. The five most-cited clusters are tree care, pressure washing, liquidation, AI agency and lawn mowing, and all five fail the hard rules (VALIDATION LE5). The popularity signal points *away* from Ricardo's constraints.
2. **Mentions, not evidence.** 79% of ideas are passing mentions, and 82% of clusters rest on a single video. Clustering by distinct videos (METHOD step 7) works as designed, but nearly nothing converges.
3. **The scorer was fooled by first-hand revenue anecdotes of any age.**
   - C1143 ranked #1 on a "$4k/month" claim about a 2005 acquisition.
   - C2253 ranked #6 although its own guest says the app "never really took off".
   - C0168's strongest claim dates from 2011.
   - The staleness rule checked the *video* date, not the date of the *event* behind the claim.
4. **The moat / copy-speed check killed nearly everything, and it ran last.** Every live marketplace gap rechecked had a 2026 copy:
   - Chatpane, 1 Oct / 16 Oct 2026
   - MakePost, 7 Oct 2026
   - Postbag, 24 Sep 2026
   - 9 Harvest-for-Jira apps
   - 107 Mermaid apps
   - Gift Aid at ≥4 suppliers
   - Equali as FreeAgent's official partner
   - HubSpot's own Xero payment sync (LE2)

   Because this was the deciding filter, it should run **first and cheaply**, not after hours of mining and scoring.
5. **Platform owners close gaps themselves.** SC04 (FreeAgent → Equali), SC05 (Google's own app), SC09 (Xero-built Stripe app) and SC16 (HubSpot native payment sync) show that integration gaps between big platforms get owned by the platforms or their official partners. "Integration gap between two big SaaS platforms" is a weak lead type.
6. **The Grok Bot-side backlog was hidden.** v7's "start now" Shopify test was defined but returned no passing term, and that only came out in v8. Tests should be run as soon as they are defined, not carried forward.
7. **Rate-limit stalls.** `call_llm_codex` backed off for up to 30 × 10 min on Codex "usage limit … try again at 2:34", and `run_claude` didn't recognise Claude's "You've hit your session limit · resets 5:20pm" as a limit, because the keywords didn't match. **Fixed in `682273f`:** `scripts/common/runner.py` fails over immediately, records the reset time, falls back to box prompts, and has a self-test. The `common8.run_claude` keywords are patched too.
8. **Small pipeline bugs cost restarts.** These were a clustering crash from duplicated field assignment, Codex JSON parse failures (8 first attempts in `mine.log`, all recovered on retry), and ingest at `medium` over-removing content (510 of 1,005 lines in one transcript), which was reverted to xhigh.

## 5. What worked and should be kept

- Locking the rules before mining (`RULES_LOCKED.md`): no re-scoring was needed.
- Sampled quote verification: 99.7% of 746 sampled quotes passed, with no reliability loss.
- The completeness gate, plus quarantining bad inputs instead of halting.
- Structured, cited validation with "unverified" labels. Every verdict can be audited.
- Grok Bot box mining as the last fallback: 127 transcripts imported with 0 errors.
- Pushing at each stage, which gave a clean audit trail.

## 6. Recommendations to raise the probability of a successful outcome

In priority order. ★ marks the 3 chosen for v9, the maximum allowed per iteration (see LOOP.md).

1. ★ **Validation-first ordering.** Generate many cheap leads, then run a **cheap web kill-check** on each one before any deep work. The kill-check covers the incumbent count, launches in the last 6 months, platform ownership, hard-rule fit and claim age. Deep evidence and high-effort validation go only to the ~10–15 that survive. In v8 this would have removed all 20 scouts and most of the top slice for roughly 10% of the compute.
2. ★ **Change the sources: lead types with built-in timing or proof, instead of generic YouTube.**
   - (a) **UK regulation-change calendar.** Dated mandates force a purchase, and incumbents often move late. Examples to verify: the MTD for Income Tax thresholds stepping down, Companies House software-only filing from 1 Apr 2028, and DMCC subscription rules.
   - (b) **Decaying paid products with paying users.** Paid apps or plugins not updated in 12+ months with recent complaints. Filter for **no new entrant in the last 6 months**.
   - (c) **Acquisition marketplaces** (Acquire.com, Flippa, Microns and similar). Listings show real, often verified revenue for small agent-runnable products. That is demand evidence, and it also opens a buy-instead-of-build path.
   - (d) **Complaint mining on paid UK-relevant tools** (Trustpilot, G2, Capterra, store reviews), where the complainer is already paying.
3. ★ **Copy-speed and claim-age as first-class hard filters.**
   - Kill on copy-speed if ≥2 competitors launched in the last 6 months, or if the platform owner or an official partner already serves the need.
   - Down-weight to zero any revenue claim whose underlying *event* is older than 18 months. The age is the event date, not the video date.
4. **Smaller, targeted corpora.** If transcripts are used again, use ≤50 hand-picked recent (≤12 months) videos about software or digital products, never the full 435.
5. **Prefer a defensible asset over a gap.** Score explicitly for proprietary or UK-specific data, rules engines, or switching costs. In v8 the only survivors had some of this: on-device data and UK-specific logic.
6. **Run any defined test immediately.** A "maybe" with a named ≤1-day test gets that test inside the same iteration, so a maybe becomes pursue or kill rather than being carried forward.
7. **A seen-ideas ledger**, so killed ideas are never re-mined or re-validated (see LOOP.md).

## 7. Top 5 findings

1. **Source, not method, is the bottleneck.** Re-mining the same 435 videos with a much better method (v8) found 0 new survivors over v7. Both v8 maybes were already on v7's list.
2. **The pipeline spent its effort in reverse order of value.** Most compute went to mining and scoring, while every decisive fact came from cheap scouts and live web validation.
3. **Copy-speed is the dominant killer, and it ran last.** Every live gap rechecked had a 2026 copy or a platform-owned fix. It must be a cheap first filter.
4. **YouTube side-hustle content works against the brief.** 79% passing mentions, 82% single-video clusters, 56% physical work, and the top 5 most-cited ideas all break the hard rules.
5. **The scorer trusts any first-hand revenue story,** including a 2005 acquisition and a self-described failure. Claim-age (the event date) must gate the score. Separately, about 3 h of v8 wall-clock went to rate-limit back-off that should have been an instant fail-over (now fixed).
