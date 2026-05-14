---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.12964
url: https://huggingface.co/papers/2605.12964
arxiv_url: https://arxiv.org/abs/2605.12964
date: 2026-05-14
---

# Asymmetric Flow Models

Flow-based generation in high-dimensional spaces is difficult because velocity prediction requires modeling high-dimensional noise, even when data has strong low-rank structure. We present Asymmetric Flow Modeling (AsymFlow), a rank-asymmetric velocity parameterization that restricts noise prediction to a low-rank subspace while keeping data prediction full-dimensional. From this asymmetric prediction, AsymFlow analytically recovers the full-dimensional velocity without changing the network architecture or training/sampling procedures. On ImageNet 256x256, AsymFlow achieves a leading 1.57 FID, outperforming prior DiT/JiT-like pixel diffusion models by a large margin. AsymFlow also provides the first-ever route for finetuning pretrained latent flow models into pixel-space models: aligning the low-rank pixel subspace to the latent space gives a seamless initialization that preserves the latent model's high-level semantics and structure, so finetuning mainly improves low-level mismatches rather than relearning pixel generation. We show that the pixel AsymFlow model finetuned from FLUX.2 klein 9B establishes a new state of the art for pixel-space text-to-image generation, beating its latent base on HPSv3, DPG-Bench, and GenEval while qualitatively showing substantially improved visual realism.
