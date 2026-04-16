---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13552
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13552
published: 2026-04-16
authors: Kaiwen Zheng, Kai Zhou, Jinwu Hu
---

# Training-Free Test-Time Contrastive Learning for Large Language Models

**arXiv:** https://arxiv.org/abs/2604.13552
**Authors:** Kaiwen Zheng, Kai Zhou, Jinwu Hu

## Abstract

arXiv:2604.13552v1 Announce Type: cross  Abstract: Large language models (LLMs) demonstrate strong reasoning capabilities, but their performance often degrades under distribution shift. Existing test-time adaptation (TTA) methods rely on gradient-based updates that require white-box access and need substantial overhead, while training-free alternatives are either static or depend on external guidance. In this paper, we propose Training-Free Test-Time Contrastive Learning TF-TTCL, a training-free adaptation framework that enables a frozen LLM to improve online by distilling supervision from its own inference experiences. Specifically, TF-TTCL implements a dynamic "Explore-Reflect-Steer" loop through three core modules: 1) Semantic Query Augmentation first diversifies problem views via multi-agent role-playing to generate different reasoning trajectories; 2) Contrastive Experience Distillation then captures the semantic gap between superior and inferior trajectories, distilling them into explicit textual rules; and 3) Contextual Rule Retrieval finally activates these stored rules during inference to dynamically steer the frozen LLM toward robust reasoning patterns while avoiding observed errors. Extensive experiments on closed-ended reasoning tasks and open-ended evaluation tasks demonstrate that TF-TTCL consistently outperforms strong zero-shot baselines and representative TTA methods under online evaluation. Code is available at https://github.com/KevinSCUTer/TF-TTCL.
