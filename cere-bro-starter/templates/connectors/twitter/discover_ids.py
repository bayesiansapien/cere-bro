#!/usr/bin/env python3
"""
Discover X's current GraphQL operation IDs and feature flags from the live web app.

X rotates the queryId (and the required `features` set) of every GraphQL operation
whenever it ships a web build. Hardcoding them means the farmer silently breaks
(a stale Bookmarks id returns nothing; a stale features set returns HTTP 400).
Instead of copying ids out of DevTools by hand, this opens X headlessly with the
reader's own session, visits the pages that fire the operations the farmer uses,
and records exactly what the web client sends: id, method, features, fieldToggles.

Writes connectors/twitter/.state/graphql_ids.json:
  {"discovered_utc": ..., "ops": {"HomeLatestTimeline": {"id", "method", "features", "fieldToggles"}, ...}}

The farmer reads this cache first and re-runs discovery automatically when an
operation returns 404/400. Run manually:  python3 connectors/twitter/discover_ids.py
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HERE = Path(__file__).parent
CACHE = HERE / ".state" / "graphql_ids.json"
CFG = json.loads((HERE / "config.json").read_text())
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128 Safari/537.36")
WANT = {"HomeLatestTimeline", "HomeTimeline", "Bookmarks", "UserByScreenName",
        "UserTweets", "UserOriginalsTimeline", "UserTweetsAndReplies"}


def _session_cookies():
    """Same auth the farmer uses: x-cookies.json if present, else the browser."""
    p = Path(CFG.get("x_cookies_path", "~/.config/{{WIKI_NAME}}/x-cookies.json")).expanduser()
    if p.exists():
        try:
            d = json.loads(p.read_text())
            if d.get("auth_token") and d.get("ct0"):
                return d
        except Exception:
            pass
    import browser_cookie3
    return {c.name: c.value for c in browser_cookie3.chrome(domain_name="x.com")}


def discover(verbose: bool = True) -> dict:
    from playwright.sync_api import sync_playwright

    ck = _session_cookies()
    if not (ck.get("auth_token") and ck.get("ct0")):
        raise RuntimeError("no X session cookies (auth_token/ct0)")
    cookies = [{"name": k, "value": v, "domain": ".x.com", "path": "/", "secure": True}
               for k, v in ck.items() if k in ("auth_token", "ct0", "twid", "kdt", "att")]
    ops = {}

    def on_req(req):
        m = re.search(r"/i/api/graphql/([A-Za-z0-9_-]+)/([A-Za-z]+)", req.url)
        if not m or m.group(2) not in WANT or m.group(2) in ops:
            return
        qid, op = m.group(1), m.group(2)
        feats, toggles = {}, None
        try:
            if req.method == "GET":
                q = parse_qs(urlparse(req.url).query)
                feats = json.loads(q.get("features", ["{}"])[0])
                toggles = json.loads(q["fieldToggles"][0]) if "fieldToggles" in q else None
            else:
                body = json.loads(req.post_data or "{}")
                feats = body.get("features", {}) or {}
                toggles = body.get("fieldToggles")
        except Exception:
            pass
        ops[op] = {"id": qid, "method": req.method, "features": feats, "fieldToggles": toggles}

    own = CFG.get("own_handle", "")
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx = b.new_context(user_agent=UA, viewport={"width": 1280, "height": 900})
        ctx.add_cookies(cookies)
        pg = ctx.new_page()
        pg.on("request", on_req)
        pg.goto("https://x.com/home", wait_until="domcontentloaded", timeout=45000)
        pg.wait_for_timeout(6000)
        try:
            pg.get_by_role("tab", name=re.compile("Following", re.I)).first.click(timeout=8000)
            pg.wait_for_timeout(5000)
        except Exception:
            pass
        pg.goto("https://x.com/i/bookmarks", wait_until="domcontentloaded", timeout=45000)
        pg.wait_for_timeout(5000)
        if own:
            pg.goto(f"https://x.com/{own}", wait_until="domcontentloaded", timeout=45000)
            pg.wait_for_timeout(5000)
            pg.mouse.wheel(0, 3000)
            pg.wait_for_timeout(3000)
        b.close()

    # Some ops (e.g. UserTweets) are not fired by the pages we visit but their ids
    # live in the main bundle; borrow feature flags from a sibling timeline op.
    try:
        import requests
        s = requests.Session(); s.headers["User-Agent"] = UA; s.cookies.update(ck)
        html = s.get("https://x.com/home", timeout=25).text
        main = next(u for u in re.findall(r'https://abs\.twimg\.com/[^"\'\s]+?\.js', html) if "/main." in u)
        bundle = s.get(main, timeout=40).text
        sibling = ops.get("UserOriginalsTimeline") or ops.get("HomeTimeline") or {}
        for op in ("UserTweets", "UserByScreenName"):
            if op in ops:
                continue
            m = re.search(r'queryId:\s*"([^"]+)",\s*operationName:\s*"%s"' % op, bundle)
            if m:
                ops[op] = {"id": m.group(1), "method": "GET", "features": sibling.get("features", {}),
                           "fieldToggles": sibling.get("fieldToggles"), "from_bundle": True}
    except Exception as e:
        print(f"  bundle scan skipped: {e}")

    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps({"discovered_utc": datetime.now(timezone.utc).isoformat(),
                                 "ops": ops}, indent=2))
    if verbose:
        for op in sorted(ops):
            print(f"  {op:24s} {ops[op]['id']}  ({ops[op]['method']}, {len(ops[op]['features'])} features)")
        missing = sorted({"HomeLatestTimeline", "HomeTimeline", "Bookmarks"} - set(ops))
        if missing:
            print(f"  WARNING: not captured: {missing}")
    return ops


if __name__ == "__main__":
    try:
        discover()
    except Exception as e:
        print(f"discovery failed: {e}")
        sys.exit(1)
