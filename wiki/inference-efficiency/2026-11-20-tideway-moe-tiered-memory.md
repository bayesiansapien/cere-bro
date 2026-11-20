# Tideway: Phase-Aware Tiered Memory for MoE Inference on Consumer Devices (2611.14848)

**TL;DR.** Large MoE models (mixture-of-experts, where each token uses only a few expert sub-networks) do not fit in a consumer PC's GPU memory, so their weights spill across VRAM, host RAM and SSD. Existing offload systems treat each tier as a separate cache and thrash. Tideway manages host RAM and VRAM as one memory pool. It uses different memory layouts for prefill (many tokens at once, broad expert access) and decode (one token at a time, sparse expert access), and its execution engine keeps CUDA Graphs (pre-recorded GPU launch sequences that cut CPU launch overhead) working even while experts are paged in and out. On consumer hardware with frontier MoE models it averages 1.97x faster end-to-end latency, 2.40x faster time-to-first-token and 1.61x higher decode throughput than the fastest baseline. Code is open.

<div class="dg-title">One pool, two layouts</div>
<div class="dg-sub">Prefill and decode touch experts differently, so they get different placements.</div>

```mermaid
flowchart LR
  W["MoE weights<br/><small>larger than VRAM</small>"] --> P["Unified pool<br/><small>VRAM plus host RAM</small>"]
  S["SSD<br/><small>cold experts</small>"] --> P
  P --> F{"Phase<br/><small>prefill or decode</small>"}
  F -->|prefill| L1["Dense layout<br/><small>broad expert streaming</small>"]
  F -->|decode| L2["Sparse layout<br/><small>hot experts resident</small>"]
  L1 --> G["CUDA Graph engine<br/><small>works under paging</small>"]
  L2 --> G
  G --> O["Tokens<br/><small>1.97x faster end to end</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class W,S input
  class P,G core
  class F,L1,L2 loop
  class O exit
```

<div class="dg-legend">Blue is storage, purple is the pool and engine, amber is the phase-aware placement, green is the result.</div>

## Relation to prior wiki pages
- **Same move, smaller box:** the [memory hierarchy page](../hardware/memory-hierarchy.md) tracks datacenter versions (DeepSeek serving KV from SSD, TPU Sync spilling KV to host DRAM). Tideway brings tier-aware placement to a single PC.
- **Practitioner echo:** consumer-MoE offload has been the main LocalLLaMA theme for months (DeepSeek-V4.1-Flash at 1-bit on desktop rigs, 11-04). Tideway is the first systems paper to treat prefill and decode as separate placement problems on that hardware.
- Pairs with [batch-aware MoE routing (11-15)](2026-11-15-batch-aware-moe-routing-energy.md): both exploit the fact that which experts are hot is predictable per phase.

## Gaps
- Abstract does not name the models or hardware; SSD-heavy configurations are not broken out.

## Sources
- [Paper](https://arxiv.org/abs/2611.14848) · [Code](https://github.com/Afterglow231/Tideway) · raw: `raw/huggingface/2026-11-19-tideway-phase-aware-tiered-memory-management-for-moe-inferen.md`

Concept pages: [memory hierarchy](../hardware/memory-hierarchy.md) · [KV cache](kv-cache.md)
