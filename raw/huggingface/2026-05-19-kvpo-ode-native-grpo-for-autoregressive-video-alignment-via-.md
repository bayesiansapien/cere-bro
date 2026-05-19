---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.14278
url: https://huggingface.co/papers/2605.14278
arxiv_url: https://arxiv.org/abs/2605.14278
date: 2026-05-19
---

# KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration

Aligning streaming autoregressive (AR) video generators with human preferences is challenging. Existing reinforcement learning methods predominantly rely on noise-based exploration and SDE-based surrogate policies that are mismatched to the deterministic ODE dynamics of distilled AR models, and tend to perturb low-level appearance rather than the high-level semantic storyline progression critical for long-horizon coherence. To address these limitations, we present KVPO, an ODE-native online Group Relative Policy Optimization (GRPO) framework for aligning streaming video generators. For diversity exploration, KVPO introduces a causal-semantic exploration paradigm that relocates the source of variation from stochastic noise to the historical KV cache. By stochastically routing historical KV entries, it constructs semantically diverse generation branches that remain strictly on the data manifold. For policy modeling, KVPO introduces a velocity-field surrogate policy based on Trajectory Velocity Energy (TVE), which quantifies branch likelihood in flow-matching velocity space and yields a reward-weighted contrastive objective fully consistent with the native ODE formulation. Experiments on multiple distilled AR video generators demonstrate consistent gains in visual quality, motion quality, and text-video alignment across both single-prompt short-video and multi-prompt long-video settings.
