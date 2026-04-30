---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00Z
arxiv_id: 2604.26694
url: https://huggingface.co/papers/2604.26694
arxiv_url: https://arxiv.org/abs/2604.26694
date: 2026-04-30
---

# Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising

**Authors:** Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu

We propose X-WAM, a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis (video + 3D reconstruction) in a single framework, addressing the critical limitations of prior unified world models (e.g., UWM) that only model 2D pixel-space and fail to balance action efficiency and world modeling quality. To leverage the strong visual priors of pretrained video diffusion models, X-WAM imagines the future world by predicting multi-view RGB-D videos, and obtains spatial information efficiently through a lightweight structural adaptation: replicating the final few blocks of the pretrained Diffusion Transformer into a dedicated depth prediction branch for the reconstruction of future spatial information. Moreover, we propose Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency. ANS applies a specialized asynchronous denoising schedule during inference, which rapidly decodes actions with fewer steps to enable efficient real-time execution, while dedicating the full sequence of steps to generate high-fidelity video. Rather than entirely decoupling the timesteps during training, ANS samples from their joint distribution to align with the inference distribution. Pretrained on over 5,800 hours of robotic data, X-WAM achieves 79.2% and 90.7% average success rate on RoboCasa and RoboTwin 2.0 benchmarks, while producing high-fidelity 4D reconstruction and generation surpassing existing methods in both visual and geometric metrics.

## Key contributions

- **X-WAM architecture**: Unifies robotic action execution and 4D world synthesis (multi-view RGB-D video + 3D reconstruction) in one framework.
- **Depth prediction branch**: Lightweight structural adaptation — replicates final few blocks of pretrained Diffusion Transformer for depth prediction, avoiding full retraining.
- **Asynchronous Noise Sampling (ANS)**: Decoupled denoising schedule — fewer steps for fast action decoding, full steps for high-fidelity video; trained on joint timestep distribution to prevent inference distribution shift.
- **Scale**: Pretrained on 5,800+ hours of robotic data.
- **Results**: 79.2% on RoboCasa, 90.7% on RoboTwin 2.0; surpasses prior methods on visual and geometric metrics.
