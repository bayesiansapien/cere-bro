---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.419298+00:00
arxiv_id: 2610.09059
url: https://huggingface.co/papers/2610.09059
arxiv_url: https://arxiv.org/abs/2610.09059
date: 2026-10-09
---

# EDiS: Edge Disjoint Subgraph Sparsification Framework for Graph Neural Networks

Sparse GNN training reduces computation, but deciding which edges to keep can be costly. Reusing one sparse graph is cheap, but locks training to a fixed topology, while varying it across epochs can require repeated sampling or recomputation. We introduce EDiS (Edge-Disjoint Subgraph sparsification framework), which separates one-time structural extraction from per-epoch graph composition. EDiS decomposes the graph once into cacheable edge-disjoint subgraphs, then recombines them into graphs with edge-budget constraints across epochs and retention ratios without re-extracting structure. Our default construction uses feature-based scores and successive maximum score covering forests, while the same composition mechanism also supports alternative edge selection rules. We provide a combinatorial analysis of the per-epoch sampler, the composition step that draws a training graph from the cached decomposition. We show that, under the default covering-forest selector, the stored decomposition deterministically preserves high-score cut edges, and we derive a selector-agnostic conditional bound on high-score cut survival in composed training graphs. Across 19 homophilic, heterophilic, and large-scale node classification benchmarks against 17 baselines under the same edge budget, EDiS achieves the highest mean benchmark score (accuracy/ROC-AUC) and the lowest average rank and gap-to-best among ranked methods. Ablations show the clearest benefits of structural decomposition and epoch variation at tight edge budgets.
