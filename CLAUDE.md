# cere-bro Wiki

A self-maintaining AI knowledge base fed daily from papers, blogs, YouTube, HuggingFace, and Twitter.
Pattern: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

---

## 🔒 Secrets policy (read this first — non-negotiable)

**Any credential the user provides — API tokens, OAuth secrets, cookies, private keys — stays on this machine and never leaves it.** This is a hard rule with zero exceptions.

Concretely:
- **Never** write a token, API key, or secret into any file under version control. Not in `connectors/*/config.json`, not in `CLAUDE.md`, not in scripts, not in commit messages, not even temporarily.
- Tokens are read from one of: (a) shell environment variables (`HF_TOKEN`, `APIFY_TOKEN`, etc.), (b) macOS Keychain (`security find-generic-password -s <name> -w`), or (c) gitignored config files under `~/.config/cere-bro/` or `connectors/*/credentials/` (chmod 600).
- If the user pastes a token into chat, treat it as **compromised** — tell them to rotate it immediately and ask for the rotated value via a safer channel (env var, keychain, or a gitignored local file).
- `.gitignore` must cover: `.env`, `.env.*`, `*.token`, `*-token`, `*token.txt`, `secrets/`, `*credentials*`, `*credential*.json`, `connectors/*/credentials/`, `~/.config/cere-bro/`. If a new secret pattern shows up, add it to `.gitignore` before writing the secret to disk.
- Before every `git add` / `git commit`, scan the diff for things that look like tokens (`hf_`, `sk-`, `ghp_`, `xoxb-`, long base64 strings, etc.). If anything matches, stop and ask the user.
- **No exfiltration via tools.** Don't fetch from URLs that embed a token in the query string when the page is public. Don't log tokens. Don't echo tokens to stdout / log files / `tee`.

This applies to everything: cron scripts, GitHub Actions, the starter template, future agents. If you are unsure whether something is safe, default to "not safe" and ask the user.

---

## 🔄 Starter-sync rule (read this second — non-negotiable)

**Whenever a change touches the pipeline, the starter must be updated in the same change.** The starter at `cere-bro-starter/` is what people fork to bootstrap their own wiki. If it drifts from the live system, anyone who clones it gets a broken or out-of-date system.

What counts as "pipeline-affecting":
- Any new connector (`connectors/<name>/`) → sync to `cere-bro-starter/templates/connectors/<name>/` with personal info scrubbed (use `{{PLACEHOLDERS}}` for things like handles, GitHub user, show names).
- Any change to an existing connector's farmer logic, config schema, or interface.
- Any change to `~/.local/bin/cerebro-*.sh` scripts → sync to `cere-bro-starter/templates/scripts/*.sh.template`.
- Any change to `site/scripts/build-data.mjs` or `site/src/` → sync the parallel file in `cere-bro-starter/templates/site/`.
- Any change to `CLAUDE.md` structure (new sections, new operational rules) → update `cere-bro-starter/templates/CLAUDE.md.template`.
- Any change to a bootstrap-skill question or follow-up → update `cere-bro-starter/.claude/skills/bootstrap/SKILL.md`.
- Any new `wiki-config.json` field → update `cere-bro-starter/wiki-config.json` schema.

After syncing:
- **Scrub for personal info** in the starter. Run `grep -rn "amit\|bayesiansapien\|amit02093\|quantiphi" cere-bro-starter/` before committing. The starter must contain no real names, handles, emails, or identifiers — only placeholders or generic defaults.
- **Commit both live and starter changes in the same commit** so reviewers see the parallel update.
- **Push to remote** at the end. The starter is what people install from a fresh clone, so the remote needs to stay in sync.

If a change is genuinely local-only (a personal preference, a one-off script, raw data), it does not need a starter update. But if you're unsure, sync it. Better to over-sync than ship a broken starter.

---

## Reader Profile

The reader is **Amit**, an AI researcher. Everything in the wiki — what gets a Deep Dive, how much explanation goes in, what open problems get flagged — should be calibrated to this attention hierarchy:

