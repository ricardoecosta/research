# Self-optimising research loop

**Written:** 23 Oct 2026 by Grok Bot. This version includes Ricardo's 23 Oct updates to the stopping rule, cost policy and inference fallbacks.

**How it relates to the other files:**
- `METHOD.md` is the canonical method.
- This file defines how the method is run, scored and improved, one iteration at a time.
- The evidence behind the design is in `RETRO_v8.md`.

## 1. Objective

Find business opportunities that pass high-effort, web-checked validation with **verdict = pursue at medium or high confidence**, under Ricardo's hard constraints. **Market scope: any country** (changed 23 Oct 2026, 19:10 BST, from UK-only). Ricardo is UK-based, so his own UK compliance applies, and outreach must be lawful where he and the recipient are.
- mostly run by AI agents, ≤5 h/week of his time
- interesting to him
- not selling to local businesses
- no face or personal brand
- no reliance on cold outreach that PECR bans

### Metrics per iteration (recorded in `loop/SCOREBOARD.md`)

| Metric | Definition | Role |
|---|---|---|
| **P (primary)** | New candidates with verdict *pursue* at medium+ confidence. | Objective |
| P_cum | Cumulative P across iterations. | Stopping rule |
| M | New *maybe* verdicts, plus how many had their named cheap test run inside the iteration. | Secondary |
| Survivor rate | (pursue + maybe) ÷ leads that entered the cheap kill-check. | Is the source any good? |
| Novelty | Share of leads not already in `loop/SEEN.csv` (key match or close name match). | Are we re-mining old ground? |
| Kill-check precision | Of 10 sampled cheap kills re-judged at xhigh, how many were wrong kills. | Safeguard for cheap triage |
| Cost | Calls by runner (Codex / Claude / pi / Grok Bot box), Grok Bot web-check count, and wall-clock. | Budget |
| Time to first verdict | From iteration start to the first validated verdict. | Speed |

## 2. Stopping rule

- **Stop** when **P_cum ≥ 5**: at least 5 opportunities with verdict pursue at medium+ confidence, counted across iterations. Or stop whenever Ricardo says so.
- **There's no iteration cap.**
- **Stall rule:** if **2 consecutive iterations add P = 0**, pause the loop. Report to Ricardo with the scoreboard and a **proposed change of direction**: a new source family, a relaxed or changed constraint, or a buy-instead-of-build route. Don't start the next iteration until he answers.
- **Note:** v8 had P = 0, so if v9 also has P = 0, the stall rule triggers after v9.

## 3. Iteration procedure

Each iteration is called vN and runs:

1. **Plan.** Read `RETRO_v(N-1).md` and choose **at most 3 method changes**, so their effect can be attributed. Record them in `vN/CHANGES.md`. Infrastructure fixes, such as runners and bug fixes, don't count toward the 3.
2. **Lock.** Write `vN/RULES_LOCKED.md` before any lead generation (METHOD EFFICIENCY rule 2).
3. **Run.**
   - Generate leads from **new or different sources and angles** only. Never re-mine material already processed. The 435 Koerner transcripts are retired.
   - Drop any lead already in `loop/SEEN.csv`, unless its `recheck_after` date has passed.
   - Then run the stages in §6, with validation first.
4. **Validate.** High-effort, web-checked validation (METHOD step 10) produces pursue/maybe/kill verdicts, each with a confidence and links. A *maybe* whose deciding test takes a day or less and is desk-only gets that test **inside the iteration**.
5. **Score the outcome.** Fill in the §1 metrics in `loop/SCOREBOARD.md`. Add every validated or killed lead to `loop/SEEN.csv`.
6. **Retro.** Write `RETRO_vN.md`:
   - what produced signal and what produced noise
   - whether each of the ≤3 changes helped, judged by survivor rate, P, cost and kill-check precision
   - the ≤3 changes proposed for vN+1
7. **Update METHOD.md as a new version.** Add a dated "vN+1 changes" section. Never rewrite history silently.
8. **Check the stopping rule (§2).** Then report to Ricardo and start vN+1, or pause.

**Pushing:** push after each stage via `push.sh` from the Mac, as now.

### Seen-ideas ledger: `loop/SEEN.csv`

- **Columns:** `key, name, source, first_seen, verdict, confidence, reason, evidence, recheck_after`.
- **Seeded with 220 rows:** v8's 35 validated candidates, the 5 most-cited step-11 rule kills, and the 180 other v8 clusters that passed the hard rules but weren't validated.
- **Rule:** a lead matching a ledger row by key or close name is skipped. The exception is a row whose `recheck_after` date has passed; those are watch items. Current watch items:
  - SC05 Google Chat for Jira / Chatpane traction: 31 Jan 2027
  - SC04 Equali / FreeAgent: 1 Apr 2027

## 4. Cost policy and budget

Optimise for **the lowest cost that keeps decision quality**. These rules are learned from v7 and v8:

