#!/usr/bin/env python3
"""
Reddit AI subreddit farmer for cere-bro wiki.

Polls a curated list of high-signal AI subreddits via Reddit's public JSON API
(no auth). Each subreddit has its own sort (top/new), score gate, optional
flair whitelist, and tier default. Posts are deduped against a state file so
re-running within the window is safe.

Output:
  raw/reddit/YYYY-MM-DD-r-<subreddit>.md  — one file per subreddit per day

State:
  connectors/reddit/.state/seen_post_ids.json  — post-id history (capped)

Run:        python3 connectors/reddit/farmer.py
Force:      python3 connectors/reddit/farmer.py --force
"""

import json
import os
import sys
import time
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────

REPO_ROOT   = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).parent / "config.json"
STATE_DIR   = Path(__file__).parent / ".state"
STATE_DIR.mkdir(exist_ok=True)
STATE_PATH  = STATE_DIR / "seen_post_ids.json"
RAW_DIR     = REPO_ROOT / "raw" / "reddit"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# ── Config ─────────────────────────────────────────────────────────────────────

cfg            = json.loads(CONFIG_PATH.read_text())
SUBREDDITS     = cfg["subreddits"]
LOOKBACK_HOURS = cfg.get("lookback_hours", 24)
UA             = cfg.get("user_agent", "macos:cere-bro-reddit-farmer:v2.0 (by /u/anonymous)")

FORCE          = "--force" in sys.argv
SEEN_CAP       = 5000  # cap state file size

# ── Reddit OAuth ────────────────────────────────────────────────────────────────
#
# As of 2026 Reddit returns HTTP 403 for ALL unauthenticated *.json requests
# (it serves an HTML block page), so the old www.reddit.com/*.json path yields
# nothing. Reading now requires OAuth. Credentials are read from env vars or a
# gitignored config file (secrets policy: never commit them):
#   env:  REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, [REDDIT_USERNAME, REDDIT_PASSWORD]
#   file: ~/.config/cere-bro/reddit.json  {"client_id","client_secret",["username","password"]}
# Create a Reddit app at https://www.reddit.com/prefs/apps (type "script") to get
# client_id + secret. With a username+password a `password` grant is used (higher
# rate limit); otherwise a read-only `client_credentials` (app-only) grant.

REDDIT_CRED_PATH = Path(os.path.expanduser("~/.config/cere-bro/reddit.json"))


def _load_reddit_creds() -> dict:
    creds = {
        "client_id":     os.environ.get("REDDIT_CLIENT_ID", ""),
        "client_secret": os.environ.get("REDDIT_CLIENT_SECRET", ""),
        "username":      os.environ.get("REDDIT_USERNAME", ""),
        "password":      os.environ.get("REDDIT_PASSWORD", ""),
    }
    if not (creds["client_id"] and creds["client_secret"]) and REDDIT_CRED_PATH.exists():
        try:
            f = json.loads(REDDIT_CRED_PATH.read_text())
            for k in creds:
                creds[k] = creds[k] or f.get(k, "")
        except Exception as e:
            print(f"  WARN: could not parse {REDDIT_CRED_PATH}: {e}")
    return creds


def get_reddit_token() -> str:
    """Return an OAuth bearer token, or '' if no credentials are configured."""
    c = _load_reddit_creds()
    if not (c["client_id"] and c["client_secret"]):
        return ""
    if c["username"] and c["password"]:
        data = {"grant_type": "password", "username": c["username"], "password": c["password"]}
    else:
        # App-only read access (no user context). Works for public listings.
        data = {"grant_type": "client_credentials"}
    try:
        r = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            data=data,
            auth=(c["client_id"], c["client_secret"]),
            headers={"User-Agent": UA},
            timeout=20,
        )
        if r.status_code != 200:
            print(f"  WARN: Reddit OAuth token request failed HTTP {r.status_code}: {r.text[:160]}")
            return ""
        return r.json().get("access_token", "")
    except Exception as e:
        print(f"  WARN: Reddit OAuth token request errored: {e}")
        return ""


