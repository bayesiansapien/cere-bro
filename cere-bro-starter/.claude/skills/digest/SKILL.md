# digest

Writes the daily digest for a given date. Reads all available raw sources, reads prior context from the wiki, and produces a newsletter-format digest at `wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md`.

---

## Instructions

When invoked, follow these steps in order.

---

### Step 0: Verify setup

Check that `CLAUDE.md` and `wiki-config.json` exist. If not, tell the user to run `/bootstrap` first.

Determine the target date. If the user provided a date argument (e.g. `/digest 2026-05-01`), use it. Otherwise, use today's date.

---

### Step 1: Collect ALL raw sources for the date

This step is mandatory. A digest written from partial sources is incomplete.

Check all SIX raw source directories for the target date:

1. `raw/gmail/<YYYY-MM-DD>-starred.md` — Gmail starred emails (newsletters, industry news)
2. `raw/rss/<YYYY-MM-DD>-*.md` — RSS feeds (blogs, TLDR AI, research blogs, etc.)
3. `raw/huggingface/<YYYY-MM-DD>-*.md` — HuggingFace Daily Papers
4. `raw/twitter/<YYYY-MM-DD>-*.{md,json}` — Twitter retweets (curated signal) + AI handle feed
5. `raw/kurate/<YYYY-MM-DD>-*.md` — Kurate weekly leaderboards (cs.AI + cs.LG) + rising-author tracking
6. `raw/reddit/<YYYY-MM-DD>-r-*.md` — curated AI subreddits (community-curated practitioner signal: what runs on consumer GPUs, real deployment patterns)

Read ALL files that exist for the date. If a directory has no file for the exact date, check for the nearest prior date (within 2 days). Note which sources are missing.

**Cross-source rule (mandatory) for HF + Kurate:** any paper appearing in BOTH today's HuggingFace top AND the current week's Kurate top-20 is HIGH CONVICTION. Surface it as Tier 1 in Deep Dives regardless of topic, label as "cross-source confirmed (HF + Kurate)". Papers in Kurate top-5 but missing from HF go in Worth Watching as "LLM-rated underrated". Use the inferred `tier=N` in each Kurate entry to weight space allocation.

**Rising authors (Kurate):** read `raw/kurate/<YYYY-MM-DD>-rising-authors.md` if present. Surface any authors who crossed the threshold in Worth Watching, naming each with one of their top papers and suggesting whether to add them to `connectors/twitter/config.json:ai_handles`.

**Deep Dive enrichment (alphaxiv):** for each Tier 1 / Tier 2 Deep Dive paper, run `python3 connectors/alphaxiv/enrich.py <arxiv_id>` to fetch alphaxiv.org's AI-generated overview (~3000 words). Use it as supplementary context. If empty, fall back to the abstract. Don't copy alphaxiv's prose verbatim — write the Deep Dive in your wiki's voice.

If none of the directories have files for the target date, tell the user and stop. Do not write an empty digest.

**Check the parallel daily digest** (if it exists): look for a daily-digest file in the user's Documents or a configured path. If the user mentioned where their parallel digest lives during bootstrap, check there. Merge any unique content.

---

### Step 2: Warm up with prior context

Before writing anything, read:

1. **Relevant concept pages** — for topics appearing in today's sources, read `wiki/<topic>/<concept>.md`. This tells you the current state of knowledge.

2. **Last 5–7 daily digests** — scan `wiki/daily-digest/YYYY-MM/` for recent files. Look specifically for:
   - "Worth Watching" bullets that today's sources might address
   - Open questions or tensions flagged in prior Big Picture sections
   - N-of-a-kind patterns that today adds to

A digest that ignores prior context is just a summary, not synthesis. The reader can get summaries from any newsletter. They come to this wiki for accumulated context.

---

### Step 3: Write the digest

Write to `wiki/daily-digest/<YYYY-MM>/<YYYY-MM-DD>.md`.

Use the reader's tier hierarchy from `CLAUDE.md` (or `wiki-config.json`) to calibrate depth:
- Tier 1 topics: 4–6 paragraph Deep Dives with mechanism + Research angle
- Tier 2 topics: 2–4 paragraph Deep Dives, flag Tier 1 intersections
- Tier 3 topics: Quick Hits paragraph
- Tier 4 topics: one sentence or skip

---

## Required format

