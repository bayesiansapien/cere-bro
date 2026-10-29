---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.993275+05:30
arxiv_id: 2610.35013
url: https://huggingface.co/papers/2610.35013
arxiv_url: https://arxiv.org/abs/2610.35013
date: 2026-10-28
---

# Multiscale Policy Optimization for Long-Horizon LLM Agents

Long-horizon LLM agents interact with their environments through complete assistant turns while generating each action token by token. We observe that critic values vary primarily across turns, motivating optimization anchored at turns with finer credit allocation among tokens. We propose Multiscale Policy Optimization (MPO), combining Multiscale Advantage Estimation (MAE) and turn-level importance sampling to align credit assignment and policy updates at the turn scale. Extensive experiments across search, tool-use, and automation tasks with 4B and 30B-A3B models demonstrate consistent gains over strong RL baselines.
