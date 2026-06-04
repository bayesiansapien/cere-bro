---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.04688
url: https://huggingface.co/papers/2606.04688
arxiv_url: https://arxiv.org/abs/2606.04688
date: 2026-06-04
---

# MeshWeaver: Sparse-Voxel-Guided Surface Weaving for Autoregressive Mesh Generation

Autoregressive mesh generation has gained attention by tokenizing meshes into sequences and training models in a language-modeling fashion. However, existing approaches suffer from two fundamental limitations: (i) low tokenization efficiency, which yields long token sequences and prevents scaling to high-poly meshes, and (ii) absence of geometry-aware guidance, as generation is conditioned only on global shape embeddings rather than local surface cues. We introduce MeshWeaver, an autoregressive framework that treats mesh generation as a surface weaving process by directly predicting the next vertex instead of independent coordinates. At its core is a multi-level sparse-voxel encoder that injects geometric context into the generative process in three complementary ways: providing voxel features as vertex representations, guiding token prediction via cross-attention to voxel features, and serving as a structural scaffold that constrains generation around the input surface. Our hierarchical design enables coarse-to-fine vertex prediction in a single decoding step, while tightly coupling the generative model with 3D geometry. Extensive experiments demonstrate that MeshWeaver achieves a state-of-the-art compression ratio of 18%, can generate meshes with up to 16K faces, and significantly improves geometric fidelity over prior approaches.
