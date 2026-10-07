---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04137
url: https://huggingface.co/papers/2610.04137
arxiv_url: https://arxiv.org/abs/2610.04137
date: 2026-10-06
---

# Dynamic Harness Search: Building Multi-Agent Systems Per-Query via Prediction

Agent harnesses specify the roles, instructions, tools, and communication structure used to solve a task, and the right harness depends on the query. Because the value of each design choice is observable only through execution, tailoring a harness to each query has required either executing alternatives at inference time or costly manual design. We introduce SHIFT, which moves execution out of the per-query search loop. A local LLM architect learns a policy over harness-building actions from search, and a value function that predicts, from measured executions, a utility balancing accuracy against execution cost. For each query, Monte Carlo tree search uses these predictions to construct a harness. Across 9,193 tasks in six benchmarks, from math to document and general-assistant tasks, with a Gemini 3.5 Flash executor, SHIFT attains the highest mean accuracy, about 80%, outperforming 17 baselines that span prompting, prompt optimization, and workflow search, and exceeding the strongest baseline by 7.2 percentage points. A cheaper mode of SHIFT also attains a higher mean accuracy than every baseline while using 32% fewer execution tokens than the strongest baseline. We further show that choosing structure, instructions, and tools jointly beats choosing only instructions or only tools by up to 9.1 percentage points, and that learned value selection identifies more accurate harnesses with lower execution cost from candidate pools.
