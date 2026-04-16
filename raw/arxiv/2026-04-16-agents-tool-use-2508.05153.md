---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2508.05153
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2508.05153
published: 2026-04-16
authors: Mohammed Daba, Jing Qiu
---

# FCBV-Net: Category-Level Robotic Garment Smoothing via Feature-Conditioned Bimanual Value Prediction

**arXiv:** https://arxiv.org/abs/2508.05153
**Authors:** Mohammed Daba, Jing Qiu

## Abstract

arXiv:2508.05153v2 Announce Type: replace-cross  Abstract: Category-level generalization for robotic garment manipulation, such as bimanual smoothing, remains a significant hurdle due to high dimensionality, complex dynamics, and intra-category variations. Current approaches often struggle, either overfitting with concurrently learned visual features for a specific instance or, despite Category-level perceptual generalization, failing to predict the value of synergistic bimanual actions. We propose the Feature-Conditioned bimanual Value Network (FCBV-Net), operating on 3D point clouds to specifically enhance category-level policy generalization for garment smoothing. FCBV-Net conditions bimanual action value prediction on pre-trained, frozen dense geometric features, ensuring robustness to intra-category garment variations. Trainable downstream components then learn a task-specific policy using these static features. In simulated PyFlex environments using the CLOTH3D dataset, FCBV-Net demonstrated superior category-level generalization. It exhibited only an 11.5% efficiency drop (Steps80) on unseen garments compared to 96.2% for a 2D image-based baseline, and achieved 89% final coverage, outperforming an 83% coverage from a 3D correspondence-based baseline that uses identical per-point geometric features but a fixed primitive. These results highlight that the decoupling of geometric understanding from bimanual action value learning enables better category-level generalization. Code, videos, and supplementary materials are available at the project website: https://dabaspark.github.io/fcbvnet/.
