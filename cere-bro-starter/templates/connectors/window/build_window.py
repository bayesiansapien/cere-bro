#!/usr/bin/env python3
"""
Collection-window builder for cere-bro: the single source of truth for which raw
inputs belong to which daily digest.

Model
-----
Digest D is written at the daily cutoff (~10:30 IST, just after US-Eastern
midnight) and covers everything FIRST CAPTURED since the previous digest's
cutoff. Windows are defined by capture time (a ledger of when each raw file was
first seen), never by date labels in filenames. So:

  * nothing is lost: a late item (a farmer that failed, a Mac that slept, HF
    adding papers late) is simply captured later and lands in the next window,
    flagged "late";
  * nothing is double-counted: every file belongs to exactly one window, fixed
    at the moment the window is closed.

Usage
-----
  build_window.py --digest-date 2026-09-27            # preview manifest (window still open)
  build_window.py --digest-date 2026-09-27 --close    # after the digest is written: persist the watermark
  build_window.py --next                              # preview the currently open window (for live drafts)

Outputs raw/_windows/<D>.json and raw/_windows/<D>.md (gitignored, local).
"""

import argparse
import json
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RAW = REPO / "raw"
OUT = RAW / "_windows"
STATE = Path(__file__).parent / ".state"
LEDGER = STATE / "ledger.json"          # path -> first_seen_utc
WATERMARKS = STATE / "watermarks.json"  # {"last_cutoff_utc": iso, "closed": {D: {start, end, files}}}
DIGEST_DIR = REPO / "wiki" / "daily-digest"

# Local timezone + daily cutoff come from config.json so any timezone works. Pick
# a cutoff just after US-Eastern midnight in your local time (e.g. 10:30 for IST).
_CFG = json.loads((Path(__file__).parent / "config.json").read_text()) if (Path(__file__).parent / "config.json").exists() else {}
IST = timezone(timedelta(minutes=_CFG.get("local_utc_offset_minutes", 330)))   # named IST for history; = local tz
CUTOFF_HOUR, CUTOFF_MIN = (int(x) for x in _CFG.get("cutoff_local", "10:30").split(":"))

# source -> (subpath glob root, file filter, stale-after hours)
SOURCES = {
    "huggingface": ("huggingface", r"\.md$", 30),
    "rss":         ("rss", r"\.md$", 30),
    "gmail":       ("gmail", r"-newsletters\.md$", 30),
    "twitter":     ("twitter", r"^\d{4}-\d{2}-\d{2}-[a-z]+\.md$", 30),
    "x_feed":      ("twitter/feed", r"-ranked\.json$", 20),
    "bookmarks":   ("twitter/bookmarks", r"\.md$", 48),
    "kurate":      ("kurate", r"\.md$", 200),       # weekly leaderboards
    "reddit":      ("reddit", r"\.md$", 30),
    "youtube":     ("youtube", r"\.json$", 30),
    "linkedin":    ("linkedin", r"\.json$", 48),
}


def _load(p, default):
    try:
        return json.loads(p.read_text())
    except Exception:
        return default


def _birth(p: Path) -> float:
    st = p.stat()
    return getattr(st, "st_birthtime", st.st_mtime)


def scan_ledger(now: datetime) -> dict:
    """Record first-seen time for every raw file. New files get `now`; files that
    predate the ledger are bootstrapped from their filesystem birth time."""
    ledger = _load(LEDGER, {})
    bootstrap = not ledger
    for name, (sub, pat, _) in SOURCES.items():
        root = RAW / sub
        if not root.is_dir():
            continue
        rx = re.compile(pat)
        for f in root.iterdir():
            if not f.is_file() or not rx.search(f.name):
                continue
            key = str(f.relative_to(REPO))
            if key not in ledger:
                ts = datetime.fromtimestamp(_birth(f), timezone.utc) if bootstrap else now
                ledger[key] = ts.isoformat()
    STATE.mkdir(exist_ok=True)
    LEDGER.write_text(json.dumps(ledger, indent=0, sort_keys=True))
    return ledger


def default_start(digest_date: str) -> datetime:
    d = datetime.strptime(digest_date, "%Y-%m-%d").replace(hour=CUTOFF_HOUR, minute=CUTOFF_MIN, tzinfo=IST)
    return (d - timedelta(days=1)).astimezone(timezone.utc)


def next_open_digest_date(now_ist: datetime) -> str:
    today = now_ist.strftime("%Y-%m-%d")
    if (DIGEST_DIR / today[:7] / f"{today}.md").exists():
        return (now_ist + timedelta(days=1)).strftime("%Y-%m-%d")
    return today


