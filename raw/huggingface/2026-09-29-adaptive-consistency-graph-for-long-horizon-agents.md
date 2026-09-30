---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935923+00:00
arxiv_id: 2609.32754
url: https://huggingface.co/papers/2609.32754
arxiv_url: https://arxiv.org/abs/2609.32754
date: 2026-09-29
---

# Adaptive Consistency Graph for Long-Horizon Agents

Large language model agents can often make reasonable local decisions on short tasks, yet their performance degrades when success requires long sequences of dependent actions and tool calls. During execution, task requirements, historical evidence, and the current execution state may gradually become disconnected, so later decisions can drift from the original objective. We study this problem by introducing the Adaptive Consistency Graph (ACG) for long-horizon execution. ACG incrementally organizes execution evidence and its provenance in a persistent graph, then constructs a temporary requirement-centered view for each decision under a bounded context budget. Rather than replacing the base agent's planner or tool executor, ACG provides a structured and traceable context view for each decision. In the matched evaluation, ACG improves GPT-5.6-luna's average success from 44.5\% with ReAct to 50.2\%, with the largest gain on BrowseComp-Plus (73.5\% versus 62.4\%). We further analyze trajectory structure and inference cost to characterize this improvement.
