#!/usr/bin/env python3
"""
AI lab watcher: keeps the wiki current with what the major labs publish.

Three mechanisms, all configured in config.json (add a lab = add an entry):
  1. feeds   official RSS/Atom feeds (OpenAI, DeepMind, Google Research, Meta Eng,
             Microsoft Research, NVIDIA, Apple, AWS, Mistral, Qwen, Ai2, ...).
  2. pages   labs with no feed (Anthropic news/research/system cards, xAI, Meta AI,
             DeepSeek, Cohere, ...): fetch the listing page, diff its post links
             against state. "browser": true renders JS/bot-walled pages headlessly.
             The first sighting of a page only records a baseline (no flood).
  3. hf_orgs new open-weight model repos on the Hugging Face Hub, with the model
             card captured (that is where open releases put their benchmarks).

Every new item is enriched with up to max_article_chars of page text (PDF system
cards: text extracted when pypdf is available) and tagged kind = system_card /
model_release / post. Output (only when something is new):
  raw/labs/YYYY-MM-DD-HHMMSS-labs.md  (+ .json)
Uniquely named so repeated captures never clobber each other; the collection
window slices them by capture time. Dedupe state: connectors/labs/.state/seen.json.

Run: python3 connectors/labs/farmer.py [--dry-run]
"""

import html
import io
import json
import re
import sys
import warnings
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urljoin

warnings.filterwarnings("ignore")
import feedparser  # noqa: E402
import requests    # noqa: E402

HERE = Path(__file__).parent
REPO = HERE.parent.parent
CFG = json.loads((HERE / "config.json").read_text())
STATE_P = HERE / ".state" / "seen.json"
OUT_DIR = REPO / "raw" / "labs"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/128 Safari/537.36"}
NOW = datetime.now(timezone.utc)
LOOKBACK = timedelta(hours=CFG.get("lookback_hours", 72))
MAXC = CFG.get("max_article_chars", 10000)
MAXN = CFG.get("max_new_per_source", 15)
DRY = "--dry-run" in sys.argv

SYSCARD = re.compile(r"system[- ]card|model[- ]card|safety (report|card)|preparedness|frontier safety", re.I)
RELEASE = re.compile(r"\b(introducing|announcing|launch|release[sd]?|now available|meet)\b|"
                     r"\b(gpt|gemini|claude|llama|grok|qwen|deepseek|mistral|gemma|phi|nemotron|kimi|glm|muse)[- ]?\d", re.I)


def load_state():
    try:
        return json.loads(STATE_P.read_text())
    except Exception:
        return {"seen": {}, "pages_baselined": []}


def html_to_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</(p|div|h\d|li|tr)>", "\n", raw)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    txt = re.sub(r"[ \t\r\f\v]+", " ", txt)
    return re.sub(r"\n\s*\n+", "\n\n", txt).strip()


def fetch_text(url):
    """Best-effort article/PDF text, capped. Never raises."""
    try:
        r = requests.get(url, headers=UA, timeout=30)
        if r.status_code != 200:
            return ""
        if url.lower().endswith(".pdf") or "pdf" in r.headers.get("content-type", ""):
            try:
                from pypdf import PdfReader
                rd = PdfReader(io.BytesIO(r.content))
                return "\n".join((p.extract_text() or "") for p in rd.pages[:25])[:MAXC]
            except Exception:
                return "(PDF; text extraction unavailable)"
        m = re.search(r"(?is)<(article|main)[^>]*>(.*?)</\1>", r.text)
        return html_to_text(m.group(2) if m else r.text)[:MAXC]
    except Exception:
        return ""


def kind_of(title, url, default="post"):
    s = f"{title} {url}"
    if default == "system_card" or SYSCARD.search(s):
        return "system_card"
    if RELEASE.search(title or ""):
        return "model_release"
    return default


def _entry_time(e):
    for k in ("published_parsed", "updated_parsed"):
        t = e.get(k)
        if t:
            return datetime(*t[:6], tzinfo=timezone.utc)
    return None


