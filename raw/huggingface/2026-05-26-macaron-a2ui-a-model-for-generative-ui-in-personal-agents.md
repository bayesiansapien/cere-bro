---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.24830
url: https://huggingface.co/papers/2605.24830
arxiv_url: https://arxiv.org/abs/2605.24830
date: 2026-05-26
---

# Macaron-A2UI: A Model for Generative UI in Personal Agents

As personal agents evolve to handle complex, user-centric tasks, static plain-text chat is rapidly becoming a bottleneck. Generative UI emerges as the necessary new interface layer, dynamically synthesizing the right controls, options, and state from the interaction context in real time. We present Macaron-A2UI, a model for Generative UI in personal agents. Our goal is to move beyond text-only interaction by enabling agents to generate natural language together with lightweight, executable UI actions for information collection, preference refinement, confirmation, and multi-goal organization. We build a large-scale Generative UI corpus from heterogeneous dialogue sources, introduce A2UI-Bench for controlled evaluation, and train 30B, 235B and 754B models with parameter-efficient LoRA-based supervised fine-tuning followed by reward-driven reinforcement learning. The best Macaron-A2UI model reaches 75.6 overall on A2UI-Bench without explicit schema hints, surpassing the strongest full-schema frontier baseline. We release the models, benchmark, and evaluation protocol to support future work on Generative UI for personal agents.
