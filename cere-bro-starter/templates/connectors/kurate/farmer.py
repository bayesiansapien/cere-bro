#!/usr/bin/env python3
"""
Kurate.org farmer for cere-bro wiki.

Pulls weekly leaderboards from kurate.org's public JSON API for the configured
arXiv categories. Each top-20 paper carries a TrueSkill-derived score, win-rate,
and an LLM-judged ai_rating (1-10). The signal is orthogonal to HuggingFace
Daily Papers (which ranks by community upvotes); we use it as a quality
cross-check and as an author-discovery feed.

Output:
  raw/kurate/YYYY-MM-DD-<cat>.md       — top-N papers per category
  raw/kurate/YYYY-MM-DD-rising-authors.md  — authors crossing the threshold

State:
  connectors/kurate/.state/authors.json  — author appearance history

Run:        python3 connectors/kurate/farmer.py
Force:      python3 connectors/kurate/farmer.py --force
"""

import json
import math
import os
import re
import sys
import requests
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────

REPO_ROOT   = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).parent / "config.json"
STATE_DIR   = Path(__file__).parent / ".state"
STATE_DIR.mkdir(exist_ok=True)
STATE_PATH  = STATE_DIR / "authors.json"
RAW_DIR     = REPO_ROOT / "raw" / "kurate"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# ── Config ─────────────────────────────────────────────────────────────────────

cfg = json.loads(CONFIG_PATH.read_text())
CATEGORIES = cfg["categories"]
PERIOD     = cfg["period"]
TOP_N      = cfg["top_n"]
TIER_KW    = {int(k): [w.lower() for w in v] for k, v in cfg["tier_keywords"].items()}
RA         = cfg["rising_author"]

UA = "wiki-kurate-farmer/1.0"
FORCE = "--force" in sys.argv

# ── Timing ─────────────────────────────────────────────────────────────────────

now_utc  = datetime.now(timezone.utc)
now_ist  = now_utc + timedelta(hours=5, minutes=30)
date_str = now_ist.strftime("%Y-%m-%d")
iso_year, iso_week, _ = now_utc.isocalendar()  # ISO week for author tracking

# ── Tier inference ─────────────────────────────────────────────────────────────

def infer_tier(title: str, default: int) -> int:
    t = title.lower()
    for tier_id in (1, 2, 3):
        for kw in TIER_KW.get(tier_id, []):
            if kw in t:
                return tier_id
    return default

# ── API ────────────────────────────────────────────────────────────────────────

def fetch_leaderboard(category: str) -> list[dict]:
    url = "https://kurate.org/api/leaderboard"
    params = {"category": category, "period": PERIOD, "limit": TOP_N}
    try:
        r = requests.get(url, headers={"User-Agent": UA}, params=params, timeout=20)
        if r.status_code != 200:
            print(f"  ERROR fetching {category}: HTTP {r.status_code}")
            return []
        data = r.json()
        return data.get("leaderboard", []) or []
    except Exception as e:
        print(f"  ERROR fetching {category}: {e}")
        return []

# ── Author state ───────────────────────────────────────────────────────────────

def load_authors() -> dict:
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text())
        except Exception:
            return {}
    return {}

def update_authors(state: dict, papers: list[dict], category: str) -> None:
    """Record this run's author appearances. Each appearance has a rank."""
    week_key = f"{iso_year}-W{iso_week:02d}"
    for p in papers:
        rank = p.get("rank")
        if not rank or rank > 10:
            continue  # only track top-10 appearances
        for author in p.get("authors", [])[:6]:  # cap authors per paper to avoid noise
            name = (author or "").strip()
            if not name or len(name) < 3 or name == ":":
                continue
            entry = state.setdefault(name, {"appearances": [], "first_seen": week_key})
            # Dedup: same paper in same category in same week shouldn't double-count
            arxiv_id = p.get("arxiv_id", "")
            seen_already = any(
                a.get("arxiv_id") == arxiv_id and a.get("week") == week_key
                for a in entry["appearances"]
            )
            if seen_already:
                continue
            entry["appearances"].append({
                "week":      week_key,
                "category":  category,
                "rank":      rank,
                "arxiv_id":  arxiv_id,
                "title":     p.get("title", "")[:200],
                "ai_rating": p.get("ai_rating"),
            })
            entry["last_seen"] = week_key

def compute_rising(state: dict) -> list[dict]:
    """Return authors who crossed the rising-author threshold."""
    cutoff_week = iso_week - RA["window_weeks"]
    decay = RA["rank_decay_per_week"]
    rising = []
    for name, entry in state.items():
        recent = [a for a in entry["appearances"]
                  if int(a["week"].split("-W")[1]) > cutoff_week
                  and a["week"].startswith(str(iso_year))]
        if len(recent) < RA["min_appearances_in_window"]:
            continue
        # rank-weighted score with weekly decay (rank 1 = 10pts, rank 10 = 1pt)
        score = 0.0
        for a in recent:
            weeks_ago = iso_week - int(a["week"].split("-W")[1])
            rank_pts = max(11 - a["rank"], 1)
            score += rank_pts * (decay ** max(weeks_ago, 0))
        if score < RA["min_total_score"]:
            continue
        rising.append({
            "name":            name,
            "score":           round(score, 1),
            "appearances":     len(recent),
            "papers":          recent,
            "first_seen":      entry["first_seen"],
            "last_seen":       entry["last_seen"],
        })
    rising.sort(key=lambda r: -r["score"])
    return rising

