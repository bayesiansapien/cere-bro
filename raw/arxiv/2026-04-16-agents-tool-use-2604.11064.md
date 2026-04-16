---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.11064
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.11064
published: 2026-04-16
authors: Wei Li, Hangjie Yuan, Zixiang Zhao
---

# A Faster Path to Continual Learning

**arXiv:** https://arxiv.org/abs/2604.11064
**Authors:** Wei Li, Hangjie Yuan, Zixiang Zhao

## Abstract

arXiv:2604.11064v2 Announce Type: replace  Abstract: Continual Learning (CL) aims to train neural networks on a dynamic stream of tasks without forgetting previously learned knowledge. Among optimization-based approaches, C-Flat has emerged as a promising solution due to its plug-and-play nature and its ability to encourage uniformly low-loss regions for both new and old tasks. However, C-Flat requires three additional gradient computations per iteration, imposing substantial overhead on the optimization process. In this work, we propose C-Flat Turbo, a faster yet stronger optimizer that significantly reduces the training cost. We show that the gradients associated with first-order flatness contain direction-invariant components relative to the proxy-model gradients, enabling us to skip redundant gradient computations in the perturbed ascent steps. Moreover, we observe that these flatness-promoting gradients progressively stabilize across tasks, which motivates a linear scheduling strategy with an adaptive trigger to allocate larger turbo steps for later tasks. Experiments show that C-Flat Turbo is 1.0$\times$ to 1.25$\times$ faster than C-Flat across a wide range of CL methods, while achieving comparable or even improved accuracy.
