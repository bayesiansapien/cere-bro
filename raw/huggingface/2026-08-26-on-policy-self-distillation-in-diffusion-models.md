---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.24646
url: https://huggingface.co/papers/2608.24646
arxiv_url: https://arxiv.org/abs/2608.24646
date: 2026-08-26
upvotes: 35
---

# On-Policy Self-Distillation in Diffusion Models

Reinforcement learning can align diffusion models with human preferences and task-specific objectives, but endpoint rewards do not specify how an intermediate denoising prediction should change. We introduce DiffusionOPSD as an on-policy self-distillation framework that converts image-level reward guidance into explicit targets for clean-output predictions at sampled queries. At each outer iteration, a frozen behavior policy generates trajectories and supplies query states and anchors. Reward gradients construct bounded positive and negative targets around each anchor. The trainable policy fits these targets as detached supervision through finite fitting before an exponential moving average update refreshes the behavior policy. This setup lets us measure target construction and finite realization separately. Controlled same-query experiments show that larger target-construction gains do not necessarily translate into larger realized gains after a single fitting update. Across SD 3.5-M and the step-distilled Z-Image-Turbo, our approach achieves the best final held-out scores in 19 of 20 reward-matched settings across two backbones and ten evaluators. It outperforms the strongest competing method by up to 44.0% and reduces training GPU-hours relative to DiffusionNFT by 40% on SD 3.5-M and 63% on Z-Image-Turbo. These results support on-policy self-distillation as an efficient and analyzable approach to diffusion post-training by converting image-level reward guidance into explicit and continually refreshed intermediate supervision, thereby opening a path toward more efficient and diagnosable alignment.
