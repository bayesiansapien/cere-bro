# RSS connector

Farms AI blogs and newsletters into `raw/rss/` for the daily digest.

## Setup

Edit `feeds.txt` — one feed URL per line, `#` for comments. The shipped file has a
few well-known AI blogs commented out as examples; uncomment or replace them with
the feeds you follow (research blogs, newsletters, lab posts, semiconductor
analysis, etc.).

## Run

```
python connectors/rss/farmer.py
```

Writes `raw/rss/YYYY-MM-DD-<source>.md`. Idempotent per day. A feed that fails to
fetch is skipped, not fatal. The daily digest reads these alongside HuggingFace,
Gmail, Twitter, Kurate, and Reddit.
