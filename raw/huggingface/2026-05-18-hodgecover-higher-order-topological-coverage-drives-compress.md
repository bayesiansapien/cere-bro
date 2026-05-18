---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.13997
url: https://huggingface.co/papers/2605.13997
arxiv_url: https://arxiv.org/abs/2605.13997
date: 2026-05-18
---

# HodgeCover: Higher-Order Topological Coverage Drives Compression of Sparse Mixture-of-Experts

Sparse Mixture-of-Experts (MoE) layers route tokens through a handful of experts, and learning-free compression of these layers reduces inference cost without retraining. A subtle obstruction blocks every existing compressor in this family: three experts can each be pairwise compatible yet form an irreducible cycle when merged together, so any score that ranks experts on pairwise signals is structurally blind to which triples are jointly mergeable. We show the obstruction is a precise mathematical object, the harmonic kernel of the simplicial Laplacian on a 2-complex whose vertices are experts, whose edges carry KL merge barriers, and whose faces carry triplet barriers; Hodge-decomposing the edge-barrier signal isolates the kernel exactly. We turn the diagnostic into a selection objective: HodgeCover greedily covers the harmonic-critical edges and triplet-critical triangles, and a hybrid variant of HodgeCover pairs it with off-the-shelf weight pruning on survivors. On three open-weight Sparse MoE backbones under aggressive expert reduction, HodgeCover matches state-of-the-art learning-free baselines on the expert-reduction axis, leads on the aggressive-compression frontier of the hybrid axis, and uniquely balances retained mass across all four Hodge components.
