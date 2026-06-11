---
source: farmer/huggingface
farmed: 2026-06-11T08:27:36Z
arxiv_id: 2606.09076
url: https://huggingface.co/papers/2606.09076
arxiv_url: https://arxiv.org/abs/2606.09076
date: 2026-06-11
---

# Beyond Scalar Rewards by Internalizing Reasoning into Score Distributions

Reward models are central to text-to-image post-training, but visual preference is subjective and better represented as a distribution over rubric scores than as a deterministic scalar. Existing scalar, score-token, and pairwise reward models over-compress uncertainty and fine-grained score differences, while reasoning-based generative rewards provide stronger judgments but are costly to deploy and difficult to use as direct optimization signals. We propose Z-Reward, a teacher-student reward modeling framework that decouples reasoning-heavy judgment from efficient reward deployment. The teacher is a large VLM that uses reasoning to infer rubric-aligned score distributions, and is trained with Group-wise Direct Score Optimization (GDSO), which combines policy-gradient rewards from distribution expectations with direct pointwise and pairwise supervision on score distributions and score gaps. The student is trained with Reasoning-Internalized Score Distillation (RISD), which transfers the teacher's reasoning-conditioned score distribution into a compact VLM without requiring explicit reasoning chains at inference time. On our internally annotated evaluation set, the 27B GDSO teacher reaches 89.6% human preference accuracy, outperforming SFT, RewardDance, and GRPO, while the 9B RISD student reaches 88.6%, outperforming the OPD baseline and closely matching the larger teacher. We further show that Z-Reward can serve as a differentiable reward signal for text-to-image optimization, yielding a 41.3% net human-preference improvement over the SFT baseline.
