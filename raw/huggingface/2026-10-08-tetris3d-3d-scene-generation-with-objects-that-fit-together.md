---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.303217+05:30
arxiv_id: 2610.10539
url: https://huggingface.co/papers/2610.10539
arxiv_url: https://arxiv.org/abs/2610.10539
date: 2026-10-08
---

# Tetris3D: 3D Scene Generation With Objects That Fit Together

We propose Tetris3D, a generative framework for single-image 3D scene reconstruction that recovers objects which are physically and geometrically coherent as a scene. Existing methods often generate objects independently or couple them implicitly, providing limited guidance for ensuring fine-grained spatial compatibility between neighboring objects that interact with one another. To address this, we explicitly condition the generation of each object on the geometry of surrounding objects and their physical relationships, guiding its shape and pose to remain geometrically and physically plausible within the scene. Moreover, we introduce ComOb, a physics simulation-based dataset of 1.2M scenes featuring physical interactions across diverse object categories, with per-object meshes and pairwise physical relation annotations. Comprehensive experiments on synthetic and realworld scenes show that Tetris3D recovers coherent object shapes and poses even when interacting regions are occluded, and achieves state-of-the-art performance in both generation quality and physical stability.
