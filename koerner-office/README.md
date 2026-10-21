# Koerner Office + Adjacent Channels — Transcript Mining

## What this is

A reproducible research pack for mining YouTube business-opportunity content.

**Sources**
- The Koerner Office Podcast — 120 latest videos
- Adjacent/smaller channels: Harry's Stealth Wealth, David Heacock, Johnny & Sergio, Tim Richard, Casper Capital, Mikey No Code, Dark Horse Entrepreneur, George McConnell, Side Hustle Nation, Starter Story, UpFlip, My First Million, Niche Pursuits, Nick Huber, Codie Sanchez

**Outputs**
- `data/channels.csv` — channels and requested video counts
- `data/videos_v2.csv` — 314 videos inventoried across 16 channels
- `data/koerner_videos_all.tsv` — full 460-video Koerner channel inventory
- `data/selected_videos_all.csv` / `analysis/selected_videos_all.csv` — all available transcripts selected
- `data/transcripts_v2.jsonl` — transcript fetch status, paths, character counts
- `transcripts/raw/<video_id>.txt` — 271 fetched English transcripts
- `scripts/fetch_transcripts.py` — reproducible fetcher (youtube-transcript-api)
- `analysis/batches/` and `analysis/v2_batches/` — Claude extraction batches
- `analysis/all_ideas_ranked.json` — 96 deduplicated opportunities, scored
- `analysis/all_ideas_ranked.csv` — spreadsheet-friendly version
- `analysis/opportunity-shortlist.md` / `analysis/all_ideas_ranked.md` — operator rundown

## Method

1. Inventory latest videos from the target channels.
2. Select high-signal business-opportunity videos by title keywords and duration.
3. Fetch English transcripts; skip members-only/unavailable videos.
4. Build compact digests: intro + sentences containing customers, money, pricing, effort, tools, and scale.
5. Use Claude Opus 5.5 (low effort) to extract structured opportunity cards.
6. Deduplicate, score, and rank.

## Scoring

Each opportunity is scored 1–5 on:
- **effort_ease** — 5 = least effort
- **value_potential** — revenue/pricing ceiling
- **speed_to_cash** — how fast a solo operator can get paid
- **scalability** — can it grow without linear labour
- **realism** — evidence quality and believable unit economics
- **async_fit** — can it be sold/delivered without calls or in-person
- **founder_fit_uk_portugal** — leverages UK/Portugal/language/network

Weighted score:
`effort 25% + value 25% + speed 15% + scale 15% + realism 10% + async 5% + founder fit 5%`

## Caveats

- Transcripts are auto-generated and may contain errors.
- 43 videos are members-only and cannot be fetched without channel membership; they are recorded in `data/transcripts_v2.jsonl`.
- Opportunity extraction is LLM-assisted and should be treated as research, not verified fact.
- Revenue claims come from YouTube creators and are not audited.
- Some opportunities are US-only or operationally heavy; the shortlist flags this.
- The current ClarityRelay manual already covers the top-ranked opportunity (AI support agents). The shortlist focuses on what to build next.
