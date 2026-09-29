---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.596841+00:00
arxiv_id: 2609.31590
url: https://huggingface.co/papers/2609.31590
arxiv_url: https://arxiv.org/abs/2609.31590
date: 2026-09-28
---

# AgentWorld: Benchmarking Long-Horizon Collaboration of Multi-agent LLMs

Existing multi-agent benchmarks primarily test in competitive settings, short-horizon interactions under 20 steps, or simply aggregate individual performance, failing to isolate and highlight genuine collaboration capabilities of LLM-based agents. We introduce AgentWorld, a benchmark of 100 human-annotated tasks (with 100 augmented variants) for evaluating long-horizon, multi-agent collaboration. Tasks span 50+ interaction rounds across a rich MMORPG sandbox and require 3-20 agents with asymmetric roles and abilities to coordinate through communication, joint planning, and resource sharing under a blackbox setting where each agent acts independently without access to others' internal states. To quantify collaboration effectiveness in addition to conventional binary task success, we propose Causal Collaboration Effectiveness (CCE), a graph-based metric that traces causal dependencies between agent actions and measures what fraction of a team's effort actually contributed to the outcome. Experiments with Gemini 3 Flash, Claude Haiku 4.5, GPT-5 Mini, and DeepSeek R1-70B show that even the best model achieves only 52.0% task success, with systematic failure modes including communication breakdowns, role confusion, and inability to maintain shared plans across rounds. AgentWorld is fully open-source.
