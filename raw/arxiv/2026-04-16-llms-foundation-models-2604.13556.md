---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13556
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13556
published: 2026-04-16
authors: You Wu, Ziheng Chen, Yizhen Zhang
---

# YOCO++: Enhancing YOCO with KV Residual Connections for Efficient LLM Inference

**arXiv:** https://arxiv.org/abs/2604.13556
**Authors:** You Wu, Ziheng Chen, Yizhen Zhang

## Abstract

arXiv:2604.13556v1 Announce Type: new  Abstract: Cross-layer key-value (KV) compression has been found to be effective in efficient inference of large language models (LLMs). Although they reduce the memory consumption of the KV cache, such methods usually introduce non-negligible performance degradation. In this work, we aim to enhance the performance of YOCO, a cross-layer KV compression method that shares the KVs of the middle layer with the top-half layers. We propose YOCO++, an enhanced YOCO that incorporates a weighted residual connection between the KVs of each bottom-half layer and the bottom layer. Compared to YOCO, YOCO++ increases model capacity while maintaining the same training and inference efficiency. Our experiments show that YOCO++ achieves state-of-the-art performance among the cross-layer KV compression methods at a 50% KV cache compression rate, outperforming the standard Transformer.
