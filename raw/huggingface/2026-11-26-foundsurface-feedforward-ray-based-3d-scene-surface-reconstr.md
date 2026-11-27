---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.905069+00:00
arxiv_id: 2611.34128
url: https://huggingface.co/papers/2611.34128
arxiv_url: https://arxiv.org/abs/2611.34128
date: 2026-11-26
---

# FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images

Accurate 3D surface reconstruction from unposed images remains a fundamental challenge in computer vision. Recent feed-forward pointmap methods eliminate the need for camera poses but inherently produce discrete, sparse representations. In this paper, we present a generalizable pipeline that directly recovers continuous, high-fidelity 3D surfaces from unposed images by seamlessly integrating pointmap- and ray-based representations. Our approach first extracts explicit geometric priors using a pre-trained pointmap model. A query-view-centric selection module then identifies geometrically relevant reference views via a robust surfel voting mechanism. Next, a cross-attention regressor bridges target query rays with reference features to estimate a continuous coarse surface. Lastly, a raylet-based module aggregates local 3D features to carve out high-frequency details and analytical normals. Trained as a single foundation model on 9 diverse datasets, our method demonstrates exceptional zero-shot generalization on 6 unseen datasets, clearly surpassing state-of-the-art baselines in geometric accuracy and detail preservation.
