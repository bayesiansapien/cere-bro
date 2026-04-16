---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2506.09163
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2506.09163
published: 2026-04-16
authors: Daniel Jenson, Jhonathan Navott, Piotr Grynfelder
---

# Scalable Spatiotemporal Inference with Biased Scan Attention Transformer Neural Processes

**arXiv:** https://arxiv.org/abs/2506.09163
**Authors:** Daniel Jenson, Jhonathan Navott, Piotr Grynfelder

## Abstract

arXiv:2506.09163v2 Announce Type: replace  Abstract: Neural Processes (NPs) are a rapidly evolving class of models designed to directly model the posterior predictive distribution of stochastic processes. While early architectures were developed primarily as a scalable alternative to Gaussian Processes (GPs), modern NPs tackle far more complex and data-hungry applications spanning geology, epidemiology, climate, and robotics. These applications have placed increasing pressure on the scalability of these models, with many architectures compromising accuracy for scalability. In this paper, we demonstrate that this trade-off is often unnecessary, particularly when modeling fully or partially translation-invariant processes. We propose a versatile new architecture, the Biased Scan Attention Transformer Neural Process (BSA-TNP), which introduces Kernel Regression Blocks (KRBlocks), group-invariant attention biases, and memory-efficient Biased Scan Attention (BSA). BSA-TNP is able to: (1) match or exceed the accuracy of the best models while often training in a fraction of the time, (2) exhibit translation invariance, enabling learning at multiple resolutions simultaneously, (3) transparently model processes that evolve in both space and time, (4) support high-dimensional fixed effects, and (5) scale gracefully, running inference on over 1M test points and 100K context points in under a minute on a single 24GB GPU. Code is provided as part of the `dl4bi` package.