1. **Validation first.** Run cheap web kill-checks (copy-speed, platform ownership, hard rules, claim age) **before** any deep mining or scoring. Spend deep effort only on survivors.
2. **Small targeted corpora.** Use about 60–100 leads per iteration, not 435 videos. If transcripts are ever used again, cap them at 50 hand-picked videos from the last 12 months.
3. **Effort tiers:**
   - **low:** harvesting, formatting, dedup against the ledger, and anything mechanical or already decided.
   - **medium:** the cheap kill-check, which must cite URLs. Each iteration, 10 sampled kills get a shadow re-judge at xhigh. If ≥2 of the 10 are wrong kills, re-run the whole kill-check at xhigh (METHOD EFFICIENCY safeguard).
   - **xhigh / Opus high:** judgement steps only: deep evidence, scoring and validation.
4. **Sampled verification, not full.** Quote and claim checks are sampled per runner (METHOD step 6).
5. **No re-mining** of seen material (the ledger).
6. **Bulk work on the Mac** (Codex, then Claude). Grok Bot spends credits only on orchestration, final spot-checks of pursue verdicts, and the last-resort box fallback.

### Per-iteration budget (hard caps; pause and report if one would be exceeded)

| Item | Cap | v8 for comparison |
|---|---|---|
| Wall-clock | **≤ 5 h** from lock to scoreboard | ~7 h (09:25–16:16) |
| Leads entering the kill-check | ≤ 100 | 2,491 clusters + 20 scouts |
| Codex calls (all efforts) | ≤ 250 | ~1,200 (435 ingest + 435 mine + clustering + 312 judge) |
| Claude Opus calls | ≤ 30 (validation and shadow checks) | 364 mining answers + 0 validation |
| Grok Bot box-fallback prompts | ≤ 50; above that, pause and ask | 127 transcripts |
| Grok Bot web checks | ≤ 40, only for pursue/maybe spot-checks or when the Mac runners are all blocked | 35 full validations |
| Ricardo's time | ≤ 30 min per iteration: read the scoreboard, approve or redirect | n/a |

## 5. Inference fallbacks (every LLM-calling stage)

**Rule:** a stage **never stalls** on a rate limit. It fails over immediately and switches back to the cheaper runner after the recorded reset.

| Order | Runner | Command | Notes |
|---|---|---|---|
| 1 | Codex `gpt-6-luna` | `~/.local/bin/codex exec … < /dev/null` (wrapped by `runner.run_codex`) | Cheapest; default for bulk work. |
| 2 | Claude `claude-opus-5-5` | `~/.local/bin/claude -p --model claude-opus-5-5` | Default for high-effort validation. |
| 3 | pi | `/opt/homebrew/bin/pi -p --no-tools @prompt` | Only works if pi has its own model account; untested in v8. |
| 4 | Grok Bot box | Prompts dumped to `/tmp/loop/box_prompts/<tag>.txt`; Grok Bot writes `/tmp/loop/box_answers/<tag>.json`; the stage re-runs and ingests them | Proven 23 Oct: 127 transcripts, 0 errors. Capped by the budget. |

**Implementation:** `koerner-office/scripts/common/runner.py` (commit `682273f`).

- **Detection** reads the output text:
  - Codex: `"You've hit your usage limit … try again at 2:34 PM"`
  - Claude: `"You've hit your session limit · resets 5:20pm"`
  - also `429`, `overloaded` and `rate limit`

  Self-test: `python runner.py` runs the 6 cases above and passes.
