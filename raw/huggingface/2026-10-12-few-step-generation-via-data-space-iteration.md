---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.225349+05:30
arxiv_id: 2610.12102
url: https://huggingface.co/papers/2610.12102
arxiv_url: https://arxiv.org/abs/2610.12102
date: 2026-10-12
---

# Few-Step Generation via Data-Space Iteration

Flow matching has emerged as a scalable paradigm for training high-quality generative models, but sampling from the learned probability flow requires many network evaluations. Distillation can reduce this cost to one or a few evaluations; however, one-step generation often sacrifices quality, making few-step generation the practical operating regime. Existing few-step methods perform their iterative computation along the probability flow and therefore require a fixed, manually chosen timestep discretization. This discretization is often chosen heuristically and is expensive to tune; it may also be restrictive when refinement difficulty differs across samples or spatial locations. We introduce data-space iteration, a few-step generation framework that removes flow discretization altogether. Starting from noise, a shared generator directly refines its prediction in data space, with every iteration trained to produce the best sample permitted by its capacity. Our formulation integrates with distribution matching distillation (DMD) with minimal changes, enabling a controlled comparison between iteration methods under matched training settings. On class-conditional ImageNet 256x256, data-space iteration outperforms standard discretization baselines and matches or improves upon variants selected through schedule search, without requiring schedule-specific training. These results show that data-space iteration provides a simple and effective alternative to discretized flow-space iteration for fast generation.
