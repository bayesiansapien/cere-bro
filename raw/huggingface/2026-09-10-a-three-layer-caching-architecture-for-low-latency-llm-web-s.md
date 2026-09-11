---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2609.05463
url: https://huggingface.co/papers/2609.05463
arxiv_url: https://arxiv.org/abs/2609.05463
date: 2026-09-10
---

# A Three-Layer Caching Architecture for Low-Latency LLM Web Search on Commodity CPU Hardware

AI-powered search products such as ChatGPT search, Google's AI Overviews, and Perplexity provide LLM-synthesized answers grounded in live web results. We developed OreoLook (formerly lixSearch), an open-source answer engine using automated browser agents and provider-routed LLM inference. Its local search, caching, session-management, and embedding stack runs on commodity CPU hardware; answer synthesis is performed by a remote inference provider. As usage grew, sessions lost context, equivalent queries triggered redundant work, and URLs were repeatedly embedded across sessions.
  We present a three-layer caching architecture: (1) a Session Context Window maintaining a rolling window of recent messages in Redis with automatic overflow to Huffman-compressed disk archives; (2) a Semantic Query Cache catches rephrasings via cosine similarity on embedding vectors, eliminating redundant LLM invocations; and (3) a URL Embedding Cache that deduplicates embedding computations across sessions. Deployed on a single 8-vCPU Intel Cascade Lake server (2 GHz, 32 GB RAM) running 30 Hypercorn worker processes across three containerized replicas, the evaluated system reported an 89.3% aggregate Redis keyspace hit rate with 0.1 ms read latency and just 1.38 MB of memory overhead. A background LRU eviction daemon migrates idle sessions from Redis to disk and re-hydrates them on demand, enabling conversations that can be resumed hours or days later under the configured retention policy.
