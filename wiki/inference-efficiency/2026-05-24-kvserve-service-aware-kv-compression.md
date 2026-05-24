# KVServe: Service-Aware KV Cache Compression for Disaggregated LLM Serving

**Source:** HuggingFace daily papers, [arXiv 2605.13734](https://arxiv.org/abs/2605.13734). Institute of Computing Technology / Chinese Academy of Sciences, Shanghai Jiao Tong University.
**Date:** 2026-05-24
**Tier:** 1 (KV cache, inference efficiency)

## TL;DR

KVServe is the first service-aware KV cache compression framework for disaggregated LLM serving. Disaggregated architectures (prefill-decode separation, KV-state disaggregation) push the KV cache from an internal GPU state into an explicit network payload, where a 70B model can produce 39 GB of KV cache at 128K context. KVServe replaces static compression configurations with a three-piece adaptive system: a modular strategy space unifying quantization, lossless coding, and data transformations; a Bayesian Profiling Engine that distills a 3D Pareto candidate set with 50x less offline search; and an online controller combining an analytical latency model with a contextual bandit to pick a profile under runtime SLO and bandwidth constraints. Integrated into vLLM, the system delivers up to 9.13x JCT speedup in PD-separated serving and 32.8x TTFT reduction in KV-disaggregated serving.

## Key findings

- KV cache communication, not compute, is now the dominant bottleneck in disaggregated serving. The bottleneck moved when the cache crossed the bus.
- A static compression choice is often actively harmful when workload mix, bandwidth, or SLO changes mid-shift. Fixed configurations can *increase* latency.
- The compression strategy space is much larger than any single method explores. By unifying quantization (4-bit, 2-bit, mixed-precision), lossless coding, and data transformations (Hadamard, Affine) into one modular space and allowing cross-method recomposition, KVServe finds Pareto points that no single technique reached.
- Online correction matters. The bandit-on-top-of-analytical-model controller closes the offline-to-online mismatch that profile-only systems suffer from.

## Why this matters

This paper sits exactly at the intersection of the wiki's two Tier 1 spotlights: KV cache and AI routing. KVServe is a routing system for cache compression. The 9.13x JCT and 32.8x TTFT numbers are not algorithmic wins, they are scheduling wins on top of existing compression primitives. The same pattern showed up in PrfaaS (2026-04-22, prefill-as-a-service across datacenters with hybrid-attention KV cache transport) where KV transport became the design constraint. KVServe formalizes the runtime-controller layer that PrfaaS-style systems were doing by hand.

It is also the first paper the wiki has tracked that treats compression configuration as a first-class control surface rather than a static hyperparameter. That reframe applies broadly: every place an inference system has a knob that gets tuned once and frozen (quantization bit-width, KV eviction threshold, speculative-decoding lookahead) is a candidate for the same online-controller treatment.

## Research angle

The Bayesian Profiling Engine's 3D Pareto framing (compression ratio vs quality vs encode/decode overhead) is a generalizable primitive. Any system that has a multi-objective hyperparameter search that gets run offline and then frozen at deployment can in principle benefit. The open question is how badly the analytical latency model degrades when network conditions are non-stationary on time scales faster than the bandit can adapt. Cross-datacenter KV transport with TCP-incast or hot-cell GPU thermal throttling are the obvious adversarial cases.

## Related

- [KV Cache](kv-cache.md) — concept page, now extended to include service-aware adaptive compression.
- [PrfaaS / Prefill-as-a-Service (2026-04-22)](../inference-efficiency/2026-04-22-prfaas-cross-datacenter-prefill.md) — the prior paper on KV transport as the disaggregated-serving bottleneck.
- [TurboQuant (2026-04-22)](kv-cache.md#key-papers) — one of the compression primitives KVServe schedules over.

## Raw source

[`raw/huggingface/2026-05-24-kvserve-service-aware-kv-cache-compression-for-communication.md`](../../raw/huggingface/2026-05-24-kvserve-service-aware-kv-cache-compression-for-communication.md)
