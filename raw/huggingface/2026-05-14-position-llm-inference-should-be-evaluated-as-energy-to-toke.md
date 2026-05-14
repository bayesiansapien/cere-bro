---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.11733
url: https://huggingface.co/papers/2605.11733
arxiv_url: https://arxiv.org/abs/2605.11733
date: 2026-05-14
---

# Position: LLM Inference Should Be Evaluated as Energy-to-Token Production

LLM inference is still evaluated mainly as a model or software problem: accuracy, latency, throughput, and hardware utilization. This is incomplete. At deployment scale, the relevant output is a quality-conditioned token produced under joint constraints from effective compute, delivered data-center power, cooling capacity, PUE, and utilization. We argue that the ML community should treat inference as energy-to-token production. We formalize this view with a dimensionally consistent Token Production Function in which token rate is bounded by both compute-per-token and energy-per-token ceilings. Listed API prices vary by over an order of magnitude across providers, but we use price dispersion only as directional motivation, not as causal evidence of marginal cost. The core physical question is instead: under fixed quality and service targets, when does the binding constraint move from theoretical peak compute toward delivered power, cooling, and operational efficiency?
