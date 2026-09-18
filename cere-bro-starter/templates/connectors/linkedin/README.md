# LinkedIn connector

Reads your LinkedIn home feed for the Media Zone (the social-media agent), so the
wiki reflects what your professional network is actually sharing. It contributes
**content / author / topic** signal only, not engagement counts (reading per-post
like counts means hammering LinkedIn, which risks detection).

## How it works

LinkedIn moved its feed to RSC (React Server Components) server-actions, so the
farmer uses a **Playwright** headless browser to let the real client fetch the
feed, intercepts the responses, and anchors on the stable `postSlugUrl` field. It
runs **MILD by design**: one page load plus a few human-paced scrolls, once a day,
to stay under bot-detection thresholds. Output is written to the **gitignored**
`raw/linkedin/` folder (private — only the synthesis publishes).

## Setup

1. Install deps: `pip install -r requirements.txt` then `python -m playwright install chromium`.
2. Auth uses your browser session. The farmer combines a cached `li_at` cookie with
   a live `JSESSIONID`; the `li_at` cookie is memory-only in a running Chrome, so
   the farmer self-heals — it caches `li_at` whenever it can read it and reuses it.
   Cookie path is set in `config.json` (`li_cookies_path`, default
   `~/.config/<wiki>/linkedin-cookies.json`, gitignored, chmod 600).
3. If cookies are missing/expired or LinkedIn changes its RSC format, the farmer
   **fails safe**: it logs the exact reason and returns empty. It never fabricates
   feed content.

## Config (`config.json`)

- `max_pagination_pages` (default 4), `count_per_page` (10) — how deep to scroll (kept mild).
- `pacing_min_seconds` / `pacing_max_seconds` — human-like delay between scrolls.
- `skip_sponsored` — drop promoted posts.

**Privacy:** your feed is private. `raw/linkedin/` is gitignored; only the curated
Media Zone synthesis (which you review) is published.
