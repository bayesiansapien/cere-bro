---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.06665
url: https://huggingface.co/papers/2609.06665
arxiv_url: https://arxiv.org/abs/2609.06665
date: 2026-09-09
---

# TransNormal-2: Geometry-Grounded Rectified Flow with Edge-Aware Decoding for Precise Normal Estimation

Diffusion-based models enable monocular geometry estimation, yet their pixel-space precision is limited by a shared, under-studied error source: VAE reconstruction degradation. The 8x spatial compression in the VAE encoder-decoder degrades surface normals at object boundaries; even encoding and decoding ground-truth normals introduces 1.3--8.5° of mean angular error (MAE), with edge MAE reaching 2.8x the global MAE. We present TransNormal-2, a FLUX.2-based rectified-flow framework with single-step deterministic inference that addresses this degradation on both sides of the VAE decoder: in how latent predictions are supervised during training, and in how decoded normals are corrected at inference. First, geometry-aware pixel-space losses, including inverse rendering self-consistency, von~Mises-Fisher angular loss, and wavelet edge-aware regularization, complement latent MSE by enforcing spherical normal geometry and diffuse image-formation cues after VAE decoding. Second, a lightweight Geometric Refinement Module (GRM) applies an RGB-guided residual correction to reduce boundary-localized decoding errors without freely rewriting the coarse prediction. On general-scene benchmarks, TransNormal-2 matches or exceeds MoGe-2 on all eight reported metrics while using only 1.4% as many task-specific normal annotations. The gains are clearest for transparent objects, reducing MAE by 4.2° on ClearGrasp and 3.1° on ClearPose over the strongest prior baselines. Code will be released at https://longxiang-ai.github.io/TransNormal-2.
