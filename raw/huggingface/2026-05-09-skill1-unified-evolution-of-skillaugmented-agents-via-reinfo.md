---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06130
url: https://huggingface.co/papers/2605.06130
arxiv_url: https://arxiv.org/abs/2605.06130
date: 2026-05-09
---

# Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning

A persistent skill library allows language model agents to reuse successful strategies across tasks. Maintaining such a library requires three coupled capabilities. The agent selects a relevant skill, utilizes it during execution, and distills new skills from experience. Existing methods optimize these capabilities in isolation or with separate reward sources, resulting in partial and conflicting evolution. We propose Skill1, a framework that trains a single policy to co-evolve skill selection, utilization, and distillation toward a shared task-outcome objective. The policy generates a query to search the skill library, re-ranks candidates to select one, solves the task conditioned on it, and distills a new skill from the trajectory. All learning derives from a single task-outcome signal. Its low-frequency trend credits selection and its high-frequency variation credits distillation. Experiments on ALFWorld and WebShop show that Skill1 outperforms prior skill-based and reinforcement learning baselines.
