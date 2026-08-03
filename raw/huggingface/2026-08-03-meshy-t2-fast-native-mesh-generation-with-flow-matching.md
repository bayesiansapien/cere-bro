---
source: farmer/huggingface
farmed: 2026-08-03T12:36:11.005337+05:30
arxiv_id: 2607.28675
url: https://huggingface.co/papers/2607.28675
arxiv_url: https://arxiv.org/abs/2607.28675
date: 2026-08-03
---

# Meshy T2: Fast Native Mesh Generation with Flow Matching

Polygonal meshes are the standard surface representation of modern 3D pipelines, and generating high-quality meshes with artist-style topology is essential for film, gaming, and interactive 3D applications. Mainstream approaches serialize a mesh into a token sequence and decode it autoregressively, which is slow at inference and sensitive to error accumulation, making them impractical for interactive asset creation. We present Meshy T2, a fast native mesh generation framework built on flow matching. At its core is a vertex-set mesh VAE that encodes a mesh into one continuous latent token per vertex and decodes vertices, edge connectivity, and face winding order in a single pass, preserving high-precision geometry and artist-authored topology without vertex quantization or welding. Generation proceeds as a coarse-to-fine cascade of two flow-matching models: an image-conditioned voxel flow first sketches the overall shape as a coarse occupancy scaffold, and a mesh flow then populates the scaffold with per-vertex latent tokens, conditioned on the image, the scaffold, and a requested vertex budget. This design delivers three practical capabilities: interactive generation speed through parallel flow-based synthesis; effective face-count control through the requested vertex budget; and native support for multi-part assets, whose components emerge directly from the generated connectivity. In our experiments, Meshy T2 achieves state-of-the-art geometric fidelity and completes end-to-end image-to-mesh generation within a median of 6 seconds, over an order of magnitude faster than autoregressive baselines. Code and weights will be available at https://github.com/meshy-dev/meshy-t2.
