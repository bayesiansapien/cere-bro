---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935397+00:00
arxiv_id: 2609.32146
url: https://huggingface.co/papers/2609.32146
arxiv_url: https://arxiv.org/abs/2609.32146
date: 2026-09-29
---

# Playing to Par: Reinforcement Learning for Provably Optimal Quadrilateral Block Decompositions

A quadrilateral block decomposition of a planar domain is judged by whether it is complete, whether its elements are well shaped, and how many of its vertices are irregular. The last has a provable floor: the discrete Gauss-Bonnet identity enforces a lower bound on the total vertex irregularity of any all-quadrilateral mesh of a given domain purely based on its topology and corner angles. We train a reinforcement learning agent to build decompositions that reach this bound, which we call par. It acts directly on the mesh's half-edge data structure through local edits, with a policy network whose convolutions follow the mesh's own connectivity, so it applies unchanged to domains larger than any seen in training. The reward targets the floor directly, and it is sparse: random play reaches it on no domain with more than eight sides. We overcome this exploration barrier via behaviour cloning on optimal meshes that are trivial to construct, walked backward into demonstrations, before training it with PPO. On 96 held-out domains the agent produces an all-quadrilateral mesh on every one, a usable one on 95.7 on average, and a provably optimal one on 90; Gmsh's strongest configuration at the same element count completes 51, is usable on 38 and optimal on none, and even at three to fourteen times the elements never produces a more regular mesh. On 64 domains twice the training size the agent completes all, is usable on 62, and keeps a median excess over par below one against Gmsh's 39 at the same element count.
