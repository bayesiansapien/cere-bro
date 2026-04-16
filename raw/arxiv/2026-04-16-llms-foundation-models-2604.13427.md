---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13427
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13427
published: 2026-04-16
authors: Junlin Li, Xinhao Song, Siqi Wang
---

# A Unified Conditional Flow for Motion Generation, Editing, and Intra-Structural Retargeting

**arXiv:** https://arxiv.org/abs/2604.13427
**Authors:** Junlin Li, Xinhao Song, Siqi Wang

## Abstract

arXiv:2604.13427v1 Announce Type: cross  Abstract: Text-driven motion editing and intra-structural retargeting, where source and target share topology but may differ in bone lengths, are traditionally handled by fragmented pipelines with incompatible inputs and representations: editing relies on specialized generative steering, while retargeting is deferred to geometric post-processing. We present a unifying perspective where both tasks are cast as instances of conditional transport within a single generative framework. By leveraging recent advances in flow matching, we demonstrate that editing and retargeting are fundamentally the same generative task, distinguished only by which conditioning signal, semantic or structural, is modulated during inference. We implement this vision via a rectified-flow motion model jointly conditioned on text prompts and target skeletal structures. Our architecture extends a DiT-style transformer with per-joint tokenization and explicit joint self-attention to strictly enforce kinematic dependencies, while a multi-condition classifier-free guidance strategy balances text adherence with skeletal conformity. Experiments on SnapMoGen and a multi-character Mixamo subset show that a single trained model supports text-to-motion generation, zero-shot editing, and zero-shot intra-structural retargeting. This unified approach simplifies deployment and improves structural consistency compared to task-specific baselines.