# ── Output formatting ──────────────────────────────────────────────────────────

def format_leaderboard(category: dict, papers: list[dict]) -> str:
    cat_id = category["id"]
    out = [
        f"# Kurate Leaderboard | {cat_id} ({category['label']}) | {PERIOD}",
        f"> Scraped {now_ist.strftime('%Y-%m-%d %H:%M IST')} | Top {len(papers)} papers by 3-LLM tournament TrueSkill score",
        "",
    ]
    if not papers:
        out.append("*No papers returned for this category.*")
        return "\n".join(out)

    for i, p in enumerate(papers, 1):
        title    = p.get("title", "(untitled)").strip()
        authors  = ", ".join(a.strip() for a in p.get("authors", [])[:5] if a.strip() and a.strip() != ":")
        if len(p.get("authors") or []) > 5:
            authors += " et al."
        link     = p.get("link") or f"https://arxiv.org/abs/{p.get('arxiv_id', '')}"
        rank     = p.get("rank", i)
        score    = p.get("score") or p.get("ts_score")
        win_rate = p.get("win_rate")
        ai_rating = p.get("ai_rating")
        published = (p.get("published") or "")[:10]
        tier      = infer_tier(title, category["tier_default"])

        out.append(f"### #{rank} — {title}")
        out.append("")
        meta_bits = []
        if score is not None:    meta_bits.append(f"score={score}")
        if win_rate is not None: meta_bits.append(f"win_rate={win_rate}%")
        if ai_rating is not None: meta_bits.append(f"ai_rating={ai_rating}/10")
        meta_bits.append(f"tier={tier}")
        if published:            meta_bits.append(f"published={published}")
        out.append(f"**Meta:** {' · '.join(meta_bits)}")
        out.append(f"**Authors:** {authors}")
        out.append(f"**Link:** [{link}]({link})")
        out.append("")
        out.append("---")
        out.append("")

    return "\n".join(out)

def format_rising_authors(rising: list[dict]) -> str:
    out = [
        "# Kurate Rising Authors",
        f"> {now_ist.strftime('%Y-%m-%d %H:%M IST')} | Authors crossing threshold "
        f"(≥{RA['min_appearances_in_window']} top-10 appearances in past {RA['window_weeks']} weeks, score ≥{RA['min_total_score']})",
        "",
    ]
    if not rising:
        out.append("*No authors crossed the threshold this run.*")
        return "\n".join(out)
    for r in rising:
        out.append(f"## {r['name']}  ·  score {r['score']}  ·  {r['appearances']} appearances")
        out.append(f"*First seen {r['first_seen']}, last seen {r['last_seen']}*")
        out.append("")
        for p in r["papers"][:5]:
            ai = f", ai_rating={p['ai_rating']}/10" if p.get("ai_rating") else ""
            out.append(f"- [{p['arxiv_id']}] **#{p['rank']}** ({p['category']}, {p['week']}{ai}): {p['title']}")
        out.append("")
    out.append("---")
    out.append("*Suggested action: review and decide whether to add any of these authors to "
               "`connectors/twitter/config.json:ai_handles`. Search each name on x.com / arxiv "
               "for an associated handle. The Twitter farmer auto-classifies new follows from "
               "your following list, but it cannot discover authors you don't already follow.*")
    return "\n".join(out)

# ── Main ───────────────────────────────────────────────────────────────────────

print(f"Kurate farmer | {date_str} IST | period={PERIOD} | categories={[c['id'] for c in CATEGORIES]}")

# Idempotency: skip if today's files already exist (unless --force)
needed_files = [RAW_DIR / f"{date_str}-{c['id'].replace('.', '-').lower()}.md" for c in CATEGORIES]
if all(p.exists() for p in needed_files) and not FORCE:
    print(f"All category files already written for {date_str}. Use --force to re-run.")
    sys.exit(0)

state = load_authors()
total_papers = 0

for cat in CATEGORIES:
    print(f"\nFetching {cat['id']} ({cat['label']})...")
    papers = fetch_leaderboard(cat["id"])
    print(f"  Got {len(papers)} papers")
    if not papers:
        continue
    total_papers += len(papers)

    out_path = RAW_DIR / f"{date_str}-{cat['id'].replace('.', '-').lower()}.md"
    out_path.write_text(format_leaderboard(cat, papers), encoding="utf-8")
    print(f"  Wrote {out_path}")

    update_authors(state, papers, cat["id"])

# Save author state
STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nAuthor state: {len(state)} authors tracked total")

# Compute and write rising authors
rising = compute_rising(state)
rising_path = RAW_DIR / f"{date_str}-rising-authors.md"
rising_path.write_text(format_rising_authors(rising), encoding="utf-8")
print(f"Rising authors: {len(rising)} crossed threshold")
print(f"Wrote {rising_path}")

print(f"\nDone. {total_papers} papers across {len(CATEGORIES)} categories.")
