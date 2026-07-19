# Model Routing Is Simple. Until It Isn't. (IBM Research)

**Source:** HuggingFace Blog (IBM Research), via RSS | **Date:** 2026-07-15 | **URL:** https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt

## TL;DR

Model-selection routing is usually framed as a classification problem: send easy queries to cheap models, hard queries to expensive ones. IBM Research argues this framing is wrong. Routing is a **system-optimization problem** across cost, quality, and latency simultaneously, and the naive version ignores three hidden factors that dominate real outcomes: cache-read pricing, invisible task difficulty, and infrastructure-level latency. Their optimization-based router stays lightweight enough not to become its own bottleneck. On AppWorld with CodeAct agents, a latency-optimized configuration hit 84% accuracy at $93 / 83s: a 21% cost reduction and 9% latency reduction versus Opus alone, for a 4% accuracy drop.

## Key points

- **Caching beats sticker pricing.** Across 417 tasks, Claude Sonnet cost $79 total while GPT-4.1 cost $155 (nearly double), despite GPT-4.1's lower per-token sticker prices. The difference was Sonnet's superior cache-read pricing on agent workloads that reuse context heavily. Sticker price is the wrong routing signal for agentic (context-reuse) workloads.
- **Task difficulty is invisible at routing time.** "Summarize this contract" looks simple but may trigger retrieval, compliance checks, and multiple refinement rounds. A technical-looking prompt might be one-shot by a small specialist. You cannot read difficulty off the surface form of the request.
- **Infrastructure dominates latency.** Which hardware a model runs on, whether the cache is warm, and how busy the endpoint is often matter more for end-to-end latency than the model's nominal speed.
- **Routing as optimization, not classification.** The proposed router optimizes cost/quality/latency jointly while staying lightweight, rather than learning a query→model classifier.

## Relation to prior wiki knowledge

- **Direct pair with "When Is Routing Meaningful?" (2026-07-20, DeepMind).** DeepMind asks whether a router is doing anything (diversity + stability diagnostics); IBM asks whether a router is optimizing the right objective (system cost, not sticker price). Together they reframe routing evaluation: not just "is it accurate?" but "is it meaningful?" (DeepMind) and "is it optimizing the real cost surface?" (IBM).
- **Extends the routing-decision-locus thread** (TraceR model-level, MinT adapter-level, CaRE/BEAM expert-level): this adds the *objective* axis. Even a well-placed routing decision optimizes the wrong thing if it uses sticker price instead of cache-adjusted system cost.
- **Confirms the cache-economics thread.** The Claude Sonnet cache-read advantage echoes the July 8 Fable-5-orchestrator economics (independent caches for sub-agents) and the Byte-Exact KV-Cache Grafting reuse story (07-17): cache economics, not raw token price, is increasingly the deciding cost factor.

## Gaps

Single vendor's framing (IBM Research). The $79-vs-$155 figure is from one 417-task workload; how it generalizes across task mixes is untested. The optimization router's overhead ("lightweight enough") is asserted, not quantified against the routing decisions it makes.

## Research angle

The objective-design axis is underexplored: most routing research optimizes accuracy-at-cost using sticker price. A router that models cache state (warm vs cold), endpoint load, and hardware placement as part of its cost function is a genuinely different object. Compose with DeepMind's HSE diagnostic: a router optimized for cache-adjusted system cost AND diversity/stability would be the first to satisfy both the "meaningful" and the "optimizing-the-real-cost" tests.

## Raw source

RSS feed `huggingface-blog`, `raw/rss/2026-07-15-huggingface-blog-model-routing-is-simple-until-it-isn-t.md` (title-only in feed; body fetched from the live blog).
