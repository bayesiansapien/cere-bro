---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00
arxiv_id: 2604.22782
url: https://huggingface.co/papers/2604.22782
arxiv_url: https://arxiv.org/abs/2604.22782
date: 2026-04-28
upvotes: 4
---

# Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing

Serving transformer language models with high throughput requires caching Key-Values (KVs) to avoid redundant computation during autoregressive generation. The memory footprint of KV caching is significant and heavily impacts serving costs. While recent work has largely addressed KV cache reduction via compression and eviction along the temporal axis, the depth dimension offers an orthogonal and robust avenue for optimization.

Although prior research suggests a full cache for every layer is redundant, implementing cross-layer cache sharing remains a practical challenge; existing methods typically suffer from reduced throughput or increased time-to-first-token. This paper demonstrates that dropping a layer's cache offers efficient optimization without information loss via random cross-layer attention: during training, layers randomly choose to attend either to their own KV states or those of a preceding layer. This stochastic process adapts the model to be robust to various depth-wise cache sharing strategies, ensuring flexibility for unknown hardware constraints at deployment time. For larger models in data-constrained settings, this approach shows regularization-like effects, frequently preserving or improving performance while significantly reducing the cache's memory footprint.