def do_feeds(seen, errors):
    out = []

    def one(item):
        lab, url = item
        try:
            r = requests.get(url, headers=UA, timeout=30)
            fp = feedparser.parse(r.content)
            if not fp.entries:
                errors.append(f"{lab}: feed returned no entries (HTTP {r.status_code})")
                return []
        except Exception as e:
            errors.append(f"{lab}: {type(e).__name__}")
            return []
        got = []
        for e in fp.entries:
            link = e.get("link") or ""
            uid = f"feed:{link or e.get('id')}"
            ts = _entry_time(e)
            if uid in seen or not link or (ts and NOW - ts > LOOKBACK):
                continue
            got.append({"lab": lab, "source": "feed", "title": html.unescape(e.get("title", "")).strip(),
                        "url": link, "published": ts.isoformat() if ts else None, "uid": uid,
                        "summary": html_to_text(e.get("summary", ""))[:600]})
        return got[:MAXN]

    with ThreadPoolExecutor(8) as ex:
        for got in ex.map(one, CFG.get("feeds", {}).items()):
            out.extend(got)
    return out


def _browser_links(urls):
    links = {}
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch(headless=True)
            ctx = b.new_context(user_agent=UA["User-Agent"])
            for u in urls:
                pg = ctx.new_page()
                try:
                    pg.goto(u, wait_until="domcontentloaded", timeout=45000)
                    pg.wait_for_timeout(5000)
                    links[u] = pg.eval_on_selector_all("a[href]", "els => els.map(e => [e.href, (e.innerText||'').trim()])")
                except Exception:
                    links[u] = None
                pg.close()
            b.close()
    except Exception:
        pass
    return links


def do_pages(state, errors):
    seen, baselined = state["seen"], set(state.get("pages_baselined", []))
    pages = CFG.get("pages", {})
    rendered = _browser_links([c["url"] for c in pages.values() if c.get("browser")])
    out = []
    for lab, c in pages.items():
        url, rx = c["url"], re.compile(c["link_regex"])
        if c.get("browser"):
            pairs = rendered.get(url)
            if pairs is None:
                errors.append(f"{lab}: page render failed")
                continue
        else:
            try:
                r = requests.get(url, headers=UA, timeout=30)
                if r.status_code != 200:
                    errors.append(f"{lab}: HTTP {r.status_code}")
                    continue
                pairs = [(h, html_to_text(t)[:200]) for h, t in
                         re.findall(r'(?is)<a[^>]+href="([^"#?]+)"[^>]*>(.*?)</a>', r.text)]
            except Exception as e:
                errors.append(f"{lab}: {type(e).__name__}")
                continue
        found = {}
        for h, t in pairs:
            hh = h.split("#")[0].split("?")[0]
            if rx.search(hh):
                full = urljoin(url, hh)
                if full.rstrip("/") != url.rstrip("/"):
                    found.setdefault(full, t)
        if not found:
            errors.append(f"{lab}: no post links matched (layout change?)")
            continue
        if lab not in baselined:
            for full in found:
                seen[f"page:{full}"] = NOW.isoformat()
            baselined.add(lab)
            continue
        new = [(f, t) for f, t in found.items() if f"page:{f}" not in seen][:MAXN]
        for full, t in new:
            title = (t or "").split("\n")[0].strip() or full.rstrip("/").rsplit("/", 1)[-1].replace("-", " ")
            out.append({"lab": lab, "source": "page", "title": title, "url": full, "published": None,
                        "uid": f"page:{full}", "default_kind": c.get("kind", "post")})
    state["pages_baselined"] = sorted(baselined)
    return out


