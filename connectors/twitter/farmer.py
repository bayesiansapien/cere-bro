#!/usr/bin/env python3
"""
Twitter/X farmer for cere-bro wiki.

Uses Nitter RSS to scrape tweets — no auth, no cookies, free.
  - @bayesiansapien's feed   : retweets/quote-tweets as curated signal
  - AI-relevant handles       : original tweets from key AI accounts, filtered by keywords

Writes: raw/twitter/YYYY-MM-DD-am.md  (before 3pm IST)
        raw/twitter/YYYY-MM-DD-pm.md  (at/after 3pm IST)

Run:        python3 connectors/twitter/farmer.py
Force:      python3 connectors/twitter/farmer.py --force
"""

import os
import sys
import json
import re
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path
from email.utils import parsedate_to_datetime

# ── Paths ──────────────────────────────────────────────────────────────────────

REPO_ROOT   = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).parent / "config.json"
ENV_PATH    = REPO_ROOT / ".env"
RAW_DIR     = REPO_ROOT / "raw" / "twitter"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# ── Config ─────────────────────────────────────────────────────────────────────

cfg = json.loads(CONFIG_PATH.read_text())

OWN_HANDLE    = cfg["own_handle"]
AI_HANDLES    = cfg["ai_handles"]
HOURS_BACK    = cfg["hours_lookback"]
AI_KEYWORDS   = [k.lower() for k in cfg["ai_keywords"]]
SKIP_DOMAINS  = cfg["skip_domains"]
FETCH_TIMEOUT = cfg["article_fetch_timeout"]
ARTICLE_CHARS = cfg["article_max_chars"]

# Nitter instance — fallback list in order of preference
NITTER_INSTANCES = [
    "https://nitter.net",
    "https://nitter.poast.org",
]

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
FORCE = "--force" in sys.argv

# ── Timing ─────────────────────────────────────────────────────────────────────

now_utc  = datetime.now(timezone.utc)
now_ist  = now_utc + timedelta(hours=5, minutes=30)
date_str = now_ist.strftime("%Y-%m-%d")
slot     = "am" if now_ist.hour < 15 else "pm"
out_path = RAW_DIR / f"{date_str}-{slot}.md"
cutoff   = now_utc - timedelta(hours=HOURS_BACK)

if out_path.exists() and not FORCE:
    print(f"Already ran today ({slot}): {out_path}. Use --force to re-run.")
    sys.exit(0)

print(f"Twitter farmer | {date_str} | {slot.upper()} run | lookback {HOURS_BACK}h")

# ── Nitter RSS helpers ─────────────────────────────────────────────────────────

def get_nitter_base() -> str:
    for base in NITTER_INSTANCES:
        try:
            r = requests.get(f"{base}/nvidia/rss", headers={"User-Agent": UA}, timeout=8)
            if r.status_code == 200 and "<rss" in r.text:
                return base
        except Exception:
            continue
    raise RuntimeError("No reachable Nitter instance found")

def fetch_rss(handle: str, nitter_base: str) -> list[dict]:
    """Fetch Nitter RSS for a handle, return list of tweet dicts."""
    url = f"{nitter_base}/{handle}/rss"
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=15)
        if r.status_code != 200:
            return []
        return parse_rss(r.text, handle)
    except Exception as e:
        print(f"  ERROR fetching @{handle}: {e}")
        return []

def parse_rss(xml_text: str, handle: str) -> list[dict]:
    """Parse Nitter RSS XML into tweet dicts."""
    tweets = []
    try:
        root = ET.fromstring(xml_text)
        ns = {"dc": "http://purl.org/dc/elements/1.1/"}
        for item in root.findall(".//item"):
            title   = (item.findtext("title") or "").strip()
            desc    = (item.findtext("description") or "").strip()
            pub     = item.findtext("pubDate") or ""
            link    = (item.findtext("link") or "").strip()
            creator = (item.findtext("dc:creator", namespaces=ns) or f"@{handle}").strip()

            # Clean HTML from description
            text = re.sub(r"<[^>]+>", " ", desc)
            text = re.sub(r"&[a-z]+;", " ", text)
            text = re.sub(r"\s+", " ", text).strip()
            if not text:
                text = title

            # Parse date
            dt = None
            if pub:
                try:
                    dt = parsedate_to_datetime(pub).astimezone(timezone.utc)
                except Exception:
                    pass

            # Extract URLs from description (href= links)
            urls = re.findall(r'href="(https?://[^"]+)"', desc)
            urls = [u for u in urls if not any(d in u for d in SKIP_DOMAINS + ["nitter."])]

            tweets.append({
                "handle":    handle,
                "creator":   creator,
                "text":      text,
                "title":     title,
                "link":      link,
                "date":      dt,
                "date_raw":  pub,
                "urls":      list(dict.fromkeys(urls)),
            })
    except Exception as e:
        print(f"  RSS parse error for @{handle}: {e}")
    return tweets

def is_recent(tweet: dict) -> bool:
    return tweet["date"] is not None and tweet["date"] >= cutoff

def is_retweet(tweet: dict) -> bool:
    return tweet["text"].startswith("RT @") or tweet["title"].startswith("RT by")

def is_quote_tweet(tweet: dict) -> bool:
    return "R to @" in tweet["title"] or tweet["link"].count("/") > 5

