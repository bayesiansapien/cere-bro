---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2410.01473
category: cs.CV
concept: inference-efficiency
url: https://arxiv.org/abs/2410.01473
published: 2026-04-16
authors: Osher Rafaeli, Tal Svoray, Ariel Nahlieli
---

# SinkSAM-Net: Knowledge-Driven Self-Supervised Sinkhole Segmentation Using Topographic Priors and Segment Anything Model

**arXiv:** https://arxiv.org/abs/2410.01473
**Authors:** Osher Rafaeli, Tal Svoray, Ariel Nahlieli

## Abstract

arXiv:2410.01473v3 Announce Type: replace  Abstract: Soil sinkholes significantly influence soil degradation, infrastructure vulnerability, and landscape evolution. However, their irregular shapes, combined with interference from shadows and vegetation, make it challenging to accurately quantify their properties using remotely sensed data. In addition, manual annotation can be laborious and costly. In this study, we introduce a novel self-supervised framework for sinkhole segmentation, termed SinkSAM-Net, which integrates traditional topographic computations of closed depressions with an iterative, geometry-aware, prompt-based Segment Anything Model (SAM). We generate high-quality pseudo-labels through pixel-level refinement of sinkhole boundaries by integrating monocular depth information with random prompts augmentation technique named coordinate-wise bounding box jittering (CWBJ). These pseudo-labels iteratively enhance a lightweight EfficientNetV2-UNet target model, ultimately transferring knowledge to a prompt-free, low-parameter, and fast inference model. Our proposed approach achieves approximately 95\% of the performance obtained through manual supervision by human annotators. The framework's performance was evaluated on a large sinkhole database, covering diverse sinkhole dateset-induced sinkholes using both aerial and high-resolution drone imagery. This paper presents the first self-supervised framework for sinkhole segmentation, demonstrating the robustness of foundational models (such as SAM and Depth Anything V2) when combined with prior topographic and geometry knowledge and an iterative self-learning pipeline. SinkSAM-Net has the potential to be trained effectively on extensive unlabeled RGB sinkholes datasets, achieving comparable performance to a supervised model. The code and interactive demo for SinkSAM-Net are available at https://osherr1996.github.io/SinkSAMNet
