#!/usr/bin/env python3
"""
Continuity step for a Cerebro Radio episode: run before NotebookLM generation.

For an edition date (Wednesday or Sunday) it:
  1. Finds the previous episode and makes sure its transcript exists (transcribe.py).
  2. Runs Claude non-interactively over continuity_prompt.md, which reads this window's
     digests + Media Zone, the previous brief/transcript and the state ledgers, then writes
       connectors/notebooklm/episodes/DATE/continuity_brief.md   (uploaded first)
       connectors/notebooklm/episodes/DATE/episode_brief.md      (main source)
       connectors/notebooklm/episodes/DATE/notebooklm_instructions.txt (prepended to the focus prompt)
     and updates connectors/notebooklm/state/{predictions,threads,trends,production_notes}.md.
  3. Checks the outputs exist and flags banned generic phrasing.

podcast.py calls this automatically; it can also run on its own.

Run: python3 connectors/notebooklm/continuity.py DATE [--force]
"""

import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CFG = json.loads((HERE / "config.json").read_text())
EPISODES = HERE / "episodes"
OUTPUTS = ("continuity_brief.md", "episode_brief.md", "notebooklm_instructions.txt")
BANNED = ("exciting developments", "continues to evolve", "interesting follow-ups", "heating up")
EDITION = {2: "Wednesday", 6: "Sunday"}


def episode_dates():
    """Dates of every episode that aired (audio or Substack note present), oldest first."""
    found = set()
    for d in (REPO / "wiki" / "daily-digest").glob("*/podcasts/*"):
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name) and any(d.glob(f"{d.name}.*")):
            found.add(d.name)
    return sorted(found)


def days_between(a, b):
    """Dates after a, up to and including b."""
    s, e = datetime.strptime(a, "%Y-%m-%d"), datetime.strptime(b, "%Y-%m-%d")
    return [(s + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, (e - s).days + 1)]


def weekday_name(d):
    return datetime.strptime(d, "%Y-%m-%d").strftime("%A")


def build(date, force=False):
    out_dir = EPISODES / date
    if all((out_dir / f).exists() for f in OUTPUTS) and not force:
        print(f"continuity {date}: briefs already exist")
        return 0
    wd = datetime.strptime(date, "%Y-%m-%d").weekday()
    edition = EDITION.get(wd, weekday_name(date))
    prior = [d for d in episode_dates() if d < date]
    if not prior:
        print(f"continuity {date}: no previous episode found; skipping")
        return 1
    prev = prior[-1]
    prev_prev = prior[-2] if len(prior) > 1 else (datetime.strptime(prev, "%Y-%m-%d") - timedelta(days=4)).strftime("%Y-%m-%d")
    window = [d for d in days_between(prev, date)
              if (REPO / "wiki" / "daily-digest" / d[:7] / f"{d}.md").exists()]
    if not window:
        print(f"continuity {date}: no digests between {prev} and {date}; skipping")
        return 1

    # The previous episode's transcript is what the audience heard; make sure it exists.
    for d in prior[-3:]:
        subprocess.run([sys.executable, str(HERE / "transcribe.py"), d], check=False)

    fill = {
        "EDITION_TYPE": edition,
        "EDITION_DATE": date,
        "PREV_DATE": prev,
        "PREV_TYPE": EDITION.get(datetime.strptime(prev, "%Y-%m-%d").weekday(), weekday_name(prev)),
        "WINDOW_DATES": ", ".join(window),
        "PREV_WINDOW_DATES": ", ".join(days_between(prev_prev, prev)),
        "BOOTSTRAP_EPISODES": ", ".join(prior[-3:]),
        "REPO": str(REPO),
    }
    prompt = (HERE / "continuity_prompt.md").read_text()
    for k, v in fill.items():
        prompt = prompt.replace("{{" + k + "}}", v)
    out_dir.mkdir(parents=True, exist_ok=True)
    (HERE / "state").mkdir(exist_ok=True)

    claude = shutil.which("claude") or str(Path.home() / ".local/bin/claude")
    cmd = [claude, "--dangerously-skip-permissions", "-p", prompt]
    if CFG.get("continuity_model"):
        cmd[1:1] = ["--model", CFG["continuity_model"]]
    timeout = shutil.which("gtimeout")
    if timeout:
        cmd = [timeout, f"{CFG.get('continuity_timeout_minutes', 45)}m"] + cmd
    print(f"continuity {date}: {edition} edition, previous {prev}, window {window[0]}..{window[-1]}; running Claude...")
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    (out_dir / "claude.log").write_text(r.stdout[-20000:] + ("\n--- stderr ---\n" + r.stderr[-5000:] if r.stderr else ""))

    missing = [f for f in OUTPUTS if not (out_dir / f).exists()]
    if missing:
        print(f"continuity {date}: FAILED, missing {missing} (rc={r.returncode}); see {out_dir / 'claude.log'}")
        return 1
    brief = (out_dir / "continuity_brief.md").read_text().lower()
    hits = [p for p in BANNED if p in brief]
    if hits:
        print(f"continuity {date}: WARNING banned generic phrasing in continuity brief: {hits}")
    print(f"continuity {date}: ok -> {out_dir.relative_to(REPO)}/")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    sys.exit(build(args[0], "--force" in sys.argv))
