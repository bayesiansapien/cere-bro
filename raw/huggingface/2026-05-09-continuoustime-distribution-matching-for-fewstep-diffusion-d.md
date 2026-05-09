---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06376
url: https://huggingface.co/papers/2605.06376
arxiv_url: https://arxiv.org/abs/2605.06376
date: 2026-05-09
---

# Continuous-Time Distribution Matching for Few-Step Diffusion Distillation

Step distillation has become a leading technique for accelerating diffusion models. We introduce Continuous-Time Distribution Matching (CDM), migrating the DMD framework from discrete anchoring to continuous optimization for the first time. CDM achieves this through two continuous-time designs: replacing the fixed discrete schedule with a dynamic continuous schedule of random length, and a continuous-time alignment objective that performs active off-trajectory matching on latents extrapolated via the student's velocity field. Extensive experiments on different architectures, including SD3-Medium and Longcat-Image, demonstrate that CDM provides highly competitive visual fidelity for few-step image generation without relying on complex auxiliary objectives.
