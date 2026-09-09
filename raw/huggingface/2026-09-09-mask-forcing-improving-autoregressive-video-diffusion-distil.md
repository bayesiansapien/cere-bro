---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.09123
url: https://huggingface.co/papers/2609.09123
arxiv_url: https://arxiv.org/abs/2609.09123
date: 2026-09-09
---

# Mask Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise Masking Rollout

Autoregressive (AR) video diffusion models have shown great potential in real-time video generation. Recent methods distill pretrained bidirectional video diffusion models into causal AR students through Distribution Matching Distillation (DMD), but the generated videos often suffer from over-saturation and over-smoothing issues, resulting in limited visual quality and realism. The key contributing factor is the mode-seeking behavior of the reverse KL objective in DMD, which can cause the student distribution to collapse onto only a few modes of the teacher distribution. To address this, we propose Mask Forcing, a Dual-Noise Masking Rollout strategy that perturbs the AR student self-rollout to mitigate mode collapse induced by reverse-KL mode seeking. The core idea is to inject cleaner signals into noisy rollout inputs via random masks along spatial and temporal axes during the self-rollout process of AR diffusion distillation. Such perturbations encourage the student rollouts to explore more regions of the teacher distribution, allowing DMD to provide learning signals beyond the modes already covered by the student. Moreover, the cleaner tokens act as denoising guidance for other noisier tokens, improving the intermediate rollout predictions and reducing error accumulation. Extensive experiments demonstrate that our method improves multiple AR video diffusion distillation methods with higher visual quality efficiently, without incorporating real video data or additional post-training stages.
