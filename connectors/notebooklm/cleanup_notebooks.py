#!/usr/bin/env python3
"""
Delete leftover NotebookLM notebooks created by the podcast pipeline.

podcast.py deletes its own notebook after downloading the audio, but a run that
crashes mid-way (auth expiry, network blip, missing digest) creates a notebook
and dies before its cleanup line — so orphans accumulate on the dashboard. This
sweep catches them.

SAFETY — this ONLY deletes notebooks whose title starts with the configured
`show_name` (e.g. "Cerebro Radio"), so notebooks you created yourself are never
touched. It also skips any notebook updated within `safety_window_hours` (default
2h) so an in-flight generation is never nuked.

Run:  python3 connectors/notebooklm/cleanup_notebooks.py            # delete orphans
      python3 connectors/notebooklm/cleanup_notebooks.py --dry-run  # list only
      python3 connectors/notebooklm/cleanup_notebooks.py --keep 3   # keep newest 3

Requires `nlm` authenticated (same as podcast.py). Exit 0 on success (incl. none
to delete); never raises — safe to call from the cron after podcast generation.
"""

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.json"
cfg = json.loads(CONFIG_PATH.read_text())
SHOW_NAME = cfg.get("show_name", "Cerebro Radio")
SAFETY_WINDOW_H = cfg.get("notebook_cleanup_safety_hours", 2)

DRY_RUN = "--dry-run" in sys.argv
KEEP = 0
if "--keep" in sys.argv:
    try:
        KEEP = int(sys.argv[sys.argv.index("--keep") + 1])
    except (IndexError, ValueError):
        KEEP = 0

# Resolve nlm absolutely (cron PATH may omit it — same story as gh).
NLM = (shutil.which("nlm")
       or next((p for p in (os.path.expanduser("~/.local/bin/nlm"),
                            "/opt/homebrew/bin/nlm") if os.path.exists(p)), "nlm"))


def _run(args, timeout=60):
    return subprocess.run([NLM] + args, capture_output=True, text=True, timeout=timeout)


def main() -> int:
    try:
        r = _run(["notebook", "list"])
    except Exception as e:
        print(f"cleanup: could not list notebooks ({e}) — skipping.")
        return 0
    if r.returncode != 0:
        print(f"cleanup: `nlm notebook list` failed (auth?) — skipping.\n{r.stderr[:200]}")
        return 0
    try:
        nbs = json.loads(r.stdout)
    except Exception:
        print("cleanup: could not parse notebook list — skipping.")
        return 0

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=SAFETY_WINDOW_H)

    # ONLY notebooks whose title starts with the show name are ours to delete.
    ours = [n for n in nbs if str(n.get("title", "")).startswith(SHOW_NAME)]
    others = len(nbs) - len(ours)

    def _updated(n):
        try:
            return datetime.fromisoformat(str(n.get("updated_at", "")).replace("Z", "+00:00"))
        except Exception:
            return datetime.min.replace(tzinfo=timezone.utc)

    ours_sorted = sorted(ours, key=_updated, reverse=True)  # newest first
    keep_ids = {n.get("id") for n in ours_sorted[:KEEP]} if KEEP else set()

    to_delete, skipped_recent = [], 0
    for n in ours_sorted:
        if n.get("id") in keep_ids:
            continue
        if _updated(n) > cutoff:
            skipped_recent += 1  # in-flight safety window
            continue
        to_delete.append(n)

    print(f"cleanup: {len(nbs)} notebooks total | {len(ours)} '{SHOW_NAME}' | "
          f"{others} yours (never touched) | keep newest {KEEP} | "
          f"skip {skipped_recent} updated <{SAFETY_WINDOW_H}h | delete {len(to_delete)}")

    deleted = 0
    for n in to_delete:
        title, nid = n.get("title", "?"), n.get("id")
        if DRY_RUN:
            print(f"  [dry-run] would delete: {title} ({nid})")
            continue
        try:
            d = _run(["notebook", "delete", nid, "--confirm"], timeout=45)
            if d.returncode == 0:
                deleted += 1
                print(f"  ✓ deleted: {title}")
            else:
                print(f"  ✗ failed: {title} — {d.stderr.strip()[:100] or d.stdout.strip()[:100]}")
        except Exception as e:
            print(f"  ✗ error deleting {title}: {e}")

    if not DRY_RUN:
        print(f"cleanup: deleted {deleted}/{len(to_delete)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
