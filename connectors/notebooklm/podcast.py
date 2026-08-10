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

# ── Day-of-week routing ────────────────────────────────────────────────────────
# Mon-Fri (weekday 0-4) → daily 50min episode using focus_prompt_daily.
# Sat (weekday 5)       → weekly review 65min episode using focus_prompt_weekly + 7-day source set.
# Sun (weekday 6)       → no podcast; exit cleanly so the cron sweep moves on.
weekday = datetime.strptime(date_str, "%Y-%m-%d").weekday()
schedule = cfg.get("weekday_schedule", {"daily_days": [0,1,2,3,4], "weekly_days": [5], "skip_days": [6]})
FORCE = "--force" in sys.argv

if weekday in schedule.get("skip_days", []):
    print(f"{date_str} is a {['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][weekday]} — no podcast on Sundays per editorial schedule.")
    sys.exit(0)

EPISODE_MODE = "weekly" if weekday in schedule.get("weekly_days", []) else "daily"
print(f"Podcast generator | {date_str} ({['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][weekday]} → {EPISODE_MODE})")
print(f"Digest: {DIGEST_PATH}")
print(f"Output: {EP_DIR}/")

if not DIGEST_PATH.exists():
    print(f"ERROR: digest not found at {DIGEST_PATH}")
    sys.exit(1)

EP_DIR.mkdir(parents=True, exist_ok=True)

if AUDIO_PATH.exists() and not FORCE:
    print(f"Audio already exists for {date_str}. Pass --force to regenerate.")
    sys.exit(0)

if FORCE and AUDIO_PATH.exists():
    print(f"--force: removing existing {AUDIO_PATH.name} before regenerating.")
    AUDIO_PATH.unlink()
    if HTML_PATH.exists():
        HTML_PATH.unlink()

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

def extract_id(out: str, *json_keys: str, regex: str = r"ID:\s*([a-f0-9-]+)"):
    """Pull a UUID from nlm output. nlm >=0.9 emits JSON (e.g. {"notebook_id": ...,
    "artifact_id": ...}); older 0.3.x emitted plain 'ID: <uuid>' text. Try the JSON
    keys first, then fall back to the legacy regex so both CLI versions work."""
    try:
        data = json.loads(out)
        if isinstance(data, dict):
            for k in json_keys:
                if data.get(k):
                    return str(data[k])
            # last resort: any value that looks like a uuid
            for v in data.values():
                if isinstance(v, str) and re.fullmatch(r"[a-f0-9-]{16,}", v):
                    return v
    except (json.JSONDecodeError, ValueError):
        pass
    m = re.search(regex, out)
    return m.group(1) if m else None

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

# ── Source discovery ──────────────────────────────────────────────────────────
# For DAILY mode: one digest, its linked summaries, today's social streams + tomorrow's
# morning slot (overnight catch).
# For WEEKLY mode: target date's digest plus the previous N digests (default 6, total 7),
# all their linked summaries, and all their social-stream files.

def parse_digest(digest_path: Path) -> tuple[list[Path], list[str]]:
    """Return (linked wiki summary paths, external Deep Dive URLs) for one digest."""
    text = digest_path.read_text(encoding="utf-8")
    summaries: list[Path] = []
    for m in re.finditer(r"\(\.\.\/\.\.\/([^)]+\.md)\)", text):
        rel = m.group(1)
        path = REPO_ROOT / "wiki" / rel
        if path.exists():
            summaries.append(path)

    urls: list[str] = []
    if cfg.get("include_external_urls_from_deep_dives", True):
        in_dd = False
        for line in text.splitlines():
            if line.startswith("## "):
                in_dd = (line.strip() == "## Deep Dives")
                continue
            if not in_dd:
                continue
            if line.startswith("**Links:**"):
                for um in re.finditer(r"\[([^\]]+)\]\((https?://[^)]+)\)", line):
                    label, url = um.group(1), um.group(2)
                    if "Wiki" in label or "nitter" in url:
                        continue
                    urls.append(url)
    return summaries, urls

# Build the list of digest dates to ingest.
if EPISODE_MODE == "weekly":
    lookback = cfg.get("weekly_lookback_days", 6)
    digest_dates = []
    for offset in range(lookback, -1, -1):  # oldest first
        d = (datetime.strptime(date_str, "%Y-%m-%d") - timedelta(days=offset)).strftime("%Y-%m-%d")
        ym = d[:7]
        p = REPO_ROOT / "wiki" / "daily-digest" / ym / f"{d}.md"
        if p.exists():
            digest_dates.append(d)
    print(f"Weekly source set: {len(digest_dates)} digest(s) — {digest_dates[0]} → {digest_dates[-1]}")
