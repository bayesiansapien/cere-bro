---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.06598
url: https://huggingface.co/papers/2610.06598
arxiv_url: https://arxiv.org/abs/2610.06598
date: 2026-10-16
---

# SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models

Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos remains challenging. Simulation offers structured motion supervision, but appearance differences hinder direct transfer, and inaccurate simulation predictions can misguide real-video generation. We present SimForcing, a simulation-guided framework that uses simulation both as a source of transferable motion knowledge and as a controllable reference for prediction. First, we transfer motion knowledge from a simulation teacher through latent-motion distillation, aligning temporal changes in latent space to internalize motion priors while mitigating the influence of appearance differences. Second, we introduce multi-block simulation conditioning with condition dropout to exploit predicted simulation trajectories without relying excessively on their accuracy. Our simulation-conditioning classifier-free guidance scheme unifies these two ideas by balancing predictions based on internalized motion knowledge with those additionally guided by simulation latents. The jointly trained student generates both simulation conditions and real-domain videos, requiring no additional world model at inference. On Bridge, SimForcing achieves the best PSNR, SSIM, LPIPS, and FVD among the compared methods without external embodied pretraining. Evaluation on InternData-A1 further supports its applicability across robot datasets. Moreover, using our trained world model to initialize a vision-language-action model improves LIBERO success, suggesting its utility for downstream policy learning. https://github.com/Wang-Xiaodong1899/SimForcing
