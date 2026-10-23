# v8 locked rules

Locked on 23 Oct 2026, before any v8 mining started, per METHOD.md (commit 31dfcc4), EFFICIENCY rule 2.
Nothing below changes during the run. If a rule must change, the change is logged in `RULE_CHANGES.md` with the reason, and every stage it touches is re-run.

## Inputs and completeness gate

- Input set: the 435 files in `koerner-office/transcripts/raw/*.txt`. Publish dates and durations come from the v7 date lookup (`/tmp/v7/dates.tsv`, copied to `analysis/v8/ingest/dates.tsv`).
- `analysis/v8/MANIFEST.csv` tracks every transcript through every stage: `ingested`, `mined`, `quarantined` (with reason).
- **Completeness gate:** clustering, scoring and ranking do not start until every one of the 435 transcripts is either `mined` or `quarantined`. The gate check is scripted (`gate.py`) and its output is committed.

## Quarantine (isolate corrupt inputs without halting)

A transcript is quarantined, listed in `analysis/v8/QUARANTINE.csv` with the reason, and the run continues, when any of these hold:

- the file can't be read or decoded (over 1% replacement characters);
- the body is under 1,500 characters;
- it's not English (under 85% of letters are ASCII);
- it's a Whisper loop or garbage (under 35% of word 5-grams are unique);
- no publish date is known;
- the ingest or mining step fails 3 times on all fallback models, or returns output that fails the schema 3 times.

## Step 1: cleaning

- Deterministic: the body is split into numbered lines (`L0001`…) at sentence ends, or every 30 words when there's no punctuation. Each line carries an approximate minute (its character offset × video duration). These original numbered lines are what every citation points to.
- Model-labelled (Codex): line ranges that are sponsor reads/ads, intros/outros/channel plugs, pure filler, or tangents unrelated to any business are marked removed with a reason. Removed ranges are recorded in `ingest/<id>.json`; the original is never edited.
- Cheap triage effort (`medium`) is used for this labelling, subject to the shadow comparison below.

## Step 2: splitting

- Ingest returns one **record per business** (`<video>#r1`, `#r2`…) with its line ranges and the business as the speaker names it. A record never mixes two businesses. Mining attaches every idea to exactly one record; an idea outside every record gets a new record flagged `added_at_mining`.

## Step 3: dates and specifics

- Every record carries the video publish date.
- `specifics_flag = true` when the idea names a specific tool, price, platform or marketplace.
- **Staleness rule:** evidence is `stale` when the video is older than 18 months (published before 23 Apr 2025), and `recheck` when it rests on tool-, price- or platform-specific claims. A cluster is `stale` when all its backing videos are stale. Stale and recheck items must be rechecked at validation; they are not dropped.

## Step 4: mining (structured output)

