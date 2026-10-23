---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.195715+00:00
arxiv_id: 2610.28909
url: https://huggingface.co/papers/2610.28909
arxiv_url: https://arxiv.org/abs/2610.28909
date: 2026-10-22
---

# DiffResearch: Accelerating Deep Research with Diffusion Language Models

Deep research systems iteratively plan, gather evidence, synthesize, and revise, making end-to-end latency a key bottleneck for interactive use. Almost all production systems are built on autoregressive (AR) language models and inherit left-to-right decoding in planning and long-form writing. We present DiffResearch, an open multi-agent deep research framework that places a diffusion language model (dLLM) at the core of every stage, and measure how a diffusion backbone changes latency and report quality. Holding the agentic scaffold, retrieval code, prompts, and evaluation fixed, we swap the backbone between an open diffusion model and a comparable AR model. Across 100 Deep Research Bench tasks, the diffusion backbone is roughly 6 times faster end-to-end, driven by order-of-magnitude reductions in planning and writing. We further introduce dFast, a decomposition mode that reads intermediate denoising states and extracts subqueries before generation finishes, providing a 1.99 times median speedup for decomposition in isolation with no loss of report quality. On the benchmark's RACE rubric, dFast obtains the best overall score among the three configurations. Finally, in a public system-level leaderboard snapshot, an instance built on a stronger diffusion model ranks above several commercial systems. We release DiffResearch under an Apache-2.0 license.
