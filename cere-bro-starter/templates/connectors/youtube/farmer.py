#!/usr/bin/env python3
"""
YouTube farmer for the cere-bro social-media agent.

Reads the reader's curated AI channel list (channels.json) and fetches each
channel's public RSS feed (https://www.youtube.com/feeds/videos.xml?channel_id=…).
RSS is a stable, auth-free interface that carries recent videos plus view counts
and star-rating, so we get engagement signal without yt-dlp or the API. Robust by
design: per-channel failures are skipped; the feed shape is stable.

Captures recent videos (last `lookback_days`) with: channel, title, video URL,
published time, description, views, rating. Output goes to raw/youtube/ (public —
this is curated channel content, not a personal algorithmic feed).

Run:  python3 connectors/youtube/farmer.py [--force]
"""

import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parents[2]
HERE      = Path(__file__).parent
CONFIG    = json.loads((HERE / "config.json").read_text())
RAW_DIR   = REPO_ROOT / "raw" / "youtube"
RAW_DIR.mkdir(parents=True, exist_ok=True)

ENABLED   = CONFIG.get("enabled", True)
LOOKBACK  = CONFIG.get("lookback_days", 3)
MAXVID    = CONFIG.get("max_videos_per_channel", 4)
TIMEOUT   = CONFIG.get("request_timeout", 8)
CHANNELS  = json.loads((HERE / CONFIG.get("channels_file", "channels.json")).read_text())

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")
now_utc  = datetime.now(timezone.utc)
now_ist  = now_utc + timedelta(hours=5, minutes=30)
date_str = now_ist.strftime("%Y-%m-%d")
cutoff   = now_utc - timedelta(days=LOOKBACK)

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt":   "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}


def fetch_channel(ch: dict) -> list:
    cid = ch.get("channel_id")
    if not cid:
        return []
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=TIMEOUT)
        if r.status_code != 200:
            return []
        root = ET.fromstring(r.text)
    except Exception:
        return []
    vids = []
    for entry in root.findall("atom:entry", NS)[:MAXVID + 4]:
        vid = entry.findtext("yt:videoId", namespaces=NS) or ""
        title = (entry.findtext("atom:title", namespaces=NS) or "").strip()
        pub = entry.findtext("atom:published", namespaces=NS) or ""
        try:
            pub_dt = datetime.fromisoformat(pub.replace("Z", "+00:00"))
        except Exception:
            pub_dt = None
        if pub_dt is None or pub_dt < cutoff:
            continue
        grp = entry.find("media:group", NS)
        desc = ""
        views = 0
        rating = 0.0
        if grp is not None:
            desc = (grp.findtext("media:description", namespaces=NS) or "").strip()
            comm = grp.find("media:community", NS)
            if comm is not None:
                st = comm.find("media:statistics", NS)
                if st is not None:
                    try:
                        views = int(st.get("views", "0"))
                    except ValueError:
                        views = 0
                sr = comm.find("media:starRating", NS)
                if sr is not None:
                    try:
                        rating = float(sr.get("average", "0"))
                    except ValueError:
                        rating = 0.0
        vids.append({
            "channel": ch.get("title", ""), "channel_id": cid,
            "title": title, "video_id": vid,
            "url": f"https://www.youtube.com/watch?v={vid}",
            "thumbnail": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
            "published_utc": pub_dt.isoformat(),
            "description": desc[:800], "views": views, "rating": rating,
        })
        if len([v for v in vids]) >= MAXVID:
            break
    return vids


def main() -> int:
    if not ENABLED:
        print("YouTube disabled in config — skipping.")
        return 0
    print(f"YouTube farmer | {date_str} | {len(CHANNELS)} channels | lookback {LOOKBACK}d")
    all_vids, ok, fail = [], 0, 0
    for ch in CHANNELS:
        vids = fetch_channel(ch)
        if vids:
            ok += 1
            all_vids.extend(vids)
        else:
            fail += 1
        time.sleep(0.15)  # be gentle
    # newest first
    all_vids.sort(key=lambda v: v["published_utc"], reverse=True)
    print(f"  channels reached: {ok} | empty/failed: {fail} | recent videos: {len(all_vids)}")

    out = {"date": date_str, "source": "youtube_subscriptions",
           "scraped_ist": now_ist.strftime("%Y-%m-%d %H:%M"),
           "lookback_days": LOOKBACK, "videos": all_vids}
    (RAW_DIR / f"{date_str}.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))

    md = [f"# YouTube (subscriptions) | {date_str}",
          f"> {len(all_vids)} videos from the last {LOOKBACK} days across {ok} channels.", "", "---", ""]
    for v in all_vids:
        md.append(f"**{v['channel']}** · {v['views']:,} views · ★{v['rating']:.2f}")
        md.append(f"### {v['title']}")
        if v["description"]:
            md.append(f"> {v['description'][:300]}")
        md.append(f"[watch]({v['url']}) · ![thumb]({v['thumbnail']})")
        md += ["", "---", ""]
    (RAW_DIR / f"{date_str}.md").write_text("\n".join(md))
    print(f"  Wrote raw/youtube/{date_str}.json + .md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
