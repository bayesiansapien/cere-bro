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
X_COOKIES_PATH    = Path(cfg.get("x_cookies_path", "~/.config/cere-bro/x-cookies.json")).expanduser()
DOWNLOAD_IMAGES   = cfg.get("download_images", True)
IMG_TIMEOUT       = cfg.get("image_download_timeout", 8)

# Bookmarks (saved posts) capture — auth-gated, needs auth_token + ct0 cookies.
BM_CFG            = cfg.get("bookmarks", {}) or {}
BM_ENABLED        = BM_CFG.get("enabled", False)
BM_MAX_PAGES      = BM_CFG.get("max_pages", 5)
BM_COUNT          = BM_CFG.get("count_per_page", 100)
BM_ONLY_NEW       = BM_CFG.get("only_new", True)
BM_FETCH_LINKS    = BM_CFG.get("fetch_linked_articles", True)
BM_QUERY_ID       = BM_CFG.get("graphql_query_id", "")

# Load X session cookies for x.com/i/article/ fetches (gitignored, user-supplied)
X_COOKIES = {}
if X_COOKIES_PATH.exists():
    try:
        raw = json.loads(X_COOKIES_PATH.read_text())
        # Support two common export formats:
        #   1. {"name": "value", ...}                (flat dict from manual export)
        #   2. [{"name": "...", "value": "...", ...}, ...]  (Chrome extension export)
        if isinstance(raw, dict):
            X_COOKIES = {k: v for k, v in raw.items() if isinstance(v, str)}
        elif isinstance(raw, list):
            X_COOKIES = {c["name"]: c["value"] for c in raw
                         if isinstance(c, dict) and "name" in c and "value" in c
                         and (c.get("domain", "").endswith("x.com") or c.get("domain", "").endswith("twitter.com"))}
        print(f"Loaded {len(X_COOKIES)} X session cookies from {X_COOKIES_PATH}")
    except Exception as e:
        print(f"WARN: failed to parse X cookies at {X_COOKIES_PATH}: {e}")
else:
    print(f"INFO: no X cookies at {X_COOKIES_PATH} — x.com/i/article/ URLs will fall back to URL-only capture.")

