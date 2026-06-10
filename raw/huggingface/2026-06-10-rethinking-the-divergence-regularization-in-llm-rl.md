---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.09821
url: https://huggingface.co/papers/2606.09821
arxiv_url: https://arxiv.org/abs/2606.09821
date: 2026-06-10
---

# Rethinking the Divergence Regularization in LLM RL

Reinforcement learning (RL) has become a key component of post-training large language models (LLMs). In practice, LLM RL is often off-policy because of training-inference mismatch and policy staleness, making trust-region control essential for stable optimization. Mainstream methods such as PPO and GRPO approximate this control with a ratio-clipping mechanism, but the importance ratio can be a poor proxy for distributional shift in long-tailed vocabularies. Recent work such as DPPO addresses this mismatch by replacing ratio-based clipping with a divergence-based mask, yielding a trust region defined by the sampled token's absolute probability shift. However, DPPO still relies on a hard mask: once a token crosses the trust-region boundary in a harmful direction, its gradient is discarded rather than corrected. To address this, we propose Divergence Regularized Policy Optimization (DRPO), which replaces the hard mask with a smooth advantage-weighted quadratic regularizer on policy shift. DRPO preserves the same trust-region geometry as DPPO while inducing bounded, continuous gradient weights that attenuate diverging updates and provide corrective signals beyond the boundary. Experiments across model scales, architectures, and precision settings show that DRPO improves the stability and efficiency of LLM RL training.
