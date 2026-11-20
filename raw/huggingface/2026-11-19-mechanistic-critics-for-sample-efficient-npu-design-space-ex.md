---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.143340+00:00
arxiv_id: 2611.24733
url: https://huggingface.co/papers/2611.24733
arxiv_url: https://arxiv.org/abs/2611.24733
date: 2026-11-19
---

# Mechanistic Critics for Sample-Efficient NPU Design-Space Exploration

NPU design-space exploration for LLM inference mainly relies on an expensive simulator that often returns only scalar feedback such as latency and power. Such feedback can rank evaluated configurations, but gives little information for deciding why a configuration is slow or which architecture parameter should be changed next. This limitation is especially severe because prefill and decode workloads can be limited by different resources, including compute throughput and HBM bandwidth. We propose CriticNPU, a sample-efficient DSE framework built around an online-calibrated mechanistic critic for NPU architecture design. The critic uses explicit hardware limits to evaluate NPU configurations: before simulation, it estimates whether a proposed configuration is likely to improve over the current best and filters weak candidates; after simulation, it aggregates operator-level runtimes into prefill/decode bottleneck summaries and predicts the effect of candidate parameter changes. We instantiate the critic with a Roofline-style model that derives compute and memory limits from architecture parameters and calibrates per-operator-type effective limits using simulator observations. And CriticNPU combines this critic with a workload extractor and an architecture planner to propose configurations. Across six LLM workloads and 16 deployment configurations per model, CriticNPU achieves best-or-tied-best latency in 74% of prefill and 87.5% of decode settings while using roughly half the simulator calls of competitive DSE baselines. We conduct extensive ablation studies and detailed analyses to validate the effectiveness of our method from multiple perspectives. Our code is available at https://github.com/bruno686/CriticNPU.
