---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13403
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13403
published: 2026-04-16
authors: Yu Wang, Sharon Li
---

# Why Multimodal In-Context Learning Lags Behind? Unveiling the Inner Mechanisms and Bottlenecks

**arXiv:** https://arxiv.org/abs/2604.13403
**Authors:** Yu Wang, Sharon Li

## Abstract

arXiv:2604.13403v1 Announce Type: new  Abstract: In-context learning (ICL) enables models to adapt to new tasks via inference-time demonstrations. Despite its success in large language models, the extension of ICL to multimodal settings remains poorly understood in terms of its internal mechanisms and how it differs from text-only ICL. In this work, we conduct a systematic analysis of ICL in multimodal large language models. Using identical task formulations across modalities, we show that multimodal ICL performs comparably to text-only ICL in zero-shot settings but degrades significantly under few-shot demonstrations. To understand this gap, we decompose multimodal ICL into task mapping construction and task mapping transfer, and analyze how models establish cross-modal task mappings, and transfer them to query samples across layers. Our analysis reveals that current models lack reasoning-level alignment between visual and textual representations, and fail to reliably transfer learned task mappings to queries. Guided by these findings, we further propose a simple inference-stage enhancement method that reinforces task mapping transfer. Our results provide new insights into the mechanisms and limitations of multimodal ICL and suggest directions for more effective multimodal adaptation. Our code is available \href{https://github.com/deeplearning-wisc/Multimocal-ICL-Analysis-Framework-MGI}{here}.
