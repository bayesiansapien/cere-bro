---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05162
url: https://huggingface.co/papers/2610.05162
arxiv_url: https://arxiv.org/abs/2610.05162
date: 2026-10-06
---

# Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy

Long-term memory enables LLM-based agents to retain and reuse information across tasks and sessions, supporting personalization and long-horizon interactions. However, persistent memories can also induce sycophancy, causing agents to over-align with users' historical beliefs even when they are inaccurate, outdated, or inconsistent with objective evidence. Existing mitigation methods assume that memory-induced sycophancy originates from biased or incorrect memories and attempt to reduce this risk by filtering such memories at different stages of the memory pipeline. However, in the real world, objective and correct memories can still induce sycophancy, and the same memory can warrant different influence across different contexts. To this end, we propose MemAdapter, a novel framework that adaptively integrates retrieved memories to support objective and reliable reasoning. Specifically, MemAdapter consists of three components: (i) Counterfactual Induction, which leverages counterfactual reasoning to uncover the potential risk of retrieved memories; (ii) Context-Aware Reflection, which calibrates the inferential influence of each retrieved memory in light of the current task via self-reflection; and (iii) Evidence-Based Reasoning, which grounds the final response in appropriate evidence while preserving the legitimate influence of memory. Extensive experiments on three benchmarks demonstrate that MemAdapter consistently improves memory reliability across diverse scenarios. Our code is available at https://github.com/DEEP-JLU/MemAdapter.
