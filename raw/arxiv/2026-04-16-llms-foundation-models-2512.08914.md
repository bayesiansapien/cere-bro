---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2512.08914
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2512.08914
published: 2026-04-16
authors: David Zenati, Eliya Nachmani
---

# SAQ: Stabilizer-Aware Quantum Error Correction Decoder

**arXiv:** https://arxiv.org/abs/2512.08914
**Authors:** David Zenati, Eliya Nachmani

## Abstract

arXiv:2512.08914v2 Announce Type: replace-cross  Abstract: Quantum Error Correction (QEC) decoding faces a fundamental accuracy-efficiency tradeoff. Classical methods like Minimum Weight Perfect Matching (MWPM) exhibit variable performance across noise models and suffer from polynomial complexity, while tensor network decoders achieve high accuracy but at prohibitively high computational cost. Recent neural decoders reduce complexity but lack the accuracy needed to compete with computationally expensive classical methods. We introduce SAQ-Decoder, a unified framework combining transformer-based learning with constraint aware post-processing that achieves both near Maximum Likelihood (ML) accuracy and linear computational scalability with respect to the syndrome size. Our approach combines a dual-stream transformer architecture that processes syndromes and logical information with asymmetric attention patterns, and a novel differentiable logical loss that directly optimizes Logical Error Rates (LER) through smooth approximations over finite fields. SAQ-Decoder achieves near-optimal performance, with error thresholds of 10.99% (independent noise) and 18.6% (depolarizing noise) on toric codes that approach the ML bounds of 11.0% and 18.9% while outperforming existing neural and classical baselines in accuracy, complexity, and parameter efficiency. Our findings establish that learned decoders can simultaneously achieve competitive decoding accuracy and computational efficiency, addressing key requirements for practical fault-tolerant quantum computing systems.
