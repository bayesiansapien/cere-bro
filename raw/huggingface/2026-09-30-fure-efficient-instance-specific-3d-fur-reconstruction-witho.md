---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.35770
url: https://huggingface.co/papers/2609.35770
arxiv_url: https://arxiv.org/abs/2609.35770
date: 2026-09-30
---

# FurE: Efficient Instance-Specific 3D Fur Reconstruction without Animal-Fur Datasets

Realistic and editable animal fur reconstruction from multi-view images is challenging due to fine-scale detail, self-occlusion and obfuscation, and, unlike human hair, the lack of animal-fur datasets. Fur usually covers most of an animal's body, with large inter-species and intra-species variability. We present FurE, an efficient strand-based animal fur reconstruction method that recovers a per-strand, editable groom by optimizing a root-conditioned latent field, decoded into strand geometry via a PCA-based decoder. We reconstruct a defurred animal body using local fur-thickness cues from a surface-constrained Gaussian Frosting representation together with part-based priors. We further show that a PCA-based decoder learned from human-hair strand data can alleviate animal-data scarcity while enabling substantially faster optimization. FurE achieves a 10x speedup in strand training over current SOTA dense per-strand optimization while retaining strand fidelity and generalizing across synthetic and real-world sequences, with quantitative and qualitative validation despite the reduction in training time.
