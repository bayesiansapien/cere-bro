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

Use the reader's attention hierarchy from `CLAUDE.md` to calibrate depth allocation. **But never expose the tier vocabulary in the reader-facing output.** Describe topics directly ("an efficiency paper", "a paper on agent benchmarks"), not by tier number.

---

## Required format

The digest flows as one story: facts → interpretation → the papers themselves → how they connect → industry side → predictions → minor items.

```markdown
# <Wiki Name> | <YYYY-MM-DD>

> <One-sentence framing of today's sharpest tension, surprise, or theme.>

---

## TL;DR

One prose paragraph, 4-7 sentences, no bullets. The compressed view of what came in today. Strip every paper to "X dropped, claiming Y. Z also happened on the industry side." A reader who reads only this paragraph knows the day's factual surface.

Do NOT duplicate Big Picture content. TL;DR is **what happened**. Big Picture is **what it means**.

---

## The Big Picture

2-3 paragraphs of **interpretation**, not facts. What thread runs through today's batch? What does today say about where the field is heading? Multiple papers attacking the same problem from different angles — say so.

Write in plain English. Never write "Tier 1 paper" or any tier-code language. Describe the topic directly.

---

## Deep Dives

The day's substantive items, 5-8 typically. Each item structured as:

### <Title>

> <One-line hook stating the most counterintuitive or surprising thing. Self-contained.>

**Source:** <HuggingFace / SemiAnalysis / r/LocalLLaMA / etc.>
**Links:** [Paper](<url>) · [Wiki summary](<relative path>)

**What is it about?**
1-2 sentences in plain English. Gloss any domain term inline on first appearance.

**What problem does it solve?**
1-2 sentences naming the prior pain point this addresses.

**What's the core novelty?**
1-2 sentences naming the specific mechanism. Avoid "a novel framework that…" — say what it actually does.

**Key takeaways**
- 2-4 short bullets. Each self-contained. Numbers welcome.

**Gaps in the study**
1-2 sentences on what is NOT yet shown. Be specific.

**Industrial implication**
1-2 sentences on what changes if this is right. Be opinionated.

[Optional visual block — embed a figure or draw a text diagram only if it adds clarity. Skip if not useful.]

→ [Full summary](<relative path>)

---

## Connecting the Dots

Cross-paper / cross-day threads in plain English. Each connection is one prose paragraph (4-6 sentences). **No "Thread #N" code labels.** Each paragraph plainly names what it is about ("Three papers this month attack the same KV cache eviction problem from different angles…"). Every paper named here gets a one-clause gloss of its claim on first mention.

If today's papers are isolated from prior wiki state, omit this section.

---

## Industry Pulse

What's happening beyond the lab. 3-6 bullets, ONE SHORT SENTENCE per bullet (≤25 words).

- **[Company/Event]** — what happened, in one short sentence.

---

## Worth Watching

Falsifiable predictions with specific timeframes.

- **[Specific claim or trend]** — what to check in 30 / 60 / 90 days.

---

## Also today

Optional section. One sentence per item, minor releases / library updates / benchmark announcements. Omit if no real items.

- [Item]: [one sentence].

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

**Carry the context for the reader.** Every named paper reference, every acronym, every prior-paper callback gets a one-clause gloss of its actual claim the first time it appears in any given section. Not just "the [paper name] from [date]" but "the [paper name] from [date], which found [the specific claim that made it matter]." The wiki is the memory; the reader is not expected to be. A new reader should follow at 60-70% minimum. This rule applies most acutely in Connecting the Dots (where it most often gets violated by name-dropping paper acronyms in a chain) but also in TL;DR, Big Picture, Deep Dive hooks, and Worth Watching. Length is not the constraint; clarity is.

**Twitter retweets with substantive linked content are sources too.** If a curated retweet links to a paper or blog post not already covered by today's primary research feeds (HuggingFace, RSS, Kurate), write a wiki summary page for it just like any other source. When the same arxiv ID appears in BOTH a Twitter retweet AND today's HF/Kurate top, label it "cross-source confirmed via social" in the Deep Dive header — a stronger signal than two paper-side feeds alone.

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
