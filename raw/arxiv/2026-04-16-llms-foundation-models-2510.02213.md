---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.02213
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.02213
published: 2026-04-16
authors: Villanelle O'Reilly, Jonathan Cox, Georgios Leontidis
---

# Getting the Numbers Right$\unicode{x2014}$Modelling Multi-Class Object Counting in Dense and Varied Scenes

**arXiv:** https://arxiv.org/abs/2510.02213
**Authors:** Villanelle O'Reilly, Jonathan Cox, Georgios Leontidis

## Abstract

arXiv:2510.02213v2 Announce Type: replace  Abstract: Density map estimation enables accurate object counting in heavily occluded, and densely packed scenes where detection-based counting fails. In multi-class density estimation, class awareness can be introduced by modelling classes non-exclusively, better reflecting crowded and visually ambiguous contexts. However, existing multi-class density estimators often degrade in less-dense scenes, while state-of-the-art detectors still struggle in the most congested settings. To bridge this gap, we propose the first vision-transformer-based approach to multi-class density estimation. Our model combines a Twins-SVT pyramid vision transformer backbone with a multiscale CNN decoder that leverages hierarchical features for robust counting across a wide range of densities. Further to that, the method adds an auxiliary segmentation task with the Category Focus Module to suppress inter-category interference at training time. The module improves the density estimation head without the need for constraining assumptions added by the application of the auxiliary task at inference time, as required in previous methods. Training and evaluation on the VisDrone and iSAID benchmarks demonstrates a leap in performance versus the previous state-of-the-art multi-class density estimation methods, attaining a 33%, 43%, and 64% reduction to MAE in testing evaluation. The method outperforms YOLO11 in less busy scenes, exceeding it by an order of magnitude in the most crowded testing samples.   Code, and trained weights available at https://github.com/LCAS/gnr_mcdest.
