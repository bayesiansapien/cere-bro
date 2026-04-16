---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2512.15742
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2512.15742
published: 2026-04-16
authors: Jeff Smith
---

# SHARe-KAN: Post-Training Vector Quantization for Cache-Resident KAN Inference

**arXiv:** https://arxiv.org/abs/2512.15742
**Authors:** Jeff Smith

## Abstract

arXiv:2512.15742v2 Announce Type: replace  Abstract: Pre-trained Vision Kolmogorov-Arnold Networks (KANs) store a dense B-spline grid on every edge, inflating prediction-head parameter counts by more than 140X relative to a comparable MLP and pushing inference into a memory-bound regime on edge accelerators. Standard magnitude pruning fails on these pre-trained models: zero-shot sparsity collapses accuracy, and restoring it requires an iterative fine-tuning loop that is impractical in deployment settings. We present SHARe-KAN, a post-training compiler that compresses spline coefficients via a Gain-Shape-Bias decomposition with a layer-shared codebook, paired with LUTHAM, an ExecuTorch runtime that maps the codebook into on-chip L2. On PASCAL VOC detection with a ResNet-50 backbone, SHARe-KAN Int8 reaches 9.3X storage compression over the Dense KAN baseline (6.32 MB vs. 58.67 MB prediction head) at a 2.0 point in-domain accuracy cost (80.22% vs. 82.22% mAP), with no retraining. Zero-shot transfer to COCO retains 88.9% of the Dense KAN mAP; most of this gap comes from the VQ clustering step itself, and further quantization from FP32 to Int8 costs only 1.3 retention points. The value of the approach compounds at scale: at 50 task heads, Dense KAN prediction-head storage reaches 2.9 GB while SHARe-KAN Int8 requires 211 MB, a 13.9X reduction that brings multi-expert KAN deployment within the memory budgets of contemporary edge silicon.
