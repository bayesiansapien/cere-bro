#!/usr/bin/env python3
"""
LinkedIn home-feed farmer for the cere-bro social-media agent.

LinkedIn migrated its feed to RSC (React Server Components) server-actions, so
there is no clean JSON API. This farmer is deliberately MILD (to avoid the bot
detection LinkedIn is aggressive about):

  1. GET /feed/foryou once  → yields a FRESH pagination token + the initial posts
     (embedded in the page). Getting a fresh token each run is what makes this
     robust instead of replaying a stale, expiring one.
  2. POST the RSC pagination action up to `max_pagination_pages` times, human-
     paced, to fetch more posts.
  3. Parse the RSC stream for: author, post URL + descriptive topic slug, text,
     and an ad filter. Engagement counts are NOT in the feed response (LinkedIn
     loads them per-post), so LinkedIn contributes content/author/topic, not
     engagement — that stays X-primary in the ranker.

PRIVATE: the feed is what the reader sees, so output goes to gitignored
raw/linkedin/ and never enters the public repo — only the synthesis publishes.

Auth: li_at + JSESSIONID cookies, auto-read from the local browser (browser_cookie3),
falling back to a gitignored cookie file. JSESSIONID doubles as the CSRF token.

Fails safe: any auth/format/challenge problem logs the exact reason and returns
[] — it never pretends it read the feed. Robust to platform change via stable
DATA-field anchors (postSlugUrl / actorName / isSponsoredActivityType) rather
than brittle UI structure.

Run:  python3 connectors/linkedin/farmer.py [--force]
"""

import glob
import json
import os
import random
import re
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO_ROOT   = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).parent / "config.json"
RAW_DIR     = REPO_ROOT / "raw" / "linkedin"
RAW_DIR.mkdir(parents=True, exist_ok=True)

import requests

cfg = json.loads(CONFIG_PATH.read_text())
ENABLED       = cfg.get("enabled", True)
MAX_PAGES     = cfg.get("max_pagination_pages", 2)
COUNT         = cfg.get("count_per_page", 10)
FETCH_LINKS   = cfg.get("fetch_linked_articles", True)
SKIP_SPON     = cfg.get("skip_sponsored", True)
PACE_MIN      = cfg.get("pacing_min_seconds", 3)
PACE_MAX      = cfg.get("pacing_max_seconds", 7)
LI_COOKIES_PATH = Path(os.path.expanduser(cfg.get("li_cookies_path", "~/.config/cere-bro/linkedin-cookies.json")))
ARTICLE_CHARS = cfg.get("article_max_chars", 8000)

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/152 Safari/537.36")
FORCE = "--force" in sys.argv

now_ist  = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
date_str = now_ist.strftime("%Y-%m-%d")


# ── Cookies (browser-first, file fallback) ──────────────────────────────────────

def _cookies_from_browser(timeout=45) -> dict:
    """Read li_at + JSESSIONID from any local Chromium profile. Inline read (proven
    reliable) guarded by a signal alarm so an unapproved macOS Keychain prompt
    can't hang the cron — it just times out and falls back to the file."""
    import signal
    def _to(s, f):
        raise TimeoutError()
    old = signal.signal(signal.SIGALRM, _to)
    signal.alarm(timeout)
    try:
        import browser_cookie3 as bc3
        home = os.path.expanduser("~")
        roots = ["Library/Application Support/Google/Chrome",
                 "Library/Application Support/BraveSoftware/Brave-Browser",
                 "Library/Application Support/Microsoft Edge"]
        for root in roots:
            for db in sorted(glob.glob(os.path.join(home, root, "*", "Cookies"))):
                if "Guest Profile" in db or "System Profile" in db:
                    continue
                try:
                    c = {ck.name: ck.value for ck in bc3.chrome(cookie_file=db, domain_name="linkedin.com") if ck.value}
                    if c.get("li_at") and c.get("JSESSIONID"):
                        return c
                except Exception:
                    continue
        return {}
    except Exception:
        return {}
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


