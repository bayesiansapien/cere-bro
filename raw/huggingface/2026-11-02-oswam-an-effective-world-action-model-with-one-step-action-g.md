---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.497675+05:30
arxiv_id: 2610.35850
url: https://huggingface.co/papers/2610.35850
arxiv_url: https://arxiv.org/abs/2610.35850
date: 2026-11-02
---

# OSWAM: An Effective World Action Model with One-Step Action Generation

Direct-policy World Action Models (WAM) have demonstrated the benefits of decoupling action generation from explicit future visual prediction for efficient inference in autonomous driving and embodied control. However, they still require tens of denoising steps to achieve competitive action quality, incurring substantial latency and hindering real-time deployment. Simply reducing the number of denoising steps will collapse the nonlinear multi-step denoising trajectory into coarse updates, substantially degrading action quality. To reduce the denoising steps while enabling real-time action generation, we present an effective world action model with one-step action generation, namely OSWAM, for autonomous driving and embodied control. We argue that it is the absence of structured action priors in random noise initialization that forces direct-policy WAMs to recover coherent action sequences through iterative denoising. Hence, we construct imagination tokens to initialize the diffusion process, providing physical priors and action-conditioned representations. We further introduce privileged information distillation with future conditioning to enhance future-aware action generation. As a result, OSWAM can efficiently and effectively generate high quality actions in just one diffusion step. Our experiments demonstrate that OSWAM achieves comparable or even better results in both autonomous driving and embodied control than direct-policy WAM and Joint-WAM that require tens of steps. It obtains approximately 3times speedup over direct-policy WAM baselines and supports real-time compiled inference with latency as low as 40ms on an NVIDIA RTX 5090 GPU. The project page is available at https://gwenzhang.github.io/OSWAM/
