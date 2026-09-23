---
source: farmer/huggingface
farmed: 2026-09-23T05:53:04.588715+00:00
arxiv_id: 2609.25165
url: https://huggingface.co/papers/2609.25165
arxiv_url: https://arxiv.org/abs/2609.25165
date: 2026-09-23
---

# Ovis-Embedding: Pushing the Frontiers of Universal Omni-Modal Embeddings

In this report, we introduce Ovis-Embedding, a state-of-the-art omni-modal embedding family built on native integration of text, image, video, and audio. Instead of assembling separate modality towers, Ovis-Embedding uses a shared multimodal backbone to encode different modalities in a common representation space. Specifically, we make three key advances: (1) native omni-modal initialization: we adopt a pretrained Qwen-omni model as the embedding backbone and adapt it through contrastive training with low-rank initialization; (2) data-centric omni-modal training: we construct a broad, high-quality corpus spanning text, images, video, audio, and interleaved multimodal data. To improve data efficiency, we introduce homogeneous-source sampling to form task-consistent batches with informative in-batch negatives; and (3) embedding-specific training and inference optimization: we use focal loss to emphasize hard examples and similarity-based Embedding Distillation to transfer fine-grained similarity structure from complementary experts. At inference time, low-rank feature decomposition enables compact embeddings with flexible dimensionality and minimal performance loss. Empirical evaluations show that the Ovis-Embedding family achieves state-of-the-art performance on MMEB-v3, MMEB-v2, MVEB, MAEB, and RTEB, demonstrating its effectiveness across text, image, video, and audio modalities. These results highlight the potential of unified omni-modal training to overcome modality fragmentation and advance universal embedding models for any-to-any retrieval.
