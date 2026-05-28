#!/usr/bin/env python3
"""
NotebookLM podcast generator for the wiki.

For a given date, this script:
  1. Parses the daily digest to find sources (wiki summaries, external URLs).
  2. Creates a NotebookLM notebook, adds all sources.
  3. Generates a long-form audio overview with the focus prompt from config.
  4. Polls until ready, downloads m4a to wiki/daily-digest/YYYY-MM/podcasts/YYYY-MM-DD/.
  5. Writes a Substack note (markdown) alongside the audio.
  6. Optionally deletes the notebook to keep your NotebookLM workspace clean.

Run:    python3 connectors/notebooklm/podcast.py                  # for today
        python3 connectors/notebooklm/podcast.py 2026-05-10       # for a specific date

Requirements: `nlm` CLI installed and authenticated (`pip install notebooklm-mcp-cli`,
then `nlm login`).
"""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────

REPO_ROOT   = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).parent / "config.json"

cfg = json.loads(CONFIG_PATH.read_text())

# ── Date ───────────────────────────────────────────────────────────────────────

if len(sys.argv) > 1 and re.match(r"^\d{4}-\d{2}-\d{2}$", sys.argv[1]):
    date_str = sys.argv[1]
else:
    now_ist = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
    date_str = now_ist.strftime("%Y-%m-%d")

year_month = date_str[:7]
DIGEST_PATH = REPO_ROOT / "wiki" / "daily-digest" / year_month / f"{date_str}.md"
EP_DIR      = REPO_ROOT / "wiki" / "daily-digest" / year_month / "podcasts" / date_str
AUDIO_PATH  = EP_DIR / f"{date_str}.m4a"
HTML_PATH   = EP_DIR / f"{date_str}.html"

print(f"Podcast generator | {date_str}")
print(f"Digest: {DIGEST_PATH}")
print(f"Output: {EP_DIR}/")

if not DIGEST_PATH.exists():
    print(f"ERROR: digest not found at {DIGEST_PATH}")
    sys.exit(1)

EP_DIR.mkdir(parents=True, exist_ok=True)

if AUDIO_PATH.exists():
    print(f"Audio already exists for {date_str}. Use --force to regenerate (not implemented; rename manually).")
    sys.exit(0)

# ── Helpers ────────────────────────────────────────────────────────────────────

