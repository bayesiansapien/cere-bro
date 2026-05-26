---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.26115
url: https://huggingface.co/papers/2605.26115
arxiv_url: https://arxiv.org/abs/2605.26115
date: 2026-05-26
---

# TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction

Sparse-view 3D reconstruction is increasingly addressed with feed-forward splatting networks that predict explicit primitives directly from images. Yet most existing methods remain centered on Gaussian primitives and expose surfaces only indirectly: extracting a usable mesh for downstream simulation, physics reasoning, or embodied interaction still requires expensive post-hoc steps that break the feed-forward promise. This limitation is especially pronounced in pose-free settings, where scene structure and camera parameters must be estimated jointly from sparse observations. We present TriSplat, a feed-forward reconstruction network that represents scenes with oriented triangle primitives and directly exports simulation-ready mesh scenes from a single forward pass. Given input images, the network predicts local 3D point maps, triangle attributes, camera poses, and optional intrinsics. Rather than regressing triangle orientation as an unconstrained latent variable, our approach constructs geometry normals from the predicted point maps, refines them with an image-conditioned normal head, and converts them into stable local frames for triangle parameterization. A mono-normal bootstrap schedule further stabilizes early training, while opacity and blur scheduling progressively sharpens the learned surface representation for direct mesh extraction. Experiments on RealEstate10K and DL3DV show that this representation produces more geometry-faithful reconstructions than Gaussian feed-forward baselines while maintaining competitive novel-view rendering quality. Because the rendering primitives are themselves surface triangles, the output can be directly ingested by physics engines, collision detectors, and standard rendering pipelines without any conversion, making it a practical simulation-ready solution for feed-forward 3D scene reconstruction.
