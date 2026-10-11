---
title: "Serving shorts: vLLM on Vera Rubin, AMD's RDMA KV transfer, parallelism map, AirLLM reality check"
date: 2026-10-11
sources:
  - https://x.com/RedHat_AI/status/2108882871234834741
  - https://x.com/PyTorch/status/2108950692975042832
  - https://x.com/_avichawla/status/2108861498252730759
  - https://x.com/oliviscusAI/status/2108875316160860402
  - https://cs2680.seas.harvard.edu
tags: [serving, kv-cache, gpu, parallelism, moe]
---

# Serving shorts (2026-10-11)

**Sources:** X Following feed, US day 2026-10-10. **Raw:** `raw/twitter/feed/2026-10-1[01]-*-ranked.json` (private)

## TL;DR

- **vLLM supports NVIDIA Vera Rubin.** Early results: more than 7.8x the throughput of GB200 on MiniMax M3 for agent workloads. First public Rubin serving number; vendor-early, configuration not given.
- **AMD MoRI + vLLM (PyTorchCon poster).** Two costs dominate cross-pod MoE serving: expert dispatch/combine traffic and moving the KV cache from prefill to decode nodes. AMD brings its MoRI communication stack into vLLM for wide expert parallelism over RDMA and RDMA KV-cache transfer on Instinct GPUs, with stability issues and long-context benchmarks to be shown Oct 20-21.
- **Parallelism map (explainer).** Data, tensor, pipeline, context (prefill-CP splits a long input for lower TTFT; decode-CP splits stored KV history for capacity but merges partial attention every layer), expert and hybrid. GPUs never share one memory pool, so every strategy trades local limits for interconnect traffic.
- **AirLLM reality check.** The viral "70B on a 4 GB GPU" is layer-by-layer loading from disk: it fits, but each token re-reads all weights from storage, so throughput is seconds per token. A memory trick, not a serving method.
- **Harvard CS2680** (public): one agent followed from the loop down through batching, KV/prefix reuse, routing, quantization and speculative decoding.

## Relation to prior wiki pages

- **Confirms** [KV cache](kv-cache.md): the 10-09 Dynamo session-ID and 10-10 SparseEngine results put cache movement, not compute, at the centre of agent serving; AMD's poster is the same problem at the network layer (disaggregated prefill/decode).
- **Extends** [memory hierarchy](../hardware/memory-hierarchy.md): Rubin's gain on an agent workload is mostly memory and interconnect, consistent with the 10-07 Rubin coverage.
