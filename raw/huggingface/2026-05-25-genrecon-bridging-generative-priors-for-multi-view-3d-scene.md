---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.23888
url: https://huggingface.co/papers/2605.23888
arxiv_url: https://arxiv.org/abs/2605.23888
date: 2026-05-25
---

# GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction

We introduce a new approach to high-fidelity 3D scene reconstruction from multi-view RGB images that tightly couples reconstruction with a strong generative 3D prior. We cast scene reconstruction as conditional 3D generation over a set of spatially-localized, overlapping chunks that together tile the scene, scaling generation to large scene extents. Crucially, we inherit the fidelity and completeness of state-of-the-art generative shape models -- we use Trellis.2 as an example -- which we generalize to the scene level. To this end, we propose a projection-based conditioning mechanism that lifts posed multi-view image features into a coherent 3D representation aligned with the generative model, independent of view ordering and spatially anchored to the scene, yielding high-fidelity, multi-view consistent generated geometry. This enables lifting the strong object-level prior of Trellis.2 to multi-view, scene-scale generation, producing faithful, editable PBR mesh reconstructions of indoor environments. As a result, we obtain high-fidelity results that outperform cutting-edge reconstruction methods by 16%.
