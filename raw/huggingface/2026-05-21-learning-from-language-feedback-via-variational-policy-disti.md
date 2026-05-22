---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.15113
url: https://huggingface.co/papers/2605.15113
arxiv_url: https://arxiv.org/abs/2605.15113
date: 2026-05-21
---

# Learning from Language Feedback via Variational Policy Distillation

Reinforcement learning from verifiable rewards (RLVR) suffers from sparse outcome signals, creating severe exploration bottlenecks on complex reasoning tasks. Recent on-policy self-distillation methods attempt to address this by utilizing language feedback to generate dense, token-level supervision. However, these approaches rely on a fixed, passive teacher to interpret the feedback. As the student policy improves, the teacher's zero-shot assessment capabilities plateau, ultimately halting further learning. To overcome this, we propose Variational Policy Distillation (VPD), a framework that formalizes learning from language feedback as a Variational Expectation-Maximization (EM) problem. VPD co-evolves both policies: in the E-step, the teacher is actively refined on trajectory outcomes via an adaptive trust-region update, translating textual feedback into a dynamically improved target token distribution. In the M-step, the student internalizes this dense distributional guidance on its own on-policy rollouts. By continuously improving the teacher's ability to extract actionable signals from textual critique, VPD overcomes the limitations of passive distillation. Evaluated across diverse sources of diagnostic feedback on scientific reasoning and code generation tasks, VPD consistently outperforms both standard RLVR and existing self-distillation baselines. Finally, by stress-testing our framework on rigid mathematical reasoning and cold-start regimes, we illuminate the fundamental bounds of feedback-driven self-distillation compared to pure environment-driven RL.
