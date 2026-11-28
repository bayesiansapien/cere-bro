---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.33885
url: https://huggingface.co/papers/2611.33885
arxiv_url: https://arxiv.org/abs/2611.33885
date: 2026-11-27
---

# LayoutRecall: Preserving Appearance in Multi-Round 3D Layout-Controlled Image Editing

3D layout-controlled image editing gives users explicit control over object placement and camera viewpoint. In a sequence of edits, however, the latest image can lose the appearance of an object when it is occluded or leaves view. The target layout specifies where the object should reappear, while its appearance must be recovered from earlier observations. We introduce LayoutRecall, a multi-round editor that stores and reuses appearance in the local coordinate systems of 3D boxes. Box-Surface Latent Memory retains image latents on box faces and retrieves them along rays in the target view. Geometry-Aligned Memory Conditioning supplies the retrieved tokens to a FLUX.2 editor using target-view positions, shared box-local embeddings, and object-wise attention. A correspondence loss encourages the editor to attend to matching observations during denoising. We also introduce LayoutLoop, a multi-round 3D layout-controlled image editing benchmark with calibrated layouts and designed revisits. We conduct extensive experiments on LayoutLoop and real-scene data to verify the ability of our method. The project page is at https://ykchizs.github.io/layoutrecall.github.io/.
