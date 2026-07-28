---
source: farmer/huggingface
farmed: 2026-07-28T09:26:01.339781
arxiv_id: 2607.22148
url: https://huggingface.co/papers/2607.22148
arxiv_url: https://arxiv.org/abs/2607.22148
date: 2026-07-28
---

# dRAE: Representation Autoencoder with Hyper-Spherical Codes

In this work, we aim to discretize the high-dimensional visual representations to bridge the gap with language models - a non-trivial challenge, as existing quantization methods suffer from codebook collapse, failing to scale while preserving semantic coherence. We identify the root cause as metric mismatch: standard Euclidean codebook objectives are fundamentally misaligned with the anisotropic geometry of representation space, leading to codebook embeddings with high-variance magnitude scales and uneven angular distributions that hinder scalability. To address this, we propose Hyper-Spherical Quantization (HSQ), which decouples semantic content from feature magnitude via angular routing, preventing code assignment from being dominated by scale rather than meaning. The resulting discrete Representation Autoencoder (dRAE) achieves high-fidelity reconstruction while preserving semantic integrity and supporting scalable codebook budget. Extensive experiments demonstrate consistent performance gains as the vocabulary size scales to 131,072, along with 100% codebook utilization, simplified training pipeline, and strong performance across understanding and generation tasks.
