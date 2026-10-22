# v7: full re-mining of every transcript (22 Oct 2026)

**Why v7.** Earlier batches (v2–v6) fed Claude *compact digests* (intro + keyword sentences) at low effort, and produced one card per idea with no quotes. v7 reads **the full text of every transcript**, extracts a fixed-schema learnings record per video with verbatim, machine-verified quotes, and rebuilds the idea catalogue and ranking from scratch with an automation-first rubric.

## Layout

| Path | What it is |
|---|---|
| `schema/transcript_learnings.schema.json` | JSON Schema (draft 2020-12) for one transcript's learnings record |
| `transcripts/<video_id>.json` | Structured record per transcript (validated against the schema) |
| `transcripts/<video_id>.md` | Readable note rendered from the JSON |
| `INDEX.md` | Browsable table of all mined transcripts (newest first) with links to notes |
| `learnings.jsonl` | Consolidated dataset: one record per line |
| `ideas_flat.{jsonl,csv}` | Every idea mention, one row each (key = `video_id:I#`) |
| `clusters/` | Deduplication/clustering passes and final `membership.json` (canonical idea → member mentions) |
| `ideas_catalogue.{md,json}` | Re-deduplicated idea catalogue; every idea links all source videos |
| `ideas_scored.{csv,json}` | Scores for every canonical idea (rubric below) |
| `scores/` | Raw judge outputs (Opus) for the shortlisted ideas |
| `synthesis/` + `SYNTHESIS.md` | Cross-transcript learnings: principles, acquisition channels, pricing, failure modes, tactics |
| `reviews/` | Opus audits of a random sample of extractions, with the corrections applied |
| `QA.md` | Quality-assurance results (quote verification, review error rates) |
| `TOP10.md` | The 10 best near-fully-automatable ideas, red-teamed |
| `cost_log.csv` | Every Claude call: stage, model, list-price cost, tokens |
| `../../scripts/v7/` | Pipeline code (extract → finalize → consolidate → review → cluster → score → synth; `driver.py` runs it unattended) |

## Record schema in one paragraph

Each record has `video` metadata (id, title, channel, upload date from YouTube, duration, transcript provider, Whisper flag), `summary`, `speakers`, `format`, `ideas[]`, `metric_claims[]`, `tactics[]`, `tools_mentioned[]`, `warnings[]`, `lessons[]`, `evidence_quality` (A–D + promotional conflicts) and `extraction` provenance. Each idea is deconstructed into **customer, problem, offer, business model, pricing (price points), acquisition channels (enum + what they did), delivery, unit-economics claims, tools, startup cost, time to first revenue, automation (acquisition / onboarding / delivery / billing / support, 0–5 each), UK applicability (0–5), risks, depth (deep / moderate / mention)** and verbatim quotes.

**Conventions.**
- Every money figure is a **claim** by a speaker (`first_hand`, `hypothetical` flags), never a verified fact.
- Fields ending `_e` and all scores are estimates **[E]**.
- Transcripts carry no timestamps, so `approx_timestamp_s` is estimated from the quote's position in the text × video length: treat it as ±1–2 minutes.
- Quotes are checked against the transcript by fuzzy matching (`verified` = score ≥ 90/100 after normalising case and punctuation).
- 118 transcripts came from local Whisper (tiny); names and numbers in them are less reliable (`transcript_is_whisper`).

## Scoring rubric (canonical ideas)

**Chance of success (0–100)** = 100 × (0.30·E + 0.20·S + 0.30·R + 0.20·M) / 5
- **E: evidence strength (0–5)**, computed from the best evidence rating among the idea's substantive (non-passing-mention) sources: A = 5, B = 4, C = 2.5, D = 1; +0.5 if there are ≥ 2 first-hand, non-hypothetical metric claims; mention-only ideas = 1. The judge may adjust by −1/0/+1 for inflated, promotional or hypothetical claims, or for unusually strong corroboration.
- **S: independent sources (0–5)**, distinct videos: 1 → 1, 2 → 2, 3–4 → 3, 5–7 → 4, 8+ → 5.
- **R: realism for Ricardo (0–5)** [E]: a solo, technical, part-time (≈6–8 h/week) founder in Bromley with a ~£300 test budget: capital, hours, skills, UK regulation and demand.
- **M: market headroom (0–5)** [E]: saturation, AI commoditisation and platform risk in 2026.

**Automation (0–100%)** = weighted mean of five parts scored 0–5 [E]: acquisition 30%, delivery 25%, support 20%, onboarding 15%, billing 10%.
- 0 = a human every time; 3 = agents do most with routine human checks; 5 = unattended software.
- Physical-world delivery caps delivery at 0–1. In-person or cold outreach to consumers/sole traders caps acquisition at ≤ 1, because UK PECR bans unsolicited marketing texts, WhatsApps, social DMs and emails to individuals and sole traders without consent. Cold email to limited companies is allowed, and cold calls need TPS/CTPS screening plus a human. **High automation therefore requires a UK-legal inbound or self-serve acquisition channel** (search, marketplaces and app stores, paid ads, content, affiliates).

**Combined** = 0.55 × success + 0.45 × automation. **TOP 10 eligibility:** automation ≥ 75% and a UK-legal acquisition channel.

Preliminary scores, which use the extractor's per-video estimates, cover every idea. A shortlist (preliminary automation ≥ 50% and either ≥ 2 sources or evidence ≥ 4) is re-scored by Claude Opus as the judge, using an aggregated dossier for each idea. The `scored_by` column says which method each row used.
