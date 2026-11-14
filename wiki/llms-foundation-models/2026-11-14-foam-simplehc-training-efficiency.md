---
title: "Cheaper training plumbing: FOAM (SOAP at near-AdamW cost) and SimpleHC (hyper-connections at 2.4% overhead)"
date: 2026-11-14
source: https://arxiv.org/abs/2611.16905
raw: ../../raw/huggingface/2026-11-13-factored-one-sided-adam-moment-for-practical-and-scalable-so.md
tags: [optimizers, soap, shampoo, muon, hyper-connections, residual-stream, training-efficiency, memory]
signal: HuggingFace 11-13 (FOAM 12 upvotes, Hyper-Connections 26 upvotes)
---

# FOAM and SimpleHC: cheaper training plumbing

## TL;DR

- **FOAM (2611.16905).** Second-order optimizers like Shampoo and SOAP converge faster per step than AdamW but cost optimizer-state memory and eigendecompositions. FOAM keeps SOAP's benefit at near-AdamW cost with two changes. (1) **One-sided preconditioning:** drop the output-side Kronecker factor, which removes memory and one eigendecomposition; the Kronecker structure of the Hessian makes this exact when output curvature is diagonal and nearly lossless when near-diagonal. (2) **Factored second moment:** replace SOAP's dense rotated second moment with a row-by-column Adam-moment estimate, exact under K-FAC with diagonal output curvature; measured K-FAC violation is only 15-20%. FOAM matches strong SOAP and Muon baselines in validation loss.
- **SimpleHC (2611.05984).** Hyper-Connections (an expanded, multi-stream residual stream now used in frontier LMs, mHC being the popular variant) add training overhead. Two interaction groups each match mHC alone: learned read/write gating without mixing, or unconstrained mixing with fixed gates. The real overhead is **repeated access to the expanded residual state**. SimpleHC drops residual mixing and shares memory access (batched reads, deferred writes, shared gate inputs), costing **2.4% extra end-to-end training time** over a plain residual at the largest tested scale while staying comparable to mHC.

<div class="dg-title">Keep the benefit, delete the expensive half</div>
<div class="dg-sub">Both papers find one component carries the gain and another carries the cost.</div>

```mermaid
flowchart LR
  S["SOAP<br/><small>two-sided preconditioner</small>"] --> F["FOAM<br/><small>input side only</small>"]
  F --> M["Factored moment<br/><small>row x column stats</small>"]
  M --> O["Near-AdamW cost<br/><small>SOAP-level loss</small>"]
  H["mHC<br/><small>mixed residual streams</small>"] --> G["Gating only<br/><small>no mixing</small>"]
  G --> A["Shared access<br/><small>batched reads</small>"]
  A --> P["+2.4% train time<br/><small>mHC-level quality</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class S,H input
  class F,M,G,A loop
  class O,P exit
```

<div class="dg-legend">Blue is the prior method, amber is the simplification, green is the result.</div>

## Relation to prior wiki pages

- Both are memory-traffic results more than math results: FOAM removes optimizer state, SimpleHC removes residual-state reads. That is the same bottleneck shape as Inkling's 4-bit training (same day), where the speedup was capped by bytes over NVLink rather than FLOPs.
- Other 11-13 HF efficiency items, for the record: **G-STAR** (2611.13004) scales token-group size quadratically with spatial compression to reach 32-64x compressed autoregressive image generation, 20x faster at 1024x1024. **Unbundling Multimodal Vision Encoding** (2611.17334, 200+ models trained from scratch) finds a pretrained visual prior unnecessary; dedicated vision capacity is what matters, and it can sit in-fusion in early backbone layers, which can lower time to first token.