| Tier | Topics | Digest treatment |
|------|--------|-----------------|
| **1 — Core** | AI routing (LLM routing, multimodal routing, agent trajectory routing), KV Cache, compression / quantization / distillation / pruning, GPU optimization (kernels, FlashAttention, batching), GPU hardware (Hopper, Blackwell, memory hierarchy) | Long Deep Dives (4–6 paragraphs). Explain *why* the technique works, not just what. Add a **Research angle** note — open problems, follow-up directions. |
| **2 — Active learning** | General LLM papers, new architectures (SSM, MoE, hybrid), agentic systems, responsible AI (interpretability, alignment, safety, explainability) | Standard Deep Dives (2–4 paragraphs). Flag any intersection with Tier 1. |
| **3 — Broad horizon** | Vision / audio / video models (multimodal, vision-language, image and video generation, speech) | Quick Hits only, unless directly relevant to routing or efficiency. |
| **4 — Low interest** | 3D mapping, spatial reconstruction, robotics hardware, game benchmarks unrelated to efficiency | One sentence or skip. |

**When a paper spans tiers**, treat it at the highest applicable tier. **Connecting the Dots** should actively surface cross-paper patterns in Tier 1 areas. **Worth Watching** bullets should prioritize falsifiable predictions about Tier 1 open problems.

---

## Architecture

