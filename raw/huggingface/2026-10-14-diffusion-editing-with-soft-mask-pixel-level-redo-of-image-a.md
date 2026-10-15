---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.510411+00:00
arxiv_id: 2610.00359
url: https://huggingface.co/papers/2610.00359
arxiv_url: https://arxiv.org/abs/2610.00359
date: 2026-10-14
---

# Diffusion Editing with Soft Mask: Pixel Level Redo of Image and Video with Adjustable Strength

Diffusion models with prompt and reference image-guided editing have seen rapid progress, yet they remain too coarse for pixel-level control. One promising direction is to incorporate a soft mask that specifies spatially varying edit strengths but training such fine-grained control demands expensive pixel-wise annotations, while existing zero-shot methods often yield unsatisfactory results. We introduce SoftPaint, a new zero-shot sampling method that leverages soft masks to enable a continuous spectrum of edits, from fully preserving the original content to completely re-synthesizing the masked region. Going beyond zero-shot inpainting methods, we design a Langevin-iteration-based sampler that respects per-pixel soft mask strengths, which applies universally to image and video diffusion models, enabling tasks such as video editing. The method is gradient-free, memory-efficient, and achieves smooth, pixel-level edits across multiple image and video backbones.
