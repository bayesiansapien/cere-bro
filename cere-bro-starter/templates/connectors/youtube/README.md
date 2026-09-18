# YouTube connector

Pulls recent videos from a curated list of AI/tech channels for the Media Zone,
so talks, explainers, and launch videos show up alongside papers and posts.

## How it works

Uses each channel's **public RSS feed**
(`https://www.youtube.com/feeds/videos.xml?channel_id=…`) — a stable, auth-free
interface that carries recent videos plus view counts and star-rating, so you get
engagement signal with no API key and no yt-dlp. Per-channel failures are skipped;
output goes to gitignored `raw/youtube/`.

## Setup

1. Install deps: `pip install -r requirements.txt`.
2. Edit `channels.json` — replace the generic AI-channel seed with the channels you
   actually want. Each entry needs a `title` and a `channel_id` (the `UC…` id, found
   in a channel's page source or via the channel URL). The shipped file has ~7
   well-known AI channels as a starting point.

## Config (`config.json`)

- `lookback_days` (default 3) — how far back to pull videos (covers a multi-day gap).
- `max_videos_per_channel` (default 4).
- `request_timeout` — per-channel RSS fetch timeout.

**Filter tip:** at synthesis time the Media Zone filters to AI/tech videos **by
title**, because most subscriptions are non-AI. Keep `channels.json` focused on
AI/tech channels to reduce noise.