# Image storage location (gitignored)
IMG_DIR = REPO_ROOT / "raw" / "twitter" / "images"
if DOWNLOAD_IMAGES:
    IMG_DIR.mkdir(parents=True, exist_ok=True)

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

            # Extract image URLs from <img src="..."> tags in description
            image_urls = extract_image_urls(desc)

            tweets.append({
                "handle":     handle,
                "creator":    creator,
                "text":       text,
                "title":      title,
                "link":       link,
                "date":       dt,
                "date_raw":   pub,
                "urls":       list(dict.fromkeys(urls)),
                "image_urls": list(dict.fromkeys(image_urls)),
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
    """Fetch and extract text from an article URL.

    For x.com / twitter.com URLs (specifically x.com/i/article/...), attaches
    user-supplied session cookies from X_COOKIES so X's native long-form articles
    fetch successfully. For all other URLs, runs unauthenticated.
    """
    try:
        is_x_url = "x.com/" in url or "twitter.com/" in url
        cookies = X_COOKIES if (is_x_url and X_COOKIES) else None
        r = requests.get(url, headers={"User-Agent": UA},
                         cookies=cookies, timeout=FETCH_TIMEOUT, allow_redirects=True)
        if r.status_code != 200:
            if is_x_url and r.status_code in (401, 403):
                print(f"  WARN: X article fetch returned {r.status_code} for {url} — cookies may be expired. Refresh at {X_COOKIES_PATH}.")
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

# ── Image extraction ───────────────────────────────────────────────────────────

def extract_image_urls(desc_html: str) -> list[str]:
    """Pull image URLs out of a Nitter RSS description HTML block.

    Nitter embeds image attachments via <img src="..."> tags. We collect those
    and filter out tracker pixels / profile-icon URLs.
    """
    if not desc_html:
        return []
    urls = re.findall(r'<img[^>]+src="(https?://[^"]+)"', desc_html)
    # Skip Nitter UI icons, profile thumbnails, and 1x1 tracker pixels
    return [u for u in urls if not any(
        x in u for x in ["/pic/profile_images/", "/pic/avatars/", "logo.png", "icon.png"]
    )]

def download_image(url: str, dest_path: Path) -> bool:
    """Download a single image. Returns True on success, False otherwise. Never raises."""
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=IMG_TIMEOUT, stream=True)
        if r.status_code != 200:
            return False
        with dest_path.open("wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        # sanity: at least 1KB to weed out empty/error pages
        if dest_path.stat().st_size < 1024:
            dest_path.unlink(missing_ok=True)
            return False
        return True
    except Exception:
        try:
            dest_path.unlink(missing_ok=True)
        except Exception:
            pass
        return False

def slug_from_link(link: str) -> str:
    """Derive a stable per-tweet slug from the original tweet link."""
    # Nitter link looks like https://nitter.net/handle/status/1234567890
    m = re.search(r"/status/(\d+)", link or "")
    return m.group(1) if m else "unknown"

def enrich(tweet: dict) -> dict:
    articles = []
    for url in tweet.get("urls", []):
        content = fetch_article(url)
        articles.append({"url": url, "content": content})
    tweet["articles"] = articles

    # Download image attachments if enabled
    if DOWNLOAD_IMAGES and tweet.get("image_urls"):
        tweet_id = slug_from_link(tweet.get("link", ""))
        # Date-stamped subfolder so the gitignore + cleanup story is simple
        date_str = (tweet.get("date") or datetime.now(timezone.utc)).strftime("%Y-%m-%d")
        sub = IMG_DIR / date_str
        sub.mkdir(parents=True, exist_ok=True)
        local_paths = []
        for i, url in enumerate(tweet["image_urls"]):
            # Pick a sensible extension; default to .jpg
            ext = ".jpg"
            for cand in (".png", ".jpeg", ".gif", ".webp"):
                if cand in url.lower():
                    ext = cand
                    break
            dest = sub / f"{tweet_id}-{i}{ext}"
            if dest.exists() and dest.stat().st_size >= 1024:
                local_paths.append(str(dest.relative_to(REPO_ROOT)))
                continue
            if download_image(url, dest):
                local_paths.append(str(dest.relative_to(REPO_ROOT)))
        tweet["image_paths"] = local_paths
    else:
        tweet["image_paths"] = []
    return tweet

# ── Bookmarks (saved posts) via X GraphQL ──────────────────────────────────────
#
# The reader's SAVED / BOOKMARKED posts are the top-priority curated X signal for
# the Media Zone (see CLAUDE.md). Bookmarks are private and auth-gated: the
# /i/bookmarks timeline is only readable by a logged-in session, so this path
# needs the auth_token + ct0 cookies already loaded into X_COOKIES from
# ~/.config/cere-bro/x-cookies.json (gitignored, chmod 600, user-supplied).
#
# We call X's internal GraphQL "Bookmarks" operation directly with the public web
# bearer token (this token ships in X's public JS bundle — it is NOT a user
# credential and is safe to hardcode). Auth is carried entirely by the session
# cookies + the ct0-derived CSRF header.

# Public web-app bearer token (shipped in x.com's JS; not a secret).
X_WEB_BEARER = (
    "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs"
    "%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
)

# Feature flags required by the Bookmarks GraphQL operation. X rejects the call
# with 400 if required flags are missing or unknown. This set is copied verbatim
# from a live x.com/i/bookmarks request (captured 2026-08-12). If X changes its
# required flags, refresh both this dict and graphql_query_id from a fresh request
# (DevTools > Network > 'Bookmarks' > copy the request URL).
BM_FEATURES = {
    "rweb_video_screen_enabled": False,
    "rweb_cashtags_enabled": True,
    "profile_label_improvements_pcf_label_in_post_enabled": True,
    "responsive_web_profile_redirect_enabled": True,
    "rweb_tipjar_consumption_enabled": False,
    "verified_phone_label_enabled": True,
    "creator_subscriptions_tweet_preview_api_enabled": True,
    "responsive_web_graphql_timeline_navigation_enabled": True,
    "premium_content_api_read_enabled": False,
    "communities_web_enable_tweet_community_results_fetch": True,
    "c9s_tweet_anatomy_moderator_badge_enabled": True,
    "responsive_web_grok_analyze_button_fetch_trends_enabled": False,
    "responsive_web_grok_analyze_post_followups_enabled": True,
    "rweb_cashtags_composer_attachment_enabled": True,
    "responsive_web_jetfuel_frame": True,
    "responsive_web_grok_share_attachment_enabled": True,
    "responsive_web_grok_annotations_enabled": True,
    "articles_preview_enabled": True,
    "responsive_web_edit_tweet_api_enabled": True,
    "rweb_conversational_replies_downvote_enabled": False,
    "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
    "view_counts_everywhere_api_enabled": True,
    "longform_notetweets_consumption_enabled": True,
    "responsive_web_twitter_article_tweet_consumption_enabled": True,
    "content_disclosure_indicator_enabled": True,
    "content_disclosure_ai_generated_indicator_enabled": True,
    "responsive_web_grok_show_grok_translated_post": True,
    "responsive_web_grok_analysis_button_from_backend": True,
    "post_ctas_fetch_enabled": False,
    "freedom_of_speech_not_reach_fetch_enabled": True,
    "standardized_nudges_misinfo": True,
    "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
    "longform_notetweets_rich_text_read_enabled": True,
    "longform_notetweets_inline_media_enabled": False,
    "responsive_web_grok_image_annotation_enabled": True,
    "responsive_web_grok_imagine_annotation_enabled": True,
    "responsive_web_grok_community_note_auto_translation_is_enabled": True,
    "responsive_web_enhance_cards_enabled": False,
}


def _bm_headers() -> dict:
    """Auth headers for the GraphQL Bookmarks call. CSRF token == ct0 cookie."""
    ct0 = X_COOKIES.get("ct0", "")
    return {
        "authorization": f"Bearer {X_WEB_BEARER}",
        "x-csrf-token": ct0,
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": "en",
        "content-type": "application/json",
        "User-Agent": UA,
        "Referer": "https://x.com/i/bookmarks",
    }


def _unwrap_tweet(result):
    """Normalize a GraphQL tweet_results.result into a farmer-shaped tweet dict.

    Returns the tweet dict, or None for entries that aren't tweets.


    Handles both 'Tweet' and 'TweetWithVisibilityResults' envelopes. Returns None
    for entries that aren't tweets (ads, tombstones, etc.).
    """
    if not isinstance(result, dict):
        return None
    if result.get("__typename") == "TweetWithVisibilityResults":
        result = result.get("tweet", {})
    legacy = result.get("legacy") or {}
    if not legacy:
        return None

    tweet_id = legacy.get("id_str") or result.get("rest_id") or ""
    full_text = legacy.get("full_text") or ""

    # Long-form (note) tweets carry the real body separately.
    note = (result.get("note_tweet") or {}).get("note_tweet_results", {}).get("result", {})
    if note.get("text"):
        full_text = note["text"]

    user = (((result.get("core") or {}).get("user_results") or {}).get("result") or {})
    screen_name = (user.get("legacy") or {}).get("screen_name") or (user.get("core") or {}).get("screen_name") or "unknown"

    # Expanded URLs (skip t.co, self x.com links via SKIP_DOMAINS).
    entities = legacy.get("entities") or {}
    url_entities = entities.get("urls") or []
    # Note tweets keep their URLs under note_tweet results too.
    if note:
        note_ent = (note.get("entity_set") or {}).get("urls") or []
        url_entities = url_entities + note_ent
    urls = []
    for u in url_entities:
        exp = u.get("expanded_url") or u.get("url") or ""
        if exp and not any(d in exp for d in SKIP_DOMAINS):
            urls.append(exp)

    # Media image URLs (public CDN).
    media = (entities.get("media") or [])
    ext_media = ((legacy.get("extended_entities") or {}).get("media") or [])
    image_urls = []
    for m in (media + ext_media):
        mu = m.get("media_url_https") or ""
        if mu and m.get("type") == "photo":
            image_urls.append(mu)

    dt = None
    created = legacy.get("created_at")
    if created:
        try:
            dt = parsedate_to_datetime(created).astimezone(timezone.utc)
        except Exception:
            pass

    return {
        "handle":     screen_name,
        "creator":    f"@{screen_name}",
        "text":       re.sub(r"\s+", " ", full_text).strip(),
        "title":      "",
        "link":       f"https://x.com/{screen_name}/status/{tweet_id}" if tweet_id else "",
        "date":       dt,
        "date_raw":   created or "",
        "urls":       list(dict.fromkeys(urls)),
        "image_urls": list(dict.fromkeys(image_urls)),
        "tweet_id":   tweet_id,
    }


def _bm_parse_page(payload: dict) -> tuple[list[dict], str]:
    """Extract (tweets, next_cursor) from one Bookmarks GraphQL response page."""
    tweets, cursor = [], ""
    try:
        timeline = (((payload.get("data") or {}).get("bookmark_timeline_v2") or {})
                    .get("timeline") or {})
        for instr in timeline.get("instructions", []):
            if instr.get("type") != "TimelineAddEntries":
                continue
            for entry in instr.get("entries", []):
                eid = entry.get("entryId", "")
                content = entry.get("content") or {}
                if eid.startswith("tweet-"):
                    result = (((content.get("itemContent") or {}).get("tweet_results") or {})
                              .get("result") or {})
                    t = _unwrap_tweet(result)
                    if t and t["tweet_id"]:
                        tweets.append(t)
                elif eid.startswith("cursor-bottom-"):
                    cursor = content.get("value", "")
    except Exception as e:
        print(f"  Bookmarks parse error: {e}")
    return tweets, cursor


def fetch_bookmarks() -> list[dict]:
    """Fetch the reader's saved posts from X, newest first, with pagination.

    Returns a list of farmer-shaped tweet dicts (not yet enriched). Degrades
    gracefully to [] on any auth/endpoint failure so it never breaks the run.
    """
    if not BM_ENABLED:
        print("  Bookmarks disabled in config — skipping.")
        return []
    if not X_COOKIES.get("auth_token") or not X_COOKIES.get("ct0"):
        print("  Bookmarks: no auth_token/ct0 in X cookies — cannot read the "
              "auth-gated bookmarks timeline. Export cookies to "
              f"{X_COOKIES_PATH} to enable. Skipping (not pretending it ran).")
        return []
    if not BM_QUERY_ID:
        print("  Bookmarks: no graphql_query_id in config — skipping.")
        return []

    endpoint = f"https://x.com/i/api/graphql/{BM_QUERY_ID}/Bookmarks"
    all_tweets: list[dict] = []
    cursor = ""
    for page in range(BM_MAX_PAGES):
        variables = {"count": BM_COUNT, "includePromotedContent": False}
        if cursor:
            variables["cursor"] = cursor
        params = {
            "variables": json.dumps(variables, separators=(",", ":")),
            "features": json.dumps(BM_FEATURES, separators=(",", ":")),
        }
        try:
            r = requests.get(endpoint, headers=_bm_headers(), cookies=X_COOKIES,
                             params=params, timeout=FETCH_TIMEOUT)
        except Exception as e:
            print(f"  Bookmarks: request error on page {page+1}: {e}")
            break

        if r.status_code == 404:
            print(f"  Bookmarks: 404 — graphql_query_id '{BM_QUERY_ID}' is stale. "
                  "Refresh it per the config 'note' field (DevTools > Network > "
                  "'Bookmarks'). Skipping.")
            break
        if r.status_code in (401, 403):
            print(f"  Bookmarks: {r.status_code} — X session cookies expired or "
                  f"insufficient. Re-export to {X_COOKIES_PATH}. Skipping.")
            break
        if r.status_code != 200:
            print(f"  Bookmarks: HTTP {r.status_code} on page {page+1}: {r.text[:200]}")
            break

        try:
            payload = r.json()
        except Exception as e:
            print(f"  Bookmarks: bad JSON on page {page+1}: {e}")
            break

        page_tweets, cursor = _bm_parse_page(payload)
        if not page_tweets:
            break
        all_tweets.extend(page_tweets)
        print(f"  Bookmarks page {page+1}: +{len(page_tweets)} (total {len(all_tweets)})")
        if not cursor:
            break
        time.sleep(1.5)  # be gentle with the endpoint

    return all_tweets


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

print(f"\n[1/3] @{OWN_HANDLE} (retweets as curated signal)...")
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

print(f"\n[2/3] Scraping {len(AI_HANDLES)} AI handles...")
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

# 3. Bookmarks (saved posts) — top-priority curated signal for the Media Zone.
#    Auth-gated: only runs when auth_token + ct0 cookies exist. Deduped by tweet
#    id via seen_bookmarks.json so each run surfaces only newly-saved posts
#    (set bookmarks.only_new=false in config to re-capture everything each run).
print(f"\n[3/3] Bookmarks (saved posts)...")
SEEN_BM_PATH = STATE_DIR / "seen_bookmarks.json"
seen_bm_ids = set()
if SEEN_BM_PATH.exists():
    try:
        seen_bm_ids = set(json.loads(SEEN_BM_PATH.read_text()))
    except Exception:
        seen_bm_ids = set()

bookmarks_all = fetch_bookmarks()
if BM_ONLY_NEW:
    bookmarks = [t for t in bookmarks_all if t["tweet_id"] not in seen_bm_ids]
else:
    bookmarks = bookmarks_all
print(f"  {len(bookmarks_all)} bookmarks fetched | {len(bookmarks)} new (unseen)")

# Persist captured bookmark ids, capped at 2000 entries.
if bookmarks:
    combined_bm = list(seen_bm_ids) + [t["tweet_id"] for t in bookmarks_all if t.get("tweet_id")]
    seen_bm_ids = set(combined_bm[-2000:])
    SEEN_BM_PATH.write_text(json.dumps(sorted(seen_bm_ids), indent=2))

# 4. Fetch article content
print("\nFetching article content...")
for t in own_curated:
    enrich(t)
for tweets in ai_results.values():
    for t in tweets:
        enrich(t)
if BM_FETCH_LINKS:
    for t in bookmarks:
        enrich(t)
else:
    for t in bookmarks:
        t["articles"] = []
        t["image_paths"] = []

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

# NOTE: bookmarks are intentionally NOT written into this shared file. This file
# and its .json sidecar are git-tracked in a PUBLIC repo; bookmarks are the
# reader's PRIVATE X saves. They are written separately to raw/twitter/bookmarks/
# (gitignored) at the end of this script. See the "Bookmarks sidecar" block below.
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
print(f"Summary: {len(bookmarks)} saved posts | {len(own_curated)} curated retweets | {sum(len(v) for v in ai_results.values())} AI tweets | {total_articles} articles")

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
        # Twitter CDN image URLs (pic.twimg.com / nitter.net) — public, load
        # directly in browsers without auth. Used by the Media Zone feed.
        "image_urls": t.get("image_urls", []),
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

# ── Bookmarks sidecar (PRIVATE — gitignored, never enters the public repo) ──────
#
# Bookmarks are the reader's private X saves. This repo is public and both the
# shared -slot.md and -slot.json above are git-tracked (the .json also feeds the
# public site tab), so bookmarks are written HERE instead, under
# raw/twitter/bookmarks/ which is gitignored. Only the local Media Zone synthesis
# (morning cron) reads these files; they never leave the machine via git.
#
# Article content is stored in FULL here (not truncated to 800 like the public
# sidecar) because the Media Zone treats each bookmark as a knowledge/learning
# item and synthesizes a compressed Deep Dive from the linked article's body.
BM_DIR = RAW_DIR / "bookmarks"
BM_DIR.mkdir(parents=True, exist_ok=True)
bm_md_path   = BM_DIR / f"{date_str}-{slot}.md"
bm_json_path = BM_DIR / f"{date_str}-{slot}.json"

bm_md = [
    f"# Saved Posts (Bookmarks) | {date_str} | {slot.upper()}",
    f"> {len(bookmarks)} newly-saved posts | PRIVATE — gitignored, local only",
    "",
    "> Each bookmark is curated intent (treat like starred Gmail). Knowledge and "
    "learning first: read the post AND its enriched linked article, then synthesize "
    "the idea for the Media Zone (digest-like but compressed).",
    "",
    "---",
    "",
]
if bookmarks:
    for t in bookmarks:
        bm_md += [fmt_tweet(t, context="saved to bookmarks on X"), "", "---", ""]
else:
    bm_md.append(
        "*No new saved posts this run. If you have bookmarks but see 0, the X "
        "cookies or bookmarks.graphql_query_id may need refreshing (see console log).*"
    )
bm_md_path.write_text("\n".join(bm_md), encoding="utf-8")

bm_json = {
    "date":        date_str,
    "slot":        slot,
    "scraped_ist": now_ist.strftime("%Y-%m-%d %H:%M"),
    "private":     True,
    "bookmarks": [
        {
            "handle":     t["handle"],
            "creator":    t["creator"],
            "text":       t["text"],
            "link":       t["link"],
            "date_utc":   t["date"].isoformat() if t.get("date") else None,
            "image_urls": t.get("image_urls", []),
            # FULL enriched article bodies for knowledge synthesis (no truncation).
            "articles":   [
                {"url": a["url"], "content": a["content"]}
                for a in t.get("articles", []) if a.get("url")
            ],
        }
        for t in bookmarks
    ],
}
bm_json_path.write_text(json.dumps(bm_json, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {bm_md_path} + sidecar ({len(bookmarks)} bookmarks, PRIVATE/gitignored)")
