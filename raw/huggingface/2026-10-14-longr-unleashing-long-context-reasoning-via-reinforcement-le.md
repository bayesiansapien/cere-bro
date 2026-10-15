---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.507323+00:00
arxiv_id: 2602.05758
url: https://huggingface.co/papers/2602.05758
arxiv_url: https://arxiv.org/abs/2602.05758
date: 2026-10-14
---

# LongR: Unleashing Long-Context Reasoning via Reinforcement Learning with Dense Utility Rewards

Reinforcement Learning (RL) has emerged as a key driver for LLM reasoning. This capability is equally pivotal in long-context scenarios---such as long-dialogue understanding and structured data analysis---where the challenge extends beyond consuming tokens to performing rigorous deduction. While existing efforts focus on data synthesis or architectural changes, recent work points out that relying solely on sparse, outcome-only rewards yields limited gains, as such coarse signals are often insufficient to effectively guide the complex long-context reasoning. To address this, we propose LongR, a unified framework that enhances long-context performance by integrating a dynamic ``Think-and-Read'' mechanism---which interleaves reasoning with document consultation---with a contextual density reward based on relative information gain to quantify the utility of the relevant documents, without evidence annotations. Empirically, LongR achieves a gain of over 9\% on LongBench v2 and consistent improvements on RULER and InfiniteBench, demonstrating robust efficiency in navigating extensive contexts. Furthermore, LongR consistently enhances performance across diverse RL algorithms (e.g., DAPO, GSPO). Finally, we conduct in-depth analyses to investigate the impact of reasoning chain length on efficiency and the model's robustness against distractors.
