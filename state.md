# Research State

**Updated:** 21 Oct 2026  
**Repository:** https://github.com/ricardoecosta/research.git  
**Status:** Transcript collection complete at practical maximum; idea mining in progress.

## Active objective

Do all possible until the most transcripts are collected, mine every unprocessed transcript, and push new research data to GitHub.

## Current counts

| Metric | Value |
|---|---:|
| Channels inventoried | 16 |
| Videos inventoried | 314 |
| Transcripts collected | **271** |
| Transcripts remaining | **43** |
| Remaining reason | Members-only / inaccessible |
| Transcripts mined into ideas | 147 |
| New transcripts awaiting mining | 124 |
| Ranked ideas (previous pass) | 96 |
| New Claude extraction batches completed | 15 |
| New extraction outputs | `koerner-office/analysis/v3_batches/` |

## What is done

- 271/314 transcripts collected.
- Local Whisper fallback used for 118 transcripts.
- FreeTranscriptAPI and TranscribeYouTube used for the rest.
- All 43 remaining videos verified members-only.
- 15 new Claude Opus 5.5 low-effort batches completed over the 177 unprocessed transcripts.
- Full transcript index: `koerner-office/data/transcripts_v2.jsonl`.
- Source notes: `koerner-office/TRANSCRIPT_SOURCES.md`.

## Next steps

1. Parse the 15 new batch outputs.
2. Deduplicate and merge into `koerner-office/analysis/all_ideas_ranked.csv`.
3. Regenerate `all_ideas_ranked.md`.
4. Commit and push the updated ranking.
5. Continue mining any remaining unprocessed transcripts.

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
