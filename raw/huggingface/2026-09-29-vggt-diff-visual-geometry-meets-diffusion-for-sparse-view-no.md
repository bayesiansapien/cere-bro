---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935769+00:00
arxiv_id: 2609.33253
url: https://huggingface.co/papers/2609.33253
arxiv_url: https://arxiv.org/abs/2609.33253
date: 2026-09-29
---

# VGGT-Diff: Visual Geometry Meets Diffusion for Sparse-View Novel View Synthesis

We present VGGT-Diff, a geometry-routed multi-view diffusion model for sparse-view novel view synthesis. Existing novel view synthesis (NVS) methods face a fundamental trade-off: reconstruction-based approaches preserve observed geometry but struggle to synthesize unseen regions, while diffusion-based methods provide strong generative priors yet rely on implicit source-to-query correspondence. VGGT-Diff bridges these regimes by routing visual geometry latents from VGGT-Ω into a pretrained video diffusion model. Each visual token is associated with a 3D point and confidence, then transformed into query-aligned latent conditions through a confidence-aware Visual Geometry Router (VGR) that preserves front and back surface evidence. These conditions guide joint target-view denoising, while Point-Track Residual Consistency (PTRC) regularizes predicted-clean residuals along reliable 3D tracks, improving multi-view stability. We further introduce robust geometry conditioning, combining training-time regularization with inference-time guidance for improved robustness. Experiments show competitive or state-of-the-art performance across interpolation and extrapolation under different viewpoint difficulties. Our code is available at https://github.com/chenkangjie1123/VGGT-Diff.
