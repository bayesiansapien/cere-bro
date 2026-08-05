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
| **1 — Core** | AI routing (LLM routing, multimodal routing, agent trajectory routing), KV Cache, compression / quantization / distillation / pruning, GPU optimization (kernels, FlashAttention, batching), GPU hardware (Hopper, Blackwell, memory hierarchy), semiconductor industry (chip manufacturing, fab economics, memory supply chain, compute infrastructure) | Long Deep Dives (4–6 paragraphs). Explain *why* the technique works, not just what. Add a **Research angle** note — open problems, follow-up directions. |
| **2 — Active learning** | General LLM papers, new architectures (SSM, MoE, hybrid), agentic systems, responsible AI (interpretability, alignment, safety, explainability) | Standard Deep Dives (2–4 paragraphs). Flag any intersection with Tier 1. |
| **3 — Broad horizon** | Vision / audio / video models (multimodal, vision-language, image and video generation, speech) | Light Industry Pulse mention only, unless directly relevant to routing or efficiency. |
| **4 — Low interest** | 3D mapping, spatial reconstruction, robotics hardware, game benchmarks unrelated to efficiency | One sentence or skip. |

**When a paper spans tiers**, treat it at the highest applicable tier. **Global View** should actively surface cross-paper patterns in Tier 1 areas. **Looking Ahead** bullets should prioritize falsifiable predictions about Tier 1 open problems.

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
  hardware/                ← GPU architecture, new chips, memory hierarchy, semiconductor industry (fab economics, chip manufacturing, memory supply chain, compute infrastructure)
  ai-industry/             ← company news, product launches, funding, policy, regulation
  social-stream/           ← Twitter/X slot syntheses + daily roll-ups (raw social ingest)
  media-zone/              ← daily synthesis of Twitter+YouTube+Reddit, topic-clustered
    YYYY-MM/
      YYYY-MM-DD.md  ← one Media Zone synthesis per day, written by morning cron
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
| **Semiconductor newsletters** | Gmail + RSS | The Semiconductor Newsletter (Substack, weekly — fab builds, chip industry, memory, advanced packaging), SemiAnalysis (GPU/datacenter economics, chip deep dives), Fabricated Knowledge (semiconductor analysis, memory/HBM supply chain). These feed directly into `wiki/hardware/`. |
| **Critical / opinion** | RSS | AI Snake Oil, Marcus on AI, Algorithmic Bridge |
| Twitter | Web | AI researchers and labs the user follows, via Nitter RSS. The farmer captures: tweet text, handle, post link, all URLs in the post body, up to **10,000 chars of article content** from each linked URL (arxiv abstracts extracted specifically; generic URLs get HTML-stripped plain text), and any image attachments downloaded to `raw/twitter/images/` (gitignored). For `x.com/i/article/...` URLs, the farmer attaches X session cookies from `~/.config/cere-bro/x-cookies.json` (gitignored, chmod 600, user-supplied via one-time browser export) so X's native long-form articles fetch successfully. When cookies are absent or expired, the farmer logs a warning and falls back to URL-only capture. Image content is read directly by Claude during the Media Live synthesis step via the Read tool (no OCR layer needed). Not captured: video transcripts, thread replies beyond the top tweet, pinned tweets re-shown. |
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

