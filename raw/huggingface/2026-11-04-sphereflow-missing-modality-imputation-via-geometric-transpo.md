---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.366920+05:30
arxiv_id: 2611.04414
url: https://huggingface.co/papers/2611.04414
arxiv_url: https://arxiv.org/abs/2611.04414
date: 2026-11-04
---

# SphereFlow: Missing Modality Imputation via Geometric Transport on Hypersphere

Missing modality imputation aims to synthesize unobserved modalities from observed ones. Existing methods treat each modality as living on its own latent manifold, forcing the generator to learn a long, unstructured jump between them. We present SphereFlow, which takes a fundamentally different view: by projecting all modalities into a shared hyperspherical latent space via a frozen self-supervised encoder, cross-modal imputation reduces to short-range geometric transport between nearby points on the sphere. Realizing this idea with flow matching, however, exposes two geometric conflicts: the standard Gaussian noise source is catastrophically mismatched with the unit-norm data manifold, and the linear interpolation path departs the sphere surface into a region where the decoder has no training signal. We resolve both with simple, geometry-aware modifications: replacing the noise source with the observed-modality latent so that the velocity field learns only the cross-modal displacement, and training the decoder with a time-weighted loss that extends its domain to the near-surface region traversed by the flow. We prove that this data-as-source formulation reduces the worst-case off-manifold deviation from a quantity that grows with the latent dimension to a small, dimension-independent bound governed by inter-modality similarity. Experiments on BraTS multi-modal MRI imputation and CT-MRI translation demonstrate state-of-the-art generation fidelity across all settings, while downstream brain tumor segmentation with our imputed data closes roughly eighty percent of the gap to the full-modality oracle. Code is available at https://github.com/WTHH031230/SphereFlow.
