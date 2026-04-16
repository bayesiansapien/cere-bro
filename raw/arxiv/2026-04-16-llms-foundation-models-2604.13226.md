---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13226
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13226
published: 2026-04-16
authors: Chuangtao Chen, Grace Li Zhang, Xunzhao Yin
---

# KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs

**arXiv:** https://arxiv.org/abs/2604.13226
**Authors:** Chuangtao Chen, Grace Li Zhang, Xunzhao Yin

## Abstract

arXiv:2604.13226v1 Announce Type: cross  Abstract: Large Language Models (LLMs) rely heavily on Key-Value (KV) caching to minimize inference latency. However, standard KV caches are context-dependent: reusing a cached document in a new context requires recomputing KV states to account for shifts in attention distribution. Existing solutions such as CacheBlend, EPIC, and SAM-KV mitigate this issue by selectively recomputing a subset of tokens; however, they still incur non-negligible computational overhead (FLOPs) and increased Time-to-First-Token (TTFT) latency. In this paper, we propose KV Packet, a recomputation-free cache reuse framework that treats cached documents as immutable ``packets'' wrapped in light-weight trainable soft-token adapters, which are trained via self-supervised distillation to bridge context discontinuities. Experiments on Llama-3.1 and Qwen2.5 demonstrate that the proposed KV Packet method achieves near-zero FLOPs and lower TTFT than recomputation-based baselines, while retaining F1 scores comparable to those of the full recomputation baseline.
