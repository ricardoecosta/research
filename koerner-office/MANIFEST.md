# Research Pack Manifest

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Channel inventory | `data/channels_v2.csv` | 16 channels |
| Combined video inventory | `data/videos_v2.csv` | 314 videos |
| Full Koerner channel inventory | `data/koerner_videos_all.tsv` | 460 videos |
| Selected videos (analysed) | `analysis/selected_videos_all.csv` | 147 analysed of 271 fetched |
| Transcript fetch index | `data/transcripts_v2.jsonl` | 314 records |
| Raw transcripts | `transcripts/raw/*.txt` | 271 English transcripts |
| Extraction batches | `analysis/v2_batches/` | 14 batches |
| Ranked opportunities | `analysis/all_ideas_ranked.json` | 96 ranked |
| Spreadsheet view | `analysis/all_ideas_ranked.csv` | 96 rows |
| Operator rundown | `analysis/all_ideas_ranked.md` | Top 30 + recommendations |
| Method and caveats | `README.md` | Complete |

## Verification

- 271 transcripts available; 96 ideas ranked from the first 147 analysed.
- 271/314 inventoried videos have transcripts; 43 are members-only and inaccessible.
- 14 Claude Opus 5.5 (low effort) extraction batches completed.
- 96 ranked opportunity cards from 147 analysed transcripts; 124 new transcripts await mining.
- Ranked CSV and JSON contain the same 96 opportunity names.
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
