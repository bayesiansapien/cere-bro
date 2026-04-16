---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13777
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13777
published: 2026-04-16
authors: Wenxuan Li, Zhenfei Zhang, Mi Zhang
---

# From Anchors to Supervision: Memory-Graph Guided Corpus-Free Unlearning for Large Language Models

**arXiv:** https://arxiv.org/abs/2604.13777
**Authors:** Wenxuan Li, Zhenfei Zhang, Mi Zhang

## Abstract

arXiv:2604.13777v1 Announce Type: cross  Abstract: Large language models (LLMs) may memorize sensitive or copyrighted content, raising significant privacy and legal concerns. While machine unlearning has emerged as a potential remedy, prevailing paradigms rely on user-provided forget sets, making unlearning requests difficult to audit and exposing systems to secondary leakage and malicious abuse. We propose MAGE, a Memory-grAph Guided Erasure framework for user-minimized, corpus-free unlearning. Given only a lightweight user anchor that identifies a target entity, MAGE probes the target LLM to recover target-related memorization, organizes it into a weighted local memory graph, and synthesizes scoped supervision for unlearning. MAGE is model-agnostic, can be plugged into standard unlearning methods, and requires no access to the original training corpus. Experiments on two benchmarks, TOFU and RWKU, demonstrate that MAGE's self-generated supervision achieves effective unlearning performance comparable to supervision generated with external reference, while preserving overall utility. These results support a practical and auditable unlearning workflow driven by minimal anchors rather than user-supplied forget corpora.