- **On a limit:**
  1. Parse the reset time into a local datetime (default +60 min if it can't be parsed).
  2. Store it in `/tmp/loop/runner_state.json`.
  3. Move to the next runner **in the same call**.
- **Blocked runners are skipped until their reset passes.** Then the cheaper runner is used again automatically.
- **If every runner is blocked,** `BoxPending` is raised:
  - The stage skips that item and continues with the others.
  - An hourly watch, or Grok Bot directly, answers the dumped prompts.
  - A re-run picks up `box_answers/<tag>.json` without calling an LLM.
- **v8 is patched too:** `common8.run_claude` now recognises Claude's "session limit / resets" wording. In v8 that message wasn't caught, and Codex's busy loop backed off for up to 30 × 10 min instead of failing over. Together these cost ~3 h.

## 6. v9 plan

### The 3 method changes (from RETRO_v8 §6)
1. **Validation-first ordering:** a cheap web kill-check runs before deep evidence and scoring.
2. **New sources** replace the 435 YouTube transcripts: the UK regulation calendar, decaying paid products, acquisition listings, and paid-tool complaints.
3. **Copy-speed and claim-age become hard filters:**
   - Kill if ≥2 competitors launched in the last 6 months.
   - Kill if the platform owner or an official partner already serves the need.
   - Revenue claims whose underlying event is >18 months old get zero weight.

### Stages

| # | Stage | Runner and effort | Output | Time |
|---|---|---|---|---|
| 0 | Load `SEEN.csv`; write `v9/RULES_LOCKED.md` and `v9/CHANGES.md` | none / Grok Bot | locked rules | 10 min |
| 1 | **Lead harvest**, 4 sources in parallel, ≤100 leads total (see below) | Codex low/medium with web search if available, else Claude with WebSearch/WebFetch; fallbacks per §5 | `v9/leads.jsonl` with URLs | 60–75 min |
| 2 | **Dedup against the ledger, then the cheap kill-check**: hard rules, copy-speed, platform ownership, claim age, incumbent count; every kill cites a URL. Shadow-check 10 kills at xhigh. | Codex medium; shadow at Codex xhigh or Claude | `v9/KILLCHECK.md`; ~10–15 survivors expected | 45 min |
| 3 | **Deep evidence** on survivors: demand size, prices, revenue proof (with event dates), defensible asset, build effort | Codex xhigh | `v9/evidence/*.json` | 45 min |
| 4 | **Score** with 4 separate scores as in METHOD step 8, plus claim-age and copy-speed fields | Codex xhigh | `v9/SCORES.md`, top ≤8 | 20 min |
| 5 | **High-effort validation** of the top ≤8, plus a ≤1-day desk test for any maybe | Claude Opus high; Grok Bot if Claude is blocked | `v9/VALIDATION.md` | 60–90 min |
| 6 | Scoreboard, ledger update, `RETRO_v9.md`, METHOD "v10 changes", stopping-rule check, report | Grok Bot (small) | pushed | 20 min |

**Expected runtime: about 4–5 h of wall-clock**, mostly unattended on the Mac, with one hourly watch routine. That compares with ~7 h for v8. The expected load is ~150–250 Codex calls, ≤30 Claude calls, and ≤40 Grok Bot web checks.

### Stage-1 sources (targets are leads, not survivors)

**S1. UK regulation-change calendar, 20–25 leads.**
- Harvest from GOV.UK, HMRC, Companies House, FCA, ICO, Ofgem and legislation.gov.uk.
- Look for changes **commencing Nov 2026 – 2028** that force a small business, landlord, charity or consumer to buy software, a digital product or a data service.
- Candidates to verify, not facts:
  - the MTD for Income Tax threshold steps
  - Companies House identity verification and software-only accounts filing from 1 Apr 2028 (confirmed in VALIDATION)
  - the DMCC Act subscription-contract rules
  - Renters' Rights Act obligations
- **Kill-check angle:** who already sells the compliant tool, and at what price floor? SC17 shows the floor can already be £5–£20.

**S2. Decaying paid products with paying users, 20–30 leads.**
- Places to look:
  - the Atlassian REST API (paid, last release ≥12 months ago, ≥200 installs, 2026 reviews ≤3★)
  - the WordPress.org plugins API (closed or not updated, ≥10k active installs, with a paid pro version)
  - Shopify and Xero app pages
  - the Chrome Web Store
  - iOS utilities, via Appaloma-style catalogues
- **Hard filter:** no new competing entrant in the last 6 months, and the incumbent isn't the platform owner.

**S3. Acquisition marketplaces, 15–20 leads.**
- Public listings on Acquire.com, Flippa and Microns-type sites for small software or digital products, priced under ~£50k, with stated revenue and low owner hours.
- **Use:** proof that a niche pays, and a buy-instead-of-build option.
- **Record:** asking price, stated revenue and its verification status, and listing date.
- **Kill if:** it needs a face, local sales, or support beyond 5 h/week.

**S4. Paid-tool complaint mining, 10–15 leads.**
- Trustpilot, G2, Capterra and store reviews of paid tools used by UK sole traders or small businesses.
- Look for complaints from **paying** users about UK-specific gaps (VAT, HMRC, Companies House, UK banks, Royal Mail).
- **Kill-check:** is the gap already fixed or copied?

### Not in v9 scope, pending Ricardo
- The two v8 maybes' tests both need spending or a long wait:
  - The vault ASO check needs a paid ASO tool, or about a day of manual work.
  - The utility-site test needs a domain and 8 weeks of watching.
- Run them alongside v9 only if Ricardo says so.

## 6b. Iteration log
- **v9:** validation-first, new UK sources, copy-speed and claim-age filters. P = 0.
- **v10:** moat gate, buy track and a single xhigh kill-check; scope changed to any country. P = 0, and the stall rule fired.
- **v11** (Ricardo, 23 Oct 22:25 BST): time-to-moat (build), a buy track judged on a 90-day handover to agents ($20k–$150k, verified revenue only, ≤5 h/week after the handover, ~60% of leads), and a demand-first source (verified revenue ≥$1k/month, within 18 months). See `v11/CHANGES.md`.
  - **PAUSED 23 Oct 2026, 22:26 BST at Ricardo's request, pending a method review.** Stage reached: stage 0 done (rules locked, `1317504`). Stage 1 (harvest) had just started, and its 5 in-flight Codex calls were stopped before returning. No leads were saved. To resume, run `cd koerner-office/scripts/v11 && /tmp/v7venv/bin/python v11.py harvest killcheck shadow evidence score validate`. Re-lock the rules first if the review changes them.

## 7. Proposed METHOD changes not yet adopted

These stay here until a retro shows they're needed:
- Score explicitly for a defensible asset (proprietary or UK-specific data, a rules engine, switching costs).
- Drop transcripts from the default sources entirely, and keep them only as a ≤50-video targeted corpus.
- Add a "buy instead of build" track with its own validation checklist (verify revenue, check transfer risk, check the platform account can transfer).
