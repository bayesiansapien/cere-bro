---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13258
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13258
published: 2026-04-16
authors: Vishal Pramanik, Maisha Maliha, Nathaniel D. Bastian
---

# Hessian-Enhanced Token Attribution (HETA): Interpreting Autoregressive LLMs

**arXiv:** https://arxiv.org/abs/2604.13258
**Authors:** Vishal Pramanik, Maisha Maliha, Nathaniel D. Bastian

## Abstract

arXiv:2604.13258v1 Announce Type: cross  Abstract: Attribution methods seek to explain language model predictions by quantifying the contribution of input tokens to generated outputs. However, most existing techniques are designed for encoder-based architectures and rely on linear approximations that fail to capture the causal and semantic complexities of autoregressive generation in decoder-only models. To address these limitations, we propose Hessian-Enhanced Token Attribution (HETA), a novel attribution framework tailored for decoder-only language models. HETA combines three complementary components: a semantic transition vector that captures token-to-token influence across layers, Hessian-based sensitivity scores that model second-order effects, and KL divergence to measure information loss when tokens are masked. This unified design produces context-aware, causally faithful, and semantically grounded attributions. Additionally, we introduce a curated benchmark dataset for systematically evaluating attribution quality in generative settings. Empirical evaluations across multiple models and datasets demonstrate that HETA consistently outperforms existing methods in attribution faithfulness and alignment with human annotations, establishing a new standard for interpretability in autoregressive language models.