```
raw/        ← immutable source files (farmers write here, humans drop files here)
wiki/       ← LLM-owned synthesis (you write everything here)
  llms-foundation-models/  ← LLMs, foundation models, new architectures (SSM, MoE, hybrid)
  agentic-systems/         ← agents, tool use, agentic reasoning, agent memory, multi-agent
  responsible-ai/          ← interpretability, alignment, safety, explainability, governance
  vision-audio-video/      ← multimodal, vision-language, image/video generation, speech
  inference-efficiency/    ← compression, quantization, distillation, KV cache, GPU opt
  ai-routing/              ← LLM routing, multimodal routing, agent trajectory routing
  hardware/                ← GPU architecture, new chips, memory hierarchy
  ai-industry/             ← company news, product launches, funding, policy, regulation
  social-stream/           ← Twitter/X slot syntheses + daily roll-ups (Media Live)
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
| HuggingFace Daily Papers | Web/RSS | hf.co/papers — daily ML paper digest, ranked by community upvotes (popularity signal) |
| **Kurate.org leaderboards** | JSON API | `kurate.org/api/leaderboard?category=cs.AI` — weekly arXiv rankings via 3-LLM tournaments (quality signal, complement to HF). Farmed via `connectors/kurate/farmer.py`. Tracks recurring authors as "rising" candidates for the Twitter handles list. |
| **alphaxiv.org overviews** | On-demand HTTP | `connectors/alphaxiv/enrich.py <arxiv_id>` — fetches alphaxiv's AI-generated 1500-3000-word structured walkthrough of a paper. Used opportunistically when writing Tier 1 / Tier 2 Deep Dives to ground claims beyond the abstract. Returns empty if the paper has no overview yet (niche papers). 30-day file cache. |
| YouTube channels | local-cli (yt-dlp) | AI creators curated by user |
| **AI News** | RSS | TLDR AI (daily), The Decoder (in-depth), VentureBeat AI (industry), The Information (premium intel) |
| **Research blogs** | RSS | Lilian Weng, Karpathy, Sebastian Raschka, Interconnects AI, SemiAnalysis, Import AI, etc. |
| **Critical / opinion** | RSS | AI Snake Oil, Marcus on AI, Algorithmic Bridge |
| Twitter | Web | AI researchers and labs the user follows |
| AI Breakfast / Ben's Bites | — | Blocked by Cloudflare — not available via RSS |
| **Gmail starred emails** | Local file | `raw/gmail/YYYY-MM-DD-starred.md` — starred newsletters and articles from personal Gmail, farmed via `connectors/gmail/farmer.py`. Includes AI Breakfast, Ken Huang, SemiAnalysis, Pragmatic Engineer, Gary Marcus, HuggingFace digest snippets, and others. |
| **Reddit AI subreddits** | JSON API | `raw/reddit/YYYY-MM-DD-r-<sub>.md` — curated high-signal AI subreddits (LocalLLaMA, MachineLearning [R]/[P], MLScaling, CUDA, LLMDevs, ControlProblem, HPC, reinforcementlearning), farmed via `connectors/reddit/farmer.py`. Community-curated practitioner signal: what actually runs on consumer GPUs, real deployment patterns, scaling-law observations. Per-sub score gates + flair whitelists suppress noise. |
| **Daily Digest (parallel job)** | Local file | `/Users/amitsinghbhatti/Documents/Claude/Projects/Daily-Digest/` — daily-digest-YYYY-MM-DD.md files from a separate scheduled Claude job; read alongside HuggingFace + RSS and merge unique content into the final digest |

---

## Ingest

When a new file lands in `raw/` (via farmer or manually dropped):

**0-pre. Run all farmers first.** Before doing anything else, run the following in order:
1. `python3 connectors/gmail/farmer.py` — pulls starred Gmail emails into `raw/gmail/`
2. `python3 connectors/twitter/farmer.py` — pulls tweets and retweets into `raw/twitter/`
3. `python3 connectors/kurate/farmer.py` — pulls Kurate.org weekly leaderboards into `raw/kurate/` (cs.AI + cs.LG, plus rising-author tracking)
4. `python3 connectors/reddit/farmer.py` — pulls curated AI subreddits into `raw/reddit/` (8 subs, score-gated + flair-filtered, state-deduped)

All four are mandatory. All are idempotent — running them twice is safe. If any fail, note the error and continue with the most recent available file from that source.

**0. Consult the knowledge base first.** Before reading the new source, check what the wiki already knows about its topic area. Read the relevant concept pages (`wiki/<concept>/<concept-name>.md`) and scan the last 5–7 daily digests. This primes your context so you can write in light of prior knowledge, not in a vacuum. Concept pages are the most efficient entry point — they compress prior work into one page.

**0b. Collect ALL raw sources — this is mandatory, not optional.** Before writing any digest, read ALL SIX raw source directories. This is a hard requirement — a digest written without checking all six is incomplete.

**Step 1 — Identify the date range.** If no files exist for the exact digest date, use the most recent available files from each directory. Run `ls raw/gmail/ raw/rss/ raw/huggingface/ raw/twitter/ raw/kurate/ raw/reddit/` to see what's available.

**Step 2 — Read Gmail starred (always).** Find the most recent `raw/gmail/YYYY-MM-DD-starred.md` file. Read it in full. Gmail carries AI Breakfast, Ken Huang, SemiAnalysis, Pragmatic Engineer, Gary Marcus, HuggingFace digest snippets, and others — sources that don't appear in RSS or HuggingFace. Missing Gmail means missing these sources entirely.

**Step 3 — Read RSS feeds (always).** Read all `raw/rss/YYYY-MM-DD-*.md` files for the target date range. RSS carries The Decoder, TLDR AI, Interconnects AI, SemiAnalysis full posts, Simon Willison, Algorithmic Bridge, Marcus on AI, and others.

**Step 4 — Read HuggingFace papers (always).** Read all `raw/huggingface/YYYY-MM-DD-*.md` files for the target date range.

**Step 5 — Read Twitter/X (always).** Find the most recent `raw/twitter/YYYY-MM-DD-*.md` file(s). Read them. The file has two sections: (a) @bayesiansapien's retweets — treat these like starred Gmail, every retweet is a curated signal worth reading; (b) AI handle feed — original tweets from Anthropic, xAI, Google Research, NVIDIA, Cursor, and others, pre-filtered by AI keywords. For retweets with article content attached, the article content is the primary source.

**Step 6 — Read Kurate leaderboards (always).** Find `raw/kurate/YYYY-MM-DD-cs-ai.md` and `raw/kurate/YYYY-MM-DD-cs-lg.md` for the target date. These are weekly arXiv leaderboards ranked by 3-LLM tournaments — quality signal, not popularity. **Cross-source rule (mandatory):** any paper appearing in BOTH today's HuggingFace top AND the current week's Kurate top-20 is HIGH CONVICTION. Surface it as Tier 1 in Deep Dives regardless of topic, and label the entry "cross-source confirmed (HF + Kurate)". Papers that are top-5 on Kurate but missing from HF are "LLM-rated underrated" — flag in Worth Watching with the ai_rating, kurate score, and a one-line reason to track. Use the inferred `tier=N` line in each Kurate entry to weight space allocation: Tier 1 entries earn Deep Dive coverage; Tier 4 skip. Also read `raw/kurate/YYYY-MM-DD-rising-authors.md` — if any authors crossed threshold, add a "Rising authors from Kurate" sub-section to Worth Watching naming each author with one of their top papers, and suggest in prose whether to add them to `connectors/twitter/config.json:ai_handles` (you'll need to find the handle manually).

**Step 7 — Read Reddit (always).** Read all `raw/reddit/YYYY-MM-DD-r-*.md` files for the target date (eight subreddits: LocalLLaMA, MachineLearning, MLScaling, CUDA, LLMDevs, ControlProblem, HPC, reinforcementlearning). Each post entry carries a `tier=N` line set from the subreddit's `tier_default`. **Treatment rules:**
- **LocalLLaMA, MLScaling, CUDA, HPC (tier_default=1)** — practitioner reports on quantization, kernel work, KV cache hacks, scaling-law observations. Posts that confirm/contradict an HF or Kurate paper go in Connecting the Dots with the prior paper named. Substantive technical posts (a new GGUF quant family, a kernel benchmark, a hardware deep dive) deserve a short Deep Dive or a generous Quick Hit. Skip pure rig-show-off / "look at my 8x4090" posts.
- **MachineLearning [R]/[P] flair (tier_default=2)** — these usually link to arXiv. If the paper isn't in HF or Kurate today, treat it as an additional research source and ingest it like one (summary page if Tier 1/2, Quick Hit otherwise).
- **LLMDevs (tier_default=2)** — production deployment patterns. If a post describes a real shipped system (not a tutorial), it informs Industry Pulse or Connecting the Dots.
- **ControlProblem (tier_default=2)** — feeds responsible-ai topic. Often opinion, occasionally substantive. Apply the usual filter: is there a concrete claim or just commentary?
- **reinforcementlearning (tier_default=2)** — RLHF/RLVR adjacent. Cross-references RL papers from HF.

Reddit signal is community-curated practitioner ground truth — what actually runs on consumer hardware, what people actually deploy, what's hype vs real. It's the empirical complement to the paper-heavy HF/Kurate signal. Skip drama, "is it AGI" meta-discussion, and vendor PR even when score-gated through.

Do not start writing the digest until all six sources have been read. If a source directory has no file for the target date, note it explicitly and use the most recent available file from that source.

**0c. Check the parallel daily digest.** Look for `/Users/amitsinghbhatti/Documents/Claude/Projects/Daily-Digest/daily-digest-YYYY-MM-DD.md` (replace YYYY-MM-DD with the date being ingested). Skip any `-status.md` files. If the file exists, read it before writing the digest. Treat it as a curated synthesis source from a parallel Claude job. Merge its unique content into the final digest — industry news, papers not in the HuggingFace feed, analytical interpretations, and cross-source synthesis. Do not duplicate content already covered from HuggingFace/RSS sources; add only what is new or provides deeper analysis.

1. Read the source. For papers, read abstract + key sections; for videos, read the transcript; for blogs, read in full.
2. **Write a summary page** in the appropriate `wiki/<concept>/` subdirectory. Filename: `<YYYY-MM-DD>-<slug>.md`. Include: one-paragraph TL;DR, key findings or claims, **explicit notes on how this relates to prior wiki pages** (confirms, contradicts, extends, or fills a gap), links to related wiki pages, link back to the raw source.
3. **Update concept pages** — for every AI concept significantly discussed in the source, update or create `wiki/<concept>/<concept-name>.md`. Add what the source contributes: new evidence, a contradiction, a refinement. Note any shift from the prior state of knowledge the concept page recorded.
4. **Write/update the daily digest** — write to `wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md`. This is a newsletter, not a log. See the Daily Digest section below for the full format.
5. **Update index.md** — add the new summary page with its one-line description.
6. **Append to log.md** — format: `## [YYYY-MM-DD] ingest | <title> | <source-type>`
7. **Push to remote** — after all sources for the day are ingested and the daily digest is in its final state, run `git push origin main`. Do this once at the end of the session, not after every individual ingest.

