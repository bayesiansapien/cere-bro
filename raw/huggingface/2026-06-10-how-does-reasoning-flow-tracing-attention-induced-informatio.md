---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.10646
url: https://huggingface.co/papers/2606.10646
arxiv_url: https://arxiv.org/abs/2606.10646
date: 2026-06-10
---

# How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted RL in LLMs

Token-level credit assignment remains a key obstacle for reinforcement learning (RL) in large language models (LLMs), where RL recipes typically treat all tokens equally, failing to distinguish decisive reasoning steps from routine formatting or fluent filler. Recent attempts leverage model-internal signals to assign finer-grained credit, but these are often point-wise heuristics that ignore the global structure of information propagation. We propose FlowTracer, an RL framework that traces answer-targeted reasoning flow on an attention-induced directed acyclic graph in which nodes correspond to tokens and edge capacities come from aggregated attention weights and derives token credit from this global structure. The edge capacities are reweighted to retain only the influence that can reach the answer region, while enforcing local flow conservation so intermediate tokens neither lose nor gain effective mass due to path length or irrelevant branches. On this graph, FlowTracer extracts an information-flow backbone connecting the question to the answer and scores tokens by flow throughput, revealing high-impact hubs and aggregation checkpoints that mediate long-range dependencies. These derived importances are used to shape token-level rewards, enabling learning signals to focus precisely on the tokens that route information toward (or away from) correct answers and delivering consistent performance gains across a range of reasoning tasks.
