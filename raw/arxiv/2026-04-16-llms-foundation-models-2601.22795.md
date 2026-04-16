---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2601.22795
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2601.22795
published: 2026-04-16
authors: Corentin Kervadec, Iuliia Lysova, Marco Baroni
---

# Sparse or Dense? A Mechanistic Estimation of Computation Density in Transformer-based LLMs

**arXiv:** https://arxiv.org/abs/2601.22795
**Authors:** Corentin Kervadec, Iuliia Lysova, Marco Baroni

## Abstract

arXiv:2601.22795v2 Announce Type: replace  Abstract: Transformer-based large language models (LLMs) are comprised of billions of parameters arranged in deep and wide computational graphs. Several studies on LLM efficiency optimization argue that it is possible to prune a significant portion of the parameters, while only marginally impacting performance. This suggests that the computation is not uniformly distributed across the parameters. We introduce here a technique to systematically quantify computation density in LLMs. In particular, we design a density estimator drawing on mechanistic interpretability. We experimentally test our estimator and find that: (1) contrary to what has been often assumed, LLM processing generally involves dense computation; (2) computation density is dynamic, in the sense that models shift between sparse and dense processing regimes depending on the input; (3) per-input density is significantly correlated across LLMs, suggesting that the same inputs trigger either low or high density. Investigating the factors influencing density, we observe that predicting rarer tokens requires higher density, and increasing context length often decreases the density. We believe that our computation density estimator will contribute to a better understanding of the processing at work in LLMs, challenging their symbolic interpretation.