**Step 6 — Read Kurate leaderboards (always).** Find `raw/kurate/YYYY-MM-DD-cs-ai.md` and `raw/kurate/YYYY-MM-DD-cs-lg.md` for the target date. These are weekly arXiv leaderboards ranked by 3-LLM tournaments — quality signal, not popularity. **Cross-source rule (mandatory):** any paper appearing in BOTH today's HuggingFace top AND the current week's Kurate top-20 is HIGH CONVICTION. Surface it as Tier 1 in Deep Dives regardless of topic, and label the entry "cross-source confirmed (HF + Kurate)". Papers that are top-5 on Kurate but missing from HF are "LLM-rated underrated" — flag in Looking Ahead with the ai_rating, kurate score, and a one-line reason to track. Use the inferred `tier=N` line in each Kurate entry to weight space allocation: Tier 1 entries earn Deep Dive coverage; Tier 4 skip. Also read `raw/kurate/YYYY-MM-DD-rising-authors.md` — if any authors crossed threshold, add a "Rising authors from Kurate" sub-section to Looking Ahead naming each author with one of their top papers, and suggest in prose whether to add them to `connectors/twitter/config.json:ai_handles` (you'll need to find the handle manually).

**Step 7 — Read Reddit (always).** Read all `raw/reddit/YYYY-MM-DD-r-*.md` files for the target date (eight subreddits: LocalLLaMA, MachineLearning, MLScaling, CUDA, LLMDevs, ControlProblem, HPC, reinforcementlearning). Each post entry carries a `tier=N` line set from the subreddit's `tier_default`. **Treatment rules:**
- **LocalLLaMA, MLScaling, CUDA, HPC (tier_default=1)** — practitioner reports on quantization, kernel work, KV cache hacks, scaling-law observations. Posts that confirm/contradict an HF or Kurate paper go in Global View with the prior paper named. Substantive technical posts (a new GGUF quant family, a kernel benchmark, a hardware deep dive) deserve a short Deep Dive or a generous Industry Pulse mention. Skip pure rig-show-off / "look at my 8x4090" posts.
- **MachineLearning [R]/[P] flair (tier_default=2)** — these usually link to arXiv. If the paper isn't in HF or Kurate today, treat it as an additional research source and ingest it like one (summary page if Tier 1/2, Quick Hit otherwise).
- **LLMDevs (tier_default=2)** — production deployment patterns. If a post describes a real shipped system (not a tutorial), it informs Industry Pulse or Global View.
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
2. **Scan recent digests** — the last 5–7 daily digests in `wiki/daily-digest/YYYY-MM/`. Look specifically for "Looking Ahead" bullets or open questions from prior days that today's papers might address. The digest files also carry the narrative thread of how thinking in this area has evolved.
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

**Looking Ahead resolution — a prediction comes true (or fails):**
> "On 04-17, Looking Ahead predicted that a verifier-based approach could close the pass@20 gap that prompt diversity cannot. VGF is not a verifier — but its transport-budget mechanism is the first concrete alternative proposal. Partial resolution."

When today's paper touches a prior prediction, name the prediction, the date it was made, and what today's paper changes about the prediction's status.

**N-of-a-kind — a pattern has now been established:**
> "This is the third paper this week routing knowledge transfer through a neutral representation layer: BLD (bytes), TESSY (hybrid token sequences), Switch-KD (shared text probability space). Three papers making the same architectural choice in one week is not coincidence — the community has converged on this frame."

The threshold for declaring a pattern: ≥3 papers making the same core claim or architectural choice. When that threshold is crossed, name the pattern, list all three papers, and state what the pattern implies.

### How to write when you have prior context

Use the wiki's prior knowledge, but **carry the context for the reader** instead of assuming they remember every paper from the last 90 days. A reader returning to a digest a month later, or a new reader landing on it for the first time, should follow at 60-70% minimum.

**The rule:** every named paper reference includes a one-clause gloss of its actual claim, the first time it appears in any given section. Not just a paper name and date. The gloss earns the right to use the name.

Do not write:
> "VGF is the clearest answer yet to a question that LongAct (04-18), PreRL (04-16), and TIP (04-16) all approached differently: where should training concentrate? Those papers worked at the gradient level, the token level, and the pre-train distribution level."

That paragraph fails because a reader who hasn't memorized LongAct, PreRL, and TIP gets four names and no understanding.

Write:
> "VGF is the clearest answer yet to a question that three earlier papers approached differently. LongAct (04-18) showed that long-context training signal is concentrated in the first 5% of tokens, so the gradient is what matters. PreRL (04-16) argued the question is really about the pre-training data distribution, not the training loop. TIP (04-16) reframed it as a token-weighting problem: most teacher-generated tokens carry no signal and should be skipped. VGF works at a fourth layer, distribution-transport: it asks where probability mass should be moved, not which tokens to weight. It is the most mathematically principled frame of the four."

The second version carries the context. Every paper reference includes the one specific claim that made it matter. A reader meeting LongAct for the first time gets the gist immediately. A reader returning a month later doesn't have to look anything up.

**Apply this in:** TL;DR bullets, Deep Dive opening hooks, Global View, Looking Ahead, and any cross-day reference anywhere. Length is not the constraint; clarity is. Let the digest run longer if it has to.

**The gloss should be specific, not generic.** A bad gloss is "LongAct (the paper about training signal concentration)." A good gloss is "LongAct (the paper that showed long-context gradient signal is concentrated in the first 5% of tokens)." Specific is short and lands the why.

This applies to acronyms too. The first time MoE, RLVR, KV cache, FlashAttention, GRPO, or any other field-specific term appears in a given section, it gets a one-phrase gloss in plain English right next to it. Subsequent mentions in the same section can use the bare term.

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

The digest is one story in five sections: TL;DR → Deep Dives → Industry Pulse → Global View → Looking Ahead. No "Also today" tail, no source-count footer. Locked-in section order as of 2026-06-03.

```markdown
# cere-bro | YYYY-MM-DD

> One-sentence framing of today's sharpest tension, surprise, or theme.

---

## TL;DR

**4-6 bullets. Each bullet ≤25 words. Plain language. No paragraphs.** This is
the only top-level summary — make it actually scannable. Each bullet names
ONE substantive thing from today: a paper's main claim, an industry move, or
a one-line theme. Reader should consume the entire TL;DR in 30 seconds.

Format each bullet with a **bold lead-in** (paper name, company, or theme),
then the one-line claim in simple English:

- **OPRD**: instead of matching teacher output tokens, match teacher hidden
  states. Closes student-teacher gap on math benchmarks.
- **Anthropic ships "When AI builds itself"**: Claude writes 90%+ of their
  own code, engineers ship 8x more code per quarter.
- **CLEAR**: ration inference compute across a batch of queries with one
  shadow price. Up to 3x accuracy when compute is scarce.

What NOT to do in TL;DR:
- No prose paragraphs of any length. Bullets only.
- No story arc weaving — that lives in Global View at the bottom of the digest.
- No paper-to-paper comparisons threading across bullets — keep each bullet
  self-contained.
- No nested clauses, no semicolons, no em dashes.

Do not say "Tier 1 paper" or "Tier 2 research" or any tier-code language. The
tier hierarchy exists to calibrate writer depth allocation. It must not appear
in reader-facing output. Describe the topic directly: "an efficiency paper on
KV cache eviction" or "a paper on agent benchmarks."

---

## Deep Dives

The day's substantive papers and posts, structured for skimming. 5-8 items
typically. Skip changelogs and routine releases — they get one Industry Pulse
bullet instead, or nothing.

For each item:

### [Title of paper or post]

> [One-line hook stating the most counterintuitive or surprising thing.
> Self-contained: the reader does not need to read further to get the point.]

**Source:** [HuggingFace / SemiAnalysis / The Decoder / r/LocalLLaMA / etc.]
**Links:** [Paper](URL) · [Wiki summary](../../<topic>/<slug>.md)

**What is it about?**
1-2 sentences in plain English. Explain what the work actually is at the level
a smart non-specialist follows. If the title contains a domain term (KV cache,
MoE, on-policy distillation, etc.), gloss it inline the first time it appears.

**What problem does it solve?**
1-2 sentences naming the prior pain point this addresses. "Until now, X. This
paper changes that by Y."

**What's the core novelty?**
1-2 sentences naming the specific technical or methodological contribution.
The one thing that makes the paper non-trivial. Avoid "a novel framework
that..." — say the actual mechanism.

**Key takeaways**
- 2-4 short bullets. Each one a self-contained statement of an observed
  result or claim. Numbers welcome ("3.8x speedup," "passes 62% on benchmark X
  where prior best was 47%").
- Each bullet stands alone — readable without surrounding context.

**Gaps in the study**
1-2 sentences on what is not yet shown. Scaling? Held-out domains? Ablations
missing? Benchmark artifacts? Be specific, not vague ("they only tested at
1.3B" beats "limited evaluation").

**Industrial implication**
1-2 sentences on what changes if this is right. Where does this show up in
production stacks, in a quarter / six months / a year? Be opinionated; this is
the section where stance is welcome.

**Diagram (mandatory for any paper with architecture / pipeline / multi-component
system).** Two acceptable options. Pick one. NEVER use ASCII / text-art
diagrams — they are banned.

  *Option A (preferred)*: download the paper's actual figure (usually Fig 1,
  the system overview) to `raw/assets/YYYY-MM-DD-<slug>-fig1.png` and embed:
  `![Architecture](../../../raw/assets/YYYY-MM-DD-<slug>-fig1.png)`

  *Option B (fallback when no usable figure exists in the paper)*: write a
  Mermaid block. Mermaid renders as a real labeled diagram both on GitHub
  (native server-side rendering) and on the Astro site (client-side lazy
  loader). Three rules:

  - **Use `flowchart LR` (landscape) by default.** Portrait (`TB`) makes the
    reader scroll vertically on the digest page. Reserve `TB` for diagrams
    with genuine multi-branch fan-out + merge that compresses badly horizontally
    (e.g. split-then-merge pipelines with 3+ parallel branches).
  - **Apply `classDef` colors per semantic node type** so the reader can read
    structure at a glance. Standard palette:
    - `classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a` — sources, inputs, queries
    - `classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f` — gates, routers, conditionals
    - `classDef output fill:#d1fae5,stroke:#10b981,color:#065f46` — results, outputs, protected items
    - `classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d` — failure modes, evicted items, clipped paths
    - `classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81` — secondary processes, side channels
  - **Keep node labels short.** Multi-line via `<br/>`. Aim for 2-4 words per
    line, max 3 lines per node.

  Example:

      ```mermaid
      flowchart LR
        Q[Query] --> R{Router}
        R -->|easy| S[Small LM]
        R -->|hard| L[Frontier LM]
        S --> O[Output]
        L --> O
        classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
        classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
        classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
        class Q input
        class R decision
        class S,L,O output
      ```

  If the paper genuinely has no architecture (a benchmark, a survey, a pure
  empirical study), the diagram block can be skipped entirely. The bar for
  skipping is high.

→ [Full summary](../../<topic>/<slug>.md)

---

## Industry Pulse

What's happening beyond the lab. Company moves, product launches, funding
rounds, regulation, policy. Sources: TLDR AI, The Decoder, VentureBeat AI,
The Information, AI Breakfast, AI Weekly / Daily Espresso, Last Week in AI
(the LWiAI podcast summaries in Gmail carry dense business news — read the
body and extract each distinct item), Pragmatic Engineer, SemiAnalysis and the
other semiconductor newsletters, Interconnects, Medium Daily Digest.

This is an **important section, not a throwaway** — give it thorough coverage.
**Typically 8-14 bullets**, more if the raw sources carry more real signal. Do
NOT over-compress to 3-5 bullets. **One short sentence per bullet** (≤25 words).
Lead with the most consequential. Skip pure PR.

- **[Company/Product/Event]** — what happened, in one short sentence ([source](URL)).

**Mandatory funding & startup sub-cluster.** The reader tracks funding, startups,
and M&A as a distinct attention tier. Before finishing the section, scan every
source specifically for: funding rounds (name amount, lead investor, valuation,
stage), IPO filings, acquisitions/M&A, new company launches, notable hires, and
large compute/infrastructure deals. Group them under a bold
`**Funding, valuations, and compute deals**` sub-heading inside Industry Pulse,
one bullet each. Never drop a funding round or valuation that appears in the raw
sources — the dollar figure alone is high-signal to this reader.

**Hardware/semiconductor items always surface** (Tier 1 reader interest):
SemiAnalysis, the Semiconductor Newsletter, and Fabricated Knowledge items on
fabs, memory/HBM, packaging, or datacenter economics get a bullet even on a
quiet day.

**Substantive blog essays get more than a bullet.** A standalone argumentative
essay (Sebastian Raschka / Ahead of AI, a SemiAnalysis deep-dive, an Interconnects
analysis, Gary Marcus) that makes a real technical or analytical claim earns a
Deep Dive or a Global View thread on its actual argument — do not reduce it to a
one-line Industry Pulse mention.

Inline flag any item that intersects research themes from today's Deep Dives.

**IMPORTANT — read the full article bodies, not just headlines.** Before
moving on to Global View below, re-open each Industry Pulse item's source
article (already in `raw/gmail/` or `raw/rss/`) and read what they actually
claim. The next section depends on this — Global View synthesizes WHERE
industry is moving against WHERE research is moving, and that synthesis is
only possible if you've actually digested the industry article bodies, not
just their headlines.

---

## Global View

The synthesis section — renamed from Global View. This is where
the wiki earns its keep.

**Two mandatory dimensions for every Global View thread:**

1. **Globally-aware.** Pattern-match today against the WHOLE wiki, not just
   today's papers. Use concept pages (`wiki/<topic>/<concept>.md`) and the
   last 5-7 daily digests as context. Name the prior paper / date / claim
   when you connect today to history.

2. **Research × industry cross-synthesis.** Every thread must explicitly weave
   research findings (today's Deep Dives + prior wiki) AND industry behavior
   (today's Industry Pulse + recent funding/products from prior digests).
   Trace where:
   - Industry decisions prove or disprove a paper's prediction
   - Products ship a research technique into production
   - Funding rounds signal market belief in a research direction
   - Research is outpacing industry adoption (a gap)
   - Industry is moving where research hasn't caught up (the other gap)

**Format**: 2-3 threads maximum. Each thread is a single prose paragraph,
4 sentences maximum. Lead the paragraph with the claim, then the evidence.
Every paper or article named on first mention gets a one-clause gloss of its
actual claim (per writing rule #10).

If today's batch is genuinely isolated from prior wiki state AND from any
industry signal, omit this section entirely rather than fabricating threads.

---

## Looking Ahead

Renamed from Looking Ahead. Forward-looking falsifiable predictions only.

**Format**: 2-5 bullets max. Each bullet has three required parts:

1. **The claim** — a specific prediction about what will happen
2. **The timeframe** — 30 / 60 / 90 days
3. **The signal** — what concretely to check for ("if X hits N forks on
   HuggingFace by date Y," "if Anthropic ships a routing product by Q3,"
   "if any frontier lab publishes Z by month-end")

Example: *"If MiniMax M3's open-weight 1M-context model gets >50 production
deployments tracked in the LocalLLaMA subreddit by 2026-07-01, the long-context-as-default
thesis is validated and Claude/GPT pricing will need to adjust within 30 days."*

Bullets are NOT a list of papers to track. They are testable claims.

Prioritize predictions about the deep-interest areas (routing, KV cache,
compression, GPU). **Omit the entire section** on days that produced no
testable predictions — better silence than vague "interesting to watch" filler.
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

**3. Show the architecture. Visuals beat prose for system explanations. This is mandatory, not optional.**

Every Deep Dive about a paper that has architecture, a routing flow, a training pipeline, a cache layout, or any multi-component system MUST include a diagram. The diagram comes BEFORE the prose explanation, not after. A reader who only looks at the diagram should understand the mechanism at a high level.

Two acceptable diagram sources, in priority order:

(a) **Embed the paper's actual figure.** If the source paper or blog has an architecture/system diagram, download it to `raw/assets/YYYY-MM-DD-<slug>-fig1.png` (or fig2, etc.) and embed it: `![Architecture](../../../raw/assets/YYYY-MM-DD-<slug>-fig1.png)`. For arxiv papers, the figures are usually accessible from the abstract page or the full PDF. Pull the most informative one (typically Figure 1 — the overview / system diagram).

(b) **Draw a text-based HLD when no figure is available, or the paper's figure is too dense.** Use box-and-arrow notation with `┌┐└┘─│` and arrows `►◄↑↓→←`. Keep it under 10 lines. Label every box and every arrow. Examples:

```
┌─────────────┐    query       ┌──────────────┐
│  Router     │ ─────────────► │  Model Pool  │
│  (cheap LM) │ ◄───────────── │  A / B / C   │
└─────────────┘    confidence  └──────────────┘
```

```
KV cache layout:
  Layer  1-4  : shared across all heads  (compressed)
  Layer  5-12 : per-head static          (memorize)
  Layer 13-32 : per-head dynamic         (rolling window)
```

```
Three-paper convergence on routing-as-policy:
  Conductor (RL orchestrator) ─┐
  CaRE (task-axis router)      ├─► routing IS the policy
  MISA (head-axis router)      ─┘
```

The diagram is the first thing the reader sees in the Deep Dive body. Then the 6-section prose (What is it about? / What problem...) explains the diagram.

Apply the SAME rule to wiki summary pages. Every summary of a paper with a system / architecture / mechanism gets a diagram at the top of the page, right after the TL;DR paragraph. Pull from the paper's figure, or draw text-based when no figure exists. A summary page with only prose has failed its purpose for any paper where the mechanism matters.

If you genuinely cannot find a figure AND the system is too simple to need a text diagram, skip — but the default should be "include a diagram." The bar for skipping is high: a paper about a benchmark with no architecture (e.g. a new eval dataset) doesn't need a diagram; almost everything else does.

**4. Calibrate depth to the Reader Profile tier.**
Tier 1 (routing, KV cache, compression, GPU): 4–6 paragraphs, deep on mechanism — not just "latency improved" but *how* (kernel fusion? smarter eviction? speculative decoding?). Always end with a **Research angle** note. Tier 2: 2–4 paragraphs, flag Tier 1 intersections. Tier 3: Quick Hit unless it touches routing or efficiency. Tier 4: one sentence or nothing.

**5. Connect before you summarize.**
TL;DR and Global View are the unique value of this digest. Any reader can get a summary from the abstract. They can't get synthesis elsewhere. Use text relationship maps when ≥2 papers compose into something bigger than either alone.

**6. Be opinionated and specific.**
"This is the third paper this month showing that benchmark accuracy doesn't predict deployment robustness — a measurement crisis is forming." That's worth reading. "This paper is interesting" is not. Name the tension, take the position.

**7. Future implications must be falsifiable.**
Looking Ahead bullets should name a specific claim and a timeframe — "if DSRL generalizes beyond math to open-ended reasoning, it could replace SFT→RLVR by Q3 2026." Not "this is important to watch." Prioritize Tier 1 predictions.

**8. Skip the boring stuff without apology.**
Datasette changelogs get a sentence. Hype posts get nothing. Tier 4 spatial/3D work gets one Industry Pulse line at most, often skipped. Length is not depth.

**9. Write as a second brain, not a daily reporter.**
The digest is not a fresh scan of today's papers. It is today's papers read by a system that has already read everything prior. Before writing, consult the relevant concept pages and recent digests. Then write every Deep Dive and the TL;DR as if you know what came before — because you do. When a paper confirms a prior finding, name the prior finding. When it contradicts one, name the contradiction. When it fills a gap that a prior paper opened, draw that thread explicitly. A digest that could have been written without reading any prior wiki pages has failed its core purpose. The reader should finish each digest feeling that the knowledge base got smarter overnight — not just bigger.

**10. The reader does not remember every paper. Carry the context for them.**
This is the most important rule. The wiki is the memory; the reader is not expected to be. Every time the digest references a prior paper, prior result, or prior concept by name, it must include a one-clause gloss of what that paper actually claimed, right there in the sentence. Not just "the Extrapolation Cliff paper from 05-14" — write "the Extrapolation Cliff paper from 05-14, which found a closed-form threshold above which on-policy distillation collapses." See the "How to write when you have prior context" section above for the worked example.

This applies in: every part of the TL;DR block, every Deep Dive's hook line, Global View (where it matters most), Looking Ahead, and any cross-day reference in any section. Acronyms get the same treatment on first mention in a given section: "MoE (mixture-of-experts, where each token routes through a small subset of specialized sub-networks)" not just "MoE." Length is not the constraint, clarity is. A digest that runs longer because every reference carries its own context is doing the right thing. A digest that name-drops papers and trusts the reader's memory is doing the wrong thing.

**Test your draft against this question:** could a smart tech-literate reader who has not been tracking AI research weekly follow at 60-70% on first read? If no, the digest needs more in-place context.

**11a. Never expose the tier vocabulary in reader-facing output.**
The Tier 1 / Tier 2 / Tier 3 / Tier 4 hierarchy exists to calibrate the writer's depth allocation. It does NOT appear in the digest's output text. Do not write "this Tier 1 paper" or "skip the Tier 4 stuff" or include a `**Tier:** N` line in Deep Dive headers. Instead describe the topic directly: "an efficiency paper" or "a paper on agent benchmarks" or "a routing paper." A reader picking up the digest cold does not know what the tiers are. They should never need to.

**11b. Twitter retweets with substantive linked content get wiki summary pages.**
The Twitter farmer captures up to 10K characters of article content for each link in each curated retweet (see Sources table). When that content is a paper or blog post not already covered by today's HuggingFace, RSS, or Kurate, write a wiki summary page for it in the appropriate topic folder. Use the same template as any other source. Twitter is not just a signal layer; it is also a source layer for substance that doesn't appear on HuggingFace.

When an arxiv ID appears in BOTH a Twitter retweet AND today's HuggingFace top, label it "cross-source confirmed via social" in the Deep Dive header. That is a stronger signal than HuggingFace + Kurate alone (which is paper-quality cross-check; social is human-curator cross-check).

---

## Media Zone

The Media Zone is the daily synthesis of social and video signal — Twitter, YouTube AI/tech, and substantive Reddit threads — rendered as a curated digest, NOT a raw feed of cards. It is the second daily output the morning cron writes alongside the Daily Digest. Locked-in format as of 2026-06-03. **Sourcing + framing updated 2026-08-05** (X saved posts, optimization lens, compact-explanatory voice).

### Primary X source: the reader's SAVED / BOOKMARKED posts (updated 2026-08-05)

The Media Zone's X content is sourced first and foremost from **Amit's saved (bookmarked) posts on X**, not just the public timeline of AI handles. Amit reads his X feed and saves posts worth keeping; those bookmarks are the curated signal, treated with the same weight as starred Gmail. Rules:

- **Read the saved post AND every link it references.** A bookmark is rarely self-contained: it points to a paper, a repo, a blog, a thread. Follow those links and pull the actual claim, the same way the Twitter farmer already captures up to 10K chars of article content per link. The bookmark is the pointer; the referenced content is the substance.
- **Saved posts are curated intent.** Amit bookmarked it for a reason. Infer that reason (usually a cost / efficiency / routing / optimization angle per the Reader Profile) and lead the item with it.
- **Bookmarks supplement, not replace, the existing scrape.** The `@bayesiansapien` curated retweets and the AI-handle feed still feed the Media Zone; saved posts are the new top-priority layer above them.

**Capability note (must respect):** the Twitter farmer currently scrapes Nitter RSS (retweets + AI-handle feed) and can fetch `x.com/i/article/` bodies only when authenticated X session cookies exist at `~/.config/cere-bro/x-cookies.json` (gitignored, chmod 600, user-supplied). Reading the private **bookmarks timeline** likewise requires those cookies (the `/i/bookmarks` endpoint is auth-gated). Until a bookmarks-capture path is wired into `connectors/twitter/farmer.py`, use whatever saved-post content is available (any bookmark URLs Amit drops into the pipeline, cookie-fetched article bodies, curated retweets as the closest proxy) and note in the day's Media Zone if the bookmark feed could not be reached. Do not silently pretend bookmarks were read when they were not.

### The optimization lens (updated 2026-08-05)

Amit is an AI researcher working on **optimization**. Every Media Zone item — and the daily digest's synthesis — should be read and framed through three optimization axes, named explicitly where they apply:

1. **Cost optimization** — how does this reduce resource usage (compute, memory, tokens, dollars, energy, serving cost)? This is the dominant axis; most Tier 1 items have a cost angle.
2. **Influence optimization** — how does this amplify impact or leverage (a technique that changes many downstream systems, a result that shifts the field, a distribution/adoption play)?
3. **Token optimization** — keep the narrative itself concise. Say more with fewer tokens; the Media Zone is the lighter, token-efficient read next to the wiki digest.

Lead each cluster or item with the optimization angle that fits. Not every item is all three — name the one(s) that apply. If an item has no optimization angle at all, it probably belongs in the daily digest's Industry Pulse, not the Media Zone.

**Signature line.** Every Media Zone (and the daily digest's opening framing) carries the line **"Some attention to your tears."** as a fixed marker that the read was done through the optimization lens. Place it in the `> ` framing quote at the top.

### Why this exists

Without synthesis, the Media Zone collapses into a dumping ground of thumbnails and tweet cards. The reader scrolls, gets fatigued, and skips. With synthesis, the reader gets one paragraph naming what mattered on social today, then topic clusters that fuse a saved post, its linked paper/repo, a video, and a Reddit thread into one coherent picture per topic — each framed by its optimization angle.

### Format: `wiki/media-zone/YYYY-MM/YYYY-MM-DD.md`

The Media Zone synthesis is written by the morning cron in the same Claude call as the daily digest. It is a separate file so the Astro site can render it under its own tab.

**Format rule — compact, but explained (updated 2026-08-05).** Media Zone is a feed-style read, lighter than the wiki digest, but NO LONGER bare one-line pointers. Each cluster is **3-5 compact bullets**, each a short sentence or two (roughly 20-40 words) that briefly explains the item and its optimization angle, so the reader gets context without opening the wiki. Still not full prose paragraphs, and still much lighter than a Deep Dive — think "a knowledgeable friend's two-line note on why this matters," not "a headline." Thumbnails and link rows are centered via HTML wrappers so the page reads like a scrollable feed.

```markdown
# Media Zone | YYYY-MM-DD

> One-line framing of what mattered in social and video signal today.

## Today's signal

- Dominant story: [one-line claim naming the topic + best evidence]
- Pattern: [cross-source convergence or divergence in one line]
- Counter-signal: [practitioner pushback or skeptical thread, one line]
- Quiet area: [what's missing today, one line]
- 4-6 bullets total, ≤20 words each. Be opinionated, not neutral.

## Routing, KV cache, compression, GPU

### [Cluster name — what unifies the items]

- Compact bullet (~20-40 words): the key claim of the cluster PLUS its optimization angle (cost / influence / token) and one line of why-it-matters.
- Compact bullet: a specific number, quote, or detail from the saved post or its linked reference.
- Compact bullet: cross-source confirmation or pushback.
- (optional) Compact bullet: a practical gotcha or open question.
- 3-5 bullets max per cluster. Brief explanation, not a headline; still lighter than the wiki.

<div class="mz-thumbs">

[![Title](https://i.ytimg.com/vi/<id>/hqdefault.jpg)](https://youtube.com/watch?v=<id>)

</div>

<div class="mz-links">

[@handle1](https://x.com/...) · [@handle2](https://x.com/...) · [r/sub thread](https://reddit.com/...)

</div>

## LLMs, agents, safety
(same format)

## Multimodal / vision / audio
(same format — often empty, omit the section if so)

## Industry and business
(same format — funding rounds, product launches, hiring, policy)

## Practitioner ground truth
(Reddit-heavy section — what r/LocalLLaMA, r/MachineLearning, r/CUDA users
actually reported running. Omit if no substantive Reddit content today.)
```

### Section order (by attention tier)

1. Today's signal (always)
2. Routing / KV cache / compression / GPU (Tier 1 topics)
3. LLMs / agents / safety (Tier 2)
4. Multimodal / vision / audio (Tier 3, often skipped)
5. Industry and business
6. Practitioner ground truth (Reddit-heavy, often skipped)

Omit any section that has nothing substantive that day. Empty sections are worse than no section.

### Cluster rules

- **Cross-source preferred.** A "cluster" is at least 2 items, ideally from different sources (saved X post + its linked paper/repo + video + Reddit). Solo items can go in a cluster if they're substantive; otherwise they belong in Industry & Business as a compact item or are dropped.
- **Compact-explanatory bullets, not bare pointers and not prose paragraphs.** 3-5 bullets per cluster, each a short sentence or two (~20-40 words) that explains the item and names its optimization angle. Lighter than the wiki digest, heavier than a one-liner. The reader should finish a cluster understanding what it is and why it matters, in ~30 seconds.
- **YouTube thumbnails wrapped in `<div class="mz-thumbs">`.** This centers them on the page. Use `[![alt](https://i.ytimg.com/vi/<id>/hqdefault.jpg)](https://youtube.com/watch?v=<id>)` inside the wrapper.
- **Link rows wrapped in `<div class="mz-links">`.** Centers the link strip below the thumbnail. Use `·` separators.
- **Tweet links go to x.com,** not nitter (convert nitter→x.com in the link).
- **Reddit linked when it adds practitioner color** that the tweets/videos don't.
- **Attention tier discipline.** Routing / KV cache / compression / GPU get the most clusters. Multimodal gets a single small cluster only if there's a real story. Cluster ordering inside a section: cross-source-confirmed clusters first, then by item count, then by recency.

### What does NOT belong in Media Zone

- **Pure papers.** Those go in the Daily Digest's Deep Dives. Media Zone clusters can MENTION the paper as the topic, but the synthesis is about how social + video talked about it, not the paper's contribution.
- **Funding rounds with no social or video signal.** Those are pure Industry Pulse in the Daily Digest.
- **Solo tweets with no cluster and no substance.** Drop them.
- **Personal / off-topic tweets from AI handles.** "Office for the day" gets cut.

### Voice & length

- 3-5 compact-explanatory bullets per cluster (~20-40 words each). Lighter than the wiki digest, but with enough context that the reader understands the item without clicking through. Reader scrolls, skims headers, stops on clusters they care about and gets a real (if brief) explanation there.
- Every item leads with or names its **optimization angle** (cost / influence / token) per the optimization-lens section above.
- Same clarity rule as the daily digest: every paper or technical term gets a one-clause gloss on first mention.
- No em dashes (writing rule #1 applies).
- Total read time target: **3-4 minutes** for the full Media Zone (up from 2-3, given the added brief explanations). Still a lighter read than the wiki digest. If it runs longer than the digest, the bullets have overgrown — trim back toward compact.

### Cadence

- Written every day, including Sundays. The Daily Digest skip-day rules do NOT apply — social signal on a Sunday is its own pattern worth capturing.
- If a day has genuinely no substantive social/video signal, the file is still written with just the "Today's signal" paragraph noting the silence.

---

## Conventions

- Dates: `YYYY-MM-DD` everywhere
- Filenames: lowercase, hyphens, no spaces
- Internal links: relative markdown links (`../agentic-systems/tool-calling.md`)
- Source attribution: every summary page links to its raw file
- log.md entries start with `## [YYYY-MM-DD]` for easy grep
