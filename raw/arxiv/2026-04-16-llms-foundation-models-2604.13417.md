---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13417
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13417
published: 2026-04-16
authors: Jonathan Pan
---

# The Cognitive Circuit Breaker: A Systems Engineering Framework for Intrinsic AI Reliability

**arXiv:** https://arxiv.org/abs/2604.13417
**Authors:** Jonathan Pan

## Abstract

arXiv:2604.13417v1 Announce Type: cross  Abstract: As Large Language Models (LLMs) are increasingly deployed in mission-critical software systems, detecting hallucinations and ``faked truthfulness'' has become a paramount engineering challenge. Current reliability architectures rely heavily on post-generation, black-box mechanisms, such as Retrieval-Augmented Generation (RAG) cross-checking or LLM-as-a-judge evaluators. These extrinsic methods introduce unacceptable latency, high computational overhead, and reliance on secondary external API calls, frequently violating standard software engineering Service Level Agreements (SLAs). In this paper, we propose the Cognitive Circuit Breaker, a novel systems engineering framework that provides intrinsic reliability monitoring with minimal latency overhead. By extracting hidden states during a model's forward pass, we calculate the ``Cognitive Dissonance Delta'' -- the mathematical gap between an LLM's outward semantic confidence (softmax probabilities) and its internal latent certainty (derived via linear probes). We demonstrate statistically significant detection of cognitive dissonance, highlight architecture-dependent Out-of-Distribution (OOD) generalization, and show that this framework adds negligible computational overhead to the active inference pipeline.
