---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.16281
url: https://huggingface.co/papers/2606.16281
arxiv_url: https://arxiv.org/abs/2606.16281
date: 2026-06-16
---

# Who Should Lead Decoding Now? Tracking Reliable Trajectories for Ensembling Masked Diffusion Language Models

Masked Diffusion Language Models (MDLMs) have emerged as a distinct paradigm for sequence generation. As MDLMs become diverse in capabilities and knowledge coverage, an important question is how to combine their knowledge. Toward this, we first investigate the unique decoding dynamics of MDLMs. We find that successful generations exhibit stable confidence dynamics over answer-relevant positions, while unreliable trajectories can often be corrected by injecting promising intermediate states from other models. Guided by this observation, we propose TIE (Trajectory-based Iterative Ensembling), a knowledge fusion framework in which MDLMs iteratively identify reliable decoding trajectories and relay them across models. TIE tracks confidence dynamics over answer-relevant positions to determine which model currently follows a more reliable trajectory and selectively transfers partially denoised sequences across models. As the model on the more promising trajectory often changes across denoising steps, TIE allows different models to contribute complementary strengths at different stages of generation. Strong performance across diverse reasoning tasks, along with our analyses, suggests that TIE offers a practical approach to the underexplored problem of MDLM ensembling.
