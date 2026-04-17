---
source: farmer/huggingface
farmed: 2026-04-17T07:40:59Z
arxiv_id: 2604.14531
url: https://huggingface.co/papers/2604.14531
arxiv_url: https://arxiv.org/abs/2604.14531
date: 2026-04-17
---

# TRACER: Trace-Based Adaptive Cost-Efficient Routing for LLM Classification

Every call to an LLM classification endpoint produces a labeled input-output pair already retained in production logs. These pairs constitute a free, growing training set: a lightweight surrogate trained on them can absorb a significant portion of future traffic at near-zero marginal inference cost. We introduce Tracer (Trace-based Adaptive Cost-Efficient Routing), an open-source system that trains ML surrogates on an LLM's own production traces and governs deployment through a parity gate: the surrogate is activated only when its agreement with the LLM exceeds a user-specified threshold. To make the routing boundary transparent, Tracer generates interpretability artifacts describing which input regions the surrogate handles, where it plateaus, and why it defers. On a 77-class intent benchmark with a Sonnet 4.6 teacher, Tracer achieves 83-100% surrogate coverage depending on the quality target; on a 150-class benchmark, the surrogate fully replaces the teacher. On a natural language inference task, the parity gate correctly refuses deployment because the embedding representation cannot support reliable separation.
