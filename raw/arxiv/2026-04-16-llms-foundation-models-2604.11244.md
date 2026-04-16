---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.11244
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.11244
published: 2026-04-16
authors: Tencent Hunyuan Team
---

# Script-a-Video: Deep Structured Audio-visual Captions via Factorized Streams and Relational Grounding

**arXiv:** https://arxiv.org/abs/2604.11244
**Authors:** Tencent Hunyuan Team

## Abstract

arXiv:2604.11244v2 Announce Type: replace  Abstract: Advances in Multimodal Large Language Models (MLLMs) are transforming video captioning from a descriptive endpoint into a semantic interface for both video understanding and generation. However, the dominant paradigm still casts videos as monolithic narrative paragraphs that entangle visual, auditory, and identity information. This dense coupling not only compromises representational fidelity but also limits scalability, since even local edits can trigger global rewrites. To address this structural bottleneck, we propose Multi-Stream Scene Script (MTSS), a novel paradigm that replaces monolithic text with factorized and explicitly grounded scene descriptions. MTSS is built on two core principles: Stream Factorization, which decouples a video into complementary streams (Reference, Shot, Event, and Global), and Relational Grounding, which reconnects these isolated streams through explicit identity and temporal links to maintain holistic video consistency. Extensive experiments demonstrate that MTSS consistently enhances video understanding across various models, achieving an average reduction of 25% in the total error rate on Video-SALMONN-2 and an average performance gain of 67% on the Daily-Omni reasoning benchmark. It also narrows the performance gap between smaller and larger MLLMs, indicating a substantially more learnable caption interface. Finally, even without architectural adaptation, replacing monolithic prompts with MTSS in multi-shot video generation yields substantial human-rated improvements: a 45% boost in cross-shot identity consistency, a 56% boost in audio-visual alignment, and a 71% boost in temporal controllability.
