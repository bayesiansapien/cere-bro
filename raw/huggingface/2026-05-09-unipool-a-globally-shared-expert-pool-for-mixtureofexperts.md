---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06665
url: https://huggingface.co/papers/2605.06665
arxiv_url: https://arxiv.org/abs/2605.06665
date: 2026-05-09
---

# UniPool: A Globally Shared Expert Pool for Mixture-of-Experts

Modern Mixture-of-Experts (MoE) architectures allocate expert capacity through a rigid per-layer rule: each transformer layer owns a separate expert set. We propose UniPool, an MoE architecture that treats expert capacity as a global architectural budget by replacing per-layer expert ownership with a single shared pool accessed by independent per-layer routers. To enable stable and balanced training under sharing, we introduce a pool-level auxiliary loss that balances expert utilization across the entire pool, and adopt NormRouter to provide sparse and scale-stable routing into the shared expert pool. Across five LLaMA-architecture model scales (182M to 978M parameters) trained on 30B tokens from the Pile, UniPool consistently improves validation loss and perplexity over matched vanilla MoE baselines.
