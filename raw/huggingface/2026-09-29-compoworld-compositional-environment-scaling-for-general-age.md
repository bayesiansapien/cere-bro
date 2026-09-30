---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.929266+00:00
arxiv_id: 2609.33665
url: https://huggingface.co/papers/2609.33665
arxiv_url: https://arxiv.org/abs/2609.33665
date: 2026-09-29
---

# CompoWorld: Compositional Environment Scaling for General Agents

Automatically generated environments provide a scalable source of interaction data for training general agents. However, existing approaches mainly generate tasks within a single environment, while real-world workflows require agents to connect information and actions across multiple services. We introduce Compositional Environment Scaling (CompoWorld), which expands the task space by composing a finite library of reusable services. Coding agents turn tool specifications into verified services with typed states and shared interfaces, while a world model handles tools that cannot be reliably implemented. A random-walk procedure connects services through dependency graphs, enabling the generation and verification of tasks that require information to flow across services. Verified trajectories support supervised fine-tuning (SFT), while our Completion-Focused Rubric Reward guides reinforcement learning (RL) toward full task completion by emphasizing criteria with lower pass rates within each rollout group. We construct 448 services exposing 10,130 tools and use 3K SFT trajectories and 1K RL tasks to train Qwen3.6-35B-A3B. Experimental results show that CompoWorld improves on its backbone by 9.17 points on average across eight benchmarks. On AutomationBench, it surpasses frontier models such as Claude Opus 4.6 and leads all compared agent-specialized 35B-A3B models.
