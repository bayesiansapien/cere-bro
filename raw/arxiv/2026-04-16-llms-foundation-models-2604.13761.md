---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13761
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13761
published: 2026-04-16
authors: Svetlana Pavlitska, Haixi Fan, Konstantin Ditschuneit
---

# Design and Behavior of Sparse Mixture-of-Experts Layers in CNN-based Semantic Segmentation

**arXiv:** https://arxiv.org/abs/2604.13761
**Authors:** Svetlana Pavlitska, Haixi Fan, Konstantin Ditschuneit

## Abstract

arXiv:2604.13761v1 Announce Type: cross  Abstract: Sparse mixture-of-experts (MoE) layers have been shown to substantially increase model capacity without a proportional increase in computational cost and are widely used in transformer architectures, where they typically replace feed-forward network blocks. In contrast, integrating sparse MoE layers into convolutional neural networks (CNNs) remains inconsistent, with most prior work focusing on fine-grained MoEs operating at the filter or channel levels. In this work, we investigate a coarser, patch-wise formulation of sparse MoE layers for semantic segmentation, where local regions are routed to a small subset of convolutional experts. Through experiments on the Cityscapes and BDD100K datasets using encoder-decoder and backbone-based CNNs, we conduct a design analysis to assess how architectural choices affect routing dynamics and expert specialization. Our results demonstrate consistent, architecture-dependent improvements (up to +3.9 mIoU) with little computational overhead, while revealing strong design sensitivity. Our work provides empirical insights into the design and internal dynamics of sparse MoE layers in CNN-based dense prediction. Our code is available at https://github.com/KASTEL-MobilityLab/moe-layers/.
