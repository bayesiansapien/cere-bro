---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2605.09649
url: https://huggingface.co/papers/2605.09649
arxiv_url: https://arxiv.org/abs/2605.09649
date: 2026-05-12
---

# Make Each Token Count: Towards Improving Long-Context Performance with KV Cache Eviction

The key-value (KV) cache is a major bottleneck in long-context inference, where memory and computation grow with sequence length. Existing KV eviction methods reduce this cost but typically degrade performance relative to full-cache inference. Our key insight is that full-cache attention is not always optimal: in long contexts, irrelevant tokens can dilute attention away from useful evidence, so selective, learnable eviction can improve generation rather than merely approximate the full cache. We introduce a global retention-based KV eviction method that learns each token's future utility under a unified memory budget. Lightweight retention gates assign utility scores to cached KV entries, and a shared final scoring projection calibrates these scores across all layers and heads. This enables a single global eviction policy in which tokens from different layers, heads, and modalities compete directly for cache capacity. We further provide theoretical analysis showing that preferentially retaining useful tokens reduces attention dilution, and we justify geometric retention as a query-agnostic proxy for future utility. Across diverse long-context language and vision-language reasoning, and multi-turn dialogue benchmarks, our method substantially reduces KV memory while matching or surpassing full-cache inference. These results suggest that learned, globally calibrated KV eviction is not only a compression technique, but also a mechanism for improving long-context reasoning.
