---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13520
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13520
published: 2026-04-16
authors: Chaoran Zhang, Guangyao Li, Dongxu Ji
---

# LEGO-MOF: Equivariant Latent Manipulation for Editable, Generative, and Optimizable MOF Design

**arXiv:** https://arxiv.org/abs/2604.13520
**Authors:** Chaoran Zhang, Guangyao Li, Dongxu Ji

## Abstract

arXiv:2604.13520v1 Announce Type: new  Abstract: Metal-organic frameworks (MOFs) are highly promising for carbon capture, yet navigating their vast design space remains challenging. Recent deep generative models enable de novo MOF design but primarily act as feed-forward structure generators. By heavily relying on predefined building block libraries and non-differentiable post-optimization, they fundamentally sever the information flow required for continuous structural editing. Here, we propose a target-driven generative framework focused on continuous structural manipulation. At its core is LinkerVAE, which maps discrete 3D chemical graphs into a continuous, SE(3)-equivariant latent space. This smooth manifold unlocks geometry-aware manipulations, including implicit chemical style transfer and zero-shot isoreticular expansion. Building upon this, we introduce a test-time optimization (TTO) strategy, utilizing an accurate surrogate model to continuously optimize the latent graphs of existing MOFs toward desired properties. This approach systematically enhances carbon capture performance, achieving a striking average relative boost of 147.5% in pure CO2 uptake while strictly preserving structural validity. Integrated with a latent diffusion model and rigid-body assembly for full MOF construction, our framework establishes a scalable, fully differentiable pathway for both the automated discovery, targeted optimization and editing of functional materials.
