---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13847
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13847
published: 2026-04-16
authors: Hongtao Xu, Jianchao Tan, Yuxuan Hu
---

# SparseBalance: Load-Balanced Long Context Training with Dynamic Sparse Attention

**arXiv:** https://arxiv.org/abs/2604.13847
**Authors:** Hongtao Xu, Jianchao Tan, Yuxuan Hu

## Abstract

arXiv:2604.13847v1 Announce Type: cross  Abstract: While sparse attention mitigates the computational bottleneck of long-context LLM training, its distributed training process exhibits extreme heterogeneity in both \textit{1)} sequence length and \textit{2)} sparsity sensitivity, leading to a severe imbalance problem and sub-optimal model accuracy. Existing algorithms and training frameworks typically focus on single issue, failing to systematically co-optimize these two problems. Therefore, we propose SparseBalance, a novel algorithm-system co-design framework, which exploits the sparsity and sequence heterogeneity to optimize model accuracy and system efficiency jointly. First, we propose workload-aware dynamic sparsity tuning, which employs a bidirectional sparsity adjustment to eliminate stragglers and exploit inherent bubbles for free accuracy. Second, we propose a sparsity-aware batching strategy to achieve coarse-grained balance, which complements dynamic sparsity tuning. Experimental results demonstrate that SparseBalance achieves up to a 1.33$\times$ end-to-end speedup while still improving the long-context capability by 0.46\% on the LongBench benchmark.
