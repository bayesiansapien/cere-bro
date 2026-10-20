---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.19636
url: https://huggingface.co/papers/2610.19636
arxiv_url: https://arxiv.org/abs/2610.19636
date: 2026-10-19
---

# Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching

Large language models (LLMs) hold broad knowledge in one set of weights, but lack interpretability and trustworthy reasoning, especially in high-stakes use cases. A neuro-symbolic model, with its interpretable architecture and System 2 reasoning capacity, is a promising alternative if built at the scale of LLMs; however, its symbolic backbone is usually constructed with human effort, so existing neuro-symbolic models are bottlenecked by the scope of the symbol component and usually domain-specific. A data-driven method could instead build a larger symbolic system by aligning and merging existing ones. We target its first, foundational step: matching units across these heterogeneous systems. Our method, SAE-IDF, encodes a symbol in its native context into a sparse code with a sparse autoencoder (SAE), re-weights each dimension by its rarity and matches across systems. On 12 tasks across 6 kinds of symbolic system, SAE-IDF outperforms the same LLM's dense baseline on all tasks with Gemma-2-9B and all but one with Llama-3.1-8B, by up to 45 points, consistently across SAE layers and configurations. SAE-IDF is also interpretable: every dimension of the sparse code has a human-readable meaning, so each match decomposes into named concepts (features). Our work paves the way to a universal symbolic backbone.
