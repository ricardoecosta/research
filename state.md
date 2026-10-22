# Research State

**Updated:** 22 Oct 2026, 02:20 BST (v7 deep re-mining in progress)  
**Repository:** https://github.com/ricardoecosta/research.git  
**Status:** 435/655 transcripts collected. **v7 full re-mining of all 435 transcripts is in progress** (structured learnings per transcript, idea deconstruction, re-clustered catalogue, automation-first top 10). Older idea rankings (344 ideas) came from low-effort batches and are superseded once v7 finishes.

## Active objective (v7, requested 22 Oct 2026)

1. Mine learnings from every transcript into a fixed JSON schema + readable note (`koerner-office/analysis/v7/`).
2. Deconstruct every idea (customer, problem, offer, pricing, acquisition, delivery, unit-economics claims, tools, automation, UK applicability, risks).
3. Re-cluster ideas, score with an explicit rubric (chance of success x automation %), and deliver a red-teamed TOP 10 of near-fully-automatable ideas.

## v7 progress

| Stage | Status |
|---|---|
| Schema + pipeline (`koerner-office/scripts/v7/`) | done |
| Per-transcript extraction (Claude Sonnet via Claude Code on Ricardo's Mac) | **69/435** — paused by the Claude plan's usage limit (resets 04:50 BST); an unattended driver resumes automatically and pushes every ~50 |
| Opus quality review (random sample of 30) | pending (1 pilot review done) |
| Clustering / dedupe | pending |
| Scoring + TOP 10 + Opus red team | pending |
| Cross-transcript synthesis | pending |

Cost log (list-price equivalent reported by Claude Code; billed against Ricardo's Claude plan): `koerner-office/analysis/v7/cost_log.csv`.

## Corpus counts (checked 22 Oct 2026)

| Metric | Value |
|---|---:|
| Channels inventoried | 16 |
| Videos inventoried (`koerner-office/data/transcripts_v2.jsonl`) | 655 |
| Transcripts collected (`koerner-office/transcripts/raw/`) | **435** |
| Not collectable | 220 (44 members-only + 176 blocked/error) |
| Transcript sources | 133 cached, 119 TranscribeYouTube, 51 multi-provider, 14 FreeTranscriptAPI, 118 local Whisper (tiny) |
| Legacy ranked ideas (pre-v7, `analysis/all_ideas_ranked.*`) | 344 |
| Playbooks (`koerner-office/playbooks/`) | 6 |
| Plans (`koerner-office/plans/`) | 3 |

Fixes vs the previous version of this file: the old header said "all 435 mined" while plan notes found 119 transcripts with no ideas cited; v6 was described both as "177 unprocessed" and "198 newly available". Those legacy batches were low-effort, so v7 re-mines **every** transcript from scratch rather than reconciling them.

## History (pre-v7)

### What was done before v7

- 435/655 transcripts collected.
- Local Whisper fallback used for 118 transcripts.
- FreeTranscriptAPI and TranscribeYouTube used for the rest.
- 43 videos were verified members-only at the time (the index now lists 44 as unavailable after `ckH5sENc108` was added); no public transcripts remain for them.
- Membership retry: `3a9wiJXt-5k` still returns “Join this channel to get access to members-only content.” No access change.
- 21 Oct 2026: added the next 15 public Koerner Office videos not yet in the repo (12 Mar – 10 Apr 2026; the repo already covered every public full-length upload from ~10 Apr to 19 Oct 2026). All 15 fetched via TranscribeYouTube captions; no Whisper. Newest upload `ckH5sENc108` is members-only and was added to `koerner_videos_all.tsv` only.
- v4 extraction: 17 cards → 15 new ranked ideas + 2 merged into existing ones.
- v6 extraction: 117 new cards from 198 newly available transcripts; 344 total ideas.
- Playbooks: `koerner-office/playbooks/snail-mail-story-subscription.md`, `koerner-office/playbooks/ai-missed-call-text-back.md`.
- 21 Oct 2026 (second run): added the next 30 public Koerner Office videos older than `mAyZZc_DjSE` (28 Dec 2025 – 10 Mar 2026). English captions were checked for all 30 before any download; all 30 fetched via TranscribeYouTube captions; no Whisper; none skipped.
- v5 extraction: 28 cards → 20 new ranked ideas + 8 merged into existing ones (incl. a second source for the snail-mail idea). All 227 ideas re-ranked together; top 22 unchanged; one new top-30 entry (#25 AI voice-agent receptionist).
- Playbooks added: `build-first-websites-local-business.md`, `apify-actor-wrapper-maps-lead-scraper.md`, `amazon-review-intelligence-tool.md` (the three fully automatable picks, with an automation section) and `photo-magnets-weddings-markets.md`. Snail-mail and missed-call playbooks updated with new evidence.
- 15 new Claude Opus 5.5 low-effort batches completed over the 177 unprocessed transcripts.
- Full transcript index: `koerner-office/data/transcripts_v2.jsonl`.
- Source notes: `koerner-office/TRANSCRIPT_SOURCES.md`.


## Key files (legacy)

- `koerner-office/analysis/all_ideas_ranked.md`
- `koerner-office/analysis/all_ideas_ranked.csv`
- `koerner-office/analysis/all_ideas_ranked.json`
- `koerner-office/data/transcripts_v2.jsonl`
- `koerner-office/MANIFEST.md`
- `koerner-office/RETRY.md`
- `koerner-office/TRANSCRIPT_SOURCES.md`

## Constraints

- Do not rotate VPN IPs to evade YouTube blocks.
- Members-only videos require channel membership.
- Opportunity scores are LLM-assisted research judgments, not audited financials.
