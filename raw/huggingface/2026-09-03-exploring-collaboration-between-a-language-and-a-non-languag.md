---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.00474
url: https://huggingface.co/papers/2609.00474
arxiv_url: https://arxiv.org/abs/2609.00474
date: 2026-09-03
---

# Exploring Collaboration between a language and a non-language agent

LLMs are increasingly deployed as orchestrators that coordinate specialized subagents to solve complex tasks through natural language. However, in many important domains like game playing and robotics, the strongest available agents are not language models. Integrating non-language agents with LLMs would require verbalization: compressing their rich continuous representations into sparse textual summaries at each interaction step. To study whether verbalization constitutes a bottleneck, we introduce LLAMIA-Bench, a suite of six diverse collaborative chess tasks spanning three facets: behavioral imitation, state assessment, and natural-language explanation. Each task instantiates a well-established chess problem that neither the LLM nor the chess engine can solve alone. To solve LLM collaboration with non-language agents, we introduce latent state internalization, which projects the subagent's continuous representations directly into the LLM's token stream as learned state tokens, with dynamic re-encoding as actions advance the environment state. Comparing internalization to verbalized integration, our experiments reveal a consistent verbalization debt: the performance gap widens throughout training and persists as the LLM scales from 4B to 14B parameters. A single 14B model, LLAMIA, trained with latent state internalization, matches or exceeds task specialists and frontier models including GPT-5.1 with tool access across all benchmark tasks, and generalizes out-of-distribution where task-specific finetunes collapse
