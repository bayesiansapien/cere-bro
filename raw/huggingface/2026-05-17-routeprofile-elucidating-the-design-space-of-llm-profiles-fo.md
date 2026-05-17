---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.00180"
url: "https://huggingface.co/papers/2605.00180"
arxiv_url: "https://arxiv.org/abs/2605.00180"
date: 2026-05-17
---

# RouteProfile: Elucidating the Design Space of LLM Profiles for Routing

As the large language model (LLM) ecosystem expands, individual models exhibit varying capabilities across queries, benchmarks, and domains, motivating the development of LLM routing. While prior work has largely focused on router mechanism design, LLM profiles, which capture model capabilities, remain underexplored. In this work, we ask: How does LLM profile design affect routing performance across different routers? Addressing this question helps clarify the role of profiles in routing, disentangle profile design from router design, and enable fairer comparison and more principled development of routing systems. To this end, we view LLM profiling as a structured information integration problem over heterogeneous interaction histories. We develop a general design space of LLM profiles, named RouteProfile, along four key dimensions: organizational form, representation type, aggregation depth, and learning configuration. Through systematic evaluation across three representative routers under both standard and new-LLM generalization settings, we show that: (1) structured profiles consistently outperform flat ones; (2) query-level signals are more reliable than coarse domain-level signals; and (3) generalization to newly introduced models benefits most from structured profiles under trainable configurations.
