---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13479
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13479
published: 2026-04-16
authors: Lakmali Nadeesha Kumari, Sen-Ching Samson Cheung
---

# Learning Class Difficulty in Imbalanced Histopathology Segmentation via Dynamic Focal Attention

**arXiv:** https://arxiv.org/abs/2604.13479
**Authors:** Lakmali Nadeesha Kumari, Sen-Ching Samson Cheung

## Abstract

arXiv:2604.13479v1 Announce Type: cross  Abstract: Semantic segmentation of histopathology images under class imbalance is typically addressed through frequency-based loss reweighting, which implicitly assumes that rare classes are difficult. However, true difficulty also arises from morphological variability, boundary ambiguity, and contextual similarity-factors that frequency cannot capture. We propose Dynamic Focal Attention (DFA), a simple and efficient mechanism that learns class-specific difficulty directly within the cross-attention of query-based mask decoders. DFA introduces a learnable per-class bias to attention logits, enabling representation-level reweighting prior to prediction rather than gradient-level reweighting after prediction. Initialised from a log-frequency prior to prevent gradient starvation, the bias is optimised end-to-end, allowing the model to adaptively capture difficulty signals through training, effectively unifying frequency-based and difficulty-aware approaches under a common attention-bias framework. On three histopathology benchmarks (BDSA, BCSS, CRAG), DFA consistently improves Dice and IoU, matching or exceeding a difficulty-aware baseline without a separate estimator or additional training stage. These results demonstrate that encoding class difficulty at the representation level provides a principled alternative to conventional loss reweighting for imbalanced segmentation.