- Bulk mining runs on Codex (gpt-6-luna, xhigh) on Ricardo's Mac, one call per transcript, fixed JSON schema (`scripts/v8/mine_schema.json`). Fallback order: Codex → pi → Grok Bot.
- Each idea: `stated_problem` (speaker's own words, verbatim, with line, captured before interpretation; `null` when no problem is stated), then `idea` (our interpretation), `citation` (line numbers and approximate minute; no citation, no idea), `claims` (each with verbatim quote and line), `feature_request` (negative tag), `specifics`, `uk_legal_risk`, acquisition channels, delivery, and triage flags (`sells_to_local_businesses`, `needs_face_or_personal_brand`, `physical_world`), plus the miner's rough automation share and hours (triage only, never used to rank).
- Feature requests are kept in `ideas_feature_requests.jsonl` and don't enter clustering as standalone businesses.

## Step 5: UK legal filter

- Under PECR, cold SMS, WhatsApp and DMs to individuals or sole traders are banned; cold email is allowed only to limited companies, with an opt-out. An idea whose acquisition **relies** on banned channels gets `uk_legal_risk.flag = true` with the reason, at mining. Flagged ideas are carried forward, not dropped, and are excluded from the top slice.
- Other UK rules noted when relevant: TPS/CTPS, UK GDPR, DMCC Act subscription rules, Conduct of Employment Agencies Regulations 2003.

## Step 6: quote verification (sampled)

- Fuzzy match (rapidfuzz `partial_ratio`, normalised text, `...` fragments matched separately, minimum fragment score) against the original transcript. **90/100 or better passes.**
- A miner is one model/runner (e.g. `codex:gpt-6-luna`, `pi`, `grokbot`). Sample: within each miner, transcripts are grouped in batches of 25 in processing order, and 40 quotes are sampled per batch (all quotes if fewer), seed 8.
- A batch whose sample passes under 95% is escalated to a full check of every quote in that batch.
- Failed quotes are `unverified`: kept for audit, never evidence. Unsampled quotes in a batch that passed count as `batch_certified`.
- Before handoff to validation, every quote backing a top-slice cluster is checked (local fuzzy matching, no model tokens).
- The cited line is also checked: the quote must match within its cited line ±2 lines; a miss is reported as a citation error.

## Step 7: clustering

- Codex (xhigh) clusters non-feature-request ideas per category (chunks of ≤250), then merges across categories. Support = **distinct videos**, never raw mentions. Single-video clusters are marked `single_video`.

## Step 8: scoring

Every cluster is scored by Codex (xhigh) in batches of 8, four separate scores, each with a written reason:

| Score | Scale |
|---|---|
| `success_12m` | 0–10: realistic odds of meaningful revenue within 12 months for Ricardo |
| `agent_runnability` | 0–10: share of day-to-day an AI-agent team can run |
| `fit` | 0–10: fit with Ricardo's interests, skills, hours and hard constraints |
| `automation_share` | 0–100%: realistic automated share of all work, including sales, support and admin |

plus `hours_per_week` (Ricardo's realistic hours), and flags `sells_to_local_businesses`, `needs_face_or_personal_brand`, `uk_legal_risk`, `physical_world`.

Ricardo's profile for scoring: technical, UK-based (London/Bromley), solo, part-time, small test budget; wants high automation and ideas he'd enjoy; rules out selling to local businesses and anything needing his face or personal brand; UK PECR applies.

The four scores are never collapsed into one number.

## Step 9: automation distribution

Report the distribution of `automation_share` across **all** scored clusters (10-point bins and counts at ≥40, 50, 60, 70%), and the miners' triage estimates across all ideas, labelled as triage.

## Top slice (handoff to step 10, not a shortlist)

- Hard constraints (prior filters): `automation_share ≥ 50`, `hours_per_week ≤ 5`, not `sells_to_local_businesses`, not `needs_face_or_personal_brand`, no `uk_legal_risk`.
- Order among clusters that pass: `success_12m`, then `fit`, then `agent_runnability`, then distinct videos (lexicographic; scores stay separate).
- Top slice = the first 15 that pass, **plus** the 5 most-cited clusters (most distinct videos) regardless of rank or constraints (step 11). Rule-breakers in the cited group are labelled with the rule they break.
- Step 10 (high-effort, web-checked validation) is the gate and is not part of this run. No final shortlist is produced here.

## Efficiency rules and shadow comparisons

- Cheap tokens only for triage (ingest labelling). Mining, clustering and scoring run at xhigh.
- Any efficiency change gets a shadow comparison on one batch first, written to `analysis/v8/qc/shadow_*.md`:
  - Ingest at `medium` vs `xhigh` on the first 10 transcripts. Revert to `xhigh` if `medium` finds fewer business records in total (more than 10% fewer) or misses a record that `xhigh` finds in 2 or more transcripts.
  - Sampled vs full quote check on the first mining batch. Revert to full checks if the sampled pass rate differs from the full rate by more than 2 points.

## Pushing

Each finished stage is pushed to main from Ricardo's Mac (`scripts/v7/push.sh`, pull --rebase, never force). The `analysis/v8/scouts/` folder belongs to the parallel scout job and is never touched by this pipeline.
