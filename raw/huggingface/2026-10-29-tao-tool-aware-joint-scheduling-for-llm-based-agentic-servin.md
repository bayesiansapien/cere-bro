---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.924008+05:30
arxiv_id: 2610.37230
url: https://huggingface.co/papers/2610.37230
arxiv_url: https://arxiv.org/abs/2610.37230
date: 2026-10-29
---

# TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving

Agentic services alternate between model inference on clustered GPUs and external tools on distributed CPUs. In this scenario, existing systems (1) overlook tool-return readiness in service evaluation, wasting limited resources, and (2) use heuristic strategies to decide admission and placement on GPUs, resulting in suboptimal scheduling decisions. To bridge this gap, we present TAO, a tool-aware joint scheduling framework for LLM-based agentic serving. Its value interface combines near-term tool readiness, node-specific cache credit with time-aware decay, and token footprint; a dynamic program jointly selects and places waiting sessions under capacity constraints. Across the 12 reported model-workload-concurrency settings, TAO reduces latency by up to 26.8%, reduces mean time to first token (TTFT) by up to 36.3%, and increases decode throughput by up to 29.5% relative to the best evaluated state-of-the-art baseline for each metric.
