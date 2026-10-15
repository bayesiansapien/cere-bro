---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.503906+00:00
arxiv_id: 2610.17552
url: https://huggingface.co/papers/2610.17552
arxiv_url: https://arxiv.org/abs/2610.17552
date: 2026-10-14
---

# FlashVSR+: Efficient Video Super-Resolution via Hybrid Attention and Reward-Yield Distribution Matching

Recent video super-resolution (VSR) models achieve efficient one-step generation through diffusion distillation. However, high-resolution inference remains costly, and distilled models are difficult to align with human preferences. These challenges call for improvements in both model architecture and training strategy. We present FlashVSR+ to address both limitations. On the architecture side, we introduce hybrid attention based on the strong locality observed in pretrained VSR models, while retaining sparse global interaction for long-range consistency. It achieves up to 2times DiT speedup and 45\% lower peak memory, enabling spatially untiled 4K VSR on a single 24GB RTX 4090. On the training side, we propose Reward-Yield Distribution Matching Distillation (Ry-DMD) for preference-aligned one-step generation. Ry-DMD uses reward-weighted teacher rollouts to incorporate black-box rewards into distribution matching, without backpropagating through the reward model. We further show that Ry-DMD generalizes beyond VSR to T2I generation. Together, FlashVSR+ delivers stronger restoration quality and substantially improves high-resolution efficiency, with consistent gains in user preference. We release our code, models, and training data at https://www.flashvsr.tech{FlashBlue{www.flashvsr.tech}}.
