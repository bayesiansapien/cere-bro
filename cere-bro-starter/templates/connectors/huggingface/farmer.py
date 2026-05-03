"""
HuggingFace Daily Papers Farmer for cere-bro.

Fetches today's papers from HuggingFace Daily Papers and writes
individual markdown files to raw/huggingface/YYYY-MM-DD-<slug>.md

HuggingFace Daily Papers page: https://huggingface.co/papers

Usage:
    python connectors/huggingface/farmer.py              # today
    python connectors/huggingface/farmer.py --date 2026-05-01
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Missing dependencies. Run: pip install -r connectors/huggingface/requirements.txt")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent.parent
RAW_OUTPUT_DIR = REPO_ROOT / "raw" / "huggingface"
HF_PAPERS_URL = "https://huggingface.co/papers"


def slugify(title, max_len=50):
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    return slug[:max_len].rstrip("-")


def fetch_papers(date):
    """Fetch papers from HuggingFace Daily Papers for a given date."""
    url = f"{HF_PAPERS_URL}?date={date}"
    print(f"Fetching: {url}")

    try:
        resp = requests.get(url, timeout=30, headers={"User-Agent": "cere-bro-farmer/1.0"})
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    soup = BeautifulSoup(resp.text, "html.parser")
    papers = []

    # HuggingFace paper cards — selector may need updating if HF changes their layout
    for card in soup.select("article"):
        title_el = card.select_one("h3") or card.select_one("h2")
        if not title_el:
            continue
        title = title_el.get_text(strip=True)
        if not title:
            continue

        link_el = card.select_one("a[href*='/papers/']")
        paper_id = ""
        arxiv_url = ""
        if link_el:
            href = link_el.get("href", "")
            paper_id = href.split("/papers/")[-1].split("?")[0]
            if re.match(r"^\d{4}\.\d{4,5}", paper_id):
                arxiv_url = f"https://arxiv.org/abs/{paper_id}"

        abstract_el = card.select_one("p")
        abstract = abstract_el.get_text(strip=True) if abstract_el else ""

        upvotes_el = card.select_one("[class*='upvote']") or card.select_one("button")
        upvotes = ""
        if upvotes_el:
            m = re.search(r"(\d+)", upvotes_el.get_text())
            upvotes = m.group(1) if m else ""

        papers.append({
            "title": title,
            "paper_id": paper_id,
            "arxiv_url": arxiv_url,
            "hf_url": f"https://huggingface.co/papers/{paper_id}" if paper_id else "",
            "abstract": abstract,
            "upvotes": upvotes,
        })

    return papers


def write_paper_file(paper, date):
    """Write a single paper to raw/huggingface/YYYY-MM-DD-<slug>.md"""
    RAW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    slug = slugify(paper["title"])
    output_path = RAW_OUTPUT_DIR / f"{date}-{slug}.md"

    lines = [
        "---",
        "source: farmer/huggingface",
        f"date: {date}",
        f"paper_id: {paper['paper_id']}",
        "---",
        "",
        f"# {paper['title']}",
        "",
    ]

    if paper["arxiv_url"]:
        lines.append(f"**arXiv:** {paper['arxiv_url']}")
    if paper["hf_url"]:
        lines.append(f"**HuggingFace:** {paper['hf_url']}")
    if paper["upvotes"]:
        lines.append(f"**Upvotes:** {paper['upvotes']}")

    lines += [
        "",
        "## Abstract",
        "",
        paper["abstract"] or "(abstract not available)",
        "",
    ]

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Fetch HuggingFace Daily Papers into raw/huggingface/")
    parser.add_argument("--date", type=str, default=None)
    args = parser.parse_args()

    date = args.date or datetime.now().strftime("%Y-%m-%d")
    papers = fetch_papers(date)

    if not papers:
        print(f"No papers found for {date}. Check the URL or try a different date.")
        sys.exit(0)

    print(f"Found {len(papers)} papers for {date}.")
    for paper in papers:
        path = write_paper_file(paper, date)
        print(f"  → {path.name}")

    print(f"\nDone. {len(papers)} files written to raw/huggingface/")


if __name__ == "__main__":
    main()
