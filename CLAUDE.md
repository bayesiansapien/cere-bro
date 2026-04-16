# cere-bro Wiki

A self-maintaining AI knowledge base fed daily from papers, blogs, YouTube, HuggingFace, and Twitter.
Pattern: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

---

## Architecture

```
raw/        ← immutable source files (farmers write here, humans drop files here)
wiki/       ← LLM-owned synthesis (you write everything here)
  llms-foundation-models/
  agents-tool-use/
  multimodal/
  inference-efficiency/
  ai-routing/
  daily-digest/
    YYYY-MM/
      YYYY-MM-DD.md  ← one newsletter per day
  index.md  ← catalog of every wiki page with one-line summaries
  log.md    ← append-only ingest + lint timeline
```

`raw/` is the source of truth. Never modify files there. `wiki/` is yours to write, update, and restructure freely.

Images: when a source has architecture diagrams or figures that matter, download them to `raw/assets/` and reference them from summary pages. Read text first, then view referenced images for additional context.

---

## Sources

Farmers pull from these daily:

| Source | Type | Notes |
|--------|------|-------|
| HuggingFace Daily Papers | Web/RSS | hf.co/papers — daily ML digest |
| arXiv | RSS | cs.AI, cs.LG, cs.CL category feeds |
| YouTube channels | local-cli (yt-dlp) | AI creators curated by user |
| Blogs / newsletters | RSS | Lilian Weng, Andrej Karpathy, Sebastian Raschka, etc. |
| Twitter | Web | AI researchers and labs the user follows |

---

## Ingest

When a new file lands in `raw/` (via farmer or manually dropped):

1. Read the source. For papers, read abstract + key sections; for videos, read the transcript; for blogs, read in full.
2. **Write a summary page** in the appropriate `wiki/<concept>/` subdirectory. Filename: `<YYYY-MM-DD>-<slug>.md`. Include: one-paragraph TL;DR, key findings or claims, links to related wiki pages, link back to the raw source.
3. **Update concept pages** — for every AI concept significantly discussed in the source, update or create `wiki/<concept>/<concept-name>.md`. Add what the source contributes: new evidence, a contradiction, a refinement.
4. **Write/update the daily digest** — write to `wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md`. This is a newsletter, not a log. See the Daily Digest section below for the full format.
5. **Update index.md** — add the new summary page with its one-line description.
6. **Append to log.md** — format: `## [YYYY-MM-DD] ingest | <title> | <source-type>`

Ingest one source at a time. A single source may touch 5–15 wiki pages. Always ingest all new raw files before the session ends.

---

## Page types

**Source summaries** (`wiki/<concept>/<date>-<slug>.md`) — one page per paper, video, or post. TL;DR, key points, figures if relevant, link to raw.

**Concept pages** (`wiki/<concept>/<concept-name>.md`) — one page per AI concept (e.g. "Mixture of Experts", "KV Cache", "Chain-of-Thought"). Synthesizes everything ingested so far. Updated every time a new source touches the concept.

**Daily digest** (`wiki/daily-digest.md`) — rolling log of what came in each day. One line per source under a date header. The pulse of the wiki.

---

## Lint

Run periodically (or on request):

- Flag concept pages with claims contradicted by newer sources
- Find orphan summary pages with no links to any concept page
- Identify concepts mentioned in ≥3 sources but lacking their own page
- Check index.md for missing or stale entries
- Suggest sources or topics worth investigating next

---

## Conventions

- Dates: `YYYY-MM-DD` everywhere
- Filenames: lowercase, hyphens, no spaces
- Internal links: relative markdown links (`../agents-tool-use/tool-calling.md`)
- Source attribution: every summary page links to its raw file
- log.md entries start with `## [YYYY-MM-DD]` for easy grep
