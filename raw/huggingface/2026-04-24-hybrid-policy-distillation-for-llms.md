---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00
arxiv_id: 2604.20244
url: https://huggingface.co/papers/2604.20244
arxiv_url: https://arxiv.org/abs/2604.20244
date: 2026-04-24
upvotes: 11
---

# Hybrid Policy Distillation for LLMs

Knowledge distillation (KD) is a powerful paradigm for compressing large language models (LLMs), whose effectiveness depends on intertwined choices of divergence direction, optimization strategy, and data regime. This paper breaks down the design of existing KD methods and presents a unified view establishing connections between them, reformulating KD as a reweighted log-likelihood objective at the token level.

Proposes Hybrid Policy Distillation (HPD), which integrates the complementary advantages of forward and reverse KL to balance mode coverage and mode-seeking, and combines off-policy data with lightweight, approximate on-policy sampling. Validated on long-generation math reasoning as well as short-generation dialogue and code tasks, demonstrating improved optimization stability, computational efficiency, and final performance across diverse model families and scales.
