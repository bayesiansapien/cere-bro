---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.31113
url: https://huggingface.co/papers/2608.31113
arxiv_url: https://arxiv.org/abs/2608.31113
date: 2026-09-01
---

# BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives

We introduce BLARM, a feed-forward method for video-driven 3D mesh animation. Given a monocular video and a static object mesh, BLARM predicts a temporally coherent animated mesh whose motion follows the video. Rather than relying on explicit rigs or directly regressing high-dimensional vertex motion, we represent animation using a compact set of learned, time-varying rigid motion components and time-invariant vertex-to-component skinning weights. This yields a low-dimensional deformation space without requiring skeletons, cages, skinning weights, or rig annotations. Our architecture conditions geometry-derived deformation latents on video features through factorized spatial-temporal attention, then decodes rigid transformations blended by predicted skinning weights. Trained with trajectory reconstruction, entropy regularization, and motion-aware contrastive learning, BLARM produces accurate and temporally stable animations while recovering compact, interpretable motion structure from monocular video.
