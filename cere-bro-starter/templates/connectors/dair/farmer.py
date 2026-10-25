#!/usr/bin/env python3
"""
DAIR.AI Academy papers, from the PUBLIC site (no login).

Reads academy.dair.ai/papers (AI Papers of the Week, newest first, paginated with
?page=N) plus the curated collections, and writes every paper not seen before to
  raw/dair/YYYY-MM-DD-HHMMSS-dair-academy.md
with the arXiv id, the week/issue, and DAIR's own "curator's take" + key points.

Self-backfilling: it walks back page by page until a whole page is already known
(capped at max_pages), so a missed week is picked up on the next run. The
dair-academy MCP server is optional on top of this; nothing depends on its login.

Run: python3 connectors/dair/farmer.py [--dry-run]
"""

import html
import json
import re
import sys
import warnings
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

warnings.filterwarnings("ignore")
import requests  # noqa: E402

HERE = Path(__file__).parent
REPO = HERE.parent.parent
CFG = json.loads((HERE / "config.json").read_text())
STATE_P = HERE / ".state" / "seen.json"
OUT_DIR = REPO / "raw" / "dair"
BASE = "https://academy.dair.ai"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/128 Safari/537.36"}
PAPER_RX = re.compile(r'href="(/papers/(?!collections/)[a-z0-9-]+-(\d{4}\.\d{4,5}))"')
DRY = "--dry-run" in sys.argv


def get(url):
    r = requests.get(url, headers=UA, timeout=30)
    r.raise_for_status()
    return r.text


def text_of(raw):
    raw = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</(p|div|h\d|li)>", "\n", raw)
    t = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", t)).strip()


def listing(url):
    return list(dict.fromkeys(PAPER_RX.findall(get(url))))


def paper(path_id):
    path, arxiv = path_id
    url = BASE + path
    try:
        t = text_of(get(url))
    except Exception as e:
        return {"url": url, "arxiv": arxiv, "error": type(e).__name__}
    title = t.split(" | DAIR.AI Academy")[0].strip().split("\n")[0][:300]
    week = (re.search(r"All papers\s*/\s*(?:Week of\s*)?([A-Z][a-z]{2}[^\n]{1,30}?\d{4})", t) or [None, ""])[1]
    m = re.search(r"The curator.s take(.*?)(?:Every Monday Get next week|Related papers|More from this week|Read the paper|$)", t, re.S)
    body = (m.group(1) if m else t)
    body = re.sub(r"Ask this paper.*?Ask in Paper Chat", " ", body, flags=re.S)
    return {"url": url, "arxiv": arxiv, "title": title, "week": week,
            "arxiv_url": f"https://arxiv.org/abs/{arxiv}", "take": body.strip()[: CFG.get("max_chars", 4000)]}


def main():
    try:
        state = json.loads(STATE_P.read_text())
    except Exception:
        state = {"seen": {}}
    seen = state["seen"]
    found, sources, errors = [], {}, []
    for page in range(1, CFG.get("max_pages", 4) + 1):
        url = f"{BASE}/papers" + (f"?page={page}" if page > 1 else "")
        try:
            items = listing(url)
        except Exception as e:
            errors.append(f"{url}: {type(e).__name__}")
            break
        new = [i for i in items if i[1] not in seen]
        for i in new:
            sources.setdefault(i[1], "AI Papers of the Week")
        found += new
        if not new:          # whole page already known: caught up
            break
    for name, path in CFG.get("collections", {}).items():
        try:
            for i in listing(BASE + path):
                if i[1] not in seen and i[1] not in sources:
                    found.append(i)
                    sources[i[1]] = f"Collection: {name}"
        except Exception as e:
            errors.append(f"{name}: {type(e).__name__}")
    found = list(dict.fromkeys(found))
    print(f"dair: {len(found)} new paper(s); {len(errors)} gap(s)")
    for e in errors:
        print(f"  gap: {e}")
    if DRY:
        for p, a in found:
            print(f"  {a}  {sources[a]}  {p}")
        return
    if found:
        with ThreadPoolExecutor(6) as ex:
            papers = list(ex.map(paper, found))
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        loc = datetime.now()
        out = OUT_DIR / f"{loc:%Y-%m-%d-%H%M%S}-dair-academy.md"
        lines = [f"# DAIR.AI Academy papers | captured {loc:%Y-%m-%d %H:%M} local", "",
                 f"{len(papers)} new paper(s), from the public academy.dair.ai site.", ""]
        if errors:
            lines += ["**Gaps this run:** " + "; ".join(errors), ""]
        for p in papers:
            lines += [f"## {p.get('title') or p['arxiv']}",
                      f"- arXiv: {p['arxiv']} ({p['arxiv_url'] if 'arxiv_url' in p else ''})",
                      f"- DAIR page: {p['url']}",
                      f"- source: {sources[p['arxiv']]}" + (f" | DAIR date: {p['week']}" if p.get("week") else ""), ""]
            if p.get("take"):
                lines += ["DAIR curator's take and key points:", "", "```text", p["take"].replace("```", "'''"), "```", ""]
            elif p.get("error"):
                lines += [f"(page fetch failed: {p['error']})", ""]
        out.write_text("\n".join(lines))
        print(f"  wrote {out.relative_to(REPO)}")
    now = datetime.now(timezone.utc).isoformat()
    for _, a in found:
        seen[a] = now
    STATE_P.parent.mkdir(exist_ok=True)
    STATE_P.write_text(json.dumps(state, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
