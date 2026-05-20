---
source: farmer/huggingface
farmed: 2026-05-20T09:54:42.723267+00:00
arxiv_id: 2605.09640
url: https://huggingface.co/papers/2605.09640
arxiv_url: https://arxiv.org/abs/2605.09640
date: 2026-05-20
---

# Overcoming Catastrophic Forgetting in Visual Continual Learning with Reinforcement Fine-Tuning

Recent studies suggest that Reinforcement Fine-Tuning (RFT) is inherently more resilient to catastrophic forgetting than Supervised Fine-Tuning (SFT). However, whether RFT (e.g., GRPO) can effectively overcome forgetting in challenging visual continual learning settings, such as class-incremental learning (CIL) and domain-incremental learning (DIL), remains an open problem. Through a pilot study, we confirm that while RFT consistently outperforms SFT, it still suffers from non-negligible forgetting. We empirically trace this bottleneck to Trajectory-level Drift Agnosticism: among candidate rollouts achieving identical task rewards, the KL divergence from the preceding-task policy varies substantially, which strongly correlates with catastrophic forgetting across sequential tasks. Motivated by this insight, we propose Retention-aware Policy Optimization (RaPO), a simple yet effective RFT method that explicitly mitigates forgetting through trajectory-level reward shaping. Specifically, RaPO comprises two core components: (1) Retention Reward that converts trajectory-level distribution drift into a continuous reward signal, preferentially reinforcing knowledge-preserving rollouts within each group; (2) Cross-Task Advantage Normalization (CTAN), which maintains a persistent exponential moving average of reward statistics across task boundaries to stabilize the optimization progress during continual learning. Leveraging the free-form textual generalization of MLLMs, we comprehensively evaluate RaPO across five visual continual learning settings. Extensive experiments demonstrate that RaPO achieves leading performance, substantially reducing catastrophic forgetting while preserving strong plasticity. To the best of our knowledge, this work represents the first systematic exploration of RFT in visual continual learning, offering insights that we hope will inspire future research.
