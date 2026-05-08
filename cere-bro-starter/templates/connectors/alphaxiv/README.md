# alphaxiv.org Enrichment Helper

On-demand library that fetches alphaxiv.org's AI-generated paper overviews. Used opportunistically by the digest writer to ground Tier 1 / Tier 2 Deep Dives with structural detail beyond the bare abstract.

## Not a daily farmer

Unlike the other connectors, alphaxiv is **not run on a schedule**. It's a callable that the morning-digest Claude session invokes per paper, only for papers that are getting Deep Dive coverage:

```bash
python3 connectors/alphaxiv/enrich.py 2605.00380
```

If alphaxiv has an overview for the paper, the helper prints up to 4000 chars of structured markdown to stdout. If not, stdout is empty (the paper is too new or too niche). The caller branches on whether stdout was non-empty.

## Setup

```bash
pip install -r requirements.txt
```

That's it. No auth, no API key, no config.

## Cache

Successful fetches are cached for 30 days at `connectors/alphaxiv/.cache/<arxiv_id>.md`. The cache directory is gitignored — never committed.

## What's in an alphaxiv overview

For papers popular enough to have one (typically a few days after publication), alphaxiv generates a 1500-3000-word structured walkthrough of the paper, with sections for:
- Authors and institutions
- How the work fits in the broader research landscape
- Key objectives and motivation
- Method (sometimes with figures)
- Results
- Implications

This is much richer than the arXiv abstract and saves the digest writer from needing to read the full PDF for context.

## Coverage

Papers most likely to have alphaxiv overviews:
- Recently popular on Hacker News, Twitter, or HuggingFace
- From major labs (OpenAI, Anthropic, DeepMind, Meta FAIR)
- With clear, citable results

Papers least likely:
- Very recent (last 1-2 days)
- Niche subfields (e.g., theoretical math, specific clinical applications)
- Workshop or non-peer-reviewed

The digest pipeline handles the misses gracefully — if `enrich.py` returns empty, the writer falls back to the abstract.

## Integration in the daily digest

The morning-digest LaunchAgent prompt instructs Claude to call `enrich.py <arxiv_id>` for each Tier 1 / Tier 2 Deep Dive paper, before writing the prose. See `templates/CLAUDE.md` (the "Deep Dive enrichment" section under Daily Digest) for the rules:

1. Don't copy alphaxiv's prose. Use it as input, not output.
2. If empty, fall back to the abstract.
3. Disagree with alphaxiv when it's wrong — alphaxiv overviews are AI-generated and can misframe a paper.