def _cookies_from_file() -> dict:
    if not LI_COOKIES_PATH.exists():
        return {}
    try:
        raw = json.loads(LI_COOKIES_PATH.read_text())
        if isinstance(raw, dict):
            return {k: v for k, v in raw.items() if isinstance(v, str)}
    except Exception as e:
        print(f"  WARN: bad {LI_COOKIES_PATH}: {e}")
    return {}


def load_cookies() -> dict:
    """Robust cookie assembly. li_at is the long-lived session cookie but a RUNNING
    Chrome often keeps it in memory (absent from the on-disk DB), while JSESSIONID
    (the CSRF) reads reliably. So we combine: prefer a live read, fall back to the
    cached li_at for whichever piece the live read is missing, and cache li_at
    whenever it IS readable. Net effect: once li_at is captured once (any moment
    it's on disk), LinkedIn keeps working across runs even when Chrome holds the
    live cookie in memory."""
    live = _cookies_from_browser()
    cached = _cookies_from_file()
    li_at = live.get("li_at") or cached.get("li_at")
    jsession = live.get("JSESSIONID") or cached.get("JSESSIONID")

    # Cache li_at whenever we have a fresh one (durable across runs).
    if live.get("li_at"):
        try:
            LI_COOKIES_PATH.parent.mkdir(parents=True, exist_ok=True)
            LI_COOKIES_PATH.write_text(json.dumps({"li_at": live["li_at"],
                                                   "JSESSIONID": jsession or ""}))
            os.chmod(LI_COOKIES_PATH, 0o600)
        except Exception:
            pass

    if li_at and jsession:
        src = "browser" if live.get("li_at") else "cached li_at + live JSESSIONID" if jsession == live.get("JSESSIONID") else "cache"
        print(f"LinkedIn: cookies OK ({src})")
        return {"li_at": li_at, "JSESSIONID": jsession}

    missing = "li_at" if not li_at else "JSESSIONID"
    print(f"LinkedIn: {missing} unavailable (Chrome may be holding li_at in memory). "
          "Skipping this run, not faking. It self-heals: the next time you open "
          "LinkedIn in Chrome (or Chrome restarts), li_at flushes to disk and gets "
          f"cached to {LI_COOKIES_PATH}, after which LinkedIn runs from cache.")
    return {}


# ── RSC parsing (stable DATA-field anchors, not brittle UI structure) ───────────

def _extract_posts(blob: str) -> list:
    """Extract feed posts from an RSC stream / feed-page HTML by anchoring on the
    post URL (stable across LinkedIn's frequent UI-structure changes)."""
    posts = []
    for m in re.finditer(r'"postSlugUrl":"(https://www\.linkedin\.com/posts/[^"]+)"', blob):
        url = m.group(1)
        win = blob[max(0, m.start() - 1400): m.start() + 300]
        actor = re.search(r'"actorName":"([^"]{1,80})"', win)
        aid = re.search(r'"activityId":"(\d+)"', win)
        sponsored = '"isSponsoredActivityType":true' in win
        # best-effort commentary: the longest text value in the window that reads
        # like prose (not a UI label). The slug already carries the topic.
        texts = re.findall(r'"text":"((?:[^"\\]|\\.){40,600})"', win)
        text = ""
        for t in sorted(texts, key=len, reverse=True):
            tt = t.encode().decode("unicode_escape", "ignore") if "\\u" in t else t
            if not re.search(r"^(See|View|Like|Comment|Repost|Send|Follow|http)", tt):
                text = tt
                break
        # topic from slug: strip author-name prefix + trailing "-share-<id>-xxxx"
        slug = url.split("/posts/")[-1]
        topic = re.sub(r"-(share|activity|ugcPost)-\d+.*$", "", slug).replace("-", " ").strip()
        posts.append({
            "url": url, "author": actor.group(1) if actor else "", "activity_id": aid.group(1) if aid else "",
            "sponsored": sponsored, "topic_slug": topic[:120], "text": text[:600],
        })
    # dedup by activity id / url
    seen, uniq = set(), []
    for p in posts:
        k = p["activity_id"] or p["url"]
        if k in seen:
            continue
        seen.add(k)
        uniq.append(p)
    return uniq


