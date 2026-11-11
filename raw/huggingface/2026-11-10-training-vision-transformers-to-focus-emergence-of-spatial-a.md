---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.325916+00:00
arxiv_id: 2611.11890
url: https://huggingface.co/papers/2611.11890
arxiv_url: https://arxiv.org/abs/2611.11890
date: 2026-11-10
---

# Training Vision Transformers to Focus: Emergence of Spatial Attention Head Specialization

Self-supervised learning in Vision Transformer models, such as DINO, enables robust visual perception without requiring labeled data by leveraging large-scale image datasets. However, these models lack a focusing mechanism during training, resulting in perceptual representations that are often ambiguous or overly similar. In this work, we introduce two visual focusing loss functions designed to establish correspondence between the model's attention and specific regions within images. Specifically, we leverage the multi-head attention mechanism within the model to selectively steer the model's focus, leading to the emergence of spatial attention head specialization, characterized by diverse and spatially focused perceptual capabilities without requiring annotations. Through both qualitative and quantitative evaluations, we demonstrate that our method substantially increases the spatial selectivity and diversity of attention heads, improving both interpretability and performance on dense prediction tasks such as zero-shot image segmentation.
