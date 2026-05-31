---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.29507
url: https://huggingface.co/papers/2605.29507
arxiv_url: https://arxiv.org/abs/2605.29507
date: 2026-05-31
---

# Xetrieval: Mechanistically Explaining Dense Retrieval

Explaining why dense retrievers assign high relevance scores remains challenging because retrieval decisions are made through opaque high-dimensional embeddings. Existing explanations often focus on surface signals, such as lexical matches, token alignments, or post-hoc textual rationales, and thus provide limited insight into the latent factors that shape dense retrieval behavior at the embedding level. We propose Xetrieval, an embedding-level mechanistic framework for explaining dense retrieval. Xetrieval first introduces a lightweight reasoning internalizer that approximates Chain-of-Thought reasoning directly in the embedding space with a single forward pass, enriching sentence embeddings with reasoning-oriented information while avoiding expensive autoregressive generation. It then decomposes these reasoning-enhanced embeddings into sparse, human-interpretable features, each associated with a coherent natural language description. By aggregating sparse feature overlaps across multiple document-side views, Xetrieval provides feature-level explanations of individual retrieval decisions. Experiments on diverse retrievers and benchmarks show that Xetrieval uncovers coherent interpretable features, yields stronger pair-level intervention effects, and supports task-level feature steering. The project page and source code are available at https://hihiczx.github.io/Xetrieval .
