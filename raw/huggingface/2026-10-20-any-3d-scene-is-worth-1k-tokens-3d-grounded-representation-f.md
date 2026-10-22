---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2604.11331
url: https://huggingface.co/papers/2604.11331
arxiv_url: https://arxiv.org/abs/2604.11331
date: 2026-10-20
---

# Any 3D Scene is Worth 1K Tokens: 3D-Grounded Representation for Scene Generation at Scale

Scene-level 3D generation has long been dominated by 2D multi-view or video diffusion models. Typically, these 2D-based approaches perform scene generation in a 2D latent space, which introduces two fundamental issues: (i) representing 3D scenes via 2D views leads to significant representation redundancy, and (ii) latent space rooted in 2D inherently limits the spatial consistency of the generated scenes. In this paper, we propose to perform 3D scene generation directly within a high-dimensional implicit 3D latent space derived from powerful 2D foundation models (e.g., DINOv2, SigLIP2, DA3). Then we tame diffusion transformers to perform diffusion modeling directly in the 3D latent space, enabling 3D-grounded scene generation. In our experiments, we not only demonstrate the advantages of our method over 2D-based approaches in terms of efficiency and spatial consistency, but also comprehensively analyze the impact of 3D latent representation on 3D scene generation performance. Furthermore, we validate the favorable scalability of our method with respect to representation and model capacity.
