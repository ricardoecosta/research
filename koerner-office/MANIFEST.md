# Research Pack Manifest

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Channel inventory | `data/channels_v2.csv` | 16 channels |
| Combined video inventory | `data/videos_v2.csv` | 655 videos |
| Full Koerner channel inventory | `data/koerner_videos_all.tsv` | 461 videos |
| Selected videos (analysed) | `analysis/selected_videos_all.csv` | 435 fetched |
| Transcript fetch index | `data/transcripts_v2.jsonl` | 655 records |
| Raw transcripts | `transcripts/raw/*.txt` | 435 English transcripts |
| Extraction batches | `analysis/v2_batches/`, `analysis/v3_batches/`, `analysis/v4_batches/`, `analysis/v5_batches/` | 14 + 15 + 2 + 4 batches |
| Ranked opportunities | `analysis/all_ideas_ranked.json` | 227 ranked |
| Spreadsheet view | `analysis/all_ideas_ranked.csv` | 227 rows |
| Playbooks (worthy ideas + 3 automation picks) | `playbooks/*.md` | 6 playbooks |
| Operator rundown | `analysis/all_ideas_ranked.md` | Top 30 + recommendations |
| Method and caveats | `README.md` | Complete |

## Verification

- 435 transcripts available; 227 ideas ranked.
- 435/655 inventoried videos have transcripts; 43 are members-only and inaccessible.
- 14 + 15 Claude Opus 5.5 (low effort) extraction batches completed, plus 2 LLM-assisted v4 batches (15 Koerner Office videos, Mar–Apr 2026) and 4 LLM-assisted v5 batches (30 Koerner Office videos, Dec 2025 – Mar 2026) on 21 Oct 2026.
- 227 ranked opportunity cards from 435 transcripts; 0 unprocessed.
- Ranked CSV and JSON contain the same 227 opportunity names.
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
