---
title: "RidgeFill: skip most upper layers during prefill and fill their cache from a ridge regression"
date: 2026-11-11
source: https://arxiv.org/abs/2611.09709
raw: ../../raw/huggingface/2026-11-10-ridgefill-training-free-late-layer-cache-fill-for-faster-pre.md
tags: [kv-cache, prefill, ttft, layer-skipping, training-free]
signal: HuggingFace Daily Papers 11-10
---

# RidgeFill: training-free late-layer cache fill for faster prefill

## TL;DR

Prefill (the pass that reads the whole prompt and writes the KV cache before the first output token) is compute-bound and sets time to first token (TTFT). RidgeFill runs the lower layers exactly up to a split layer. From that layer's hidden state, a per-layer linear map predicts what every later layer's input would have been. Each late layer then writes its keys and values from that prediction using its own unchanged projections. The map is a ridge regression fit once, in closed form, from one pass over calibration text. The last few thousand prompt tokens and every decode step still run the full model. Nothing is trained and no token is dropped. This retrofits the YOCO and DeepSeek-V4.1-Flash idea (a trained cross-layer projection that lets upper layers skip prefill) onto models never trained for it.

<div class="dg-title">The upper layers never see most of the prompt</div>
<div class="dg-sub">A closed-form map stands in for the skipped layers, but only for cache writing. Decode is exact.</div>

```mermaid
flowchart LR
  P["Prompt<br/><small>16K to 120K tokens</small>"] --> L["Lower layers<br/><small>run exactly to split</small>"]
  L --> M["Ridge map<br/><small>fit once, closed form</small>"]
  M --> K["Late-layer KV<br/><small>written from prediction</small>"]
  P -->|last few K tokens| F["Full model<br/><small>exact tail and decode</small>"]
  K --> F
  F --> O["First token<br/><small>1.25 to 1.6x sooner</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class P input
  class L,F core
  class M loop
  class K,O exit
```

<div class="dg-legend">Blue is the prompt, purple runs the real model, amber is the fitted stand-in, green is the cache and the faster first token.</div>

## Key findings

- **Qwen3.8-27B in a llama.cpp fork on an A100:** TTFT 1.25 to 1.31x faster at 16K to 120K tokens with the maps in VRAM. RULER moves -1.2 and -1.4 points, LongBench v2 -1.4. The 95% intervals include zero but do not rule out losses of a few points.
- **Qwen3.8-Flash-Next in vLLM:** 1.50 to 1.60x faster than exact at 9K to 32K tokens. RULER needle tasks 99.8 vs 100.0. Perplexity on novel tokens +2.65% [-0.02%, +4.93%].
- **Against an identity fill** (copy the split layer's state upward) on three 8-9B models, the fitted map recovers 49.1 and 49.6 more filled-region RULER points on the two dense models. Its long-document loss is within ±0.03 nats of the released SwiftKV checkpoint, which was trained for this.
- **Measurement is the main contribution.** Average loss over all tokens hides the error. Needle retrieval inside the filled region, loss on tokens that depend on distant context, and splice tests (swap filled keys or values for exact ones) locate it: in the keys on Llama-3.1-8B (half of it in their scale), and in the values and recurrent state on Qwen3.5-9B.

## Relation to prior wiki

- **Extends the prefill line.** The 11-07 [PACT](2026-11-07-pact-prefill-to-autoregressive-transfer.md) paper (big model reads, small model writes) moved prefill to a different model. RidgeFill keeps one model and removes most of the upper-layer prefill compute. Both bet that prefill is over-provisioned relative to what decode needs.
- **Complements LowRAM (11-10)** ([summary](2026-11-10-lowram-kv-value-amortisation.md)), which predicts values from keys to shrink KV memory. RidgeFill predicts layer inputs from a lower layer to shrink prefill compute. Same family of idea: much of the cache is a predictable function of other parts of the model.
- **Confirms the [KV cache concept page](kv-cache.md) warning** that headline perplexity hides long-range damage. The splice-test methodology is the reusable artifact.

## Gaps

Confidence intervals still admit losses of a few points. No test above 120K tokens. Speedups are TTFT only; throughput under batching is not reported. The calibration text choice is not ablated across domains.

## Links

- Paper: [arXiv 2611.09709](https://arxiv.org/abs/2611.09709)
- Concept: [KV cache](kv-cache.md)
