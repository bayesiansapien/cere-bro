---
source: farmer/huggingface
farmed: 2026-05-05T00:00:00
arxiv_id: 2605.02222
url: https://huggingface.co/papers/2605.02222
arxiv_url: https://arxiv.org/abs/2605.02222
date: 2026-05-05
---

# Generative Modeling with Orbit-Space Particle Flow Matching

We present Orbit-Space Geometric Probability Paths (OGPP), a particle-native flow-matching framework for generative modeling of particle systems. The method addresses two key insights: particles possess permutation symmetries that inflate variance, and particles exist in physical space where terminal velocity carries geometric meaning.

OGPP implements three components: orbit-space canonicalization of probability-path endpoints, particle index embeddings for role specialization, and geometric probability paths with arc-length-aware terminal velocities that generate normals as a byproduct.

The framework demonstrates significant improvements across benchmarks. On minimal-surface tasks, it reduces metric error by up to two orders of magnitude in single inference steps. On ShapeNet, it achieves state-of-the-art results using 5x fewer steps, reaching airplane results comparable to DiT-3D while using 26x fewer parameters and 5x fewer steps. For single-shape encoding, it produces competitive normals and reconstructions while operating entirely in 3D space.
