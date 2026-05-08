# Twitter / X Connector

Pulls tweets from your X account (retweets/quote-tweets as curated signal) plus AI-relevant tweets from a curated list of AI handles. Uses Nitter RSS, no auth required for tweet scraping.

## What this connector produces

For each scraped slot, two files:
- `raw/twitter/YYYY-MM-DD-<slot>.md` — human-readable digest of tweets + article snippets
- `raw/twitter/YYYY-MM-DD-<slot>.json` — machine-readable for the Astro site (Media Live tab)

Slots are determined by IST hour at scrape time:
- `night` (00–06), `morning` (06–12), `afternoon` (12–18), `evening` (18–24)

## Setup

### 1. Configure your handle

Edit `config.json` and set `own_handle` to your X handle (without the `@`):
```
"own_handle": "your_x_handle"
```

### 2. (Optional) Set Apify token for auto-discovery

If you want the farmer to auto-detect new follows on your X account and classify them as AI-relevant or not, get an Apify API token from https://apify.com (free tier works) and add it to repo-root `.env`:
```
APIFY_API_TOKEN=apify_api_<your_token>
```

Without this, the farmer skips auto-discovery — you'll edit `ai_handles` in `config.json` manually when you follow someone new.

### 3. Install Python deps

```bash
pip install -r requirements.txt
```

### 4. Test run

```bash
python3 farmer.py --force
```

You should see output ending with `Wrote raw/twitter/<date>-<slot>.{md,json}`.

## What gets scraped

**Stream 1 — your reposts (curated signal):** every retweet + quote-tweet from `@own_handle` in the lookback window. State file `connectors/twitter/.state/seen_reposts.json` tracks captured links so reposting an old tweet still surfaces it (Nitter's RSS reports the original tweet's date, not the repost timestamp).

**Stream 2 — AI handle feed (keyword-filtered):** original tweets from each handle in `ai_handles[]`, filtered through `ai_keywords[]`. Retweets from these handles are dropped (avoid double-counting).

**Article enrichment:** any external link in a kept tweet gets fetched (10s timeout, 3000-char cap, arXiv abstracts specially-handled). Domains in `skip_domains[]` are excluded.

## Customizing the AI handles list

The default `ai_handles[]` ships with a minimal seed (GoogleResearch, nvidia). Add the X handles of researchers and labs you actually follow. The format is:

```json
{"handle": "username", "name": "Display Name", "org": "Org", "timezone": "PT", "focus": ["topic1", "topic2"]}
```

Bootstrap can populate this from your following list automatically if you provided an Apify token.

## Scheduling

The starter ships LaunchAgent / cron templates (see `templates/scripts/`) to run the farmer 4× per day at 6h gaps. The morning slot is invoked from the daily-digest LaunchAgent so it runs at 9am with the digest writer. Afternoon (3pm) and evening (10pm) slots run separately.
