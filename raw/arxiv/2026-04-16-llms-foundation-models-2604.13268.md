---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13268
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13268
published: 2026-04-16
authors: Bahey Tharwat, Giorgos Kordopatis-Zilos, Pavel Suma
---

# Indexing Multimodal Language Models for Large-scale Image Retrieval

**arXiv:** https://arxiv.org/abs/2604.13268
**Authors:** Bahey Tharwat, Giorgos Kordopatis-Zilos, Pavel Suma

## Abstract

arXiv:2604.13268v1 Announce Type: cross  Abstract: Multimodal Large Language Models (MLLMs) have demonstrated strong cross-modal reasoning capabilities, yet their potential for vision-only tasks remains underexplored. We investigate MLLMs as training-free similarity estimators for instance-level image-to-image retrieval. Our approach prompts the model with paired images and converts next-token probabilities into similarity scores, enabling zero-shot re-ranking within large-scale retrieval pipelines. This design avoids specialized architectures and fine-tuning, leveraging the rich visual discrimination learned during multimodal pre-training. We address scalability by combining MLLMs with memory-efficient indexing and top-$k$ candidate re-ranking. Experiments across diverse benchmarks show that MLLMs outperform task-specific re-rankers outside their native domains and exhibit superior robustness to clutter, occlusion, and small objects. Despite strong results, we identify failure modes under severe appearance changes, highlighting opportunities for future research. Our findings position MLLMs as a promising alternative for open-world large-scale image retrieval.
