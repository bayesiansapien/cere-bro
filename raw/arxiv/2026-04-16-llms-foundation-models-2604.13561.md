---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13561
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13561
published: 2026-04-16
authors: Shivika, Kartik Bose, Pankaj Gupta
---

# CLIP Architecture for Abdominal CT Image-Text Alignment and Zero-Shot Learning: Investigating Batch Composition and Data Scaling

**arXiv:** https://arxiv.org/abs/2604.13561
**Authors:** Shivika, Kartik Bose, Pankaj Gupta

## Abstract

arXiv:2604.13561v1 Announce Type: cross  Abstract: Vision-language models trained with contrastive learning on paired medical images and reports show strong zero-shot diagnostic capabilities, yet the effect of training batch composition on learned representations remains unexplored for 3D medical imaging. We reproduce Merlin, a dual-encoder model that aligns 3D abdominal CT volumes with radiology reports using symmetric InfoNCE loss, achieving a zero-shot macro F1 of 74.45% across 30 findings (original: 73.00%). We then investigate two axes of variation. First, we control the normal-to-abnormal ratio within training batches at 25:75, 50:50, and 75:25 using section-level balanced sampling on the full dataset. All three configurations underperform the unbalanced baseline by 2.4 to 2.8 points, with 75:25 achieving the best result (72.02%) among balanced variants. Second, we conduct data scaling ablations on a 4,362-study subset, training with 20%, 40%, and 100% of the data. Performance scales sub-linearly from 65.26% to 71.88%, with individual findings varying dramatically in data sensitivity. Enforcing 50:50 balanced sampling on the same subset further degrades performance to 68.01%, confirming that explicit class balancing hurts regardless of dataset or balancing granularity. Our results indicate that the stochastic diversity of random sampling, combined with Merlin's alternating batching over anatomical subsections, provides more effective regularization than engineered class ratios at the small batch sizes required by 3D medical volumes.
