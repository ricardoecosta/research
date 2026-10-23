# Retrospective: v9

**Written:** 23 Oct 2026, ~17:45 BST, by Grok Bot.
**Evidence:** `v9/leads.jsonl`, `v9/KILLCHECK.md` + `killcheck.json`, `v9/evidence/*.json`, `v9/SCORES.md`, `v9/VALIDATION.md`, `/tmp/loop/v9/run.log` and `calls.jsonl` on Ricardo's Mac.

## 1. Outcome

**P = 0, M = 0. P_cum = 0.** v8 also had P = 0, so the **stall rule (LOOP §2) triggers: the loop is paused** until Ricardo picks a direction (§5).

| Stage | Count |
|---|---|
| Leads harvested (7 Codex calls + 2 top-ups) | 78 |
| Dropped as ledger duplicates | 1 |
| Into kill-check | 77 (S1 23, S2 20, S3 20, S4 14) |
| Survived medium kill-check | 35 |
| Survived xhigh kill-check (safeguard re-run, used downstream) | 23 (S1 12, S2 4, S3 4, S4 3) |
| Deep evidence + scored | 23; best success score 5/10, only 1 above 4 |
| Validated (top 8) | 8 → **0 pursue, 0 maybe, 8 kill** (4 high, 4 medium confidence) |

**Why the 8 died** (`VALIDATION.md`): copy-speed or platform/partner already serving it (L019 SAML tracer, L014 Shopify banner, L070 spreadsheet→MTD, L074 FX bank feeds); demand too small or already owned by government/free tools (L009 Land Registry agreements, L031 landlord ombudsman, L037 fire-and-rehire); crowded cheap incumbents plus a paused trigger (L003 Companies House filing; the validator reports the P&L-filing change was paused on 23 Oct 2026, which I have not independently checked).

## 2. Did the 3 v9 changes help?

| Change | Verdict | Evidence |
|---|---|---|
| 1. Validation-first | **Helped on cost and speed, not on outcome.** | ~100 Codex + 8 Claude calls vs ~1,200 + 364 in v8; first verdict in 57 min vs ~6 h; run time about 1 h vs ~7 h. The yield didn't change: 0 pursue in both. |
| 2. New sources | **Mixed.** Novelty was 99%, so this is genuinely new ground, but no source produced a survivor. | S1 (regulation) had the best kill-check survival (12/23) but the lowest value: these needs are small, dated, and served by free GOV.UK/Acas/HMLR tools or bundled incumbents. S3 (acquisitions) listings were tiny (mostly <$25k ARR) and were judged as "build a rival", which is the wrong frame for them. S4 complaints were mostly MTD-related, and MTD software is a crowded, price-floored market (free to £5/month). S2 (decaying apps) revealed real orphaned users (e.g. the Chrome AppBox removals), but replacements appeared within weeks. |
| 3. Copy-speed + claim-age as hard filters | **Correct, but not strict enough early.** | K3 (platform/partner/free official tool) was the biggest killer: 35 of 54 xhigh kills; K2 copy-speed 12. Even after the xhigh kill-check, **4 of 8 validated candidates were killed on K2/K3**, so the kill-check's launch-date search is too shallow. Claim-age did no killing this round, since the new sources carry recent claims. |

## 3. What produced signal and what produced noise

- **Signal:** Claude validation with live fetches (dated competitor launches, official integrations, impact assessments). The xhigh shadow check, which caught that the medium kill-check was unreliable.
- **Noise:**
  - The **medium kill-check**: 28/77 verdicts flipped at xhigh, and 2/10 shadow kills were wrong. Its 20 calls were wasted, and 11 deep-evidence calls were spent on medium survivors that xhigh then killed.
  - The **scoring step**: 6 of the top 8 have `automation_share_pct = 0` because the evidence schema template defaulted it to 0 and the model left it. This is a bug, not a finding (infrastructure fix for v10). Scores were uniformly low (≤5), so ranking added little over the kill-check.
  - **"Build a rival" framing for acquisition listings.**
- **Structural finding (v7 → v9):** across ~110 validated or deep-checked candidates in three iterations, every software *gap* that a solo builder could fill in weeks had either been filled in 2026 or is served free by the platform or government. With AI coding, copy-speed in small SaaS/plugin niches is now weeks. **Searching for uncopied gaps is the losing strategy, not the sources.**

## 4. Cost and time

- Runners: Codex `gpt-6-luna` ~100 calls (29 medium, 65 xhigh, ~6 aborted/test), Claude Opus 5.5 8 calls, pi 0, Grok Bot box 0. No rate limits hit, so no fail-over was needed. Grok Bot web checks: 0.
- All within the LOOP §4 budget (≤250 Codex, ≤30 Claude, ≤5 h).
- Infrastructure fixes (don't count toward the 3): `runner.py` got `web=True` and a per-call `order`; `v9.py` is resumable with a per-call cache.

## 5. Proposed changes for v10 (max 3), and the stall decision for Ricardo

Because the stall rule fired, v10 should **change direction**, not just tune. My proposal is that v10 adopts all three changes below together:

1. **Defensible-asset-first sourcing and scoring** (LOOP §7, item 1). Only take leads where the product's value comes from something hard to copy in weeks: proprietary or compiled UK data (e.g. structured datasets assembled from many public sources), a maintained UK rules engine, a two-sided marketplace or network effect, or high switching cost. Score `defensible_asset` 0–10 and make "none" a kill. This attacks the dominant killer, K2/K3, at the source.
2. **Buy-instead-of-build track** (LOOP §7, item 3). Evaluate acquisition listings as purchases, with their own checklist: revenue verified via Stripe/marketplace screenshots, churn, transferability of platform accounts, owner hours, price ≤ ~3× annual profit. An existing customer base is itself the moat that a gap lacks. Source: Acquire.com, Flippa, Microns listings with ≥£1k/month verified profit.
3. **Single xhigh kill-check with an explicit dated-launch search.** Drop the medium pass (28/77 flips made it worthless). Require per lead: a search for competing launches in the last 6 months with dates, plus the platform-owner/official-partner check, before survival. Keep the 10-kill shadow check at Claude. Target: no validated candidate killed on K2/K3 at validation.

**Constraint question for Ricardo (only he can decide):** the hard constraints plus copy-speed leave very little space. Options he could consider: (a) the three changes above as-is; (b) also allow lawful B2B outreach to limited companies (PECR permits cold email to corporate subscribers with an opt-out); (c) also allow a modest time budget above 5 h/week for the first 3 months of a bought business.
