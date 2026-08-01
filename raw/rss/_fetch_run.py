import feedparser, os, re, json
from datetime import datetime, timezone, timedelta

FEEDS = {
    "tldr-ai":              "https://tldr.tech/api/rss/ai",
    "the-decoder":          "https://the-decoder.com/feed/",
    "venturebeat-ai":       "https://venturebeat.com/category/ai/feed/",
    "ai-snake-oil":         "https://aisnakeoil.substack.com/feed",
    "the-information":      "https://www.theinformation.com/feed",
    "agentic-ai":           "https://kenhuangus.substack.com/feed",
    "ahead-of-ai":          "https://magazine.sebastianraschka.com/feed",
    "ai-research-strategy": "https://deliprao.substack.com/feed",
    "ai-safety-china":      "https://aisafetychina.substack.com/feed",
    "ai-safety-newsletter": "https://newsletter.safe.ai/feed",
    "ai-tidbits":           "https://www.aitidbits.ai/feed",
    "ai-guide-humans":      "https://aiguide.substack.com/feed",
    "algorithmic-bridge":   "https://www.thealgorithmicbridge.com/feed",
    "amit-chaudhary":       "https://amitness.substack.com/feed",
    "breaking-stagnation":  "https://marksaroufim.substack.com/feed",
    "chinese-characteristics": "https://lillianli.substack.com/feed",
    "davis-summarizes":     "https://dblalock.substack.com/feed",
    "exploring-lms":        "https://newsletter.maartengrootendorst.com/feed",
    "fabricated-knowledge": "https://www.fabricatedknowledge.com/feed",
    "gradient-flow":        "https://gradientflow.substack.com/feed",
    "import-ai":            "https://importai.substack.com/feed",
    "interconnects-ai":     "https://www.interconnects.ai/feed",
    "language-models-co":   "https://newsletter.languagemodels.co/feed",
    "last-week-in-ai":      "https://lastweekin.ai/feed",
    "marcus-on-ai":         "https://garymarcus.substack.com/feed",
    "nlp-news":             "https://newsletter.ruder.io/feed",
    "pragmatic-engineer":   "https://newsletter.pragmaticengineer.com/feed",
    "the-gradient":         "https://thegradientpub.substack.com/feed",
    "huggingface-blog":     "https://huggingface.co/blog/feed.xml",
    "karpathy-blog":        "http://karpathy.github.io/feed.xml",
    "lilian-weng":          "https://lilianweng.github.io/index.xml",
    "simon-willison":       "https://simonwillison.net/atom/everything/",
    "semianalysis":         "https://newsletter.semianalysis.com/feed",
    "dair-ai":              "https://medium.com/feed/dair-ai",
}

RAW_DIR = "/Users/amitsinghbhatti/Code/cere-bro/raw/rss"
FLOOR = datetime(2026, 7, 31, 0, 0, 0, tzinfo=timezone.utc)

existing_slugs = set()
for f in os.listdir(RAW_DIR):
    if f.endswith(".md"):
        existing_slugs.add(f)

def slugify(title, maxlen=55):
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:maxlen].rstrip("-")

written = []
skipped = []
errors = []

for feed_key, url in FEEDS.items():
    try:
        d = feedparser.parse(url)
    except Exception as e:
        errors.append((feed_key, str(e)))
        continue
    if d.bozo and not d.entries:
        errors.append((feed_key, str(d.get("bozo_exception", "parse error, no entries"))))
        continue
    for entry in d.entries:
        # determine published date
        pub_struct = entry.get("published_parsed") or entry.get("updated_parsed")
        if not pub_struct:
            continue  # skip entries with no pub date
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

print(json.dumps({"written": written, "skipped": skipped, "errors": errors}, indent=2))
