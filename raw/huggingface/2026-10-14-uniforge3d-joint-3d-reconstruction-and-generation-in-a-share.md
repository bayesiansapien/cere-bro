---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.508890+00:00
arxiv_id: 2610.15357
url: https://huggingface.co/papers/2610.15357
arxiv_url: https://arxiv.org/abs/2610.15357
date: 2026-10-14
---

# UniForge3D: Joint 3D Reconstruction and Generation in a Shared Anchor-Guided Space

Generating complete 3D assets from sparse, unposed images requires preserving observed geometry while completing unseen regions. Joint reconstruction and generation offers a way to address both goals: reconstruction recovers the geometry observed in the input images, while generation contributes learned shape priors. However, combining camera-relative reconstruction with canonical-space generation introduces a coordinate mismatch that makes direct geometric interaction more difficult. Moreover, conditioning each 3D location on all views without accounting for their relevance may mix useful geometric evidence with unrelated image content, hindering local detail recovery. We present UniForge3D, which jointly models reconstruction and generation in a shared anchor-guided space, resolving their coordinate mismatch. This space follows the anchor view's azimuth while keeping the object upright. The two branches exchange features bidirectionally to predict per-view point maps and a complete sparse voxel structure. We further condition point-map prediction on the generated structure to establish pixel-to-voxel correspondences and select the most informative input view for each voxel. Features from the selected views then guide detailed shape generation, helping preserve observed geometric details. Our method achieves state-of-the-art appearance and geometry results on Toys4K and GSO, generating complete 3D assets with improved fidelity. Project webpage: https://xishuxishu.github.io/uniforge3d-project/
