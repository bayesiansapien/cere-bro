---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.502893+00:00
arxiv_id: 2610.17227
url: https://huggingface.co/papers/2610.17227
arxiv_url: https://arxiv.org/abs/2610.17227
date: 2026-10-14
---

# AReA: Adaptive Receptive-Field Attention for Efficient High-Resolution Diffusion Transformers

Generating images beyond the training resolution of Diffusion Transformers (DiTs) remains challenging, as the number of tokens grows rapidly with resolution, full attention becomes expensive, and outputs often suffer from structural distortions and degraded detail. We identify uniform full attention as the common source of both problems. Attending to all tokens at every step causes quadratic cost and exposes the model to more tokens and relative distances beyond the training range, pushing the model out of distribution. We observe that attention's effective receptive field narrows during denoising, from global in early steps that form structure to local in later steps that refine details. We propose AReA, a training-free attention mechanism whose receptive field evolves from coarse to fine, following the denoising progression. In early steps, AReA applies cross-scale coarse attention over downsampled keys and values, capturing global context, while in later steps it applies local attention within progressively shrinking windows. Without additional parameters or training, experiments show that AReA consistently outperforms state-of-the-art training-free baselines across target resolutions and different models, while also being faster and more efficient.
