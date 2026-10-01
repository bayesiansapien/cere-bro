---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37147
url: https://huggingface.co/papers/2609.37147
arxiv_url: https://arxiv.org/abs/2609.37147
date: 2026-09-30
---

# Improved Distributional Diffusion Models

Distributional Diffusion Models (DDMs) replace the standard mean-prediction denoiser with a distributional denoiser trained via a scoring rule objective, learning a stochastic approximation to p(x_1 mid x_t) rather than its conditional mean. However, scaling DDMs to modern image-generation settings faces two obstacles: (i) multi-particle training incurs overhead that scales with the number of particles, (ii) DDMs use globally fixed scoring rule hyperparameters, forcing a single trade-off across sampling budgets. We mitigate these limitations by deferring particle expansion to late transformer layers, and the hyperparameter trade-off by introducing time-dependent scoring rule schedules informed by the dynamical regimes of~Biroli2024. Combined with a DiT-based latent setup, these changes make DDM training practical on class-conditional ImageNet-256^2, achieving 4.48 FID at 4 steps and 2.38 at 50 steps with DiT-XL/2, from a single model trained from scratch in one stage, without a teacher, self-distillation or JVPs. The result is a stochastic few-step generator whose FID does not degrade as the sampling budget grows from 4 to 50 NFE, and the same recipe transfers to text-to-image generation. Code and pre-trained models available at https://github.com/CompVis/iDDM.
