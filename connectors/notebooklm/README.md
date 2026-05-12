# NotebookLM podcast generator

Generates a one-hour daily podcast from your wiki's daily digest using Google NotebookLM's Audio Overview feature. The script is driven by a single `focus_prompt` in `config.json` — that's what makes the podcast sound like your show instead of generic AI summary content.

## How it works

After the morning digest is written, this connector:

1. **Parses the digest** for cross-linked wiki summary pages and external URLs in Deep Dive sections.
2. **Creates a temporary NotebookLM notebook** named after the show + date.
3. **Adds sources**: the digest itself, all referenced wiki summaries, all social-stream files for the date, and external Deep Dive URLs (articles, blog posts, arXiv papers).
4. **Triggers audio generation** with the focus prompt from `config.json`, format `deep_dive`, length `long` (~50–60 min).
5. **Polls until ready** (~12 min on a populated notebook), downloads the `.m4a`.
6. **Writes a Substack note** alongside the audio at `wiki/daily-digest/YYYY-MM/podcasts/YYYY-MM-DD/YYYY-MM-DD.md` — episode title (`# N — Show Name`), short summary pulled from the digest's framing, and a "In this episode" bullet list from the TL;DR. Paste it into Substack's new-podcast form when uploading.
7. **Deletes the temporary notebook** to keep your NotebookLM workspace clean.

The audio file is gitignored — host it on HuggingFace, R2, or upload directly to your podcast platform (Substack, Spotify for Podcasters, etc.).

## Setup

```bash
# 1. Install the NotebookLM CLI (pulls in both `nlm` and the MCP server)
pip install notebooklm-mcp-cli
# or with uv:
uv tool install notebooklm-mcp-cli

# 2. Authenticate (opens Chrome for Google login, saves cookies)
nlm login

# 3. Verify auth
nlm doctor
```

NotebookLM Plus / Pro tier is recommended — free tier caps at 3 audio overviews per day. Plus gives you 20/day (the daily run uses 1).

## Configuration

Edit `connectors/notebooklm/config.json`. The `focus_prompt` is the most important field — it controls the show's voice, structure, and treatment. Tweak it as you discover what works for your domain.

Other knobs:
- `audio_length`: `short` (~10 min), `default` (~20 min), `long` (~50–60 min)
- `include_external_urls_from_deep_dives`: pull article URLs from `**Links:**` lines in the digest (default true)
- `include_wiki_summary_pages`: add cross-linked wiki pages as sources (default true)
- `delete_notebook_after_download`: clean up the NotebookLM notebook after download (default true)

## Running

```bash
python3 connectors/notebooklm/podcast.py              # today
python3 connectors/notebooklm/podcast.py 2026-05-10   # specific date
```

The morning cron (`scripts/cerebro-morning-digest.sh.template`) calls this automatically after the digest is written.

## Distribution

The script writes three files per episode to `wiki/daily-digest/YYYY-MM/podcasts/YYYY-MM-DD/`:

- `YYYY-MM-DD.m4a` — the audio (gitignored)
- `YYYY-MM-DD.md`  — the Substack note in markdown (editing source)
- `YYYY-MM-DD.html` — the same note rendered to HTML (paste source for Substack)

**Substack upload workflow** (~2 min daily):

1. **Audio**: open Substack → New → Podcast episode. Upload the `.m4a`.
2. **Title**: copy from the `<h1>` of the .html — `N — Show Name` becomes the episode title.
3. **Show notes / body**:
   - Open the `.html` in a browser: `open wiki/daily-digest/YYYY-MM/podcasts/YYYY-MM-DD/YYYY-MM-DD.html`
   - Cmd+A to select all, Cmd+C to copy.
   - Paste into Substack's body field with **regular Cmd+V** (NOT Cmd+Shift+V).
   - Headings, bold, lists, and links transfer as Substack's native rich-text elements.

**Why HTML and not markdown?** Substack's editor doesn't parse markdown on paste — pasting raw `.md` shows literal `#` and `**` characters. Pasting from a browser-rendered HTML page transfers as styled rich text. Cmd+Shift+V strips formatting into one plain-text block, also wrong.

After publishing, Substack auto-syndicates the episode to Spotify, Apple Podcasts, and other directories subscribed to its podcast RSS feed.

For fully-automated distribution (no manual upload), use a HuggingFace dataset for audio storage and have Astro generate `/podcast.xml`. Submit that RSS feed once to Spotify for Podcasters + Apple Podcasts Connect — they pull new episodes automatically thereafter.

## Caveats

NotebookLM uses internal Google APIs. The CLI handles cookie management but the session expires periodically — re-run `nlm login` if `nlm doctor` reports auth issues. The focus prompt is the difference between a generic "list of papers" episode and a real synthesis show; treat it as the most important file in this connector and iterate on it.
