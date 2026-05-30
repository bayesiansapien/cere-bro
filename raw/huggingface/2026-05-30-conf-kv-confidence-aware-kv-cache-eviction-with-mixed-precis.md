---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.24786
url: https://huggingface.co/papers/2605.24786
arxiv_url: https://arxiv.org/abs/2605.24786
date: 2026-05-30
---

# CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM

Long-horizon LLM inference turns the key--value (KV) cache into the dominant GPU memory consumer and makes per-token attention increasingly expensive. Many common eviction policies use static recency windows or historical attention, leaving unused a signal computed on every decoding step: the model's current uncertainty. We introduce CONF-KV, a KV-cache manager that converts the next-token distribution into a scalar confidence score and uses it to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively when it is confident. Within each budget, tokens are ranked by a composite of accumulated attention mass and recency, while a protected recent window preserves local coherence. We combine the policy with blockwise online-softmax attention, mixed FP16/INT8 storage, and a pyramidal per-layer budget variant. Across four model families and generated lengths up to 4K, CONF-KV stays near the footprint of a fixed 512-token sliding window while remaining within 1.5--2.1 perplexity points of full KV. On Needle-in-a-Haystack up to 32K tokens, CONF-KV reaches 91.4% retrieval accuracy versus 53.8% for sliding windows and 80.6% for H2O; on 75 VisualWebArena tasks it retains 95.3% of full-KV success at 2.8 times lower peak memory.