```markdown
# <Wiki Name> | <YYYY-MM-DD>

> <One-sentence framing of today's sharpest tension, surprise, or theme.>

---

## TL;DR

3–6 bullets. One line each. Tier 1 findings first, then most important industry item.

- **[Paper/concept]** — what it found, in one punchy clause
- ...

---

## The Big Picture

2–3 paragraphs. Lead with the most interesting observation, not a list of what arrived.
What thread runs through today's batch? Do multiple papers attack the same problem from
different angles? What does today say about where the field is heading?
Write like the opening of a good essay.

---

## Deep Dives

For each substantive source (Tier 1 and 2). 5–8 items. Skip changelogs, routine releases, minor updates.

---

### <Title>

> <One-line hook — most counterintuitive or surprising thing>

**Source:** <HuggingFace / Interconnects AI / TLDR AI / etc.>
**Links:** [Paper](<url>) · [Wiki](<relative path to summary page>)
**Tier:** <N> — <topic label>

[Include a visual block when it adds clarity:]
- If architecture diagram exists in raw/assets/: embed it
- Otherwise draw a text-based HLD using box-and-arrow notation:
  ┌─────────┐    query    ┌──────────┐
  │ Router  │ ──────────► │ Models   │
  └─────────┘             └──────────┘
  Keep it under 10 lines.

<N paragraphs — calibrated to tier. Cover: what they built, why the mechanism works,
what's surprising, what it implies. Do NOT restate the abstract — add interpretation.>

**Why it matters:** <One sentence. What changes if this paper is right?>

**Research angle:** ← Tier 1 only. What open problem does this point at?

→ [Full summary](<relative path>)

---

## Industry Pulse

What's happening beyond the lab. 3–6 bullets. 2–3 sentences each.
Lead with most consequential. Skip pure PR noise.
Flag anything that intersects Tier 1 areas.

- **[Company/Event]** — what happened. Why it matters.

---

## Connecting the Dots

The most valuable section. Synthesis that no single paper or newsletter provides.

Draw connections:
- Within today's batch: papers attacking the same problem from different angles
- Across days: today's paper confirms/contradicts/fills a gap from a prior date — name the prior paper and date explicitly
- Research → Industry: a VC, product launch, or chip announcement that relates to a research finding
- Worth Watching resolution: if a prior prediction is addressed today, call it out

Use a text relationship map when ≥2 papers compose into something larger:
  Paper A (approach X) ──► Paper B (extends) ──► Paper C (applies)
       └─── all three converge on: <the pattern> ───────────────┘

This section is mandatory when cross-paper or cross-day connections exist.

---

## Worth Watching

Specific, falsifiable predictions. Tier 1 open problems preferred.

- **[Specific claim or trend]** — why it matters and what to check in 30/60/90 days.

---

## Quick Hits

One tight paragraph per minor-but-notable item. Tier 3 sources, blog asides, changelogs.
Tier 4 items get one sentence here or nothing.

---

*Sources ingested today: N | Wiki pages updated: N*
```

---

## Writing rules

**Write simply. Keep every technical term.** Short sentences. One idea per sentence. Active voice. When a term appears for the first time in a section, give it a one-phrase gloss in plain English right next to it.

Bad: *"The standard approach to on-policy distillation has been shown to be massively wasteful in terms of learning signal density."*
Good: *"Standard distillation trains on every token. Most tokens carry no real signal. You only need 10%."*

**Be opinionated and specific.** "This is the third paper this month showing X — a pattern is forming" is worth reading. "This is interesting" is not.

**Future implications must be falsifiable.** Name a specific claim and timeframe. Not "this is important to watch."

**Connect before you summarize.** Big Picture and Connecting the Dots are the unique value of this digest. Any reader can get summaries from an abstract. They can't get accumulated synthesis anywhere else.

**Link everything.** Every Deep Dive must have a direct URL in the Links line. Every wiki reference must be a relative markdown link.

**Show the architecture.** For every Deep Dive, ask: would a diagram make this clearer? If yes, draw one.

---

### After writing

Update `wiki/index.md` with the digest entry.

Append to `wiki/log.md`:
```
## [YYYY-MM-DD] digest | Daily Digest | digest
- Sources: N
- Deep Dives: N
- Industry items: N
```

**Optional: generate the podcast.** If `connectors/notebooklm/` exists and the user has `nlm` authenticated (`nlm doctor`), run:
```
python3 connectors/notebooklm/podcast.py YYYY-MM-DD
```
This creates a NotebookLM notebook with the digest + wiki summaries + social-stream + external Deep Dive URLs as sources, generates a ~60 min audio overview using the focus prompt in `connectors/notebooklm/config.json`, downloads the .m4a, and drafts a Substack note alongside. Total time ~15 min, idempotent (skips if today's audio already exists).

Tell the user the digest is written and link to it. If the podcast was generated, link to that too.
