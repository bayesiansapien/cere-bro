---
source: farmer/huggingface
farmed: 2026-09-11T16:31:48.372582+05:30
arxiv_id: 2609.11042
url: https://huggingface.co/papers/2609.11042
arxiv_url: https://arxiv.org/abs/2609.11042
date: 2026-09-10
---

# T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks

Agent usage is shifting toward long-horizon tasks such as coding and scientific discovery, among which terminal tasks are especially important. We introduce T1, a Mixture-of-Experts model of 122B total trained with reinforcement learning, operating a real shell in a cloud sandbox for up to 300+ tool-call turns per task, rewarded by executing each task's own verifier. We provide a comprehensive recipe: First, an aggressively warm-started to stabilize actor-critic training, with a dense process reward scoring trajectories by the absolute number of passing verifiers. Second, stable optimization through TITO construction, training on the exact sampled token identifiers with drift repair at turn boundaries, and rollout routing replay, recording the sampler's per-token expert choices at every MoE layer and replaying them during training. Third, fully out-of-distribution training corpus: isolated seeds and synthesized tasks disjoint from Terminal-Bench 2.1 ensures gains reflect genuine capability transfer over benchmark overfitting. Together, TITO and R3 cut the training-to-inference log-probability difference from 0.021 to 0.013, with exactly aligned zero token drift in the loss region. On Terminal-Bench 2.1, our post-train pipeline raises initial base model from 43.8% to T1 with 64.0% resolved. On Long-Horizon Terminal Bench, T1 reaches 27.9% and surpasses GPT-5.4 and GLM-5.1.
