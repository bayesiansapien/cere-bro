---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2605.09241
url: https://huggingface.co/papers/2605.09241
arxiv_url: https://arxiv.org/abs/2605.09241
date: 2026-05-12
---

# Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models

Joint-Embedding Predictive Architectures (JEPAs) provide a simple framework for learning world models by predicting future latent representations. However, JEPA training is subject to a bias-variance tradeoff. Without sufficient structural constraints, excessive representational variance causes the model to collapse to trivial solutions. The recent LeWorldModel (LeWM) shows that this issue can be alleviated by simply constraining latent embeddings with an isotropic Gaussian prior. However, latent representations inherently lie on low-dimensional manifolds within a high-dimensional ambient space, and enforcing an isotropic Gaussian prior directly in this ambient space introduces an overly strong bias. In this work, we propose Sub-JEPA, which seeks a favorable operating point on the bias-variance frontier by applying Gaussian constraints in multiple random subspaces rather than in the original embedding space. This design relaxes the global constraint while preserving its anti-collapse effect, leading to a better balance between training stability and representation flexibility. Extensive experiments across four continuous-control environments demonstrate that Sub-JEPA consistently outperforms LeWM with very clear margins.
