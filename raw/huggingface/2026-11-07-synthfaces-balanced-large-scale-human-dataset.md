---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.597006+00:00
arxiv_id: 2610.40119
url: https://huggingface.co/papers/2610.40119
arxiv_url: https://arxiv.org/abs/2610.40119
date: 2026-11-07
---

# SynthFaces: Balanced Large Scale Human Dataset

The pursuit of fair and equitable AI in human-centric tasks is critically hindered by the inherent biases and privacy risks of real-world datasets, which offer imbalanced representations of identity and often contain sensitive personal information. Consequently, state-of-the-art generative models trained on this skewed data exhibit unfair performance, particularly in identity-preserving generation. In this work we propose a pipeline for controllable generation of dataset with diverse faces for generative models training and finetuning. We achieve this by expanding foundational Arc2Face diffusion model with a flow matching generative model in the manifold of identity embeddings. We demonstrate that such approach achieves both goals of generative fidelity and label diversity not present in real human-centric datasets. As a result we collect and further contextualize a highly balanced identity-centric dataset of humans named SynthFaces. By design, our released images and identities are synthetic, reducing direct reliance on real personal images; we empirically check identity separation with a nearest-neighbor non-leakage metric. We purpose it for training and tuning of fair models for various downstream tasks, and showcase its usability in finetuning an existing adapter-based method for personalized generation.