def _fresh_token(html: str) -> str:
    m = re.search(r"\b(\d{6,}-\d{10,}-[0-9a-f]{32})\b", html)
    return m.group(1) if m else ""


def _headers(csrf: str) -> dict:
    return {
        "accept": "*/*", "content-type": "application/json", "csrf-token": csrf,
        "x-li-anchor-page-key": "d_flagship3_feed",
        "x-li-page-instance": "urn:li:page:d_flagship3_feed;RI2QunudSi+nAd6UWvblUg==",
        "x-li-rsc-stream": "true",
        "x-li-track": '{"clientVersion":"0.2.7139","osName":"web","timezone":"Asia/Calcutta","deviceFormFactor":"DESKTOP","mpName":"web"}',
        "User-Agent": UA, "Referer": "https://www.linkedin.com/feed/foryou/",
    }


def _pagination_body(token: str, start: int, count: int) -> str:
    args = ('{"$type":"proto.sdui.actions.requests.RequestedArguments","requestedStateKeys":[],'
            '"payload":{"startIndex":%d,"count":%d,"token":"%s","feedSortOrder":"FeedSortOrder_RELEVANCE","requestType":"Pagination"},'
            '"requestMetadata":{"$type":"proto.sdui.common.RequestMetadata"}') % (start, count, token)
    return ('{"pagerId":"com.linkedin.sdui.pagers.feed.mainFeed","clientArguments":{%s,"states":[],'
            '"screenId":"com.linkedin.sdui.flagshipnav.feed.ForYouFeed","knownTemplateIds":[]},'
            '"paginationRequest":{"$type":"proto.sdui.actions.requests.PaginationRequest",'
            '"pagerId":"com.linkedin.sdui.pagers.feed.mainFeed","trigger":{"$case":"itemDistanceTrigger",'
            '"itemDistanceTrigger":{"$type":"proto.sdui.actions.requests.ItemDistanceTrigger","preloadDistance":5,"preloadLength":2000}},'
            '"retryCount":1,"requestedArguments":{%s}}}') % (args, args)


