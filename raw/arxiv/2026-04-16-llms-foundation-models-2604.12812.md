---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.12812
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.12812
published: 2026-04-16
authors: Hao Yan, Yuliang Liu, Xingchen Liu
---

# DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding

**arXiv:** https://arxiv.org/abs/2604.12812
**Authors:** Hao Yan, Yuliang Liu, Xingchen Liu

## Abstract

arXiv:2604.12812v2 Announce Type: replace  Abstract: Existing Multimodal Large Language Models (MLLMs) suffer from significant performance degradation on the long document understanding task as document length increases. This stems from two fundamental challenges: 1) a low Signal-to-Noise Ratio (SNR), with crucial evidence buried in irrelevant pages; and 2) supervision scarcity, as datasets offering only final short answers provide a weak learning signal. In this paper, we address these challenges by proposing a paradigm that requires the model to execute a structured Analysis, Localization and Reasoning workflow. To instill this capability, we design a two-stage training framework: we first perform Supervised Fine-Tuning on high-quality data generated via an efficient knowledge distillation strategy. Subsequently, we employ an Evidence-aware Group Relative Policy Optimization which jointly optimizes for both evidence localization and answer accuracy. Additionally, we introduce a Evidence-Guided Resolution Allocation strategy to mitigate memory constraints of training on multi-pages documents. Extensive experiments demonstrate that DocSeeker achieves superior performance on both in-domain and out-of-domain tasks. We show it robustly generalizes from short-page training to ultra-long documents and is naturally synergistic with visual Retrieval-Augmented Generation systems, serving as a solid foundation for their implementation.
