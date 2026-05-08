# Kurate.org Connector

Pulls weekly arXiv leaderboards from kurate.org's public JSON API. Kurate runs 3-LLM tournaments to rank papers by impact, giving a quality signal that complements HuggingFace Daily Papers' upvote-popularity signal.

## What this connector produces

- `raw/kurate/YYYY-MM-DD-cs-ai.md` — top 20 papers in cs.AI (Artificial Intelligence)
- `raw/kurate/YYYY-MM-DD-cs-lg.md` — top 20 papers in cs.LG (Machine Learning)
- `raw/kurate/YYYY-MM-DD-rising-authors.md` — authors crossing the rising-author threshold
- `connectors/kurate/.state/authors.json` — cumulative author state (gitignored, accumulates over time)

Each paper entry has: title, authors, arXiv link, kurate score, win-rate, ai-rating (1-10), and an inferred tier (1-3 based on title keywords matched against your reader profile).

## Setup

### 1. Install Python deps

```bash
pip install -r requirements.txt
```

### 2. (Optional) Customize categories

Default categories are `cs.AI` and `cs.LG`. If you also want robotics (cs.RO), statistics (stat.ML), or others, edit `config.json`:

```json
"categories": [
  {"id": "cs.AI", "label": "Artificial Intelligence", "tier_default": 2},
  {"id": "cs.LG", "label": "Machine Learning",        "tier_default": 2},
  {"id": "cs.RO", "label": "Robotics",                "tier_default": 4}
]
```

### 3. Customize tier-inference keywords

`config.json:tier_keywords` maps Tier 1, 2, 3 to the keywords that trigger each. Bootstrap personalizes this from your tier preferences. After installation, edit if you want to retune what gets surfaced as Tier 1.

### 4. Test run

```bash
python3 farmer.py
```

You should see `Got 20 papers` for each category, then `Author state: NN authors tracked total`. Initial run finds 0 rising authors (needs ~3 weeks of history).

## How rising-author detection works

Each weekly run records every author who appeared in the top-10 of any category. The state file accumulates these appearances. An author is "rising" if they:
- Appeared in top-10 ≥3 times in the past 4 weeks
- Have a rank-decayed score ≥15 (rank 1 = 10 points, rank 10 = 1 point, multiplied by an exponential decay per week)

When the threshold is crossed, the author is surfaced in the daily digest's Worth Watching section as a candidate to add to your Twitter farmer's `ai_handles` list. You decide whether to actually follow them.

## How the digest uses Kurate

Read CLAUDE.md (Step 6 of ingest) for the full rule. Briefly:

1. **Cross-source confirmation**: any paper in BOTH HuggingFace top AND Kurate weekly top-20 → high-conviction Tier 1 Deep Dive regardless of topic.
2. **LLM-rated underrated**: papers in Kurate top-5 but missing from HF → Worth Watching with the ai_rating.
3. **Tier weighting**: each Kurate entry has an inferred tier — Tier 1 entries get Deep Dive space, Tier 4 are skipped.
4. **Rising authors**: detected weekly, surfaced in Worth Watching.

## Note on signal quality

Kurate's tournament is automated and uses 3 LLM judges. It's biased toward papers LLMs find legible (clear methodology, named results). It's a complement to HuggingFace popularity, not a replacement. Both signals together work better than either alone.
