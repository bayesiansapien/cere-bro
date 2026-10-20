---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.09221
url: https://huggingface.co/papers/2610.09221
arxiv_url: https://arxiv.org/abs/2610.09221
date: 2026-10-19
---

# Consistent Distribution Matching for Data-Free Diffusion Distillation

Flow and diffusion models suffer from slow inference due to computationally expensive numerical integration. Distillation provides a promising way for a student model to learn from a teacher's dynamics, enabling one-step or few-step generation. However, existing methods often depend on curated distillation datasets, costly teacher rollouts, or auxiliary proxy networks, which complicate model training and scaling. In this work, we propose Consistent Distribution Matching, a simulation-free and data-free distillation method for accelerating diffusion and flow models while preserving strong generative capacity. Our key insight is to unify sample generation and score estimation with one student network. Thus, our framework uses only two models, a frozen teacher and a trainable student, and optimizes one objective. We prove that minimizing our objective indicates Wasserstein convergence of the student flow-map pushforwards to the teacher marginals. On ImageNet 256times256, our method attains an FID of 2.04 with a single function evaluation (1-NFE) and a 4-NFE FID of 1.37 within 40 epochs of training, surpassing the state-of-the-art distillation baselines without data. Our code code and model are available at https://consistentdmd.github.io/.
