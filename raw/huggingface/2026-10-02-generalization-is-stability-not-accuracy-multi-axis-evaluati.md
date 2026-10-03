---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821375+00:00
arxiv_id: 2610.01428
url: https://huggingface.co/papers/2610.01428
arxiv_url: https://arxiv.org/abs/2610.01428
date: 2026-10-02
---

# Generalization Is Stability, Not Accuracy: Multi-Axis Evaluation of LLMs

Generalization in large language models (LLMs) is the ability to produce consistent and semantically stable outputs when the same input is expressed in different ways. Existing work typically evaluates generalization through aggregate accuracy on a single prompt format, task, or set of variations, which conflates robustness with overall benchmark performance. In this work, we show generalization evaluation at the level of individual examples, across multiple input variants, and across different aspects of model behavior, focusing on variability rather than reducing performance to a score that can be improved through narrow training or other ways that obfuscate generalization evaluation. Following this view, we introduce the Stability-Aware Generalization Objective (SAGO), a framework that measures how much model behavior changes for the same input under different variations and benchmarks, capturing variability across several dimensions including generation consistency, internal activations, confidence, and response mirroring. We show that many commonly used models exhibit statistically significant and consistent generalization instability: no model generalizes uniformly, behavioral axes capture independent failure modes, and cross-dataset variation can reverse model rankings.
