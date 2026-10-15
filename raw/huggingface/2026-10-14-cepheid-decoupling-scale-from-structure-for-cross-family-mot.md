---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.504603+00:00
arxiv_id: 2610.18871
url: https://huggingface.co/papers/2610.18871
arxiv_url: https://arxiv.org/abs/2610.18871
date: 2026-10-14
---

# Cepheid: Decoupling Scale from Structure for Cross-Family Motion Completion

Sparse-to-dense motion completion recovers dense mesh motion from sparse vertex displacements. Residual priors trained on one geometry family frequently fail to beat parameter-free harmonic extension off-family. Moreover, cross-family training meets a scaling barrier: residual amplitude varies by more than an order of magnitude across geometry families and collapses as observations become denser. Since this scale depends on unknown target motion, it cannot be measured directly at test time. We decouple residual structure from physical scale by learning a dimensionless prior, estimating amplitude from observables and a lightweight correction fitted only on training sources. Our unified model surpasses harmonic extension across all evaluated families, including unseen cloth and legged bodies, without skeletons, registration, or cross-mesh correspondence. The same prior applies without retraining to point-tracked animal video and a robot grasping a soft body. Project page: https://su-terry.github.io/cepheid-website/
