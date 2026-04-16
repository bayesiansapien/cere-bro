---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2505.18232
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2505.18232
published: 2026-04-16
authors: Mingkuan Feng, Jinyang Wu, Siyuan Liu
---

# Two-Stage Regularization-Based Structured Pruning for LLMs

**arXiv:** https://arxiv.org/abs/2505.18232
**Authors:** Mingkuan Feng, Jinyang Wu, Siyuan Liu

## Abstract

arXiv:2505.18232v3 Announce Type: replace-cross  Abstract: The deployment of large language models (LLMs) is largely hindered by their large number of parameters. Structural pruning has emerged as a promising solution. Prior structured pruning methods directly remove unimportant parameters based on certain metrics, which often causes knowledge loss and necessitates extensive retraining. To overcome this, we introduce a novel pruning method TRSP: Two-Stage Regularization-Based Structured Pruning for LLMs. Specifically, we multiply the output of each transformer layer by an initial learnable weight and iteratively learn these weights by adding their $\ell_1$-norm as a regularization term to the loss function, serving as the first-stage regularization. Subsequently, we apply additional regularization to the difference between the output and input of layers with smaller weights, encouraging the shift of knowledge to the preserved layers. This serves as the second-stage regularization. TRSP retains more knowledge and better preserves model performance than direct parameter elimination. Through extensive experimentation we show that TRSP outperforms strong layer-wise structured pruning methods without requiring retraining. As a layer-wise pruning method, it delivers notable end-to-end acceleration, making it a promising solution for efficient LLM deployment.
