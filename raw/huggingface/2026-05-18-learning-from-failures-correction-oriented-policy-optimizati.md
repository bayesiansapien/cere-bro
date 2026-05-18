---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.14539
url: https://huggingface.co/papers/2605.14539
arxiv_url: https://arxiv.org/abs/2605.14539
date: 2026-05-18
---

# Learning from Failures: Correction-Oriented Policy Optimization with Verifiable Rewards

Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as an effective paradigm for improving the reasoning capabilities of large language models. However, RLVR training is often hindered by sparse binary rewards and weak credit assignment, resulting in ambiguous optimization signals and underutilization of the useful information embedded in failed trajectories. To address this challenge, we propose Correction-Oriented Policy Optimization (CIPO), a simple and effective extension to RLVR that converts on-policy failed trajectories into correction-oriented supervision, without relying on any external signals. By jointly optimizing correction samples derived from the model's own failed attempts together with the standard RLVR objective, CIPO improves learning effectiveness while explicitly enhancing the model's ability to correct its own errors. Extensive experiments across 11 benchmarks spanning mathematical reasoning and code generation demonstrate that CIPO consistently and significantly outperforms strong baselines in both reasoning and correction performance. Moreover, CIPO yields stronger pass@K gains, indicating that it improves the model's intrinsic reasoning capacity rather than merely redistributing probability mass over existing correct answers.
