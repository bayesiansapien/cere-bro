---
source: farmer/huggingface
farmed: 2026-07-22T05:46:30Z
arxiv_id: 2607.18722
url: https://huggingface.co/papers/2607.18722
arxiv_url: https://arxiv.org/abs/2607.18722
date: 2026-07-22
---

# Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning

Asynchronous reinforcement learning improves throughput by decoupling rollout generation from optimization, but staleness is an inevitable byproduct compounded by policy lag, engine delays, and mixture-of-experts routing. From a trust-region perspective, this mismatch is critical: training-inference divergence governs approximation error in finite-horizon bounds, whereas PPO clipping only gates sampled outward updates, acting as a sampled surrogate rather than a full-policy constraint. As a result, high-staleness updates remain weakly controlled in the asynchronous regime where stale rollouts matter most.
  We introduce the Staleness-Adaptive Trust Region (SAT), which uses the detached sampled log-ratio as a practical staleness proxy, identifies high-mismatch tails within each batch via staleness-based kernel scaling, and contracts only the sign-selected endpoint of the nominal PPO interval. This preserves baseline behavior on ordinary tokens while enforcing more conservative updates on newly intercepted outward bands. We prove local interval containment and pointwise pessimism relative to PPO, showing how the adaptive rule reshapes update geometry under heterogeneous staleness.
  We evaluate SAT in a decoupled asynchronous RL setup built on Qwen3-30B-A3B-Base, using SGLang as the inference engine and Megatron for training. In this setting, SAT-GSPO w/ R3 achieves the best observed AIME24 avg@8, reaching 35.83 at lag 1 and 34.79 at lag 8, while SAT-GSPO reaches 34.17 at lag 1. Adaptive clipping and routing replay act as complementary stabilizers targeting mismatch tails and routing inconsistency, respectively. Overall, aligning clip intervals with staleness heterogeneity effectively stabilizes asynchronous RL.
