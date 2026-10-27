---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.800001+00:00
arxiv_id: 2610.23234
url: https://huggingface.co/papers/2610.23234
arxiv_url: https://arxiv.org/abs/2610.23234
date: 2026-10-26
---

# MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation

In a hierarchical multi-agent system, a Leader assigns tasks and subagents carry them out. Jointly training the Leader and the subagents is difficult because a final answer gives only indirect feedback to the subagents. An LLM judge can score the performance of the subagents, but these scores depend on the judge's own assessment of the quality of subagents' responses. We present MultiAgent-OPD, which combines on-policy distillation with reinforcement learning to jointly train a shared-parameter Leader-Searcher-Answerer team end to end. We first train a Teacher in a Searcher-Answerer workflow using answer correctness. During team training, the frozen Teacher scores student-generated search and summary tokens to provide local process supervision for the Searchers, while the Leader learns from team success and the Answerer from candidate correctness. Across seven datasets, the trained system reaches 38.68% macro avg@4, exceeding Prompted Critic by 4.06 percentage points and C-MAS + RL, the trained cascaded multiagent system, by 2.61 percentage points. The team also solves more questions within four attempts.
