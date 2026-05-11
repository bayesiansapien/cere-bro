#!/usr/bin/env python3
"""
Twitter/X farmer for cere-bro wiki.

Uses Nitter RSS to scrape tweets — no auth, no cookies, free.
  - @{own_handle}'s feed   : retweets/quote-tweets as curated signal
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
import time
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


def _load_env():
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

_load_env()

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
_h       = now_ist.hour
slot     = "night" if _h < 6 else ("morning" if _h < 12 else ("afternoon" if _h < 18 else "evening"))
out_path = RAW_DIR / f"{date_str}-{slot}.md"
json_path = RAW_DIR / f"{date_str}-{slot}.json"
cutoff   = now_utc - timedelta(hours=HOURS_BACK)

if out_path.exists() and not FORCE:
    print(f"Already ran today ({slot}): {out_path}. Use --force to re-run.")
    sys.exit(0)

print(f"Twitter farmer | {date_str} | {slot.upper()} run | lookback {HOURS_BACK}h")

# ── Auto-discovery of new follows ──────────────────────────────────────────────

def _classify_from_bio(bio: str, name: str, username: str) -> tuple[bool, list, str]:
    """Returns (is_ai_relevant, focus_list, inferred_org)."""
    bio_kws = [k.lower() for k in cfg.get("bio_ai_keywords", [])]
    text = (bio + " " + name + " " + username).lower()

    is_relevant = any(kw in text for kw in bio_kws)

    org_map = [
        ("Anthropic",       ["anthropic"]),
        ("OpenAI",          ["openai"]),
        ("Google DeepMind", ["deepmind", "google deepmind"]),
        ("Google",          ["@google", "google research", "google brain"]),
        ("Meta AI",         ["meta ai", "@meta", "fair "]),
        ("xAI",             ["@xai", " xai "]),
        ("Mistral",         ["mistral"]),
        ("Cohere",          ["cohere"]),
        ("Hugging Face",    ["hugging face", "huggingface"]),
        ("NVIDIA",          ["nvidia"]),
        ("Microsoft",       ["microsoft", "msft", "@microsoft"]),
        ("AWS",             ["amazon", " aws "]),
        ("Tesla",           ["tesla"]),
        ("Cursor",          ["cursor"]),
    ]
    org = "Independent"
    for o, pats in org_map:
        if any(p in text for p in pats):
            org = o
            break

    focus_map = [
        ("routing",               ["routing"]),
        ("KV cache",              ["kv cache"]),
        ("quantization",          ["quantization"]),
        ("distillation",          ["distillation"]),
        ("GPU/CUDA",              ["gpu", "cuda", "kernel"]),
        ("LLMs",                  ["llm", "language model"]),
        ("foundation models",     ["foundation model"]),
        ("agents",                ["agent"]),
        ("reinforcement learning",["reinforcement learning", " rl "]),
        ("alignment/safety",      ["alignment", "safety", "interpretability"]),
        ("multimodal",            ["multimodal", "vision-language"]),
        ("robotics",              ["robotics", "autonomous"]),
        ("semiconductors",        ["chip", "semiconductor", "silicon", "tpu"]),
        ("inference",             ["inference"]),
        ("training",              ["training"]),
        ("NLP",                   ["nlp"]),
        ("research",              ["researcher", "scientist"]),
    ]
    focus = [tag for tag, kws in focus_map if any(k in text for k in kws)]
    return is_relevant, (focus[:5] or ["AI"]), org


def refresh_following_list():
    """Check Apify for new follows, classify them, update config.json automatically."""
    last_str   = cfg.get("following_last_checked")
    refresh_d  = cfg.get("following_refresh_days", 3)
    actor_id   = cfg.get("following_actor_id")
    api_token  = os.environ.get("APIFY_API_TOKEN")

    if last_str:
        last_dt = datetime.fromisoformat(last_str)
        if last_dt.tzinfo is None:
            last_dt = last_dt.replace(tzinfo=timezone.utc)
        age_d = (now_utc - last_dt).days
        if age_d < refresh_d:
            print(f"[auto-discovery] Following list is {age_d}d old (refresh every {refresh_d}d) — skipping.")
            return

    print(f"[auto-discovery] Checking for new follows (last checked: {last_str or 'never'})...")

    if not api_token:
        print("  WARNING: APIFY_API_TOKEN missing — skipping auto-discovery")
        return
    if not actor_id:
        print("  WARNING: following_actor_id missing from config — skipping")
        return

    # Start Apify run
    run_url = f"https://api.apify.com/v2/acts/{actor_id}/runs"
    payload = {"screenName": OWN_HANDLE, "maxItems": 1000}
    try:
        r = requests.post(
            run_url, json=payload,
            headers={"Authorization": f"Bearer {api_token}"},
            timeout=30,
        )
        if r.status_code not in (200, 201):
            print(f"  ERROR: Apify start failed {r.status_code}: {r.text[:300]}")
            return
        run_id = r.json().get("data", {}).get("id")
        if not run_id:
            print(f"  ERROR: No run ID returned: {r.text[:300]}")
            return
        print(f"  Apify run started: {run_id}")
    except Exception as e:
        print(f"  ERROR starting Apify run: {e}")
        return

    # Poll until done (max ~3 min)
    status_url = f"https://api.apify.com/v2/actor-runs/{run_id}"
    for i in range(18):
        time.sleep(10)
        try:
            s = requests.get(
                status_url,
                headers={"Authorization": f"Bearer {api_token}"},
                timeout=15,
            ).json().get("data", {}).get("status", "")
            print(f"  Run status: {s} ({(i+1)*10}s)")
            if s == "SUCCEEDED":
                break
            if s in ("FAILED", "TIMED-OUT", "ABORTED"):
                print(f"  ERROR: Run ended with {s}")
                return
        except Exception as e:
            print(f"  ERROR polling: {e}")
    else:
        print("  ERROR: Run did not complete within 3 minutes — skipping")
        return

    # Fetch results
    try:
        items = requests.get(
            f"https://api.apify.com/v2/actor-runs/{run_id}/dataset/items",
            headers={"Authorization": f"Bearer {api_token}"},
            params={"limit": 1000},
            timeout=30,
        ).json()
        print(f"  Got {len(items)} following accounts")
    except Exception as e:
        print(f"  ERROR fetching dataset: {e}")
        return

    # Known handle sets (case-insensitive)
    known_ai    = {h["handle"].lower() for h in cfg.get("ai_handles", [])}
    known_other = {h.lower() for h in cfg.get("known_non_ai_handles", [])}

    new_ai, new_other = [], []
    for item in items:
        uname = (
            item.get("username") or item.get("screen_name") or
            item.get("handle") or item.get("userName") or ""
        ).lstrip("@").strip()
        if not uname or uname.lower() in known_ai or uname.lower() in known_other:
            continue

        bio    = item.get("description") or item.get("bio") or ""
        name   = item.get("name") or item.get("displayName") or uname
        relevant, focus, org = _classify_from_bio(bio, name, uname)

        if relevant:
            new_ai.append({"handle": uname, "name": name, "org": org, "timezone": "PT", "focus": focus})
        else:
            new_other.append(uname)

    if new_ai:
        print(f"  NEW AI handles ({len(new_ai)}):")
        for h in new_ai:
            print(f"    @{h['handle']} [{h['org']}] {h['focus']}")
        cfg["ai_handles"].extend(new_ai)

    if new_other:
        preview = ", ".join(f"@{h}" for h in new_other[:8])
        suffix  = f"... +{len(new_other)-8} more" if len(new_other) > 8 else ""
        print(f"  NEW non-AI handles ({len(new_other)}): {preview}{suffix}")
        cfg["known_non_ai_handles"].extend(new_other)

    cfg["following_last_checked"] = now_utc.isoformat()
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Config saved — {len(new_ai)} AI added, {len(new_other)} non-AI added.")


refresh_following_list()

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

# 1. Own handle — retweets/quotes as curated signal.
#    Nitter RSS reports the ORIGINAL tweet's date for reposts, not the repost
#    timestamp. So we can't rely on pubDate to detect "new" reposts. Instead
#    we maintain a state file of seen repost links and capture anything new.
STATE_DIR  = Path(__file__).parent / ".state"
STATE_DIR.mkdir(exist_ok=True)
SEEN_PATH  = STATE_DIR / "seen_reposts.json"
seen_links = set()
if SEEN_PATH.exists():
    try:
        seen_links = set(json.loads(SEEN_PATH.read_text()))
    except Exception:
        seen_links = set()

print(f"\n[1/2] @{OWN_HANDLE} (retweets as curated signal)...")
own_all     = fetch_rss(OWN_HANDLE, nitter_base)
own_reposts = [t for t in own_all if is_retweet(t) or is_quote_tweet(t)]
own_curated = [t for t in own_reposts if t.get("link") and t["link"] not in seen_links]
print(f"  {len(own_all)} feed items | {len(own_reposts)} reposts | {len(own_curated)} new (unseen)")

# Persist newly captured links to the seen set, but cap the file at 500 entries
# so it doesn't grow forever. We keep the most recent N by appending.
if own_curated:
    new_seen = list(seen_links) + [t["link"] for t in own_curated if t.get("link")]
    seen_links = set(new_seen[-500:])
    SEEN_PATH.write_text(json.dumps(sorted(seen_links), indent=2))

# 2. AI handles — keep ALL original (non-retweet) tweets from hand-curated handles.
#    The handles are themselves the curation; running the AI-keyword filter on top
#    drops real signal (e.g. a researcher's career-move tweet that's worth seeing).
#    Dedup across slots is handled by SEEN_AI_TWEETS_PATH below.
SEEN_AI_PATH = STATE_DIR / "seen_ai_tweets.json"
seen_ai_links = set()
if SEEN_AI_PATH.exists():
    try:
        seen_ai_links = set(json.loads(SEEN_AI_PATH.read_text()))
    except Exception:
        seen_ai_links = set()

print(f"\n[2/2] Scraping {len(AI_HANDLES)} AI handles...")
ai_results: dict[str, list] = {}
new_ai_links: list[str] = []
for h in AI_HANDLES:
    handle = h["handle"]
    tweets = fetch_rss(handle, nitter_base)
    # Keep all non-retweet originals from this handle, within the lookback window.
    # No AI-keyword filter — the handle being curated is sufficient signal.
    # Dedup across slots via SEEN_AI_PATH so wider lookback doesn't double-count.
    recent  = [t for t in tweets if is_recent(t)]
    originals = [t for t in recent if not is_retweet(t)]
    fresh = [t for t in originals if t.get("link") and t["link"] not in seen_ai_links]
    if fresh:
        ai_results[handle] = fresh
        new_ai_links.extend(t["link"] for t in fresh if t.get("link"))
        print(f"  @{handle}: {len(fresh)} new tweets (of {len(originals)} originals in {HOURS_BACK}h)")
    else:
        print(f"  @{handle}: 0 new (of {len(originals)} originals in {HOURS_BACK}h, all already seen)")

# Persist newly captured AI-handle tweet links, capped at 1000 entries
if new_ai_links:
    combined = list(seen_ai_links) + new_ai_links
    seen_ai_links = set(combined[-1000:])
    SEEN_AI_PATH.write_text(json.dumps(sorted(seen_ai_links), indent=2))

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
        out += [fmt_tweet(t, context=f"{OWN_HANDLE} retweeted/quoted"), "", "---", ""]
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

# ── JSON sidecar (machine-readable for Media-Live site tab) ────────────────────

def _tweet_to_dict(t: dict, is_curated: bool = False, handle_org: str = "") -> dict:
    return {
        "handle":     t["handle"],
        "creator":    t["creator"],
        "text":       t["text"][:600],
        "link":       t["link"],
        "date_utc":   t["date"].isoformat() if t["date"] else None,
        "is_curated": is_curated,
        "org":        handle_org,
        "articles":   [
            {"url": a["url"], "content": a["content"][:800]}
            for a in t.get("articles", []) if a.get("url")
        ],
    }

json_payload = {
    "date":        date_str,
    "slot":        slot,
    "scraped_ist": now_ist.strftime("%Y-%m-%d %H:%M"),
    "lookback_h":  HOURS_BACK,
    "curated": [_tweet_to_dict(t, is_curated=True) for t in own_curated],
    "ai_feed": [
        {
            "handle": handle,
            "org": next((h.get("org", "") for h in AI_HANDLES if h["handle"] == handle), ""),
            "focus": next((h.get("focus", []) for h in AI_HANDLES if h["handle"] == handle), []),
            "tweets": [_tweet_to_dict(t) for t in tweets],
        }
        for handle, tweets in sorted(ai_results.items())
    ],
}

json_path.write_text(json.dumps(json_payload, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {json_path}")
