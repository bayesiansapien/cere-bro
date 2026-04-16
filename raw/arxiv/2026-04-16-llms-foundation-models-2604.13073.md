---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13073
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13073
published: 2026-04-16
authors: Qianqi Yan, Yichen Guo, Ching-Chen Kuo
---

# OmniTrace: A Unified Framework for Generation-Time Attribution in Omni-Modal LLMs

**arXiv:** https://arxiv.org/abs/2604.13073
**Authors:** Qianqi Yan, Yichen Guo, Ching-Chen Kuo

## Abstract

arXiv:2604.13073v1 Announce Type: cross  Abstract: Modern multimodal large language models (MLLMs) generate fluent responses from interleaved text, image, audio, and video inputs. However, identifying which input sources support each generated statement remains an open challenge. Existing attribution methods are primarily designed for classification settings, fixed prediction targets, or single-modality architectures, and do not naturally extend to autoregressive, decoder-only models performing open-ended multimodal generation. We introduce OmniTrace, a lightweight and model-agnostic framework that formalizes attribution as a generation-time tracing problem over the causal decoding process. OmniTrace provides a unified protocol that converts arbitrary token-level signals such as attention weights or gradient-based scores into coherent span-level, cross-modal explanations during decoding. It traces each generated token to multimodal inputs, aggregates signals into semantically meaningful spans, and selects concise supporting sources through confidence-weighted and temporally coherent aggregation, without retraining or supervision. Evaluations on Qwen2.5-Omni and MiniCPM-o-4.5 across visual, audio, and video tasks demonstrate that generation-aware span-level attribution produces more stable and interpretable explanations than naive self-attribution and embedding-based baselines, while remaining robust across multiple underlying attribution signals. Our results suggest that treating attribution as a structured generation-time tracing problem provides a scalable foundation for transparency in omni-modal language models.
