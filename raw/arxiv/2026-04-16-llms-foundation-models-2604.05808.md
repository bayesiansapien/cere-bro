---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.05808
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.05808
published: 2026-04-16
authors: Shuai Zhen, Yanhua Yu, Ruopei Guo
---

# Hierarchical Reinforcement Learning with Augmented Step-Level Transitions for LLM Agents

**arXiv:** https://arxiv.org/abs/2604.05808
**Authors:** Shuai Zhen, Yanhua Yu, Ruopei Guo

## Abstract

arXiv:2604.05808v2 Announce Type: replace  Abstract: Large language model (LLM) agents have demonstrated strong capabilities in complex interactive decision-making tasks. However, existing LLM agents typically rely on increasingly long interaction histories, resulting in high computational cost and limited scalability. In this paper, we propose STEP-HRL, a hierarchical reinforcement learning (HRL) framework that enables step-level learning by conditioning only on single-step transitions rather than full interaction histories. STEP-HRL structures tasks hierarchically, using completed subtasks to represent global progress of overall task. By introducing a local progress module, it also iteratively and selectively summarizes interaction history within each subtask to produce a compact summary of local progress. Together, these components yield augmented step-level transitions for both high-level and low-level policies. Experimental results on ScienceWorld and ALFWorld benchmarks consistently demonstrate that STEP-HRL substantially outperforms baselines in terms of performance and generalization while reducing token usage. Our code is available at https://github.com/TonyStark042/STEP-HRL.
