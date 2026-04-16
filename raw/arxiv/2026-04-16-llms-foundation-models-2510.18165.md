---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.18165
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.18165
published: 2026-04-16
authors: Yihong Dong, Zhaoyu Ma, Xue Jiang
---

# Saber: An Efficient Sampling with Adaptive Acceleration and Backtracking Enhanced Remasking for Diffusion Language Model

**arXiv:** https://arxiv.org/abs/2510.18165
**Authors:** Yihong Dong, Zhaoyu Ma, Xue Jiang

## Abstract

arXiv:2510.18165v2 Announce Type: replace  Abstract: Diffusion language models (DLMs) are emerging as a powerful and promising alternative to the dominant autoregressive paradigm, offering inherent advantages in parallel generation and bidirectional context modeling. However, the performance of DLMs on code generation tasks, which have stronger structural constraints, is significantly hampered by the critical trade-off between inference speed and output quality. We observed that accelerating the code generation process by reducing the number of sampling steps usually leads to a catastrophic collapse in performance. In this paper, we introduce efficient Sampling with Adaptive acceleration and Backtracking Enhanced Remasking (i.e., Saber), a novel training-free sampling algorithm for DLMs to achieve better inference speed and output quality in code generation. Specifically, Saber is motivated by two key insights in the DLM generation process: 1) it can be adaptively accelerated as more of the code context is established; 2) it requires a backtracking mechanism to reverse the generated tokens. Extensive experiments on multiple mainstream code generation benchmarks show that Saber boosts Pass@1 accuracy by an average improvement of 1.9% over mainstream DLM sampling methods, meanwhile achieving an average 251.4% inference speedup. By leveraging the inherent advantages of DLMs, our work significantly narrows the performance gap with autoregressive models in code generation.