def run(cmd: list[str], check: bool = True) -> str:
    """Run a subprocess and return stdout."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"ERROR: {' '.join(cmd)}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout

def nlm(*args, capture: bool = True) -> str:
    return run(["nlm", *args])

# ── Episode number ─────────────────────────────────────────────────────────────

def compute_episode_number() -> int:
    """Count prior episode folders to figure out the number for this one."""
    podcasts_root = REPO_ROOT / "wiki" / "daily-digest"
    n = 0
    if not podcasts_root.exists():
        return 1
    for ep in sorted(podcasts_root.rglob("podcasts/*/")):
        if ep.is_dir() and re.match(r"^\d{4}-\d{2}-\d{2}$", ep.name) and ep.name < date_str:
            n += 1
    return n + 1

EPISODE_NUMBER = compute_episode_number()
print(f"Episode #: {EPISODE_NUMBER}")

# ── Parse digest for sources ───────────────────────────────────────────────────

digest_text = DIGEST_PATH.read_text(encoding="utf-8")

# Wiki summary pages cross-linked from the digest (relative .md links)
wiki_summary_paths: list[Path] = []
for m in re.finditer(r"\(\.\.\/\.\.\/([^)]+\.md)\)", digest_text):
    rel = m.group(1)
    path = REPO_ROOT / "wiki" / rel
    if path.exists():
        wiki_summary_paths.append(path)
# dedup
wiki_summary_paths = sorted(set(wiki_summary_paths))

# External URLs from Deep Dive Links lines
# Match section: ### <title> ... **Links:** [Name](url) ...
deep_dive_urls: list[str] = []
in_deep_dives = False
current_section_text: list[str] = []
for line in digest_text.splitlines():
    if line.startswith("## "):
        in_deep_dives = (line.strip() == "## Deep Dives")
        continue
    if not in_deep_dives:
        continue
    if line.startswith("**Links:**") and cfg.get("include_external_urls_from_deep_dives", True):
        for url_match in re.finditer(r"\[([^\]]+)\]\((https?://[^)]+)\)", line):
            label, url = url_match.group(1), url_match.group(2)
            # Skip wiki cross-links and skip nitter (already in social streams)
            if "Wiki" in label or "nitter" in url:
                continue
            deep_dive_urls.append(url)

# Social-stream (Media Live) files — full 24h window for the target podcast date.
#
# Convention: the podcast is LAGGED BY ONE DAY relative to the cron. The 9 AM cron
# on day Y generates the podcast for day X (where X = Y - 1). By that time, X's full
# day window (9 AM X → 9 AM Y) is complete:
#   - All 4 daytime slot files for X exist (morning/afternoon/evening/pm).
#   - The midnight rollup for X exists (X.md, aggregating the 4 slots).
#   - The overnight tail from 10 PM X to 9 AM Y is captured by Y's morning slot
#     (just written by today's farmer at 9 AM), tagged with Y's date.
#
# Source set for date_str = X:
#   - All X-prefixed files (X-morning, X-afternoon, X-evening, X-pm, X.md rollup)
#   - Y-morning.md (the next-day morning slot — overnight catch)
social_stream_paths: list[Path] = []
if cfg.get("include_media_live_files", True):
    # Target date's own social-stream files (4 slots + daily rollup)
    ss_dir = REPO_ROOT / "wiki" / "social-stream" / year_month
    if ss_dir.exists():
        social_stream_paths.extend(sorted(ss_dir.glob(f"{date_str}*.md")))

    # Next-day morning slot — captures the overnight tail of date_str (10 PM → 9 AM)
    tomorrow         = (datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow_ym      = tomorrow[:7]
    tomorrow_morning = REPO_ROOT / "wiki" / "social-stream" / tomorrow_ym / f"{tomorrow}-morning.md"
    if tomorrow_morning.exists():
        social_stream_paths.append(tomorrow_morning)

print(f"\nSources discovered:")
print(f"  Digest:           1")
print(f"  Wiki summaries:   {len(wiki_summary_paths)}")
print(f"  Social-stream:    {len(social_stream_paths)}")
print(f"  External URLs:    {len(deep_dive_urls)}")
TOTAL = 1 + len(wiki_summary_paths) + len(social_stream_paths) + len(deep_dive_urls)
print(f"  TOTAL:            {TOTAL}")

if TOTAL > cfg["max_sources_per_notebook"]:
    print(f"WARN: source count {TOTAL} exceeds max {cfg['max_sources_per_notebook']}; trimming wiki summaries first.")
    while TOTAL > cfg["max_sources_per_notebook"] and wiki_summary_paths:
        wiki_summary_paths.pop()
        TOTAL -= 1

# ── Create notebook ───────────────────────────────────────────────────────────

print("\nCreating notebook...")
title = f"{cfg['show_name']} {date_str}"
out = nlm("notebook", "create", title)
m = re.search(r"ID:\s*([a-f0-9-]+)", out)
if not m:
    print(f"ERROR: couldn't parse notebook ID from:\n{out}")
    sys.exit(1)
NOTEBOOK_ID = m.group(1)
print(f"  Notebook ID: {NOTEBOOK_ID}")

# ── Add sources ────────────────────────────────────────────────────────────────

def add_file_source(path: Path, title_hint=None):
    args = ["source", "add", NOTEBOOK_ID, "--file", str(path)]
    if title_hint:
        args += ["--title", title_hint]
    print(f"  + {path.name}")
    nlm(*args)

def add_url_sources(urls: list[str]):
    if not urls:
        return
    args = ["source", "add", NOTEBOOK_ID]
    for u in urls:
        args += ["--url", u]
    print(f"  + {len(urls)} URL(s)")
    nlm(*args)

print("\nAdding sources:")
add_file_source(DIGEST_PATH, title_hint=f"Daily digest {date_str}")
for p in social_stream_paths:
    add_file_source(p)
for p in wiki_summary_paths:
    add_file_source(p)
add_url_sources(deep_dive_urls)

# ── Generate audio ─────────────────────────────────────────────────────────────

print("\nKicking off audio generation...")
out = nlm("audio", "create", NOTEBOOK_ID,
          "--format", cfg["audio_format"],
          "--length", cfg["audio_length"],
          "--focus", cfg["focus_prompt"],
          "--confirm")
m = re.search(r"Artifact ID:\s*([a-f0-9-]+)", out)
if not m:
    print(f"ERROR: couldn't parse artifact ID from:\n{out}")
    sys.exit(1)
ARTIFACT_ID = m.group(1)
print(f"  Artifact ID: {ARTIFACT_ID}")

# ── Poll until ready ───────────────────────────────────────────────────────────

print("\nPolling for completion...")
start = time.time()
poll_interval = cfg["poll_interval_seconds"]
timeout = cfg["poll_timeout_minutes"] * 60
while True:
    out = nlm("studio", "status", NOTEBOOK_ID)
    try:
        artifacts = json.loads(out)
    except json.JSONDecodeError:
        artifacts = []
    status = next((a["status"] for a in artifacts if a.get("id") == ARTIFACT_ID), "unknown")
    elapsed = int(time.time() - start)
    print(f"  [+{elapsed}s] status={status}")
    if status in ("completed", "complete", "ready", "done"):
        break
    if status in ("failed", "error"):
        print("Generation failed.")
        sys.exit(1)
    if elapsed > timeout:
        print(f"Timeout after {cfg['poll_timeout_minutes']} min.")
        sys.exit(1)
    time.sleep(poll_interval)

# ── Download ───────────────────────────────────────────────────────────────────

print(f"\nDownloading audio to {AUDIO_PATH}...")
nlm("download", "audio", NOTEBOOK_ID, "--id", ARTIFACT_ID, "-o", str(AUDIO_PATH))
print(f"  ✓ {AUDIO_PATH.stat().st_size // (1024 * 1024)} MB")

# ── Write Substack note ───────────────────────────────────────────────────────

print("\nDrafting Substack note...")
# Extract one-sentence framing (blockquote on line 3-ish)
framing_match = re.search(r"^>\s*(.+)$", digest_text, flags=re.MULTILINE)
framing = framing_match.group(1).strip() if framing_match else ""

# Extract TL;DR bullets
tldr_bullets: list[str] = []
in_tldr = False
for line in digest_text.splitlines():
    if line.strip() == "## TL;DR":
        in_tldr = True
        continue
    if in_tldr and line.startswith("##"):
        break
    if in_tldr and line.startswith("- "):
        # Strip the bold lead and keep the gist
        b = re.sub(r"^- \*\*([^*]+)\*\*\s*[—-]?\s*", r"\1: ", line[2:].strip())
        b = re.sub(r"\(\[[^\]]+\]\([^)]+\)\)", "", b)  # drop trailing source link
        tldr_bullets.append(b.strip())

# Extract Deep Dive titles
deep_dive_titles: list[str] = []
in_dd = False
for line in digest_text.splitlines():
    if line.strip() == "## Deep Dives":
        in_dd = True
        continue
    if in_dd and line.startswith("## ") and not line.startswith("###"):
        break
    if in_dd and line.startswith("### "):
        deep_dive_titles.append(line[4:].strip())

# Compute actual audio duration so the note's "Run time" is accurate
try:
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(AUDIO_PATH)],
        capture_output=True, text=True, check=True
    )
    run_min = int(round(float(probe.stdout.strip()) / 60))
    run_time_str = f"~{run_min} min"
except Exception:
    run_time_str = "~45 min"

note = []
note.append(f"# {EPISODE_NUMBER} — {cfg['show_name']}")
note.append("")
note.append(f"**Date:** {date_str}  ")
note.append(f"**Run time:** {run_time_str}")
note.append("")
if framing:
    note.append(framing)
    note.append("")
if tldr_bullets:
    note.append("**In this episode**")
    for b in tldr_bullets[:6]:
        note.append(f"- {b}")
    note.append("")
note.append("---")
note.append("")
note.append(f"🎧 Audio attached. Full digest: [{date_str}](https://{{GITHUB_USERNAME}}.github.io/{{GITHUB_REPO}}/digests/{date_str}/)")
note.append("")

note_md = "\n".join(note)
# Substack's editor doesn't read markdown on paste — we render to HTML below
# and only persist the HTML. The .md text is kept in memory as the source for
# the renderer.


# ── Render HTML for Substack paste ─────────────────────────────────────────────
# Substack's editor is rich-text, not markdown. Pasting raw .md shows literal
# `#` and `**`. Render to HTML so the user can open in browser, select all,
# copy, and paste into Substack with regular Cmd+V — formatting transfers.

def _process_inline(text: str) -> str:
    """Inline markdown → HTML: links, bold, italic."""
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    return text

def _md_to_html_blocks(md_text: str) -> str:
    """Minimal markdown → HTML for the small note subset we use."""
    blocks = re.split(r"\n\s*\n", md_text.strip())
    out_blocks = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if block == "---":
            out_blocks.append("<hr>")
            continue
        # Heading: single line starting with #+
        first_line = block.split("\n")[0]
        heading_match = re.match(r"^(#+)\s+(.+)$", first_line)
        if heading_match and "\n" not in block:
            level = min(len(heading_match.group(1)), 6)
            text = _process_inline(heading_match.group(2))
            out_blocks.append(f"<h{level}>{text}</h{level}>")
            continue
        # List: every non-empty line starts with "- "
        lines = block.split("\n")
        non_empty = [ln for ln in lines if ln.strip()]
        if non_empty and all(ln.lstrip().startswith("- ") for ln in non_empty):
            items = [f"  <li>{_process_inline(ln.lstrip()[2:].strip())}</li>" for ln in non_empty]
            out_blocks.append("<ul>\n" + "\n".join(items) + "\n</ul>")
            continue
        # Paragraph: join lines (preserve `  ` line-break as <br>)
        para_parts = []
        for ln in lines:
            content = _process_inline(ln.rstrip())
            if ln.endswith("  "):
                para_parts.append(content + "<br>")
            else:
                para_parts.append(content)
        out_blocks.append("<p>" + " ".join(para_parts) + "</p>")
    return "\n\n".join(out_blocks)

note_html_body = _md_to_html_blocks(note_md)
html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{cfg['show_name']} — episode {EPISODE_NUMBER} ({date_str})</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
          max-width: 680px; margin: 2rem auto; padding: 0 1rem;
          line-height: 1.6; color: #1a1a1a; }}
  h1 {{ font-size: 1.8rem; margin-bottom: 0.5rem; }}
  ul {{ padding-left: 1.5rem; }}
  li {{ margin-bottom: 0.4rem; }}
  hr {{ border: 0; border-top: 1px solid #ddd; margin: 1.5rem 0; }}
  a  {{ color: #0066cc; }}
  p  {{ margin: 0.75rem 0; }}
</style>
</head>
<body>
{note_html_body}
</body>
</html>
"""
HTML_PATH.write_text(html_doc, encoding="utf-8")
print(f"  ✓ {HTML_PATH}  (open in browser → Cmd+A → Cmd+C → paste into Substack)")


