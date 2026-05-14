---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.13724
url: https://huggingface.co/papers/2605.13724
arxiv_url: https://arxiv.org/abs/2605.13724
date: 2026-05-14
---

# AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation

Few-step video generation has been significantly advanced by consistency distillation. However, the performance of consistency-distilled models often degrades as more sampling steps are allocated at test time, limiting their effectiveness for any-step video diffusion. This limitation arises because consistency distillation replaces the original probability-flow ODE trajectory with a consistency-sampling trajectory, weakening the desirable test-time scaling behavior of ODE sampling. To address this limitation, we introduce AnyFlow, the first any-step video diffusion distillation framework based on flow maps. Instead of distilling a model for only a few fixed sampling steps, AnyFlow optimizes the full ODE sampling trajectory. To this end, we shift the distillation target from endpoint consistency mapping (z_t to z_0) to flow-map transition learning (z_t to z_r) over arbitrary time intervals. We further propose Flow Map Backward Simulation, which decomposes a full Euler rollout into shortcut flow-map transitions, enabling efficient on-policy distillation that reduces test-time errors (i.e., discretization error in few-step sampling and exposure bias in causal generation). Extensive experiments across both bidirectional and causal architectures, at scales ranging from 1.3B to 14B parameters, demonstrate that AnyFlow achieves performance matches or surpasses consistency-based counterparts in the few-step regime, while scaling with sampling step budgets.
