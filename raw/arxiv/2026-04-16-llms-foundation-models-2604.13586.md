---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13586
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13586
published: 2026-04-16
authors: Danish Nazir, Antoine Hanna-Asaad, Lucas G\"ornhardt
---

# Efficient Multi-View 3D Object Detection by Dynamic Token Selection and Fine-Tuning

**arXiv:** https://arxiv.org/abs/2604.13586
**Authors:** Danish Nazir, Antoine Hanna-Asaad, Lucas G\"ornhardt

## Abstract

arXiv:2604.13586v1 Announce Type: new  Abstract: Existing multi-view three-dimensional (3D) object detection approaches widely adopt large-scale pre-trained vision transformer (ViT)-based foundation models as backbones, being computationally complex. To address this problem, current state-of-the-art (SOTA) \texttt{ToC3D} for efficient multi-view ViT-based 3D object detection employs ego-motion-based relevant token selection. However, there are two key limitations: (1) The fixed layer-individual token selection ratios limit computational efficiency during both training and inference. (2) Full end-to-end retraining of the ViT backbone is required for the multi-view 3D object detection method. In this work, we propose an image token compensator combined with a token selection for ViT backbones to accelerate multi-view 3D object detection. Unlike \texttt{ToC3D}, our approach enables dynamic layer-wise token selection within the ViT backbone. Furthermore, we introduce a parameter-efficient fine-tuning strategy, which trains only the proposed modules, thereby reducing the number of fine-tuned parameters from more than $300$ million (M) to only $1.6$ M. Experiments on the large-scale NuScenes dataset across three multi-view 3D object detection approaches demonstrate that our proposed method decreases computational complexity (GFLOPs) by $48\%$ ... $55\%$, inference latency (on an \texttt{NVIDIA-GV100} GPU) by $9\%$ ... $25\%$, while still improving mean average precision by $1.0\%$ ... $2.8\%$ absolute and NuScenes detection score by $0.4\%$ ... $1.2\%$ absolute compared to so-far SOTA \texttt{ToC3D}.
