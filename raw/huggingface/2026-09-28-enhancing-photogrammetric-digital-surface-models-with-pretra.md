---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.596077+00:00
arxiv_id: 2609.31199
url: https://huggingface.co/papers/2609.31199
arxiv_url: https://arxiv.org/abs/2609.31199
date: 2026-09-28
---

# Enhancing Photogrammetric Digital Surface Models with Pretrained Diffusion Models and Multimodal Conditioning

Large-scale Digital Surface Models (DSMs) can be produced cost-effectively from satellite images via stereo-photogrammetry. However, the resulting 3D maps are often contaminated by noise, outliers, and voids. On the other hand, aerial LiDAR provides high-accuracy elevation measurements at a substantially higher cost. In this work, we study diffusion models conditioned both on photogrammetric DSMs and Pléiades imagery to refine vertically co-registered DSMs. We introduce a modified Stable Diffusion 3 architecture with a pruned text stream and a patch-wise normalization strategy, enabling stable training on LiDAR data and transfer from natural images to elevation maps. Experiments in French cities demonstrate that multimodal conditioning improves elevation accuracy, reducing Dense Urban RMSE from 6.00 to 3.45 m in the in-context cities and from 4.16 to 2.77 m in the held-out city of Bordeaux.
