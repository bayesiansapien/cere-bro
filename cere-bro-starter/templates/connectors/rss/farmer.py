"""
RSS Feed Farmer for cere-bro.

Reads a list of RSS feed URLs from feeds.txt and writes each feed's
recent entries to raw/rss/YYYY-MM-DD-<feed-name>.md

Usage:
    python connectors/rss/farmer.py              # today
    python connectors/rss/farmer.py --hours 48   # last 48 hours
    python connectors/rss/farmer.py --date 2026-05-01
"""

import argparse
import hashlib
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import feedparser
except ImportError:
    print("ERROR: feedparser not installed. Run: pip install -r connectors/rss/requirements.txt")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent.parent
RAW_OUTPUT_DIR = REPO_ROOT / "raw" / "rss"
FEEDS_FILE = Path(__file__).parent / "feeds.txt"


def load_feeds():
    """Load feed URLs from feeds.txt. Lines starting with # are comments."""
    if not FEEDS_FILE.exists():
        print(f"ERROR: {FEEDS_FILE} not found. Create it with one RSS URL per line.")
        sys.exit(1)
    feeds = []
    for line in FEEDS_FILE.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            feeds.append(line)
    return feeds


def feed_slug(url):
    """Create a short filename-safe identifier from a feed URL."""
    domain = re.sub(r"https?://", "", url).split("/")[0]
    domain = re.sub(r"[^a-z0-9]", "-", domain.lower())
    return domain[:30]


def clean_html(text):
    """Strip basic HTML tags for plain text output."""
    text = re.sub(r"<[^>]+>", "", text or "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch_feed(url, since_dt):
    """Fetch entries from a single RSS/Atom feed published after since_dt."""
    try:
        d = feedparser.parse(url)
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return []

    entries = []
    for entry in d.entries:
        # Parse published date
        pub = None
        for date_field in ("published_parsed", "updated_parsed"):
            if hasattr(entry, date_field) and getattr(entry, date_field):
                import calendar
                t = getattr(entry, date_field)
                pub = datetime.fromtimestamp(calendar.timegm(t), tz=timezone.utc)
                break

        if pub and pub < since_dt:
            continue

        title = entry.get("title", "(no title)")
        link = entry.get("link", "")
        summary = clean_html(entry.get("summary", entry.get("description", "")))
        if len(summary) > 3000:
            summary = summary[:3000] + f"\n\n[truncated — {len(summary) - 3000} chars omitted]"

        entries.append({
            "title": title,
            "link": link,
            "published": pub.strftime("%Y-%m-%d %H:%M UTC") if pub else "unknown",
            "summary": summary,
        })

    return entries


def write_raw_file(entries, feed_url, slug, target_date):
    """Write feed entries to raw/rss/YYYY-MM-DD-<slug>.md"""
    RAW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RAW_OUTPUT_DIR / f"{target_date}-{slug}.md"

    lines = [
        "---",
        "source: farmer/rss",
        f"feed: {feed_url}",
        f"date: {target_date}",
        f"entry_count: {len(entries)}",
        "---",
        "",
        f"# RSS: {slug} — {target_date}",
        "",
        f"*{len(entries)} entries from `{feed_url}`*",
        "",
    ]

    for i, entry in enumerate(entries, 1):
        lines += [
            "---",
            "",
            f"## {i}. {entry['title']}",
            "",
            f"**Published:** {entry['published']}  ",
            f"**Link:** [{entry['link']}]({entry['link']})",
            "",
            entry["summary"] or "(no summary)",
            "",
        ]

    if not entries:
        lines += ["*No new entries found for this period.*", ""]

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Fetch RSS feeds into raw/rss/")
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--date", type=str, default=None)
    args = parser.parse_args()

    target_date = args.date or datetime.now().strftime("%Y-%m-%d")
    since_dt = datetime.now(timezone.utc) - timedelta(hours=args.hours)

    feeds = load_feeds()
    print(f"Fetching {len(feeds)} feeds since {since_dt.strftime('%Y-%m-%d %H:%M UTC')}...")

    total_entries = 0
    for url in feeds:
        slug = feed_slug(url)
        print(f"  {slug} ({url})")
        entries = fetch_feed(url, since_dt)
        if entries:
            path = write_raw_file(entries, url, slug, target_date)
            print(f"    → {len(entries)} entries → {path.name}")
            total_entries += len(entries)
        else:
            print(f"    → 0 entries (nothing new)")

    print(f"\nDone. {total_entries} total entries across {len(feeds)} feeds.")


if __name__ == "__main__":
    main()
