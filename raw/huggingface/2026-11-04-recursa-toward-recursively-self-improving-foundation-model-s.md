---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.362192+05:30
arxiv_id: 2611.04035
url: https://huggingface.co/papers/2611.04035
arxiv_url: https://arxiv.org/abs/2611.04035
date: 2026-11-04
---

# Recursa: Toward Recursively Self-Improving Foundation Model Systems

Foundation models in changing environments can encounter unfamiliar domain knowledge that their original training did not cover. However, new domains rarely provide large amounts of expert-created training data or reliable supervisory signals for further training. We introduce Recursa, a foundation model system that adapts to new domains by learning from its own experience without human experts or a stronger teacher model. Recursa uses a knowledge repository to store what it learns: domain-specific skills and instructions on when to apply them, along with memories of past task experiences and reflections on what to improve. Recursa bootstraps the repository from domain materials and then refines it through recursive self-improvement. It uses parallel learners to execute tasks and synthesize local improvements, then validates and merges the improvements into the knowledge repository. On Harvey LAB's Firm Knowledge benchmark, Recursa raises the all-pass rate on held-out test tasks from 30.0% to 55.0% with DeepSeek-V4.1-Flash and from 35.0% to 46.0% with Qwen3.8-Flash.