REDDIT_TOKEN = get_reddit_token()
if REDDIT_TOKEN:
    print("Reddit: authenticated via OAuth (oauth.reddit.com).")
else:
    print("Reddit: NO OAuth credentials — unauthenticated *.json is blocked (HTTP 403) "
          "since 2026, so all subs will return empty. Add credentials to "
          f"{REDDIT_CRED_PATH} or REDDIT_CLIENT_ID/SECRET env vars. See farmer.py header.")

# ── Timing ─────────────────────────────────────────────────────────────────────

now_utc  = datetime.now(timezone.utc)
now_ist  = now_utc + timedelta(hours=5, minutes=30)
date_str = now_ist.strftime("%Y-%m-%d")
cutoff_utc = now_utc - timedelta(hours=LOOKBACK_HOURS)

# ── State ──────────────────────────────────────────────────────────────────────

def load_seen() -> list[str]:
    if STATE_PATH.exists():
        try:
            data = json.loads(STATE_PATH.read_text())
            return data if isinstance(data, list) else []
        except Exception:
            return []
    return []

def save_seen(seen: list[str]) -> None:
    # keep last SEEN_CAP entries
    trimmed = seen[-SEEN_CAP:]
    STATE_PATH.write_text(json.dumps(trimmed, ensure_ascii=False), encoding="utf-8")

# ── API ────────────────────────────────────────────────────────────────────────

def fetch_subreddit(sub: dict) -> list[dict]:
    name  = sub["name"]
    sort  = sub.get("sort", "new")
    limit = sub.get("limit", 25)

    # Authenticated path: oauth.reddit.com with a bearer token (the only path
    # that still returns JSON). Falls back to the legacy www path (now 403) so
    # the failure mode is explicit rather than silent.
    if REDDIT_TOKEN:
        base = "https://oauth.reddit.com"
        headers = {"User-Agent": UA, "Authorization": f"bearer {REDDIT_TOKEN}"}
    else:
        base = "https://www.reddit.com"
        headers = {"User-Agent": UA}

    if sort == "top":
        t = sub.get("time", "day")
        url = f"{base}/r/{name}/top?limit={limit}&t={t}&raw_json=1"
    else:
        url = f"{base}/r/{name}/{sort}?limit={limit}&raw_json=1"
    try:
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code != 200:
            hint = " (unauthenticated Reddit is blocked; add OAuth creds)" if not REDDIT_TOKEN else ""
            print(f"  ERROR fetching r/{name}: HTTP {r.status_code}{hint}")
            return []
        data = r.json()
        return [c["data"] for c in data.get("data", {}).get("children", []) if c.get("kind") == "t3"]
    except Exception as e:
        print(f"  ERROR fetching r/{name}: {e}")
        return []

# ── Filtering ──────────────────────────────────────────────────────────────────

def passes_filter(post: dict, sub: dict) -> tuple[bool, str]:
    created = post.get("created_utc", 0)
    if created < cutoff_utc.timestamp():
        return False, "too old"
    if post.get("stickied"):
        return False, "stickied"
    if post.get("over_18"):
        return False, "nsfw"
    score = post.get("score", 0)
    if score < sub.get("min_score", 0):
        return False, f"score {score} < min {sub['min_score']}"
    flair_whitelist = sub.get("flair_whitelist")
    if flair_whitelist:
        flair = (post.get("link_flair_text") or "").strip()
        # Match flair text against whitelist tokens (case-insensitive, substring ok)
        flair_l = flair.lower()
        if not any(w.lower() == flair_l or w.lower() in flair_l for w in flair_whitelist):
            return False, f"flair '{flair}' not in whitelist"
    return True, ""

# ── Output formatting ──────────────────────────────────────────────────────────

