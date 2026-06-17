---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.15236
url: https://huggingface.co/papers/2606.15236
arxiv_url: https://arxiv.org/abs/2606.15236
date: 2026-06-17
---

# Show the Signal, Hide the Noise: Spectral Forcing for Pixel-Space Diffusion

Pixel-space diffusion models are trained on full-bandwidth noisy images, yet the useful signal available to the denoiser is strongly frequency dependent. Under rectified-flow diffusion and natural-image power-law spectra, the per-band data-to-noise contour k^{*}(t) = (1-t)^{-2/α} separates a signal-bearing low-frequency region from a noise-dominated high-frequency region at each time t. We show that this implicit coarse-to-fine structure is not merely descriptive: it induces a capacity-allocation problem. A standard pixel-space denoiser must discover the moving bandwidth boundary internally and can spend computation on frequency-time regions where the optimal prediction collapses to deterministic baselines rather than data-distribution modeling. To make this boundary explicit, we introduce Spectral Forcing, a parameter-free, time-conditional 2D-DCT low-pass operator applied to the noisy input before the patch embedder. Its cutoff expands monotonically with the diffusion time and becomes the identity at the data endpoint. Through controlled synthetic experiments, we identify the regime in which the operator is beneficial: coarse patch tokenization and data whose high-frequency content is predominantly noise rather than essential signal. On ImageNet-256 with JiT-700M/32, Spectral Forcing consistently improves both FID and Inception Score across different training epochs, demonstrating robust gains throughout training; at finer tokenization, the spectral forcing is still competitive. We further insert the unchanged operator into SenseNova-U1, a unified text-to-image model, where it improves DPG-Bench and GenEval, showing that the input-side spectral prior transfers beyond class-conditional generation. These results suggest a route to capacity-efficient pixel-space diffusion by showing the signal and hiding the noise.