# ── Upload audio to GitHub Release ────────────────────────────────────────────
# The /radio page on the Astro site links to audio via GitHub Releases:
#   github.com/<user>/<repo>/releases/download/podcasts-YYYY-MM/YYYY-MM-DD.m4a
# Episodes are grouped by month, one release tag per month. Idempotent —
# `gh release upload` with --clobber overwrites in case of re-runs.
#
# Requires `gh` CLI authenticated for the repo. If gh is missing or auth
# fails, log a warning and continue (the .html note is still committed; the
# audio is local-only until uploaded manually).
print("\nUploading audio to GitHub Release...")
RELEASE_TAG = f"podcasts-{date_str[:7]}"
try:
    # Check if release exists; create it if not.
    check = subprocess.run(["gh", "release", "view", RELEASE_TAG],
                           capture_output=True, text=True)
    if check.returncode != 0:
        print(f"  Release {RELEASE_TAG} does not exist — creating it.")
        subprocess.run(["gh", "release", "create", RELEASE_TAG,
                        "--title", f"Cerebro Radio — {date_str[:7]} episodes",
                        "--notes", f"Audio assets for Cerebro Radio episodes published in {date_str[:7]}."],
                       capture_output=True, text=True, check=True)
    # Upload the m4a as a release asset.
    up = subprocess.run(["gh", "release", "upload", RELEASE_TAG, str(AUDIO_PATH), "--clobber"],
                        capture_output=True, text=True)
    if up.returncode == 0:
        print(f"  ✓ Uploaded {AUDIO_PATH.name} to release {RELEASE_TAG}")
        print(f"  ✓ Audio URL: https://github.com/{{GITHUB_USERNAME}}/{{GITHUB_REPO}}/releases/download/{RELEASE_TAG}/{AUDIO_PATH.name}")
    else:
        print(f"  WARN: gh release upload failed: {up.stderr.strip()[:200]}")
except FileNotFoundError:
    print("  WARN: gh CLI not installed — skipping audio upload. Episode .html is committed; audio stays local-only.")
except subprocess.CalledProcessError as e:
    print(f"  WARN: gh release create failed: {e.stderr.strip()[:200] if e.stderr else e}")
except Exception as e:
    print(f"  WARN: unexpected upload error: {e}")

# ── Cleanup notebook ──────────────────────────────────────────────────────────

if cfg.get("delete_notebook_after_download", True):
    print("\nDeleting NotebookLM notebook (cleanup)...")
    try:
        subprocess.run(["nlm", "notebook", "delete", NOTEBOOK_ID, "--confirm"],
                       capture_output=True, text=True, check=False)
    except Exception:
        pass

print(f"\n✓ Done. Episode #{EPISODE_NUMBER} ready at {EP_DIR}/")
print(f"  • Audio: {AUDIO_PATH.name}")
print(f"  • Notes: {HTML_PATH.name}  (paste source for Substack)")
