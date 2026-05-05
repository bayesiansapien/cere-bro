---
source: farmer/huggingface
farmed: 2026-05-05T00:00:00
arxiv_id: 2605.02730
url: https://huggingface.co/papers/2605.02730
arxiv_url: https://arxiv.org/abs/2605.02730
date: 2026-05-05
---

# Perceptual Flow Network for Visually Grounded Reasoning

Despite advances in Large-Vision Language Models, standard training objectives like MLE inadequately constrain visual trajectories, resulting in language bias and hallucination issues. Existing approaches add geometric priors from visual experts as supplementary supervision, but these prove suboptimal, emphasizing geometric accuracy over reasoning effectiveness.

The authors introduce Perceptual Flow Network (PFlowNet), which avoids rigid alignment with expert priors to enable interpretable and more effective visual reasoning. The method separates perception from reasoning, establishing a self-conditioned generation framework. It combines multi-dimensional rewards with nearby geometric shaping through variational reinforcement learning, promoting reasoning-focused perceptual behaviors while maintaining visual fidelity.

The approach provides theoretical performance guarantees and achieves strong empirical outcomes, establishing new state-of-the-art records on V* Bench (90.6%) and MME-RealWorld-lite (67.0%).