Ingest one source at a time. A single source may touch 5–15 wiki pages. Always ingest all new raw files before the session ends.

---

## Page types

**Source summaries** (`wiki/<concept>/<date>-<slug>.md`) — one page per paper, video, or post. TL;DR, key points, figures if relevant, link to raw.

**Concept pages** (`wiki/<concept>/<concept-name>.md`) — one page per AI concept (e.g. "Mixture of Experts", "KV Cache", "Chain-of-Thought"). Synthesizes everything ingested so far. Updated every time a new source touches the concept.

**Daily digest** (`wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md`) — one file per day, structured as a newsletter. Written for the reader, not as a log. See the Daily Digest section below for the full format and writing rules.

---

## Knowledge Synthesis — Reading with Memory

The wiki is a living knowledge base, not a collection of daily snapshots. The unique value of cere-bro over any individual paper or newsletter is **accumulated context**. Every summary page and digest must be written in light of what the wiki already knows — not just what arrived today.

### What to look up before writing

For every incoming source, before writing its summary or the day's digest:

1. **Read the relevant concept pages** — `wiki/<concept>/<concept-name>.md`. This is the most efficient memory lookup: concept pages compress all prior work on a topic into one page. They tell you the prior state of knowledge, the open questions, and which papers established the current baseline.
2. **Scan recent digests** — the last 5–7 daily digests in `wiki/daily-digest/YYYY-MM/`. Look specifically for "Worth Watching" bullets or open questions from prior days that today's papers might address. The digest files also carry the narrative thread of how thinking in this area has evolved.
3. **Read prior summary pages directly** when a prior paper is in the same narrow area (same method family, same benchmark, same problem). Read it before writing about today's paper, not after.

