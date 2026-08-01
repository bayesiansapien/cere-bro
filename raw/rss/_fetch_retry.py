import feedparser, os, re, json
from datetime import datetime, timezone

RAW_DIR = "/Users/amitsinghbhatti/Code/cere-bro/raw/rss"
FLOOR = datetime(2026, 7, 31, 0, 0, 0, tzinfo=timezone.utc)

SOURCES = {
    "venturebeat-ai": "/tmp/vb.xml",
    "the-information": "/tmp/info.xml",
}

existing_slugs = set(f for f in os.listdir(RAW_DIR) if f.endswith(".md"))

def slugify(title, maxlen=55):
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:maxlen].rstrip("-")

written = []
skipped = []

for feed_key, path in SOURCES.items():
    d = feedparser.parse(path)
    for entry in d.entries:
        pub_struct = entry.get("published_parsed") or entry.get("updated_parsed")
        if not pub_struct:
            continue
        pub_dt = datetime(*pub_struct[:6], tzinfo=timezone.utc)
        if pub_dt < FLOOR:
            continue
        pub_date_str = pub_dt.strftime("%Y-%m-%d")
        title = entry.get("title", "untitled")
        slug = slugify(title)
        fname = f"{pub_date_str}-{feed_key}-{slug}.md"
        fpath = os.path.join(RAW_DIR, fname)
        if fname in existing_slugs or os.path.exists(fpath):
            skipped.append(fname)
            continue

        url_link = entry.get("link", "")
        author = entry.get("author", "")
        content = ""
        if "content" in entry and entry["content"]:
            content = entry["content"][0].get("value", "")
        elif "summary" in entry:
            content = entry["summary"]
        farmed_ts = datetime.now(timezone.utc).isoformat()

        fm = "---\n"
        fm += "source: farmer/rss\n"
        fm += f"feed: {feed_key}\n"
        fm += f"farmed: {farmed_ts}\n"
        fm += f"title: {title}\n"
        fm += f"url: {url_link}\n"
        fm += f"published: {pub_date_str}\n"
        if author:
            fm += f"author: {author}\n"
        fm += "---\n\n"

        body = f"# {title}\n\n{content}\n"

        with open(fpath, "w", encoding="utf-8") as out:
            out.write(fm + body)

        existing_slugs.add(fname)
        written.append(fpath)

print(json.dumps({"written": written, "skipped": skipped}, indent=2))
