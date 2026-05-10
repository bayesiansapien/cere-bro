---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.05566
url: https://huggingface.co/papers/2605.05566
arxiv_url: https://arxiv.org/abs/2605.05566
date: 2026-05-10
---

# Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration

Reinforcement learning with verifiable rewards, particularly Group Relative Policy Optimization (GRPO), has significantly advanced the reasoning capabilities of Large Language Models (LLMs). However, in complex tasks, GRPO frequently suffers from the 'zero-advantage problem': when all sampled rollouts for a query fail, the relative advantage collapses to zero. We propose Lorem Perturbation for Exploration (LoPE), a simple yet effective training framework to break this exploration bottleneck. We posit that task-irrelevant prompt-space perturbations can shift the model's output distribution enough to unlock orthogonal reasoning pathways for hard questions. Specifically, LoPE prepends sequences stochastically assembled from Lorem Ipsum vocabulary to the prompts before resampling.