else:
    digest_dates = [date_str]
    # Catch-forward rule: if the immediately prior calendar day was a skip-day
    # (Sunday by default), it never got its own podcast. Pull its digest +
    # summaries + social-stream into today's source set so today's episode
    # covers Sunday's content. Walks backwards across consecutive skip-days
    # in case the schedule ever expands beyond just Sundays.
    skip_days = schedule.get("skip_days", [])
    cursor = datetime.strptime(date_str, "%Y-%m-%d") - timedelta(days=1)
    catch_forward = []
    while cursor.weekday() in skip_days:
        d = cursor.strftime("%Y-%m-%d")
        p = REPO_ROOT / "wiki" / "daily-digest" / d[:7] / f"{d}.md"
        if p.exists():
            catch_forward.insert(0, d)  # chronological order
        cursor -= timedelta(days=1)
    if catch_forward:
        print(f"Catch-forward: including prior skip-day(s) {', '.join(catch_forward)} in today's source set.")
        digest_dates = catch_forward + digest_dates

# Gather digests + summaries + URLs across all selected dates.
digest_paths: list[Path] = []
wiki_summary_paths: list[Path] = []
deep_dive_urls: list[str] = []
for d in digest_dates:
    p = REPO_ROOT / "wiki" / "daily-digest" / d[:7] / f"{d}.md"
    digest_paths.append(p)
    s, u = parse_digest(p)
    wiki_summary_paths.extend(s)
    deep_dive_urls.extend(u)
# dedup
wiki_summary_paths = sorted(set(wiki_summary_paths))
deep_dive_urls = list(dict.fromkeys(deep_dive_urls))

# Use target-date digest's text for downstream Substack-note extraction below.
digest_text = DIGEST_PATH.read_text(encoding="utf-8")

