#!/usr/bin/env python3
"""
alphaxiv.org enrichment helper.

Given an arXiv ID, fetch the AI-generated "overview" (a structured
1500-3000-word walkthrough alphaxiv produces for popular papers) as
markdown. Used opportunistically by the digest writer to give Tier 1 /
Tier 2 Deep Dives more depth than the bare abstract.

Usage (called by the morning-digest Claude session):
  python3 connectors/alphaxiv/enrich.py 2410.21276
  python3 connectors/alphaxiv/enrich.py http://arxiv.org/abs/2604.27899v1

Behaviour:
  - prints the overview markdown to stdout if alphaxiv has one
  - prints nothing (empty stdout) if no overview is available
  - always exits 0; the caller branches on whether stdout was non-empty
  - caches successful fetches at .cache/<arxiv_id>.md for 30 days
"""

import re
import sys
import requests
from datetime import datetime, timedelta
from pathlib import Path

CACHE_DIR      = Path(__file__).parent / ".cache"
CACHE_DIR.mkdir(exist_ok=True)
CACHE_TTL_DAYS = 30
MAX_CHARS      = 4000      # cap overview output so it doesn't dominate context
MIN_CHARS      = 500       # below this, treat as "no real overview"
NO_OVERVIEW_RE = re.compile(r"^\s*no intermediate report available", re.IGNORECASE)


def normalize_arxiv_id(raw: str) -> str:
    """Accept any of:
       - bare ID:           '2410.21276' or '2410.21276v2'
       - URL:               'http://arxiv.org/abs/2604.27899v1'
       - alphaxiv URL:      'https://alphaxiv.org/overview/2410.21276'
    Returns canonical id without 'vN' suffix, or empty string if not parseable.
    """
    m = re.search(r"(\d{4}\.\d{4,6})", raw or "")
    return m.group(1) if m else ""


def fetch_overview(arxiv_id: str) -> str:
    """Return overview markdown (capped at MAX_CHARS) or empty string."""
    if not arxiv_id:
        return ""

    cache_path = CACHE_DIR / f"{arxiv_id}.md"
    if cache_path.exists():
        age = datetime.now() - datetime.fromtimestamp(cache_path.stat().st_mtime)
        if age < timedelta(days=CACHE_TTL_DAYS):
            return cache_path.read_text(encoding="utf-8")

    url = f"https://www.alphaxiv.org/overview/{arxiv_id}.md"
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "cere-bro/1.0 (+enrichment)"},
            timeout=15,
        )
        if r.status_code != 200:
            return ""
        text = (r.text or "").strip()
        if not text or NO_OVERVIEW_RE.match(text) or len(text) < MIN_CHARS:
            return ""
        capped = text[:MAX_CHARS]
        cache_path.write_text(capped, encoding="utf-8")
        return capped
    except Exception:
        return ""


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: enrich.py <arxiv_id_or_url>", file=sys.stderr)
        return 2
    arxiv_id = normalize_arxiv_id(sys.argv[1])
    if not arxiv_id:
        print(f"Could not parse arxiv id from: {sys.argv[1]}", file=sys.stderr)
        return 0  # exit 0 anyway; empty stdout is the "no overview" signal
    overview = fetch_overview(arxiv_id)
    if overview:
        print(overview)
    return 0


if __name__ == "__main__":
    sys.exit(main())
