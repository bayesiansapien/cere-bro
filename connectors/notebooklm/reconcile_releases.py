#!/usr/bin/env python3
"""
Reconcile podcast audio: ensure every local episode .m4a is uploaded to its
GitHub Release, so the Spotify RSS feed never points at a 404.

Background: podcast.py generates <date>.m4a locally and uploads it to the
GitHub Release `podcasts-YYYY-MM`. The upload leg can fail silently (network
blip, auth hiccup) while generation succeeds — the episode then appears in the
feed but its audio 404s, and Spotify skips it. This happened to 10 episodes
between June and August 2026 before it was caught.

This script walks every wiki/daily-digest/YYYY-MM/podcasts/<date>/<date>.m4a,
checks whether the matching asset exists on the `podcasts-YYYY-MM` Release
(via `gh`, authoritative — not the CDN, which lags), and re-uploads any that
are missing. Creating the Release if it does not exist yet.

Idempotent and safe to run every day. Exit code 0 on success (including
"nothing to do"), non-zero only if an upload genuinely failed after retry.

Run:  python3 connectors/notebooklm/reconcile_releases.py
      python3 connectors/notebooklm/reconcile_releases.py --dry-run
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DIGEST_ROOT = REPO_ROOT / "wiki" / "daily-digest"
DRY_RUN = "--dry-run" in sys.argv

# Resolve `gh` to an absolute path. Under launchd/cron the Homebrew bin dir is
# not on PATH, so a bare "gh" raises FileNotFoundError and every Release upload
# silently fails (podcasts generate but never reach Spotify). Find it on PATH,
# then fall back to the common Homebrew locations.
GH = (shutil.which("gh")
      or next((p for p in ("/opt/homebrew/bin/gh", "/usr/local/bin/gh")
               if os.path.exists(p)), None))


def run(cmd, check=False):
    # Rewrite a leading bare "gh" to the resolved absolute path.
    if cmd and cmd[0] == "gh":
        if not GH:
            print("ERROR: `gh` (GitHub CLI) not found on PATH or in Homebrew "
                  "bins. Install it (brew install gh) or add it to PATH; "
                  "podcast Release uploads cannot run without it.", file=sys.stderr)
            return subprocess.CompletedProcess(cmd, 127, "", "gh not found")
        cmd = [GH] + cmd[1:]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode != 0:
        print(f"ERROR: {' '.join(cmd)}\n{r.stderr}", file=sys.stderr)
    return r


def release_assets(tag: str) -> set[str]:
    """Asset names on a release, or empty set if the release doesn't exist."""
    r = run(["gh", "release", "view", tag, "--json", "assets",
             "-q", ".assets[].name"])
    if r.returncode != 0:
        return set()  # release missing
    return {line.strip() for line in r.stdout.splitlines() if line.strip()}


def ensure_release(tag: str) -> None:
    if run(["gh", "release", "view", tag]).returncode == 0:
        return
    ym = tag.replace("podcasts-", "")
    print(f"  creating release {tag}")
    if not DRY_RUN:
        run(["gh", "release", "create", tag,
             "--title", f"Cerebro Radio {ym} podcasts",
             "--notes", f"Audio assets for {ym} episodes."], check=True)


def main() -> int:
    if not DIGEST_ROOT.exists():
        print(f"No digest root at {DIGEST_ROOT}")
        return 0

    # Gather every local m4a, grouped by release tag.
    local: dict[str, list[Path]] = {}
    for ym_dir in sorted(DIGEST_ROOT.iterdir()):
        pods = ym_dir / "podcasts"
        if not pods.is_dir():
            continue
        for ep_dir in sorted(pods.iterdir()):
            m4a = ep_dir / f"{ep_dir.name}.m4a"
            if m4a.is_file():
                local.setdefault(f"podcasts-{ym_dir.name}", []).append(m4a)

    total = sum(len(v) for v in local.values())
    missing: list[tuple[str, Path]] = []
    for tag, files in local.items():
        have = release_assets(tag)
        for m4a in files:
            if m4a.name not in have:
                missing.append((tag, m4a))

    print(f"Reconcile: {total} local episodes, {len(missing)} missing from Releases.")
    if not missing:
        print("  All episodes present on Releases. Nothing to do.")
        return 0

    failed = []
    for tag, m4a in missing:
        size_mb = m4a.stat().st_size // (1024 * 1024)
        print(f"  {'[dry-run] would upload' if DRY_RUN else 'uploading'} "
              f"{m4a.name} ({size_mb} MB) -> {tag}")
        if DRY_RUN:
            continue
        ensure_release(tag)
        ok = False
        for attempt in range(1, 4):  # 3 attempts
            if run(["gh", "release", "upload", tag, str(m4a), "--clobber"]).returncode == 0:
                ok = True
                break
            print(f"    attempt {attempt} failed, retrying...")
        if ok:
            print(f"    ✓ {m4a.name}")
        else:
            print(f"    ✗ {m4a.name} FAILED after 3 attempts")
            failed.append(m4a.name)

    if failed:
        print(f"RECONCILE INCOMPLETE: {len(failed)} upload(s) still failing: {failed}")
        return 1
    print("Reconcile complete: all missing episodes uploaded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
