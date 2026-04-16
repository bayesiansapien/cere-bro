---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2508.06433
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2508.06433
published: 2026-04-16
authors: Runnan Fang, Yuan Liang, Xiaobin Wang
---

# Memp: Exploring Agent Procedural Memory

**arXiv:** https://arxiv.org/abs/2508.06433
**Authors:** Runnan Fang, Yuan Liang, Xiaobin Wang

## Abstract

arXiv:2508.06433v4 Announce Type: replace-cross  Abstract: Large Language Models (LLMs) based agents excel at diverse tasks, yet they suffer from brittle procedural memory that is manually engineered or entangled in static parameters. In this work, we investigate strategies to endow agents with a learnable, updatable, and lifelong procedural memory. We propose Memp that distills past agent trajectories into both fine-grained, step-by-step instructions and higher-level, script-like abstractions, and explore the impact of different strategies for Build, Retrieval, and Update of procedural memory. Coupled with a dynamic regimen that continuously updates, corrects, and deprecates its contents, this repository evolves in lockstep with new experience. Empirical evaluation on TravelPlanner and ALFWorld shows that as the memory repository is refined, agents achieve steadily higher success rates and greater efficiency on analogous tasks. Moreover, procedural memory built from a stronger model retains its value: migrating the procedural memory to a weaker model can also yield substantial performance gains. Code is available at https://github.com/zjunlp/MemP.
