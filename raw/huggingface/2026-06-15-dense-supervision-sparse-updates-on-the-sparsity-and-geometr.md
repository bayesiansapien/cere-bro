---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.13657
url: https://huggingface.co/papers/2606.13657
arxiv_url: https://arxiv.org/abs/2606.13657
date: 2026-06-15
---

# Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation

On-policy distillation (OPD) has recently become a prominent post-training recipe as it combines two desirable ingredients: on-policy student trajectories and dense teacher supervision, yet how this hybrid changes a model's parameters remains unclear. Across several language and vision-language model pairs and use cases, our analysis yields two main findings. On sparsity, OPD-style updates are small and coordinate-sparse. They are distributed across layers and are usually FFN-heavy. This sparse structure is operationally useful: training only the discovered subnetwork recovers nearly the same performance as full OPD. However, the sparsity-inducing SGD optimizer underperforms AdamW in our optimizer ablation, likely because dense teacher supervision preserves heterogeneous coordinate-wise gradient scales where AdamW's adaptive scaling remains useful. On geometry, the updates are numerically full-rank but spectrally concentrated; they lie mostly away from the principal singular subspaces of the source weights and fall disproportionately on coordinates where the source weights are close to zero. These findings suggest that dense teacher supervision does not turn OPD into ordinary dense parameter rewriting; instead, OPD retains important geometric signatures of on-policy post-training.