def fetch_feed() -> list:
    """Robust path: drive a real (headless) browser so LinkedIn's own client makes
    the RSC feed calls, and intercept the responses. This survives LinkedIn's
    frequent RSC/token/format changes because we never reconstruct the request —
    we let the client do it and read the coherent responses. Mild: one feed load
    + a couple of paced scrolls, once a day.

    We anchor extraction on the stable DATA field postSlugUrl, so response-shape
    changes don't break us as long as posts still carry a URL.
    """
    if not ENABLED:
        print("  LinkedIn disabled in config — skipping.")
        return []
    ck = load_cookies()
    if not ck:
        return []
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        print("  LinkedIn: playwright not installed (pip install playwright && "
              "playwright install chromium) — skipping.")
        return []

    li_at = ck["li_at"]
    jsession = ck["JSESSIONID"].strip('"')
    captured = []  # raw RSC response bodies

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(user_agent=UA, viewport={"width": 1440, "height": 900})
        # Inject the session cookies exactly as LinkedIn sets them: both scoped to
        # .linkedin.com, JSESSIONID keeps its surrounding quotes. Over-scoping to
        # multiple domains or stale file cookies triggers a redirect loop.
        context.add_cookies([
            {"name": "li_at", "value": li_at, "domain": ".linkedin.com", "path": "/"},
            {"name": "JSESSIONID", "value": f'"{jsession}"', "domain": ".linkedin.com", "path": "/"},
        ])
        page = context.new_page()

        def _on_response(resp):
            # Capture ANY response that carries feed posts (initial load, stream,
            # or pagination all differ), anchored on the stable postSlugUrl field.
            u = resp.url
            if "linkedin.com" not in u:
                return
            if not any(k in u for k in ("rsc-action", "feed", "sdui", "voyager", "graphql")):
                return
            try:
                body = resp.text()
            except Exception:
                return
            if body and "postSlugUrl" in body:
                captured.append(body)

        page.on("response", _on_response)
        try:
            page.goto("https://www.linkedin.com/feed/foryou/", wait_until="domcontentloaded", timeout=45000)
        except Exception as e:
            print(f"  LinkedIn: page load error: {e}")
            browser.close()
            return []
        # challenge / logged-out detection
        if any(x in page.url for x in ("login", "checkpoint", "challenge", "authwall")):
            print(f"  LinkedIn: redirected to {page.url[:60]} — session invalid/challenge. "
                  "Re-log into LinkedIn in Chrome. Skipping (not faking).")
            browser.close()
            return []
        # Let the initial feed settle, then mild human-paced scrolling to pull more
        # batches. More scroll passes = more of the feed, still gentle.
        page.wait_for_timeout(4000)
        for i in range(max(MAX_PAGES + 2, 5)):
            page.mouse.wheel(0, 3000)
            page.wait_for_timeout(int(random.uniform(PACE_MIN, PACE_MAX) * 1000))
        browser.close()

    print(f"  LinkedIn: captured {len(captured)} feed responses")
    posts, seen = [], set()
    for body in captured:
        for p in _extract_posts(body):
            k = p["activity_id"] or p["url"]
            if k in seen:
                continue
            seen.add(k)
            posts.append(p)
    if SKIP_SPON:
        before = len(posts)
        posts = [p for p in posts if not p["sponsored"]]
        if before - len(posts):
            print(f"  LinkedIn: dropped {before - len(posts)} sponsored/ad posts")
    return posts


# ── Link enrichment (arxiv/blog/github referenced in posts) ─────────────────────

def fetch_article(url: str) -> str:
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=10)
        if r.status_code != 200:
            return ""
        html = r.text
        if "arxiv.org/abs/" in url:
            m = re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', html, re.DOTALL)
            if m:
                return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(1))).strip()[:ARTICLE_CHARS]
        txt = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.DOTALL)
        txt = re.sub(r"<style[^>]*>.*?</style>", " ", txt, flags=re.DOTALL)
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", txt)).strip()[:ARTICLE_CHARS]
    except Exception:
        return ""


def main() -> int:
    print(f"LinkedIn farmer | {date_str} | MILD (1 GET + up to {MAX_PAGES} paged POSTs)")
    posts = fetch_feed()
    print(f"  captured {len(posts)} organic posts")

    if FETCH_LINKS:
        for p in posts:
            for u in re.findall(r"https?://[^\s\")]+", p.get("text", "")):
                if any(d in u for d in ("arxiv.org", "github.com", "medium.com", "substack.com")):
                    p["article"] = {"url": u, "content": fetch_article(u)}
                    break

    out = {"date": date_str, "private": True, "source": "linkedin_home_feed",
           "scraped_ist": now_ist.strftime("%Y-%m-%d %H:%M"), "posts": posts}
    (RAW_DIR / f"{date_str}.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))

    md = [f"# LinkedIn Home Feed | {date_str}",
          f"> {len(posts)} organic posts | PRIVATE — gitignored. Content/author/topic "
          "(LinkedIn engagement not available without per-post hammering).", "", "---", ""]
    for p in posts:
        md.append(f"**{p['author'] or '?'}** — {p['topic_slug']}")
        if p.get("text"):
            md.append(f"> {p['text'][:400]}")
        md.append(f"[post]({p['url']})")
        if p.get("article", {}).get("url"):
            md.append(f"**link:** {p['article']['url']}")
            if p["article"].get("content"):
                md.append(p["article"]["content"][:1000])
        md += ["", "---", ""]
    (RAW_DIR / f"{date_str}.md").write_text("\n".join(md))
    print(f"  Wrote raw/linkedin/{date_str}.json + .md (PRIVATE/gitignored)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
