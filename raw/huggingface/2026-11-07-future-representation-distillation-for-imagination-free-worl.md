---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.593052+00:00
arxiv_id: 2611.04527
url: https://huggingface.co/papers/2611.04527
arxiv_url: https://arxiv.org/abs/2611.04527
date: 2026-11-07
---

# Future Representation Distillation for Imagination-free World Action Models

World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction. However, iterative video denoising is costly, and inaccurate visual predictions can compromise action prediction. Our key idea is to make this predictive knowledge available through visual representations computed from the current observation, enabling action prediction without generating future videos. We introduce DreamFree, a WAM that repurposes a pretrained video diffusion model as a predictive visual encoder through representation distillation. The visual encoder learns to predict a frozen video diffusion model's representation using only the current observation. An action module is then trained to predict actions by extracting action-relevant information from the visual encoder. Across real-world and simulated tasks, DreamFree achieves higher success rates than state-of-the-art VLAs and WAMs, while performing real-time closed-loop control at 11Hz with a 14B video diffusion backbone. Experiments show that DreamFree can translate stronger video priors and additional video data into better robot control and enable learning new robot tasks from video demonstrations, including videos from a different embodiment, without action annotation for the new tasks.
