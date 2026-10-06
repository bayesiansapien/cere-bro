---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.33804
url: https://huggingface.co/papers/2609.33804
arxiv_url: https://arxiv.org/abs/2609.33804
date: 2026-10-05
---

# MinkowskiPE: Minkowski Positional Encoding for Spatiotemporal Perception

Modeling spatiotemporal coupling is a key challenge in building physical intelligence across scales, from microscopic to macroscopic. Existing models capture such structure broadly through physics-motivated dynamical formulations or learning-motivated architectures. The former provide stronger priors but may constrain flexibility, whereas the latter are more flexible but leave the spatiotemporal coupling largely implicit. We therefore seek an approach that combines flexible learning with an explicit geometric bias for jointly modeling time and space. To this end, we propose Minkowski Positional Encoding (MinkowskiPE), which uses joint temporal and spatial coordinates to parameterize Lorentz transformations applied to query and key features. With MinkowskiPE, the query-key attention score depends on position only through the relative spacetime displacement between the two tokens and is therefore invariant to global translation of the coordinates. This paradigm retains the standard dot-product attention interface and remains compatible with efficient attention implementations. We evaluate MinkowskiPE on microscopic molecular dynamics and macroscopic video prediction tasks, achieving the best results on all nine multi-trajectory molecular evaluations and reducing KTH video-prediction MSE by 9.9% relative to the best baseline while using roughly one-tenth as many parameters.
