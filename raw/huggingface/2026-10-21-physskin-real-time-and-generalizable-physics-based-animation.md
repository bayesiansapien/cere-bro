---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.642111
arxiv_id: 2610.26067
url: https://huggingface.co/papers/2610.26067
arxiv_url: https://arxiv.org/abs/2610.26067
date: 2026-10-21
---

# PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning

Generalizing real-time physics-based animation across diverse 3D shapes and spatial discretizations remains challenging. In this paper, we introduce PhysSkin++, a physics-informed framework that learns continuous neural skinning fields from static geometries to construct compact deformation subspaces. Specifically, we propose a Neural Skinning Fields Autoencoder that predicts shape-dependent deformation subspaces without per-object network training. To learn these subspaces without simulation trajectories, we develop a Physics-Informed Self-Supervised Learning strategy that combines skinning-field normalization with conflict-aware gradient correction, stabilizing joint optimization under physical and orthogonality constraints. The learned representation supports efficient reduced dynamics with user control and contact interactions, together with direct animation binding to meshes, point clouds, and 3D Gaussians. For prescribed rig animation, we further introduce a self-supervised complementarity objective to learn complementary elastic responses without enforcing complementarity constraints at runtime. Experiments demonstrate cross-shape generalization of the learned skinning fields, real-time reduced simulation, and applications to controllable, collision-aware, and rig-complementary animation.