This does not mean reading everything. Concept pages are the entry point. If a concept page flags a prior paper as directly relevant, then go read that summary. Otherwise, the concept page is sufficient context.

### Signals to name explicitly in every digest and summary

These are not optional observations. They are the primary reason this wiki exists. When any of the following are present, name them directly in the text — with paper names, dates, and the specific claim.

**Confirmation — a pattern is building:**
> "This is the second paper this month (after TIP on 04-16) showing that uniform gradient updates are wasteful. A pattern is forming: the field is converging on selective training."

Never bury a confirmation as "this aligns with prior work." Name the prior paper, give the date, state the shared claim precisely.

**Contradiction — a genuine tension exists:**
> "AIMO 3 (04-17) argued prompt diversity is a dead end for inference-time scaling. VGF's transport-step approach is a different form of test-time compute — but it hasn't been tested on AIMO's benchmarks. Whether these are compatible claims or genuinely conflicting is unresolved."

When two papers conflict, do not pick a winner. Name both, state the specific point of disagreement, and flag it as open.

**Gap-filling — today's paper solves a prior open problem:**
> "The 04-18 LongAct Research Angle asked whether saliency profiling could run online during training. VGF sidesteps this by never profiling — it uses gradient flow directly. Whether this fully resolves the LongAct question or just avoids it is worth tracking."