# Social-stream (Media Live) files — full window for the target podcast date(s).
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
    # For each digest date in our set, collect its 4 slots + daily rollup.
    for d in digest_dates:
        ss_dir = REPO_ROOT / "wiki" / "social-stream" / d[:7]
        if ss_dir.exists():
            social_stream_paths.extend(sorted(ss_dir.glob(f"{d}*.md")))

    # Next-day morning slot for the LATEST digest date — captures its overnight tail.
    tomorrow         = (datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow_ym      = tomorrow[:7]
    tomorrow_morning = REPO_ROOT / "wiki" / "social-stream" / tomorrow_ym / f"{tomorrow}-morning.md"
    if tomorrow_morning.exists():
        social_stream_paths.append(tomorrow_morning)
# dedup
social_stream_paths = sorted(set(social_stream_paths))

# Media Zone synthesis files (wiki/media-zone/YYYY-MM/YYYY-MM-DD.md). These carry
# the curated social + video + industry synthesis (saved-post/bookmark articles,
# YouTube signal, the optimization-lens framing) that the daily digest's Industry
# Pulse does not fully capture. Including them makes the podcast comprehensive
# across media, video, and industry, not just papers. One file per digest date.
media_zone_paths: list[Path] = []
if cfg.get("include_media_zone_files", True):
    for d in digest_dates:
        mz = REPO_ROOT / "wiki" / "media-zone" / d[:7] / f"{d}.md"
        if mz.exists():
            media_zone_paths.append(mz)
media_zone_paths = sorted(set(media_zone_paths))

print(f"\nSources discovered:")
print(f"  Digests:          {len(digest_paths)}")
print(f"  Wiki summaries:   {len(wiki_summary_paths)}")
print(f"  Social-stream:    {len(social_stream_paths)}")
print(f"  Media Zone:       {len(media_zone_paths)}")
print(f"  External URLs:    {len(deep_dive_urls)}")
TOTAL = (len(digest_paths) + len(wiki_summary_paths) + len(social_stream_paths)
         + len(media_zone_paths) + len(deep_dive_urls))
print(f"  TOTAL:            {TOTAL}")

if TOTAL > cfg["max_sources_per_notebook"]:
    print(f"WARN: source count {TOTAL} exceeds max {cfg['max_sources_per_notebook']}; trimming wiki summaries first.")
    while TOTAL > cfg["max_sources_per_notebook"] and wiki_summary_paths:
        wiki_summary_paths.pop()
        TOTAL -= 1
    # If still over, trim external URLs next (digests + social are essential).
    while TOTAL > cfg["max_sources_per_notebook"] and deep_dive_urls:
        deep_dive_urls.pop()
        TOTAL -= 1

# ── Create notebook ───────────────────────────────────────────────────────────

print("\nCreating notebook...")
title_suffix = "weekly review" if EPISODE_MODE == "weekly" else date_str
title = f"{cfg['show_name']} {date_str} ({title_suffix})" if EPISODE_MODE == "weekly" else f"{cfg['show_name']} {date_str}"
out = nlm("notebook", "create", title)
NOTEBOOK_ID = extract_id(out, "notebook_id", "id")
if not NOTEBOOK_ID:
    print(f"ERROR: couldn't parse notebook ID from:\n{out}")
    sys.exit(1)
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
for p in digest_paths:
    add_file_source(p, title_hint=f"Daily digest {p.stem}")
for p in media_zone_paths:
    add_file_source(p, title_hint=f"Media Zone {p.stem} (social + video + industry synthesis)")
for p in social_stream_paths:
    add_file_source(p)
for p in wiki_summary_paths:
    add_file_source(p)
add_url_sources(deep_dive_urls)

# ── Generate audio ─────────────────────────────────────────────────────────────

# Pick the right focus prompt for this episode mode.
focus_key = "focus_prompt_weekly" if EPISODE_MODE == "weekly" else "focus_prompt_daily"
focus_prompt = cfg.get(focus_key) or cfg.get("focus_prompt")  # fallback to legacy field
if not focus_prompt:
    print(f"ERROR: no focus prompt found in config (looked for '{focus_key}' and 'focus_prompt').")
    sys.exit(1)

print(f"\nKicking off audio generation ({EPISODE_MODE} mode)...")
out = nlm("audio", "create", NOTEBOOK_ID,
          "--format", cfg["audio_format"],
          "--length", cfg["audio_length"],
          "--focus", focus_prompt,
          "--confirm")
ARTIFACT_ID = extract_id(out, "artifact_id", "id", regex=r"Artifact ID:\s*([a-f0-9-]+)")
if not ARTIFACT_ID:
    print(f"ERROR: couldn't parse artifact ID from:\n{out}")
    sys.exit(1)
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
note.append(f"🎧 Audio attached. Full digest: [{date_str}](https://bayesiansapien.github.io/cere-bro/digests/{date_str}/)")
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


# ── Upload audio to GitHub Release (hardened) ─────────────────────────────────
# The /radio page on the Astro site links to audio via GitHub Releases:
#   github.com/<user>/<repo>/releases/download/podcasts-YYYY-MM/YYYY-MM-DD.m4a
# Episodes are grouped by month, one release tag per month. Idempotent —
# `gh release upload` with --clobber overwrites in case of re-runs.
#
# Hardening (added 2026-06-12 after a Jun 11 silent-failure incident):
#   - Up to 3 attempts with exponential backoff
#   - After each upload, VERIFY the asset is actually listed on the release
#     (gh release view --json assets). This catches the rare "exit code 0 but
#     asset didn't land" mode that left 2026-06-10.m4a orphaned.
#   - On persistent failure, call notify.py (banner + Gmail) AND exit non-zero
#     so the cron's outer wrapper sees the failure and reports it.
#   - Audio URL is derived from `gh repo view` rather than hardcoded.

def _gh_repo_slug():
    """Return 'owner/repo' for the current git checkout via gh CLI."""
    try:
        r = subprocess.run(
            ["gh", "repo", "view", "--json", "owner,name",
             "-q", ".owner.login + \"/\" + .name"],
            capture_output=True, text=True, timeout=15,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except Exception:
        pass
    return None

def _asset_present_on_release(release_tag: str, asset_name: str) -> bool:
    """Authoritative check: does `gh release view` list this asset?"""
    try:
        r = subprocess.run(
            ["gh", "release", "view", release_tag,
             "--json", "assets", "-q", ".assets[].name"],
            capture_output=True, text=True, timeout=30,
        )
        if r.returncode != 0:
            return False
        return asset_name in [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]
    except Exception:
        return False

def _notify_failure(subject: str, body: str):
    """Fire-and-forget notify; never raises."""
    notify_script = REPO_ROOT / "connectors" / "notify" / "notify.py"
    if not notify_script.exists():
        return
    try:
        subprocess.run(["python3", str(notify_script), subject, body],
                       capture_output=True, text=True, timeout=30)
    except Exception:
        pass

def upload_audio_with_retry(release_tag: str, audio_path: Path,
                            max_attempts: int = 3) -> bool:
    """Upload + verify. Returns True only when the asset is confirmed listed
    on the release after upload. Retries with exponential backoff. Calls
    notify.py on persistent failure."""
    asset_name = audio_path.name
    repo_slug = _gh_repo_slug() or "bayesiansapien/cere-bro"
    public_url = f"https://github.com/{repo_slug}/releases/download/{release_tag}/{asset_name}"

    # Ensure the release tag exists (idempotent).
    check = subprocess.run(["gh", "release", "view", release_tag],
                           capture_output=True, text=True)
    if check.returncode != 0:
        print(f"  Release {release_tag} does not exist — creating it.")
        create = subprocess.run(
            ["gh", "release", "create", release_tag,
             "--title", f"{cfg['show_name']} — {release_tag.replace('podcasts-', '')} episodes",
             "--notes", f"Audio assets for {cfg['show_name']} episodes published in {release_tag.replace('podcasts-', '')}."],
            capture_output=True, text=True,
        )
        if create.returncode != 0:
            print(f"  ERROR: failed to create release {release_tag}: {create.stderr.strip()[:200]}")
            _notify_failure(
                f"Podcast upload — release create failed ({date_str})",
                f"Could not create GitHub release {release_tag}.\n\nstderr:\n{create.stderr.strip()[:500]}",
            )
            return False

    backoff = [0, 15, 45]  # seconds to wait BEFORE each attempt
    for attempt in range(1, max_attempts + 1):
        if backoff[attempt - 1] > 0:
            print(f"  Backing off {backoff[attempt - 1]}s before attempt {attempt}...")
            time.sleep(backoff[attempt - 1])
        print(f"  Attempt {attempt}/{max_attempts}: uploading {asset_name}...")
        up = subprocess.run(
            ["gh", "release", "upload", release_tag, str(audio_path), "--clobber"],
            capture_output=True, text=True, timeout=600,
        )
        if up.returncode != 0:
            print(f"  Attempt {attempt}: gh upload exit {up.returncode}: {up.stderr.strip()[:200]}")
            continue

        # Upload claimed success — VERIFY the asset is actually listed.
        # The rare failure mode (silent on Jun 11) returns 0 but asset never lands.
        time.sleep(3)  # GH backend needs a moment to register the asset
        if _asset_present_on_release(release_tag, asset_name):
            print(f"  ✓ Uploaded + verified: {asset_name} listed on {release_tag}")
            print(f"  ✓ Audio URL: {public_url}")
            return True
        print(f"  Attempt {attempt}: upload returned 0 but asset NOT listed on release; retrying")

    # All attempts exhausted.
    _notify_failure(
        f"Podcast audio upload FAILED ({date_str})",
        (f"After {max_attempts} attempts, {asset_name} was not present on "
         f"GitHub Release {release_tag}.\n\n"
         f"The local m4a is at:\n  {audio_path}\n\n"
         f"To recover manually:\n"
         f"  gh release upload {release_tag} {audio_path} --clobber\n\n"
         f"Then bump the GUID for {date_str} in site/src/pages/podcast.xml.ts so Spotify refetches."),
    )
    return False

print("\nUploading audio to GitHub Release (with retry + verify)...")
RELEASE_TAG = f"podcasts-{date_str[:7]}"
UPLOAD_OK = False
try:
    UPLOAD_OK = upload_audio_with_retry(RELEASE_TAG, AUDIO_PATH)
except FileNotFoundError:
    print("  WARN: gh CLI not installed — skipping audio upload. Episode .html is committed; audio stays local-only.")
    _notify_failure(
        f"Podcast upload skipped — gh CLI missing ({date_str})",
        f"The `gh` CLI is not on PATH. Audio at {AUDIO_PATH} did not reach GitHub Releases.",
    )
except Exception as e:
    print(f"  ERROR: unexpected upload error: {e}")
    _notify_failure(
        f"Podcast upload error ({date_str})",
        f"Unexpected exception during upload:\n{e}\n\nLocal audio: {AUDIO_PATH}",
    )

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

# Defense-in-depth: if the upload step failed persistently, exit non-zero so
# the cron's outer `|| notify` wrapper catches it as a second-layer alert.
# The html note + local m4a are still on disk, so a re-run with --force will
# replay generation and upload cleanly.
if not UPLOAD_OK:
    print(f"  ✗ Audio upload to GitHub Release FAILED — see notify alerts.")
    sys.exit(2)
