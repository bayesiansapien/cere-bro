---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.887726+00:00
arxiv_id: 2610.25376
url: https://huggingface.co/papers/2610.25376
arxiv_url: https://arxiv.org/abs/2610.25376
date: 2026-10-23
---

# TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models

Large-scale action pretraining equips Embodied Foundation Models (EFMs) with strong manipulation capabilities, with particular strengths in generalization and closed-loop robustness, but reproducing such pretraining requires substantial robot data and computation. To transfer these capabilities from pretrained EFMs to policies without action pretraining, we introduce TILDE (Teacher-In-the-Loop Distillation from EFMs), which synergizes on-policy distillation at student-induced states with learning from teacher-executed recovery trajectories. We further propose AutoDAgger, an autonomous data aggregation pipeline in which a robotic reward model is utilized to monitor task progress and trigger teacher intervention, thereby collecting recovery experience without human monitoring or manual control. AutoDAgger accelerates recovery-trajectory collection by more than 2times compared with the human-in-the-loop method. By unifying learning from demonstrations, on-policy teacher supervision, and teacher's corrective behavior, TILDE improves task performance by up to 4.1times over behavior cloning across three real-world tasks and supports effective cross-architecture distillation.