Always trace the explicit thread: this paper addresses the open question that was raised on [date] in [paper/digest].

**Worth Watching resolution — a prediction comes true (or fails):**
> "On 04-17, Worth Watching predicted that a verifier-based approach could close the pass@20 gap that prompt diversity cannot. VGF is not a verifier — but its transport-budget mechanism is the first concrete alternative proposal. Partial resolution."

When today's paper touches a prior prediction, name the prediction, the date it was made, and what today's paper changes about the prediction's status.

**N-of-a-kind — a pattern has now been established:**
> "This is the third paper this week routing knowledge transfer through a neutral representation layer: BLD (bytes), TESSY (hybrid token sequences), Switch-KD (shared text probability space). Three papers making the same architectural choice in one week is not coincidence — the community has converged on this frame."

The threshold for declaring a pattern: ≥3 papers making the same core claim or architectural choice. When that threshold is crossed, name the pattern, list all three papers, and state what the pattern implies.

### How to write when you have prior context

Do not write:
> "VGF proposes a new RL paradigm."

Write:
> "VGF is the clearest answer yet to a question that LongAct (04-18), PreRL (04-16), and TIP (04-16) all approached differently: where should training concentrate? Those papers worked at the gradient level, the token level, and the pre-train distribution level. VGF works at the distribution-transport level — the most mathematically principled frame so far."

The second version assumes the reader has been reading this wiki. They have. Use that context. Every paper arrives in a field that has prior work. Write as if you know that prior work — because the wiki does.

### What concept pages are for

Concept pages are the primary memory of the wiki. After every ingest, update them with what the new source added, changed, or contradicted. The concept page is what future-you reads before writing about the next paper in that area — it should tell you the complete prior state of knowledge in one read.

A concept page that has not been updated across ≥3 ingests in its area is a gap. Flag it during lint.

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

The daily digest is the most important output of the wiki. Amit reads it first every morning. It must be worth reading on its own — not a log, not a summary table, but a newsletter that makes him *want* to click through.

### Deep Dive enrichment

For each Tier 1 and Tier 2 Deep Dive, before writing prose run `python3 connectors/alphaxiv/enrich.py <arxiv_id>` and read the output if non-empty. The output is alphaxiv.org's AI-generated walkthrough of the paper (typically 1500-3000 words, structured into method / results / implications, with figure references). Use it to ground claims about what the paper actually does — much richer signal than the abstract alone.

Three rules:
1. **Don't copy alphaxiv's prose.** Write the Deep Dive in cere-bro's voice. Use the overview as input, not output.
2. **If the helper returns empty, fall back to the abstract.** Niche papers often have no alphaxiv overview yet; that's fine.
3. **Disagree with alphaxiv when it's wrong.** AlphaxIv overviews are AI-generated and can misframe a paper. If the abstract or RSS commentary contradicts the overview, trust the abstract.

### Format: `wiki/daily-digest/YYYY-MM/YYYY-MM-DD.md`

