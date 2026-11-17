#!/usr/bin/env python3
"""
Tag every wiki summary page with 1-3 fine-grained research themes for the Atlas.

Themes live in taxonomy.json; tags are stored in tags.json ({"<wiki-relative path>": ["theme-id", ...]}).
Only untagged pages are sent to the model, so the daily run is cheap. Classification uses
`claude -p` with a small model over each page's title + TL;DR, in batches.

Run: python3 connectors/themes/tag.py            # tag new pages
     python3 connectors/themes/tag.py --retag    # re-classify everything (after editing the taxonomy)
     python3 connectors/themes/tag.py --dry-run  # show what would be tagged
"""

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent
WIKI = REPO / "wiki"
TAX = json.loads((HERE / "taxonomy.json").read_text())["themes"]
TAGS_FILE = HERE / "tags.json"
SKIP_DIRS = {"daily-digest", "media-zone", "social-stream"}
BATCH, WORKERS, MODEL = 40, 4, "haiku"
IDS = {t["id"] for t in TAX}


def pages():
    for p in sorted(WIKI.glob("*/20*.md")):
        if p.parent.name not in SKIP_DIRS:
            yield p.relative_to(WIKI).as_posix()


def gist(rel):
    """Title + the first ~600 chars of the TL;DR (or body) of a summary page."""
    md = (WIKI / rel).read_text(errors="ignore")
    md = re.sub(r"(?s)^---.*?---\n", "", md)
    title = (re.search(r"(?m)^# (.+)$", md) or [None, rel])[1]
    tldr = md.split("## TL;DR", 1)[1] if "## TL;DR" in md else md
    tldr = re.sub(r"<[^>]+>|```.*?```|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", tldr, flags=re.S)
    return f"{title.strip()} :: {' '.join(tldr.split())[:600]}"


def classify(batch):
    menu = "\n".join(f"- {t['id']}: {t['desc']}" for t in TAX)
    items = "\n".join(f"{i}. [{rel.split('/')[0]}] {gist(rel)}" for i, rel in enumerate(batch))
    prompt = (
        "Assign each AI research item 1 to 3 theme ids from this list, most specific first. "
        "Use only ids from the list. Prefer the specific efficiency/routing/hardware themes when they fit.\n\n"
        f"THEMES:\n{menu}\n\nITEMS (index. [folder] title :: summary):\n{items}\n\n"
        'Reply with JSON only: {"0": ["id", ...], "1": [...], ...}'
    )
    r = subprocess.run(["claude", "-p", "--model", MODEL], input=prompt, capture_output=True, text=True, timeout=600)
    m = re.search(r"\{.*\}", r.stdout, re.S)
    if not m:
        print(f"  batch failed: {r.stderr.strip()[:200] or r.stdout.strip()[:200]}")
        return {}
    out = {}
    for k, v in json.loads(m.group(0)).items():
        ids = [x for x in v if x in IDS][:3]
        if k.isdigit() and int(k) < len(batch) and ids:
            out[batch[int(k)]] = ids
    return out


def main():
    retag, dry = "--retag" in sys.argv, "--dry-run" in sys.argv
    tags = {} if retag or not TAGS_FILE.exists() else json.loads(TAGS_FILE.read_text())
    todo = [p for p in pages() if p not in tags]
    print(f"themes: {len(todo)} page(s) to tag, {len(tags)} already tagged")
    if dry or not todo:
        return 0
    batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
    with ThreadPoolExecutor(WORKERS) as ex:
        for n, res in enumerate(ex.map(classify, batches), 1):
            tags.update(res)
            TAGS_FILE.write_text(json.dumps(dict(sorted(tags.items())), indent=0))
            print(f"  batch {n}/{len(batches)}: {len(res)} tagged")
    left = len([p for p in pages() if p not in tags])
    print(f"themes: done, {len(tags)} tagged, {left} still untagged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
