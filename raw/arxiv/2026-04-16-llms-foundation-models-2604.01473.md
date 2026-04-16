---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.01473
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.01473
published: 2026-04-16
authors: Zikai Zhang, Rui Hu, Olivera Kotevska
---

# SelfGrader: Stable Jailbreak Detection for Large Language Models using Token-Level Logits

**arXiv:** https://arxiv.org/abs/2604.01473
**Authors:** Zikai Zhang, Rui Hu, Olivera Kotevska

## Abstract

arXiv:2604.01473v2 Announce Type: replace-cross  Abstract: Large Language Models (LLMs) are powerful tools for answering user queries, yet they remain highly vulnerable to jailbreak attacks. Existing guardrail methods typically rely on internal features or textual responses to detect malicious queries, which either introduce substantial latency or suffer from the randomness in text generation. To overcome these limitations, we propose SelfGrader, a lightweight guardrail method that formulates jailbreak detection as a numerical grading problem using token-level logits. Specifically, SelfGrader evaluates the safety of a user query within a compact set of numerical tokens (NTs) (e.g., 0-9) and interprets their logit distribution as an internal safety signal. To align these signals with human intuition of maliciousness, SelfGrader introduces a dual-perspective scoring rule that considers both the maliciousness and benignness of the query, yielding a stable and interpretable score that reflects harmfulness and reduces the false positive rate simultaneously. Extensive experiments across diverse jailbreak benchmarks, multiple LLMs, and state-of-the-art guardrail baselines demonstrate that SelfGrader achieves up to a 22.66% reduction in ASR on LLaMA-3-8B, while maintaining significantly lower memory overhead (up to 173x) and latency (up to 26x).