```markdown
# cere-bro | YYYY-MM-DD

> One-sentence framing of today's sharpest tension, surprise, or theme.

---

## TL;DR

3–6 bullets. One line each. The things worth knowing even if you read nothing else today.
Lead with Tier 1 research findings, then the most important industry news item.
Write the punchline, not the setup — assume the reader is skimming before deciding
what to read in depth.

- **[Paper/concept]** — what it found or did, in one punchy clause
- **[Paper/concept]** — what it found or did
- ...

---

## The Big Picture

2–3 paragraphs. Lead with the most interesting observation, not a list of what arrived.
What thread runs through today's batch? Do multiple papers attack the same problem from
different angles? Does a blog contradict a paper? What does today say about where the
field is heading? Write this like the opening of a good essay — pull the reader in.

---

## Deep Dives

5–8 most substantive sources. Skip changelogs, minor updates, routine releases.

---

### [Title of Paper or Post]

> [One-line hook — the most counterintuitive or surprising thing about this work]

**Source:** HuggingFace / Interconnects AI / etc.
**Links:** [Paper](https://arxiv.org/abs/XXXX.XXXXX) · [Wiki](../../<concept>/<slug>.md)
**Tier:** 1 — Routing / KV Cache / Compression / GPU  ← (or Tier 2, etc.)

[VISUAL BLOCK — include one of the following when it adds clarity:]

Option A — Embed a real figure from the paper (if architecture diagram exists in raw/assets/):
  ![Architecture](../../../raw/assets/YYYY-MM-DD-<slug>-fig1.png)

Option B — Text-based HLD when no figure is available but the design is non-obvious:
  ┌─────────────┐     query      ┌──────────────┐
  │  Router     │ ─────────────► │  Model Pool  │
  │  (cheap)    │ ◄───────────── │  A / B / C   │
  └─────────────┘    confidence  └──────────────┘
  Use boxes (┌┐└┘─│), arrows (►◄↑↓→←), labels. Keep it under 10 lines.

Option C — Relationship map for "Connecting the Dots" cross-paper diagrams:
  PreRL (expand horizon) ──► DSRL (combine) ──► TIP (distill cheaply)
       └─────── all three compose into a new training pipeline ───────┘

2–4 paragraphs (4–6 for Tier 1). Cover: what they built, why the mechanism works
(not just what it achieves), what's surprising or counterintuitive, what it implies.
Don't restate the abstract — add interpretation.

**Why it matters:** One sentence, punchy. What changes if this paper is right?

**Research angle:** ← Tier 1 only. What open problem does this point at? What would a
follow-up need to solve? What's still missing?

→ [Full summary](../../<concept>/<slug>.md)

---

## Industry Pulse

What's happening in AI beyond the lab. Cover company moves, product launches,
funding rounds, policy, regulation, and anything that shapes the business and
deployment landscape of AI. Sources: TLDR AI, The Decoder, VentureBeat AI,
The Information, Pragmatic Engineer.

Format: 3–6 bullet points. Each one is 2–3 sentences max — enough context to
understand what happened and why it matters. Lead with the most consequential
item. Skip pure PR/marketing noise. Flag anything that intersects Tier 1 research
areas (e.g. a new chip announcement, a routing product launch, a KV cache patent).

- **[Company/Product/Event]** — what happened. Why it matters in one sentence.

---

## Connecting the Dots

The most valuable section in the digest. Synthesis that nobody else can give the reader.

Connections to draw:
- **Within today's batch**: two or more papers attacking the same problem from different angles
- **Across days**: today's paper confirms, contradicts, or fills the gap from a paper covered on a prior date — name that prior paper and date explicitly
- **Research → Industry**: a VC funds a routing startup the same week a routing paper drops; a chip announcement relates to a training efficiency paper
- **Worth Watching resolution**: if a prior prediction is answered (partially or fully) by today's batch, call it out here

Include a text relationship map (Option C) when ≥2 papers compose into something larger than either alone.

This section is not optional when cross-paper or cross-day connections exist. Omit only when today's papers are genuinely isolated from everything prior in the wiki.

---

## Worth Watching

- **[Specific claim or trend]** — Why it matters and what to check in 30/60/90 days.
  Keep predictions falsifiable. Prioritize Tier 1 open problems.

---

## Quick Hits

One tight paragraph per minor-but-notable item. Tier 3 papers, blog asides,
changelogs, tool releases. Tier 4 items get one sentence here or nothing.

---

*Sources ingested today: N | Wiki pages updated: N*
```

---

### Writing rules

**0. Every item must link to its source.**
Every Deep Dive, every Industry Pulse bullet, every Quick Hit — include a hyperlink to the original paper, post, or article. No exceptions. Format: `([Source Name](URL))` inline, or `[Paper](URL)` in the Links line for Deep Dives. If the item came from a newsletter that covered a story (e.g. AI Breakfast covering an OpenAI announcement), link to the newsletter post — not a vague attribution. Never write "(Source Name)" without a URL. Never group items by source with a separator header — all items go directly into the section they belong in.

