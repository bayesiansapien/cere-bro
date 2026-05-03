# ingest

Processes one or more raw source files into the wiki. Reads new files from `raw/`, synthesizes them into summary pages and concept page updates, and maintains `index.md` and `log.md`.

---

## Instructions

When invoked, follow these steps exactly. Do not skip steps. Quality matters more than speed — a good ingest that connects to prior knowledge is worth 10x a rote summary.

---

### Step 0: Check that bootstrap has run

Verify that `CLAUDE.md` exists and is not the starter placeholder. If `wiki-config.json` does not exist, stop and tell the user to run `/bootstrap` first.

---

### Step 1: Find unprocessed raw files

Look in `raw/huggingface/`, `raw/rss/`, and `raw/gmail/` for files that have not yet been ingested.

Check `wiki/log.md` for previously ingested sources (entries have the format `## [YYYY-MM-DD] ingest | <title> | <source-type>`). Any raw file not mentioned in the log is unprocessed.

If the user specified a particular file or date as an argument, process that. Otherwise, ask:
> "I found these unprocessed files: [list]. Process all of them, or a specific one?"

Ingest one source at a time. Batch ingests are fine but log each separately.

---

### Step 2: Consult the knowledge base first

Before reading the new source, warm up your context:

1. **Read the relevant concept pages** — find `wiki/<topic>/<concept>.md` for the topic areas this source touches. These compress all prior knowledge into one page.

2. **Scan the last 5–7 daily digests** — look for "Worth Watching" bullets or open questions that today's source might address. Check `wiki/daily-digest/YYYY-MM/` for the most recent files.

3. **Read directly related prior summaries** when the source is in a narrow area you've covered recently (same method family, same benchmark, same problem). The concept page will point you to these.

This is not optional. A summary written without prior context is just a restatement of the abstract.

---

### Step 3: Read the source

Read the full raw file. For papers: abstract + key sections + figures. For videos: transcript. For blogs/newsletters: full text.

Note: raw files may contain multiple sources (especially RSS and Gmail). Process each source within the file as a separate ingest pass.

---

### Step 4: Determine topic and tier

Use `wiki-config.json` to classify this source:
- Which wiki topic does it belong to? (Match to a `key` in the topics array)
- What tier is that topic? (Drives depth of the summary)

If it spans multiple topics, classify it at the highest-tier applicable topic.

---

### Step 5: Write the summary page

Write to `wiki/<topic-key>/<YYYY-MM-DD>-<slug>.md`.

**Slug**: lowercase, hyphens, 3–5 words from the title. E.g. `2026-05-01-flash-attention-3.md`

**Required sections:**

```markdown
# <Title>

> <One-sentence TL;DR — the most important claim or finding>

**Source:** <type: HuggingFace / RSS / Gmail / Manual>  
**Raw:** [<filename>](../../../raw/<subdir>/<filename>)  
**Date:** YYYY-MM-DD  
**Tier:** <N>

## TL;DR

<1–2 sentence summary. Lead with the most important finding, not background context.>

## Key points

<Bullet list of the 3–7 most substantive claims. Each bullet should be a complete thought, not a fragment.>

## Mechanism

<For Tier 1 and 2 topics: explain HOW it works, not just WHAT it achieves. This is the section that ages well — abstracts don't explain mechanism, but this wiki should.>

## Connections to prior work

<MANDATORY. Name prior pages in this wiki that this source confirms, contradicts, extends, or fills a gap in. Use relative markdown links. If this is the first source on this topic, say so explicitly.>

- Confirms: [<title>](../path/to/page.md) — <one line on the shared claim>
- Contradicts: [<title>](../path/to/page.md) — <one line on the tension>
- Extends: [<title>](../path/to/page.md) — <one line on what's new>
- Gap filled: <what prior work opened this question and where>

## Open questions

<For Tier 1: what does this paper NOT solve? What would a follow-up need to address? What's the falsifiable prediction from this work?>

## Links

- [Source paper/post](<url>)
- [Wiki page](../../<topic>/<concept>.md)
```

Depth calibration by tier:
- **Tier 1**: 400–700 words. Full mechanism section. Explicit open questions. Research angle.
- **Tier 2**: 200–400 words. Mechanism summary. Flag any Tier 1 intersection.
- **Tier 3**: 100–200 words. TL;DR and key points only.
- **Tier 4**: 1–3 sentences. No separate page — just a log entry.

---

### Step 6: Update concept pages

For every topic significantly discussed in the source, update its concept page at `wiki/<topic-key>/<concept-name>.md`.

A concept page should always reflect the *current state of knowledge* — not a history of what arrived when.

**What to add:**
- New evidence for or against an existing claim
- A new method or result that changes the picture
- A contradiction (flag it — don't resolve it unless the evidence is clear)
- A new open question the field is grappling with
- Cross-paper patterns when ≥3 sources converge on the same finding

**What NOT to do:**
- Do not append "as of [date], paper X showed..." in a list format
- Do not simply describe what each paper did — synthesize across them
- If the concept page is getting long, consolidate. Prior evidence can be compressed; current state should be clear.

If a concept page does not exist yet for a Tier 1 topic this source touches: create it.

---

### Step 7: Surface cross-paper patterns (Connecting the Dots)

After reading the source and looking at prior pages: are there patterns forming?

Check for:
- **Confirmation**: is this the 2nd or 3rd paper in the wiki making the same claim? Name it explicitly.
- **Contradiction**: does this paper conflict with a prior one? Name both, state the specific disagreement, leave it unresolved.
- **Gap-filling**: does this solve an open question raised in a prior summary or digest? Name the question and the prior source.
- **N-of-a-kind**: ≥3 papers making the same architectural choice or claim is a pattern — declare it.

Write these observations into the Connections section of the summary page, and flag the most important ones in a short "Patterns to note" block if they warrant attention in the next digest.

---

### Step 8: Update index.md

Add the new summary page to `wiki/index.md` with a one-line description:

```markdown
- [<YYYY-MM-DD> — <Title>](<relative-path>.md) — <one-line description>
```

Group by topic. Keep it in reverse-chronological order within each group.

---

### Step 9: Append to log.md

```markdown
## [YYYY-MM-DD] ingest | <Title> | <source-type>

- Summary: [<Title>](<relative path>)
- Concept pages updated: <list>
- Patterns flagged: <any cross-paper patterns noted, or "none">
```

---

### After all sources are ingested

Tell the user:
- How many sources were processed
- Which concept pages were updated
- Any cross-paper patterns flagged
- Whether any Tier 1 topics now have ≥3 sources without a concept page (potential gap)

Remind: "Run /digest to write today's digest incorporating these ingests."
