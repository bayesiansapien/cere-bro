---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.00623
url: https://huggingface.co/papers/2605.00623
arxiv_url: https://arxiv.org/abs/2605.00623
date: 2026-05-10
---

# Recovering Hidden Reward in Diffusion-Based Policies

This paper introduces EnergyFlow, a framework that unifies generative action modeling with inverse reinforcement learning by parameterizing a scalar energy function whose gradient is the denoising field. We establish that under maximum-entropy optimality, the score function learned via denoising score matching recovers the gradient of the expert's soft Q-function, enabling reward extraction without adversarial training. Formally, we prove that constraining the learned field to be conservative reduces hypothesis complexity and tightens out-of-distribution generalization bounds. Empirically, EnergyFlow achieves state-of-the-art imitation performance on various manipulation tasks while providing an effective reward signal for downstream reinforcement learning that outperforms both adversarial IRL methods and likelihood-based alternatives.
