---
source: farmer/huggingface
farmed: 2026-05-23T00:00:00Z
arxiv_id: 2605.13734
url: https://huggingface.co/papers/2605.13734
arxiv_url: https://arxiv.org/abs/2605.13734
date: 2026-05-23
---

# KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving

LLMs are widely adopted in production, pushing inference systems to their limits. Disaggregated LLM serving (e.g., PD separation and KV state disaggregation) improves scalability and cost efficiency, but it also turns KV into an explicit payload crossing network and storage boundaries, making KV a dominant end-to-end bottleneck. Existing KV compression are typically static runtime configurations, despite production service context varies over time in workload mix, bandwidth, and SLO/quality budgets. As a result, a fixed choice can be suboptimal or even increase latency. We present KVServe, the first service-aware and adaptive KV communication compression framework for disaggregated LLM serving: KVServe (1) unifies KV compression into a modular strategy space with new components and cross-method recomposition; (2) introduces Bayesian Profiling Engine that efficiently searches this space and distills a 3D Pareto candidate set, reducing 50times offline search overhead; and (3) deploys a Service-Aware Online Controller that combines an analytical latency model with a lightweight bandit to select profiles under constraints and correct offline-to-online mismatch. Integrated into vLLM and evaluated across datasets, models, GPUs and networks, KVServe achieves up to 9.13times JCT speedup in PD-separated serving and up to 32.8times TTFT reduction in KV-disaggregated serving.
