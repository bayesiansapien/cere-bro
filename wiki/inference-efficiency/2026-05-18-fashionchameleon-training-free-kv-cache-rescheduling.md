# FashionChameleon: Training-Free KV Cache Rescheduling for Interactive Video Customization

**Date ingested:** 2026-05-18
**Source:** HuggingFace Daily Papers 2026-05-18
**arXiv:** [2605.15824](https://arxiv.org/abs/2605.15824)
**Tier:** 1 (KV cache, autoregressive video generation)
**Raw:** [raw/huggingface/2026-05-18-fashionchameleon-...md](../../raw/huggingface/2026-05-18-fashionchameleon-towards-real-time-and-interactive-human-gar.md)

## TL;DR

FashionChameleon delivers real-time interactive human-garment video customization with three contributions. A Teacher Model with In-Context Learning trains on reference-garment image pairs. Streaming Distillation introduces in-context teacher forcing that eliminates the data-intensive ODE initialization step and uses gradient-reweighted distribution matching distillation to stabilise long-video extrapolation. The Tier-1-relevant contribution is Training-Free KV Cache Rescheduling for interactive multi-garment switching, which composes three mechanisms: garment KV refresh, historical KV withdraw, and reference KV disentangle. The system runs at 720p / 23.8 FPS on a single H200 GPU.

## Why it matters (Tier 1 lens)

The wiki's KV cache thread has been tracking three orthogonal compression and routing axes: learned eviction (Make Each Token Count 2026-05-12, the paper that scored each cached entry with a small projection and showed selective retention can surpass the full cache), head-role compression (Forcing-KV 2026-05-15, the head-role-conditioned KV cache compression for video diffusion that found static heads tolerate aggressive pruning while dynamic heads do not), and architectural sharing (Gemma 4's cross-layer KV sharing surveyed by Raschka 2026-05-17).

FashionChameleon adds a fourth axis: **content-aware KV cache rescheduling** for autoregressive video generation. The three mechanisms together address the fundamental challenge of interactive multi-condition video generation: when a user switches a garment mid-sequence, the cache must simultaneously refresh entries pertaining to the new garment, withdraw entries that encoded the old garment, and disentangle entries that came from reference inputs versus generated history. This is not eviction (which entry to drop), not compression (how many bits per entry), and not sharing (which layers reuse). It is the cache-as-state-machine view: which entries belong to which causal conditioning thread.

## Connection to prior wiki context

**Forcing-KV (2026-05-15).** Forcing-KV separated heads by static vs dynamic functional role in video diffusion. FashionChameleon separates entries by causal-conditioning role (garment vs history vs reference). The two are orthogonal and compose: route the cache by head role (Forcing-KV) within each conditioning thread (FashionChameleon).

**Stream-T1 (2026-05-07).** Stream-T1 introduced reward-feedback-guided KV eviction for streaming video diffusion. FashionChameleon's cache rescheduling is the multi-conditioning generalisation: when there is only one conditioning thread, Stream-T1's reward signal is sufficient; when there are multiple, you need to track which thread each entry serves.

**MotionCache (2026-05-05) and Make Each Token Count (2026-05-12).** Cache eviction as a quality intervention rather than a compression tradeoff. FashionChameleon adds the interactive-customization dimension to that frame.

## Research angle

Whether the three-mechanism rescheduling pattern (refresh / withdraw / disentangle) generalises to multi-thread text generation (multi-document QA, multi-tool agentic conversations) is the natural extension. The wiki has no entry yet for KV cache rescheduling in text. This is the candidate template.

## Links

- arXiv: <https://arxiv.org/abs/2605.15824>
- Related: [Forcing-KV 2026-05-15](2026-05-15-forcing-kv-video-diffusion-kv-cache-compression.md), [Stream-T1 2026-05-07](2026-05-07-stream-t1-test-time-scaling-streaming-video.md), [Make Each Token Count 2026-05-12](2026-05-12-make-each-token-count-kv-eviction.md), [kv-cache concept](kv-cache.md)