def is_ai_relevant(text: str) -> bool:
    t = text.lower()
    return any(kw in t for kw in AI_KEYWORDS)

# ── Article fetching ───────────────────────────────────────────────────────────

def fetch_article(url: str) -> str:
    """Fetch and extract text from an article URL."""
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=FETCH_TIMEOUT)
        if r.status_code != 200:
            return ""
        html = r.text

        if "arxiv.org/abs/" in url:
            match = re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', html, re.DOTALL)
            if match:
                text = re.sub(r"<[^>]+>", " ", match.group(1))
                return re.sub(r"\s+", " ", text).strip()[:ARTICLE_CHARS]

        text = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.DOTALL)
        text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.DOTALL)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"&[a-z]+;", " ", text)
        return re.sub(r"\s+", " ", text).strip()[:ARTICLE_CHARS]
    except Exception:
        return ""

def enrich(tweet: dict) -> dict:
    articles = []
    for url in tweet.get("urls", []):
        content = fetch_article(url)
        articles.append({"url": url, "content": content})
    tweet["articles"] = articles
    return tweet

# ── Scraping ────────────────────────────────────────────────────────────────────

try:
    nitter_base = get_nitter_base()
    print(f"Using Nitter: {nitter_base}")
except RuntimeError as e:
    print(f"FATAL: {e}")
    sys.exit(1)

# 1. Own handle — retweets + replies as curated signal
print(f"\n[1/2] @{OWN_HANDLE} (retweets as curated signal)...")
own_all    = fetch_rss(OWN_HANDLE, nitter_base)
own_recent = [t for t in own_all if is_recent(t)]
own_curated = [t for t in own_recent if is_retweet(t) or is_quote_tweet(t)]
print(f"  {len(own_recent)} recent tweets | {len(own_curated)} retweets/QTs kept")

# 2. AI handles — original tweets filtered by AI keywords
print(f"\n[2/2] Scraping {len(AI_HANDLES)} AI handles...")
ai_results: dict[str, list] = {}
for h in AI_HANDLES:
    handle = h["handle"]
    tweets = fetch_rss(handle, nitter_base)
    recent = [t for t in tweets if is_recent(t)]
    relevant = [t for t in recent if not is_retweet(t) and is_ai_relevant(t["text"])]
    if relevant:
        ai_results[handle] = relevant
        print(f"  @{handle}: {len(relevant)} AI tweets")
    else:
        print(f"  @{handle}: 0 (nothing recent or AI-relevant)")

# 3. Fetch article content
print("\nFetching article content...")
for t in own_curated:
    enrich(t)
for tweets in ai_results.values():
    for t in tweets:
        enrich(t)

# ── Format output ───────────────────────────────────────────────────────────────

def fmt_tweet(t: dict, context: str = "") -> str:
    date_fmt = t["date"].strftime("%Y-%m-%d %H:%M UTC") if t["date"] else t["date_raw"]
    lines = [f"**@{t['handle']}** ({t['creator']}) · {date_fmt}"]
    if context:
        lines.append(f"*{context}*")
    lines.append("")
    lines.append(f"> {t['text'][:600]}")
    if t["link"]:
        lines.append(f"\n[View tweet]({t['link']})")
    for art in t.get("articles", []):
        if art["url"]:
            lines.append(f"\n**Article:** {art['url']}")
        if art["content"]:
            lines.append(f"\n{art['content'][:1500]}")
    return "\n".join(lines)

total_tweets   = len(own_curated) + sum(len(v) for v in ai_results.values())
total_articles = sum(len(t.get("articles", [])) for t in own_curated) + \
                 sum(len(t.get("articles", [])) for v in ai_results.values() for t in v)

out = [
    f"# Twitter/X Digest | {date_str} | {slot.upper()}",
    f"> Scraped {now_ist.strftime('%Y-%m-%d %H:%M IST')} | Lookback: {HOURS_BACK}h | {total_tweets} tweets | {total_articles} articles",
    "",
    "---",
    "",
    f"## @{OWN_HANDLE} Retweets (Curated Signal)",
    "",
]

if own_curated:
    out.append(f"*{len(own_curated)} retweets/quote-tweets from the past {HOURS_BACK}h*\n")
    for t in own_curated:
        out += [fmt_tweet(t, context="bayesiansapien retweeted/quoted"), "", "---", ""]
else:
    out.append(f"*No retweets found in the past {HOURS_BACK}h*\n")

out += ["## AI Account Feed", ""]
if ai_results:
    for handle, tweets in sorted(ai_results.items()):
        info = next((h for h in AI_HANDLES if h["handle"] == handle), {})
        org  = info.get("org", "")
        out += [
            f"### @{handle}{f' ({org})' if org else ''}",
            f"*{len(tweets)} AI-relevant tweets*\n",
        ]
        for t in tweets:
            out += [fmt_tweet(t), "", "---", ""]
else:
    out.append("*No AI-relevant tweets in this window from tracked handles*")

out += ["", "---", f"*Twitter farmer | {date_str} {slot.upper()} | {total_tweets} tweets | {total_articles} articles*"]

out_path.write_text("\n".join(out), encoding="utf-8")
print(f"\nWrote {out_path}")
print(f"Summary: {len(own_curated)} curated retweets | {sum(len(v) for v in ai_results.values())} AI tweets | {total_articles} articles")
