---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.303538+00:00
arxiv_id: 2611.03228
url: https://huggingface.co/papers/2611.03228
arxiv_url: https://arxiv.org/abs/2611.03228
date: 2026-11-05
---

# AnchorComplete: Recovering Complete Scene Meshes from Partial Point Clouds

Most image-based 3D reconstructors primarily recover visible surfaces, producing partial point clouds with large holes and leaving unobserved geometry unresolved. To address this limitation, we introduce AnchorComplete, a framework that reconstructs complete scene meshes from partial point clouds while preserving observed geometry and supporting scenes of varying scales. Building on TRELLIS.2, our method combines partial-point conditioning, which integrates global scene tokens with local spatial evidence to anchor generation to the input, and metric-scale coarse-to-fine generation, which progressively refines scene geometry within fixed-size windows while maintaining global structural consistency. Experiments on Replica and SCRREAM demonstrate that AnchorComplete consistently outperforms strong baselines in complete-scene reconstruction, particularly under sparse-view settings.
