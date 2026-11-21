---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.388090+00:00
arxiv_id: 2611.26511
url: https://huggingface.co/papers/2611.26511
arxiv_url: https://arxiv.org/abs/2611.26511
date: 2026-11-20
---

# Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain

Native 3D generation has largely been built around latent diffusion, with recent advances concentrating on stronger variational autoencoders (VAE) and increasingly elaborate latent representations, from vecset and triplanes to structured sparse voxels. Despite their architectural differences, these methods all share the same premise: geometry is first compressed into a latent space and only then modeled by the generator. We take a different route and propose Direct3D-V3, a latent-free diffusion transformer (DiT) framework that discards the VAE altogether and operates in the native voxel domain, directly modeling raw SDF voxel grids during both training and sampling. To make this direct voxel formulation geometrically reliable, we introduce an implicit manifold regularization over neighboring voxels to suppress non-watertight surfaces, and convert predicted SDF grids into meshes via Marching Cubes so that rendered normal losses can supervise the model directly from its predicted SDF. To improve alignment between the conditioning image and generated geometry, Direct3D-V3 also predicts the camera parameters of the conditioning image as an auxiliary task, encouraging the DiT to learn the mapping from image observations to 3D shape. This latent-free design removes the reconstruction bottleneck, brings training under an objective in the native voxel domain, and yields meshes with substantially richer local detail. The predicted camera and native SDF voxel output further make Direct3D-V3 extensible to generative reconstruction, where diffusion is interleaved with normal-guided refinement to improve alignment with the observed view while the generative prior completes unseen regions. Project page: https://dreamtechai.github.io/Direct3D-V3.
