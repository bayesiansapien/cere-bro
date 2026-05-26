---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.26108
url: https://huggingface.co/papers/2605.26108
arxiv_url: https://arxiv.org/abs/2605.26108
date: 2026-05-26
---

# Reinforcing Few-step Generators via Reward-Tilted Distribution Matching

Recent advances in few-step diffusion distillation have enabled efficient image generation, yet aligning these models with human preferences remains challenging. We propose Reward-Tilted Distribution Matching Distillation (RTDMD), a two-stage framework that unifies distribution matching distillation with reward-guided reinforcement learning for few-step flow generators. We show that minimizing the KL divergence to a reward-tilted teacher distribution naturally decomposes into a distribution matching term and a reward maximization term. In the first stage, we introduce Ambient-Consistent Distribution Matching Distillation (AC-DMD), which performs subinterval-wise distribution matching and augments the fake score objective with a consistency regularizer to help the fake score model track the shifting generator distribution under limited updates. In the second stage, we jointly optimize both terms: for the reward maximization term, we derive a hybrid policy gradient that combines a GRPO-style estimator for the stochastic intermediate transitions with direct reward backpropagation through the deterministic final step, and further introduce step-subset GRPO (SubGRPO) to reduce variance. Experiments on SD3, SD3.5, and FLUX.2 demonstrate that RTDMD establishes new state-of-the-art results across preference, aesthetic, and compositional metrics with only 4 inference steps, outperforming previous few-step text-to-image generation methods. Code and models are available at https://github.com/Harahan/RTDMD.
