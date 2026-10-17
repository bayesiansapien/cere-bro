---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.16105
url: https://huggingface.co/papers/2610.16105
arxiv_url: https://arxiv.org/abs/2610.16105
date: 2026-10-16
---

# Beyond Policy Rollouts: Embedding-Space Directional Exploration with Anchored Noise for LLM RLVR

Reinforcement learning with verifiable rewards (RLVR) typically uses small rollout groups per prompt, where repeated sampling from the same policy can yield highly similar trajectories, reducing within-group reward variation and weakening group-relative advantage signals. Existing remedies such as higher sampling temperature, entropy bonuses, asymmetric clipping, and larger rollout budgets broaden sampling or modify policy updates but leave rollout conditioning unchanged. In this paper, we propose EDEN (Embedding-space Directional Exploration via anchored Noise), which intervenes at the rollout source through anchored input perturbations. EDEN explores beyond the policy's own rollouts. Within the same rollout budget, it replaces a small fraction of standard rollouts in each group with rollouts that the same policy generates from the prompt plus a single appended, perturbed embedding position, rather than from the prompt alone. Gaussian noise drives variation, while a shared anchor provides a common conditioning direction within each prompt group. Selected perturbed rollouts contribute to GRPO updates with downweighted advantages, and the model architecture, discrete decoding, and test-time inference remain unchanged. Across model scales and mathematical reasoning benchmarks, EDEN outperforms GRPO and the exploration controls evaluated in the same pipeline, with the largest gains in sampled solution coverage. Analyses show that more prompt groups provide non-zero group-relative learning signals and that noise and anchoring play complementary roles. Intervening at the rollout source is thus an effective lever for exploration in RLVR.
