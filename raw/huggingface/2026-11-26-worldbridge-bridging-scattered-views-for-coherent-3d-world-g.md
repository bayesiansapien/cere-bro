---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.907172+00:00
arxiv_id: 2611.34079
url: https://huggingface.co/papers/2611.34079
arxiv_url: https://arxiv.org/abs/2611.34079
date: 2026-11-26
---

# WorldBridge: Bridging Scattered Views for Coherent 3D World Generation

Generating coherent and explorable 3D worlds from scattered images with little or no visual overlap is a fundamental and long-standing challenge in computer vision, which existing geometry-aware methods fail to address. Meanwhile, existing image- and video-based methods may generate unseen regions but produce inconsistent geometry across views. To bridge this gap, we present WorldBridge, a framework for coherent and controllable 3D world generation under scattered images with little or no visual overlap. WorldBridge encodes scattered references into a global scene context to guide geometry and appearance generation across views. Our temporal and spatial reference attention mechanism further enhances the fidelity of temporal references along the target trajectory and supports flexible spatial references outside it. A plug-and-play latent-reference consistency strategy improves reference fidelity through reprojection-guided test-time optimization. We also introduce the WorldBridge benchmark suite to evaluate 3D world generation from scattered, low-overlap references, which is rarely explored by current benchmarks. Both qualitative and quantitative results demonstrate that our method enables controllable and coherent 3D world generation, surpassing the existing state-of-the-art solutions. Our project page is available at https://davidyan2001.github.io/WorldBridge/.
