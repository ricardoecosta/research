# Research State

**Updated:** 21 Oct 2026 (membership retry)  
**Repository:** https://github.com/ricardoecosta/research.git  
**Status:** 316/359 transcripts collected and mined; 227 ideas ranked; 43 remaining videos verified members-only and inaccessible. Pushed to `origin/main`.

## Active objective

Do all possible until the most transcripts are collected, mine every unprocessed transcript, and push new research data to GitHub.

## Current counts

| Metric | Value |
|---|---:|
| Channels inventoried | 16 |
| Videos inventoried | 359 |
| Transcripts collected | **316** |
| Transcripts remaining | **43** |
| Remaining reason | Members-only / inaccessible |
| Transcripts mined into ideas | 316 |
| New transcripts awaiting mining | 0 |
| Ranked ideas | 227 |
| Extraction batches completed | 35 (29 Claude + 2 v4 + 4 v5) |
| New extraction outputs | `koerner-office/analysis/v5_batches/` |
| Playbooks | 6 (`koerner-office/playbooks/`) |

## What is done

- 316/359 transcripts collected.
- Local Whisper fallback used for 118 transcripts.
- FreeTranscriptAPI and TranscribeYouTube used for the rest.
- All 43 remaining videos verified members-only; no public transcripts remain.
- Membership retry: `3a9wiJXt-5k` still returns “Join this channel to get access to members-only content.” No access change.
- 21 Oct 2026: added the next 15 public Koerner Office videos not yet in the repo (12 Mar – 10 Apr 2026; the repo already covered every public full-length upload from ~10 Apr to 19 Oct 2026). All 15 fetched via TranscribeYouTube captions; no Whisper. Newest upload `ckH5sENc108` is members-only and was added to `koerner_videos_all.tsv` only.
- v4 extraction: 17 cards → 15 new ranked ideas + 2 merged into existing ones. Top 21 unchanged; new entries at #22, #24 and #29.
- Playbooks: `koerner-office/playbooks/snail-mail-story-subscription.md`, `koerner-office/playbooks/ai-missed-call-text-back.md`.
- 21 Oct 2026 (second run): added the next 30 public Koerner Office videos older than `mAyZZc_DjSE` (28 Dec 2025 – 10 Mar 2026). English captions were checked for all 30 before any download; all 30 fetched via TranscribeYouTube captions; no Whisper; none skipped.
- v5 extraction: 28 cards → 20 new ranked ideas + 8 merged into existing ones (incl. a second source for the snail-mail idea). All 227 ideas re-ranked together; top 22 unchanged; one new top-30 entry (#25 AI voice-agent receptionist).
- Playbooks added: `build-first-websites-local-business.md`, `apify-actor-wrapper-maps-lead-scraper.md`, `amazon-review-intelligence-tool.md` (the three fully automatable picks, with an automation section) and `photo-magnets-weddings-markets.md`. Snail-mail and missed-call playbooks updated with new evidence.
- 15 new Claude Opus 5.5 low-effort batches completed over the 177 unprocessed transcripts.
- Full transcript index: `koerner-office/data/transcripts_v2.jsonl`.
- Source notes: `koerner-office/TRANSCRIPT_SOURCES.md`.

## Next steps

1. Keep `state.md` updated after each run.
2. Re-push when new data is added.
3. No further transcript mining is possible without members-only access.

## Key files

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
