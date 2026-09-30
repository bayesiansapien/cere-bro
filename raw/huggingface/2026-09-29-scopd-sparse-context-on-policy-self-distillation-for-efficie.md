---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936373+00:00
arxiv_id: 2609.34044
url: https://huggingface.co/papers/2609.34044
arxiv_url: https://arxiv.org/abs/2609.34044
date: 2026-09-29
---

# SCOPD: Sparse-Context On-Policy Self-Distillation for Efficient Vision-Language Models

Reasoning vision-language models (VLMs) process images and videos as long sequences of visual tokens, making inference expensive. Training-free token pruning reduces this cost, but aggressive compression can sharply degrade performance, often attributed to irreversible loss of task-relevant visual information. We show that this explanation is incomplete. In a fixed-context Pass@K analysis, repeated sampling from the same pruned visual representation recovers many examples missed by greedy decoding, indicating that useful visual evidence can remain accessible but be used unreliably. We call this the representation-utilization gap. Motivated by this observation, we introduce SCOPD, a sparse-context on-policy self-distillation framework in which a student generates reasoning trajectories from pruned visual tokens while a privileged full-context teacher supervises the same on-policy prefixes. SCOPD requires no ground-truth responses, architectural changes, or additional inference-time computation. We further introduce SCOPD+, which uses a small visual-budget intervention to identify visually sensitive response positions and selectively distill them. At 10% visual-token retention, the Vanilla model retains 86.37% of its unpruned performance across 13 benchmarks. SCOPD raises this to 90.49%, while SCOPD+ further improves it to 92.43%. Across token budgets, benchmarks, and pruning operators, our results show that efficient reasoning depends not only on which visual information survives pruning, but also on how reliably the model learns to use it.
