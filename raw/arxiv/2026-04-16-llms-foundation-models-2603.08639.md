---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.08639
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2603.08639
published: 2026-04-16
authors: Simone Carnemolla, Chiara Russo, Simone Palazzo
---

# UNBOX: Unveiling Black-box visual models with Natural-language

**arXiv:** https://arxiv.org/abs/2603.08639
**Authors:** Simone Carnemolla, Chiara Russo, Simone Palazzo

## Abstract

arXiv:2603.08639v2 Announce Type: replace-cross  Abstract: Ensuring trustworthiness in open-world visual recognition requires models that are interpretable, fair, and robust to distribution shifts. Yet modern vision systems are increasingly deployed as proprietary black-box APIs, exposing only output probabilities and hiding architecture, parameters, gradients, and training data. This opacity prevents meaningful auditing, bias detection, and failure analysis. Existing explanation methods assume white- or gray-box access or knowledge of the training distribution, making them unusable in these real-world settings. We introduce UNBOX, a framework for class-wise model dissection under fully data-free, gradient-free, and backpropagation-free constraints. UNBOX leverages Large Language Models and text-to-image diffusion models to recast activation maximization as a purely semantic search driven by output probabilities. The method produces human-interpretable text descriptors that maximally activate each class, revealing the concepts a model has implicitly learned, the training distribution it reflects, and potential sources of bias. We evaluate UNBOX on ImageNet-1K, Waterbirds, and CelebA through semantic fidelity tests, visual-feature correlation analyses and slice-discovery auditing. Despite operating under the strictest black-box constraints, UNBOX performs competitively with state-of-the-art white-box interpretability methods. This demonstrates that meaningful insight into a model's internal reasoning can be recovered without any internal access, enabling more trustworthy and accountable visual recognition systems.