**1. Write simply. Keep every technical term. Never use em dashes.**
The digest is a lightweight daily read — for Amit, and potentially for a public audience too. Use short sentences. One idea per sentence. Active voice. No nested clauses. **Do not use em dashes (—) anywhere in the digest.** Replace them with a period, a comma, or rewrite the sentence so it flows naturally without a break. Em dashes create choppy, AI-sounding prose. Every sentence should read as natural flowing language. When a technical term appears for the first time in a section, give it a one-phrase gloss in plain English right next to it — for example: "KV cache (the memory store that saves previous attention computations so they don't get recomputed)". The term stays. The sentence around it should be easy to follow even for a smart reader outside the subfield. Think: clear, not dumbed down.

Bad: *"The standard approach to on-policy distillation, whereby the student model generates rollouts under teacher supervision at the token level, has been shown to be massively wasteful in terms of learning signal density."*
Good: *"Standard distillation trains on every token the teacher generates. TIP found that most of those tokens carry no real signal. You only need 10%."*

**2. Link everything directly.**
Every Deep Dive must include the direct URL to the paper (arxiv) or post in the **Links** line — not just the wiki summary. The reader should be one click from the source without ever leaving the digest.

**3. Show the architecture, don't just describe it.**
For every Deep Dive, ask: would a diagram make this clearer? If yes, either embed a figure downloaded from the source to `raw/assets/`, or draw a text-based HLD using box-and-arrow notation. Architecture papers, routing systems, and training pipelines especially benefit from this. A 6-line text diagram communicates more than two paragraphs of prose.

**4. Calibrate depth to the Reader Profile tier.**
Tier 1 (routing, KV cache, compression, GPU): 4–6 paragraphs, deep on mechanism — not just "latency improved" but *how* (kernel fusion? smarter eviction? speculative decoding?). Always end with a **Research angle** note. Tier 2: 2–4 paragraphs, flag Tier 1 intersections. Tier 3: Quick Hit unless it touches routing or efficiency. Tier 4: one sentence or nothing.

**5. Connect before you summarize.**
Big Picture and Connecting the Dots are the unique value of this digest. Any reader can get a summary from the abstract. They can't get synthesis elsewhere. Use text relationship maps when ≥2 papers compose into something bigger than either alone.

**6. Be opinionated and specific.**
"This is the third paper this month showing that benchmark accuracy doesn't predict deployment robustness — a measurement crisis is forming." That's worth reading. "This paper is interesting" is not. Name the tension, take the position.

**7. Future implications must be falsifiable.**
Worth Watching bullets should name a specific claim and a timeframe — "if DSRL generalizes beyond math to open-ended reasoning, it could replace SFT→RLVR by Q3 2026." Not "this is important to watch." Prioritize Tier 1 predictions.

**8. Skip the boring stuff without apology.**
Datasette changelogs get a sentence. Hype posts get nothing. Tier 4 spatial/3D work gets one line in Quick Hits at most. Length is not depth.

**9. Write as a second brain, not a daily reporter.**
The digest is not a fresh scan of today's papers. It is today's papers read by a system that has already read everything prior. Before writing, consult the relevant concept pages and recent digests. Then write every Deep Dive and the Big Picture as if you know what came before — because you do. When a paper confirms a prior finding, name the prior finding. When it contradicts one, name the contradiction. When it fills a gap that a prior paper opened, draw that thread explicitly. A digest that could have been written without reading any prior wiki pages has failed its core purpose. The reader should finish each digest feeling that the knowledge base got smarter overnight — not just bigger.

---

## Conventions

- Dates: `YYYY-MM-DD` everywhere
- Filenames: lowercase, hyphens, no spaces
- Internal links: relative markdown links (`../agentic-systems/tool-calling.md`)
- Source attribution: every summary page links to its raw file
- log.md entries start with `## [YYYY-MM-DD]` for easy grep
