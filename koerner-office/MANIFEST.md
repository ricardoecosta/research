# Research Pack Manifest

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Channel inventory | `data/channels_v2.csv` | 16 channels |
| Combined video inventory | `data/videos_v2.csv` | 329 videos |
| Full Koerner channel inventory | `data/koerner_videos_all.tsv` | 461 videos |
| Selected videos (analysed) | `analysis/selected_videos_all.csv` | 286 fetched |
| Transcript fetch index | `data/transcripts_v2.jsonl` | 329 records |
| Raw transcripts | `transcripts/raw/*.txt` | 286 English transcripts |
| Extraction batches | `analysis/v2_batches/`, `analysis/v3_batches/`, `analysis/v4_batches/` | 14 + 15 + 2 batches |
| Ranked opportunities | `analysis/all_ideas_ranked.json` | 207 ranked |
| Spreadsheet view | `analysis/all_ideas_ranked.csv` | 207 rows |
| Playbooks for worthy new ideas | `playbooks/*.md` | 2 playbooks |
| Operator rundown | `analysis/all_ideas_ranked.md` | Top 30 + recommendations |
| Method and caveats | `README.md` | Complete |

## Verification

- 286 transcripts available; 207 ideas ranked.
- 286/329 inventoried videos have transcripts; 43 are members-only and inaccessible.
- 14 + 15 Claude Opus 5.5 (low effort) extraction batches completed, plus 2 LLM-assisted v4 batches (15 Koerner Office videos, Mar–Apr 2026) on 21 Oct 2026.
- 207 ranked opportunity cards from 286 transcripts; 0 unprocessed.
- Ranked CSV and JSON contain the same 207 opportunity names.
- All artifacts live under `research/koerner-office/`.

## Reproduce

```bash
# Best fallback: free services
/usr/bin/python3 research/koerner-office/scripts/fetch_transcripts_multi.py 30

# Or FreeTranscriptAPI only
/usr/bin/python3 research/koerner-office/scripts/fetch_freetranscript.py 20

# Or local Whisper fallback (see TRANSCRIPT_SOURCES.md)
```

The multi-provider fetcher reads `data/videos_v2.csv`, skips existing files, and updates `data/transcripts_v2.jsonl`.

## Notes

- Transcripts are YouTube auto-captions, not human-verified.
- Members-only videos cannot be fetched without channel membership.
- Opportunity scores are LLM-assisted research judgments, not audited financials.
- `analysis/all_ideas_ranked.md` is the file to read first.
