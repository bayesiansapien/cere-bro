---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2605.30789
url: https://huggingface.co/papers/2605.30789
arxiv_url: https://arxiv.org/abs/2605.30789
date: 2026-06-15
---

# Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO

We identify a new dimension for enhancing rollout diversity in Group Relative Policy Optimization (GRPO) for LLMs. While GRPO relies on diverse rollouts, prevailing strategies primarily increase diversity by injecting more token-level randomness, which may introduce step-wise noise and lead to incoherent trajectories. We uncover that smaller models within the same model family inherently exhibit higher policy-level diversity, indicated by their superior pass@k relative to larger counterparts as sample counts increase. Unlike token-level noise, this diversity is temporally correlated, preserves logical consistency, and provides structured exploration signals for gradient estimation. We thus propose S2L-PO (Small-to-Large Policy Optimization), a framework that leverages fixed small models as natural explorers to train larger models. To balance exploration and exploitation, we design a progressive annealing strategy that transitions from offline small-model rollouts to the large learner's own sampling. This shift elegantly avoids mid-training performance drops caused by the small model's capacity limits, achieving faster convergence and unlocking a higher performance ceiling. S2L-PO improves accuracy on diverse mathematical reasoning benchmarks (e.g., +8.8% on AIME 24 using a 1.7B explorer to guide the 8B model) while reducing rollout compute.
