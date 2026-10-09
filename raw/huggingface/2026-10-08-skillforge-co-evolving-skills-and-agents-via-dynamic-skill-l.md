---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.309677+05:30
arxiv_id: 2610.09832
url: https://huggingface.co/papers/2610.09832
arxiv_url: https://arxiv.org/abs/2610.09832
date: 2026-10-08
---

# SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles

Memory-augmented reinforcement learning strengthens LLM agents' ability to solve complex long-horizon tasks. Skills are one such form of memory, pairing instructions with an applicability condition over task types. However, retaining every skill indiscriminately as the policy improves lets obsolete or harmful entries accumulate and mislead the agent. We propose SkillForge, an agentic RL method that compiles and evolves the skill library through a fitness-driven skill lifecycle of trial, active, stable, and retired states, so that the skills and the model co-evolve throughout training. A pre-RL evaluation phase first uses the base model's own rollouts to pre-retire low-fitness skills, yielding a filtered library that then seeds supervised fine-tuning. Reinforcement learning takes over from this checkpoint, and at each iteration selective retirement, stabilization, and LLM-guided mutation continue to forge the skill library alongside policy optimization. Across multiple interactive agent benchmarks, SkillForge achieves the highest aggregate success rate, delivering up to 7.8% relative improvement over the strongest baseline while keeping the skill library compact throughout training. We introduce SkillFurnace, a dataset of 5k+ annotated records bundling retirement-filtered SFT trajectories, evolved skill libraries with fitness annotations, and retirement events with human-annotated failure categories to support research on skill quality and lifecycle management.
