---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.11550
url: https://huggingface.co/papers/2605.11550
arxiv_url: https://arxiv.org/abs/2605.11550
date: 2026-05-14
---

# The DAWN of World-Action Interactive Models

A plausible scene evolution depends on the maneuver being considered, while a good maneuver depends on how the scene may evolve. Existing World Action Models (WAMs) largely miss this reciprocity, treating world prediction and action generation as either isolated parallel branches or rigid predict-then-plan pipelines. We formalize this perspective as World-Action Interactive Models (WAIMs), and instantiate it in autonomous driving with DAWN (Denoising Actions and World iNteractive model), a simple yet strong latent generative baseline. DAWN operates in a compact semantic latent space and couples a World Predictor with a World-Conditioned Action Denoiser: the predicted world hypothesis conditions action denoising, while the denoised action hypothesis is fed back to update the world prediction, so that both are recursively refined during inference. Rather than eliminating test-time world evolution altogether or rolling out the full future in pixel space, DAWN performs a short explicit latent rollout that is sufficient to support long-horizon trajectory generation in complex interactive scenes. Experiments show that DAWN achieves strong planning performance and favorable safety-related results across multiple autonomous driving benchmarks. More broadly, our results suggest that interactive world-action generation is a principled path toward truly actionable world models.
