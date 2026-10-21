# Transcript Sources — Test Results

**Test video:** `-AVFpzAfjW0` — *The High-Paying Remote Skill Nobody Talks About!* (public, captions available)

| Surface | Status | Limits / notes |
|---|---|---|
| `youtube-transcript-api` direct | ❌ Blocked | `IpBlocked` / `RequestBlocked`; YouTube blocks this IP/VPN range |
| `yt-dlp --write-auto-subs` | ❌ Blocked | Subtitle endpoint returns `429 Too Many Requests` |
| Chrome cookies + new IP | ❌ No | Authentication works, but subtitle endpoint still 429 / IP-blocked |
| **FreeTranscriptAPI** | ✅ Works | No key; **20 requests/hour/IP**; global daily cap; some 404s |
| **TranscribeYouTube** | ✅ Works | No key; **5/min, 30/hour, 100/day**; ~70–80% success; 6h cache |
| **Local audio + whisper.cpp** | ✅ Works | Download audio with `yt-dlp` cookies, convert to 16k WAV, transcribe locally; base.en took ~4 min for 55 min audio; CPU/disk heavy |
| Supadata | 🔑 Key required | 100 free credits/month |
| TranscriptAPI.io | 🔑 Key required | 20 free credits on signup |
| Crawlora | 🔑 Key required | 2,000 free credits/month; no-key UI has captcha |
| Apify transcript actors | 🔑 Paid/free credits | Good for bulk; not free at scale |
| Tactiq / NoteGPT / DownSub | ⚠️ Web-only | Free UI, but no stable public API tested |

## Best current combination

1. **TranscribeYouTube** — first choice; 30/hour.
2. **FreeTranscriptAPI** — second choice; 20/hour.
3. **Local Whisper** — fallback for high-value videos that both services miss.
4. Keep direct YouTube attempts off until the block clears.

## Commands

### Multi-provider fetcher

```bash
cd /Users/ricardo/hustling
/usr/bin/python3 research/koerner-office/scripts/fetch_transcripts_multi.py 30
```

### FreeTranscriptAPI only

```bash
/usr/bin/python3 research/koerner-office/scripts/fetch_freetranscript.py 20
```

### Local Whisper fallback

```bash
# 1. Download audio
yt-dlp --cookies-from-browser chrome -f bestaudio -o "/tmp/audio.%(ext)s" "https://www.youtube.com/watch?v=VIDEO_ID"

# 2. Convert
ffmpeg -y -i /tmp/audio.webm -ar 16000 -ac 1 -c:a pcm_s16le /tmp/audio.wav

# 3. Transcribe
whisper-cli -m ~/.cache/whisper.cpp/ggml-base.en.bin -f /tmp/audio.wav -otxt -of /tmp/transcript
```

## Practical plan

- Run the multi-provider fetcher once per hour.
- It will fetch up to 30 via TranscribeYouTube, then fall back to FreeTranscriptAPI.
- When both are rate-limited, stop; do not rotate VPN IPs.
- Use local Whisper only for the highest-value missing videos.
