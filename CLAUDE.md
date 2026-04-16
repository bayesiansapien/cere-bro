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

**Daily digest** (`wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md`) — one file per day, structured as a newsletter. Written for the reader, not as a log. See the Daily Digest section below for the full format and writing rules.

---

## Lint

Run periodically (or on request):

- Flag concept pages with claims contradicted by newer sources
- Find orphan summary pages with no links to any concept page
- Identify concepts mentioned in ≥3 sources but lacking their own page
- Check index.md for missing or stale entries
- Suggest sources or topics worth investigating next

---

## Daily Digest

The daily digest is the most important output of the wiki. The reader (Amit) reads this first every morning to decide what to dig into. It must be worth reading on its own — not a table of contents.

### Format: `wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md`

```
# cere-bro | YYYY-MM-DD

> One-sentence framing of today's theme or the most interesting tension in today's batch.

---

## The Big Picture

2–3 paragraphs connecting today's sources into a coherent narrative. What thread runs through the day? Are multiple papers attacking the same problem from different angles? Does a blog post contradict or validate a paper? What does today's batch say about where the field is heading? Write this like the opening of a good newsletter — lead with the most interesting observation, not a summary.

---

## Deep Dives

One section per source worth reading in depth. Not every source needs one — skip routine releases (changelogs, minor updates). Focus on the 5–8 most substantive pieces.

### [Paper/Post Title]
**Source:** huggingface / rss/interconnects-ai / etc. | **Date:** YYYY-MM-DD

2–4 paragraphs. Cover: what they did, why it matters, what's surprising or counterintuitive, what it implies for the field. Don't just restate the abstract — add interpretation. End each section with a **"Why it matters"** line.

Link to wiki summary page if one exists.

---

## Connecting the Dots

A section that only appears when ≥2 sources are clearly related. Explicitly draw the connection: "Both UI-Copilot and TREX are attacking the same problem from different sides — the former in GUI execution, the latter in training automation. Together they sketch an emerging picture of fully automated AI workflows..." This is the most valuable part of the digest.

---

## Worth Watching

2–4 bullet points on implications, open questions, or things to follow up on. Not summaries — observations and predictions.

---

## Quick Hits

One-paragraph entries for minor but notable items that don't warrant a deep dive. Changelog items, brief quotes, small papers.

---

*Sources ingested today: N | Wiki pages updated: N*
```

### Writing rules

- **Write for curiosity, not completeness.** If a paper is boring, say so briefly and move on. If it's fascinating, give it space.
- **Connect before you summarize.** The Big Picture and Connecting the Dots sections are the unique value — any reader can get a summary from the abstract. What they can't get is synthesis.
- **Be opinionated.** "This is the third paper this week showing that benchmark scores don't capture robustness — there's clearly a measurement problem brewing." That kind of observation is what makes a digest worth reading.
- **Chronological storytelling where it applies.** If today's sources build on each other, say so explicitly.
- **Skip the boring stuff.** Simon Willison's datasette changelog doesn't need a deep dive. Marcus on AI ranting about hype gets a sentence.
- **Future implications.** End the digest with what to watch — not vague "this is important" but specific "if DSRL's pre-train RL approach generalizes to non-math tasks, it could replace standard RLVR by Q3."

---

## Conventions

- Dates: `YYYY-MM-DD` everywhere
- Filenames: lowercase, hyphens, no spaces
- Internal links: relative markdown links (`../agents-tool-use/tool-calling.md`)
- Source attribution: every summary page links to its raw file
- log.md entries start with `## [YYYY-MM-DD]` for easy grep
