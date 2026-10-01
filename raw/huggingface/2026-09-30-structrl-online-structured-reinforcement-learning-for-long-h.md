---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36352
url: https://huggingface.co/papers/2609.36352
arxiv_url: https://arxiv.org/abs/2609.36352
date: 2026-09-30
---

# StructRL: Online Structured Reinforcement Learning for Long-Horizon Vision-Language-Action Tasks

Vision-language-action (VLA) models perform well on shorter-horizon manipulation tasks but still struggle with long-horizon tasks that require multiple dependent manipulations from a single command. Online reinforcement learning (RL) can improve these policies through environment interaction, yet many existing methods provide reward only after the complete task succeeds. However, such terminal supervision is sparse and does not distinguish early failures from rollouts that make substantial partial progress. We propose StructRL, an online RL framework that constructs structured intermediate supervision from verifiable subtask completions. StructRL decomposes each task into verifiable subtasks, grants intermediate rewards only after the prerequisite subtasks have been completed, and scales each reward according to completion pace. Across RoboCasa365 and LIBERO-Long with GR00T-N1.5 and pi 0.5, StructRL consistently outperforms evaluated online RL baselines. These results show that verifiable, structured intermediate rewards improve long-horizon VLA post-training. Code is available at https://github.com/amazon-science/StructRL.