def do_hf(seen, errors):
    out = []

    def one(org):
        try:
            r = requests.get("https://huggingface.co/api/models",
                             params={"author": org, "sort": "createdAt", "direction": -1, "limit": 20},
                             headers=UA, timeout=30)
            models = r.json() if r.status_code == 200 else []
        except Exception as e:
            errors.append(f"HF {org}: {type(e).__name__}")
            return []
        got = []
        for m in models:
            mid, created = m.get("id") or m.get("modelId"), m.get("createdAt")
            if not mid or not created:
                continue
            ts = datetime.fromisoformat(created.replace("Z", "+00:00"))
            uid = f"hf:{mid}"
            if uid in seen or NOW - ts > LOOKBACK:
                continue
            got.append({"lab": f"HF {org}", "source": "hf", "title": mid, "url": f"https://huggingface.co/{mid}",
                        "published": ts.isoformat(), "uid": uid, "default_kind": "model_release",
                        "card_url": f"https://huggingface.co/{mid}/raw/main/README.md",
                        "tags": [t for t in m.get("tags", []) if not t.startswith(("region:", "endpoints"))][:12]})
        return got[:MAXN]

    with ThreadPoolExecutor(8) as ex:
        for got in ex.map(one, CFG.get("hf_orgs", [])):
            out.extend(got)
    return out


def enrich(it):
    if it["source"] == "hf":
        try:
            r = requests.get(it["card_url"], headers=UA, timeout=30)
            card = r.text if r.status_code == 200 else ""
            it["content"] = re.sub(r"(?s)^---.*?---\s*", "", card)[:MAXC]
        except Exception:
            it["content"] = ""
    else:
        it["content"] = fetch_text(it["url"])
    it["kind"] = kind_of(it["title"], it["url"], it.pop("default_kind", "post"))
    return it


def write(items, errors):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    loc = datetime.now()
    stem = OUT_DIR / f"{loc:%Y-%m-%d-%H%M%S}-labs"
    order = {"system_card": 0, "model_release": 1, "post": 2}
    items.sort(key=lambda x: (order[x["kind"]], x["lab"]))
    lines = [f"# AI lab releases | captured {loc:%Y-%m-%d %H:%M} local", "",
             f"{len(items)} new item(s): "
             f"{sum(i['kind']=='system_card' for i in items)} system/model cards, "
             f"{sum(i['kind']=='model_release' for i in items)} model releases, "
             f"{sum(i['kind']=='post' for i in items)} posts.", ""]
    if errors:
        lines += ["**Watcher gaps this run:** " + "; ".join(errors), ""]
    head = {"system_card": "## System and model cards", "model_release": "## Model releases",
            "post": "## Lab posts"}
    cur = None
    for it in items:
        if it["kind"] != cur:
            cur = it["kind"]
            lines += [head[cur], ""]
        lines += [f"### [{it['lab']}] {it['title']}", f"- url: {it['url']}",
                  f"- published: {it.get('published') or 'unknown (page watch: first seen this run)'}",
                  f"- via: {it['source']}" + (f" | tags: {', '.join(it['tags'])}" if it.get("tags") else ""), ""]
        body = it.get("content") or it.get("summary") or ""
        if body:
            lines += ["```text", body.replace("```", "'''"), "```", ""]
    stem.with_suffix(".md").write_text("\n".join(lines))
    stem.with_suffix(".json").write_text(json.dumps({"captured": loc.isoformat(), "errors": errors,
                                                     "items": items}, indent=1))
    return stem.with_suffix(".md")


def main():
    state = load_state()
    errors = []
    items = do_feeds(state["seen"], errors) + do_pages(state, errors) + do_hf(state["seen"], errors)
    # same URL from two mechanisms -> keep one
    uniq = {}
    for it in items:
        uniq.setdefault(it["url"].rstrip("/"), it)
    items = list(uniq.values())
    print(f"labs: {len(items)} new item(s); {len(errors)} gap(s)")
    for e in errors:
        print(f"  gap: {e}")
    if DRY:
        for it in items:
            print(f"  [{it['lab']}] {it['title'][:90]}")
        return
    if items:
        with ThreadPoolExecutor(8) as ex:
            items = list(ex.map(enrich, items))
        path = write(items, errors)
        print(f"  wrote {path.relative_to(REPO)}")
    for it in items:
        state["seen"][it["uid"]] = NOW.isoformat()
    # prune state entries older than 120 days
    cutoff = (NOW - timedelta(days=120)).isoformat()
    state["seen"] = {k: v for k, v in state["seen"].items() if v >= cutoff or k.startswith("page:")}
    STATE_P.parent.mkdir(exist_ok=True)
    STATE_P.write_text(json.dumps(state, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
