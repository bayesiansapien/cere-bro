---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.911191+00:00
arxiv_id: 2611.34064
url: https://huggingface.co/papers/2611.34064
arxiv_url: https://arxiv.org/abs/2611.34064
date: 2026-11-26
---

# SPARC: Geometry-Guided Attention Pruning for Long-Horizon Camera-Controlled Video Generation

We present SPARC, a geometry-guided attention pruning framework that turns the native self-attention of pretrained video diffusion transformers into a unified mechanism for camera control and persistent scene memory. Our key insight is that attention connectivity can simultaneously serve as geometric conditioning for camera control and spatial addressing for historical memory retrieval. Motivated by the asymmetric contextual requirements of reconstructing observed content and synthesizing novel regions, SPARC restricts observed tokens to geometrically corresponding historical tokens and local spatiotemporal context, while preserving dense attention for unobserved regions. Correspondence-aware attention biasing and order-invariant historical positioning further enable stable retrieval across long temporal gaps. Without introducing additional learnable control or memory modules, SPARC achieves precise camera adherence and faithful scene revisitation while substantially reducing attention computation. Extensive experiments demonstrate the effectiveness of aggressive attention pruning in improving camera adherence, revisit consistency, and visual fidelity, with an inference speedup of over 50x when combined with four-step distillation. Project page is available at https://zju3dv.github.io/SPARC.
