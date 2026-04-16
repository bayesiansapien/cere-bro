---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2506.01247
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2506.01247
published: 2026-04-16
authors: Gerasimos Chatzoudis, Zhuowei Li, Gemma E. Moran
---

# Visual Sparse Steering (VS2): Unsupervised Adaptation for Image Classification using Sparsity-Guided Steering Vectors

**arXiv:** https://arxiv.org/abs/2506.01247
**Authors:** Gerasimos Chatzoudis, Zhuowei Li, Gemma E. Moran

## Abstract

arXiv:2506.01247v2 Announce Type: replace-cross  Abstract: Steering vision foundation models at test time, without updating foundation-model weights or using labeled target data, is a desirable yet challenging goal. We present Visual Sparse Steering (VS2), a lightweight, label-free adaptation method that constructs a steering vector from sparse features extracted by a Sparse Autoencoder (SAE) trained on unlabeled in-domain training-split activations of the vision encoder. VS2 offers three key advantages over existing test-time adaptation methods: (1) a feature-level intervention space in sparse SAE representations; (2) efficiency, requiring only a forward pass with no test-time optimization or backpropagation; and (3) a reliability diagnostic based on SAE reconstruction loss that can skip steering when reconstruction is poor, enabling safe fallback to the baseline, a capability not standard in conventional steering vectors and test-time adaptation methods. Across CIFAR-100, CUB-200, and Tiny-ImageNet and two CLIP backbones (ViT-B/32, ViT-B/16), VS2 improves zero-shot top-1 accuracy by 3.45-4.12\%, 0.93-1.08\%, and 1.50-1.84\%, respectively, while remaining forward-only and adding minimal compute overhead. A retrieval-based upper-bound analysis suggests substantial headroom if task-relevant sparse features can be selected reliably, motivating future work on selective feature amplification for interpretable, efficient test-time steering.
