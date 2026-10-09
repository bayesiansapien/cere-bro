# AI lab watcher

Keeps the wiki current with what the major AI labs publish: blog posts, model launches, and system/model cards.

- **Feeds**: official RSS/Atom feeds (`feeds` in `config.json`).
- **Page watch**: labs without a feed (`pages`). The listing page is fetched and its post links are diffed against state. `"browser": true` renders JS or bot-walled pages with headless Chromium (Playwright). A newly added page is baselined on first sight, so it never floods the digest.
- **Hugging Face Hub**: new model repos from the orgs in `hf_orgs`, with the model card captured.

Each new item is enriched with up to `max_article_chars` of text (PDF system cards are extracted with `pypdf`) and tagged `system_card`, `model_release` or `post`.

Output, only when something is new: `raw/labs/YYYY-MM-DD-HHMMSS-labs.md` (+ `.json`). Dedupe state: `.state/seen.json`. Each run lists "watcher gaps" for any lab that failed or changed its page layout.

```sh
python3 connectors/labs/farmer.py            # capture
python3 connectors/labs/farmer.py --dry-run  # list what is new, write nothing
```

Requirements: `requests`, `feedparser`, `playwright` (for `browser` pages), optional `pypdf`.

To add a lab, add one entry to `feeds`, `pages` or `hf_orgs`. No code change is needed.
