# HuggingFace connector

Fetches the day's papers from [HuggingFace Daily Papers](https://huggingface.co/papers)
(community-ranked by upvotes — a popularity signal) into `raw/huggingface/` for the
daily digest.

## Run

```
python connectors/huggingface/farmer.py
```

Writes one markdown file per paper: `raw/huggingface/YYYY-MM-DD-<slug>.md`, with the
title, authors, abstract, and links. No auth or API key required. Idempotent per day.

The digest cross-references these against the Kurate leaderboard (quality signal):
a paper in **both** today's HuggingFace top and the current Kurate top-20 is treated
as high-conviction. See `../kurate/README.md`.
