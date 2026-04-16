---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13183
category: cs.CV
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13183
published: 2026-04-16
authors: Hongyang Zhang, Yinhao Liu, Haitao Zhang
---

# GeoLink: A 3D-Aware Framework Towards Better Generalization in Cross-View Geo-Localization

**arXiv:** https://arxiv.org/abs/2604.13183
**Authors:** Hongyang Zhang, Yinhao Liu, Haitao Zhang

## Abstract

arXiv:2604.13183v1 Announce Type: new  Abstract: Generalizable cross-view geo-localization aims to match the same location across views in unseen regions and conditions without GPS supervision. Its core difficulty lies in severe semantic inconsistency caused by viewpoint variation and poor generalization under domain shift. Existing methods mainly rely on 2D correspondence, but they are easily distracted by redundant shared information across views, leading to less transferable representations. To address this, we propose GeoLink, a 3D-aware semantic-consistent framework for Generalizable cross-view geo-localization. Specifically, we offline reconstruct scene point clouds from multi-view drone images using VGGT, providing stable structural priors. Based on these 3D anchors, we improve 2D representation learning in two complementary ways. A Geometric-aware Semantic Refinement module mitigates potentially redundant and view-biased dependencies in 2D features under 3D guidance. In addition, a Unified View Relation Distillation module transfers 3D structural relations to 2D features, improving cross-view alignment while preserving a 2D-only inference pipeline. Extensive experiments on multiple benchmarks show that GeoLink consistently outperforms state-of-the-art methods and achieves superior generalization across unseen domains and diverse weather environments.
