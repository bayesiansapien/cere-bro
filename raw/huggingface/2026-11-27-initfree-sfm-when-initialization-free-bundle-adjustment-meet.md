---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.31516
url: https://huggingface.co/papers/2611.31516
arxiv_url: https://arxiv.org/abs/2611.31516
date: 2026-11-27
---

# InitFree-SfM: When Initialization-Free Bundle Adjustment meets Learned Structure-from-Motion

Initialization-free bundle adjustment (InitFree BA) aims to jointly recover camera poses and scene structure without requiring an initial global estimate. It is a very challenging problem, especially compared to traditional BA where a good estimation is assumed. While recent methods optimize surrogate Object Space Error (OSE) objectives from random initialization, a low objective value does not necessarily yield an accurate reconstruction, revealing a gap between optimization and reconstruction. We show that existing InitFree BA pipelines struggle to produce accurate 3D reconstructions on modern SfM benchmarks, and demonstrate that incorporating learned metric depth substantially improves their practical feasibility. We introduce InitFree-SfM, a complete initialization-free SfM pipeline combining learned correspondences, metric depth, depth-consistent track construction, and joint metric refinement. Within this framework, we propose a simple depth-augmented OSE (dOSE), which complements the directional constraints of OSE by constraining landmark positions along their viewing rays. Our approach substantially outperforms existing InitFree BA methods and achieves competitive accuracy with established SfM pipelines, including on challenging low-overlap image collections. Importantly, our analysis challenges the prevailing emphasis on surrogate objectives in previous InitFree BA research, revealing that geometric constraints play a central role in accurate reconstruction, while OSE-based optimization provides further improvements.