def build(digest_date: str, close: bool, now: datetime) -> dict:
    wm = _load(WATERMARKS, {"closed": {}})
    ledger = scan_ledger(now)

    if digest_date in wm["closed"]:           # re-run of an already-closed window: reuse it exactly
        c = wm["closed"][digest_date]
        start, end = datetime.fromisoformat(c["start"]), datetime.fromisoformat(c["end"])
    else:
        last = wm.get("last_cutoff_utc")
        start = datetime.fromisoformat(last) if last else default_start(digest_date)
        end = now

    nominal_prev = (datetime.strptime(digest_date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    files, fresh = {}, {}
    for key, seen in ledger.items():
        t = datetime.fromisoformat(seen)
        src = next((n for n, (sub, pat, _) in SOURCES.items()
                    if key.startswith(f"raw/{sub}/") and "/" not in key[len(f"raw/{sub}/"):]), None)
        if not src:
            continue
        fresh[src] = max(fresh.get(src, t), t)
        if start < t <= end:
            dates = re.findall(r"\d{4}-\d{2}-\d{2}", Path(key).name)
            late = bool(dates) and dates[0] < nominal_prev   # file labelled for an earlier day than D-1
            files.setdefault(src, []).append({"path": key, "first_seen_utc": seen, "late": late})

    gaps = []
    for name, (_, _, stale_h) in SOURCES.items():
        last = fresh.get(name)
        if last is None or (end - last) > timedelta(hours=stale_h):
            gaps.append({"source": name, "last_capture_utc": last.isoformat() if last else None,
                         "stale_after_h": stale_h})

    manifest = {
        "digest_date": digest_date,
        "covers_us_eastern_day": nominal_prev,
        "window_start_utc": start.isoformat(), "window_end_utc": end.isoformat(),
        "window_start_ist": start.astimezone(IST).strftime("%Y-%m-%d %H:%M")+" local",
        "window_end_ist": end.astimezone(IST).strftime("%Y-%m-%d %H:%M")+" local",
        "status": "closed" if close or digest_date in wm["closed"] else "open",
        "counts": {k: len(v) for k, v in files.items()},
        "stale_sources": gaps,
        "files": {k: sorted(v, key=lambda x: x["path"]) for k, v in files.items()},
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{digest_date}.json").write_text(json.dumps(manifest, indent=2))
    lines = [f"# Collection window for the {digest_date} digest", "",
             f"- Window: **{manifest['window_start_ist']} → {manifest['window_end_ist']}** "
             f"(covers the US-Eastern day {nominal_prev}); status: **{manifest['status']}**",
             f"- Files: {sum(manifest['counts'].values())} across {len(manifest['counts'])} sources", ""]
    if gaps:
        lines += ["## Stale / missing sources (name these gaps in the digest)", ""]
        lines += [f"- **{g['source']}**: last capture {g['last_capture_utc'] or 'never'} "
                  f"(expected within {g['stale_after_h']}h)" for g in gaps] + [""]
    for src, items in manifest["files"].items():
        lines += [f"## {src} ({len(items)})", ""]
        lines += [f"- `{i['path']}`" + ("  _(late: labelled for an earlier day)_" if i["late"] else "") for i in items]
        lines.append("")
    (OUT / f"{digest_date}.md").write_text("\n".join(lines))

    if close and digest_date not in wm["closed"]:
        wm["closed"][digest_date] = {"start": start.isoformat(), "end": end.isoformat(),
                                     "files": sum(manifest["counts"].values())}
        wm["last_cutoff_utc"] = end.isoformat()
        STATE.mkdir(exist_ok=True)
        WATERMARKS.write_text(json.dumps(wm, indent=2))
    return manifest


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--digest-date")
    g.add_argument("--next", action="store_true", help="preview the currently open window")
    ap.add_argument("--close", action="store_true")
    a = ap.parse_args()
    now = datetime.now(timezone.utc)
    d = a.digest_date or next_open_digest_date(now.astimezone(IST))
    m = build(d, a.close, now)
    print(f"window {d}: {m['window_start_ist']} -> {m['window_end_ist']} [{m['status']}] "
          f"files={sum(m['counts'].values())} {m['counts']}")
    for gap in m["stale_sources"]:
        print(f"  STALE: {gap['source']} (last {gap['last_capture_utc']})")


if __name__ == "__main__":
    main()
