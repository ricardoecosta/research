# Transcript Status

## Final state

- **271 transcripts available**
- **43 members-only / inaccessible**
- **314 total videos inventoried**
- All non-members-only videos have been fetched

## Working surfaces

1. **TranscribeYouTube** — no key, 5/min / 30/hour / 100/day
2. **FreeTranscriptAPI** — no key, 20/hour
3. **Local Whisper** — `whisper.cpp` + `ggml-tiny.en.bin`; used for the final 118 transcripts

## Remaining work

The remaining 43 videos are members-only. They cannot be transcribed without channel membership. No further retries are expected to succeed unless access changes.

## Next useful step

Mine the 124 newly fetched transcripts and merge them into `analysis/all_ideas_ranked.csv`.