def format_post(post: dict, sub: dict) -> list[str]:
    title       = (post.get("title") or "(untitled)").strip()
    author      = post.get("author") or "deleted"
    score       = post.get("score", 0)
    num_comments = post.get("num_comments", 0)
    flair       = post.get("link_flair_text") or ""
    permalink   = "https://www.reddit.com" + post.get("permalink", "")
    url         = post.get("url") or permalink
    is_self     = bool(post.get("is_self"))
    selftext    = (post.get("selftext") or "").strip()
    created     = post.get("created_utc", 0)
    created_ts  = datetime.fromtimestamp(created, tz=timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    tier        = sub.get("tier_default", 3)

    out = []
    out.append(f"### {title}")
    out.append("")
    meta = [f"score={score}", f"comments={num_comments}", f"tier={tier}"]
    if flair:
        meta.append(f"flair={flair}")
    meta.append(f"posted={created_ts}")
    out.append(f"**Meta:** {' · '.join(meta)}")
    out.append(f"**Author:** u/{author}")
    out.append(f"**Reddit:** [{permalink}]({permalink})")
    if not is_self and url and url != permalink:
        out.append(f"**Link:** [{url}]({url})")
    if is_self and selftext:
        # Trim long self-posts; let Claude follow the permalink if needed
        body = selftext if len(selftext) <= 1500 else selftext[:1500] + "\n\n[…truncated, see permalink]"
        out.append("")
        out.append(body)
    out.append("")
    out.append("---")
    out.append("")
    return out

def format_subreddit_file(sub: dict, posts: list[dict]) -> str:
    name  = sub["name"]
    sort  = sub.get("sort", "new")
    out = [
        f"# r/{name} | {date_str} IST | sort={sort}",
        f"> Scraped {now_ist.strftime('%Y-%m-%d %H:%M IST')} | "
        f"lookback={LOOKBACK_HOURS}h | tier_default={sub.get('tier_default', 3)}",
        f"> {sub.get('notes', '')}",
        "",
    ]
    if not posts:
        out.append("*No posts passed filters in this window.*")
        return "\n".join(out)
    for p in posts:
        out.extend(format_post(p, sub))
    return "\n".join(out)

# ── Main ───────────────────────────────────────────────────────────────────────

print(f"Reddit farmer | {date_str} IST | lookback={LOOKBACK_HOURS}h | {len(SUBREDDITS)} subs")

# Idempotency check
needed = [RAW_DIR / f"{date_str}-r-{s['name'].lower()}.md" for s in SUBREDDITS]
if all(p.exists() for p in needed) and not FORCE:
    print(f"All subreddit files already written for {date_str}. Use --force to re-run.")
    sys.exit(0)

seen = load_seen()
seen_set = set(seen)
total_kept = 0
total_seen = 0

for sub in SUBREDDITS:
    name = sub["name"]
    print(f"\nFetching r/{name} ({sub.get('sort', 'new')}, limit={sub.get('limit', 25)})...")
    posts = fetch_subreddit(sub)
    print(f"  Got {len(posts)} raw posts")

    kept = []
    for p in posts:
        pid = p.get("id")
        if not pid:
            continue
        ok, reason = passes_filter(p, sub)
        if not ok:
            continue
        total_seen += 1
        if pid in seen_set:
            continue
        kept.append(p)
        seen_set.add(pid)
        seen.append(pid)

    print(f"  Kept {len(kept)} after filter+dedup")
    total_kept += len(kept)

    out_path = RAW_DIR / f"{date_str}-r-{name.lower()}.md"
    out_path.write_text(format_subreddit_file(sub, kept), encoding="utf-8")
    print(f"  Wrote {out_path}")

    # Be polite to Reddit
    time.sleep(1.5)

save_seen(seen)
print(f"\nDone. {total_kept} new posts ({total_seen} passed filters, rest were duplicates).")
print(f"State: {len(seen)} post IDs tracked (cap={SEEN_CAP}).")
