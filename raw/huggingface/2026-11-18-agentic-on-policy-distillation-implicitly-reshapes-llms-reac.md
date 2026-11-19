---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.19244
url: https://huggingface.co/papers/2611.19244
arxiv_url: https://arxiv.org/abs/2611.19244
date: 2026-11-18
---

# Agentic On-Policy Distillation Implicitly Reshapes LLMs' ReAct Patterns

On-policy distillation (OPD) transfers specialized capabilities to language-model agents, but its cross-domain effects on interaction remain unclear. We investigate how OPD reshapes ReAct interaction patterns across mathematics, ALFWorld, and τ^2-bench, focusing on reasoning, actions, and observation acquisition. General-reasoning supervision reduces mathematical tool attempts from 70.4% to 14.4% while increasing accuracy from 16.7% to 38.0%; code-interpreter supervision improves household actions and retail queries. In contrast, ALFWorld supervision reduces τ^2-bench accuracy from 41.5% to 6.6%, accompanied by frequent tool calls that violate user-information dependencies. To address negative transfer using only source-domain training trajectories, we explore selective OPD guided by teacher preference changes before and after domain-specific RL. Retaining the top 95% of positions raises τ^2 accuracy from 11.5% to 29.9% with a source-learning trade-off.
