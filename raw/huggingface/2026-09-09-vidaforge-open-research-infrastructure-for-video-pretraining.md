---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.06652
url: https://huggingface.co/papers/2609.06652
arxiv_url: https://arxiv.org/abs/2609.06652
date: 2026-09-09
---

# VidaForge: Open Research Infrastructure for Video Pretraining Data Recipes

Video foundation models increasingly rely on large-scale pretraining data, yet the end-to-end data pipelines behind them remain largely closed and difficult to inspect or reuse. Researchers seeking to understand how video data recipes affect model pretraining often need to build substantial infrastructure before testing even a focused hypothesis. We present VIDAFORGE, an open research infrastructure that represents a video data recipe as an executable five-stage workflow from raw videos to training datasets. A decision in this workflow can be varied to construct alternative datasets while preserving how every sample was produced. To demon strate this research workflow, we compare data recipes with different coverage and quality in early from-scratch pretraining of Wan 2.1 and V-JEPA 2.1. Across both learning objectives, the broader-coverage recipe achieves the highest downstream benchmark scores, while loss-based evaluation favors different recipes. This study demonstrates how VidaForge connects data-recipe choices to downstream model performance. We further release VIDAFORGE-3M, containing 3.14 million scene level clips totaling 6,475 hours, with fine-grained annotations and curation signals for video data-recipe research.
