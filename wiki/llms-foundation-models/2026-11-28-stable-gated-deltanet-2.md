---
title: "Stable Gated DeltaNet-2: why GDN-2 blows up on long context, and a symmetric fix"
date: 2026-11-28
arxiv: 2611.34051
url: https://arxiv.org/abs/2611.34051
tags: [linear-attention, recurrent-state, deltanet, long-context, hybrid-models]
raw: ../../raw/huggingface/2026-11-27-stable-gated-deltanet-2-understanding-and-mitigating-recurre.md
---

# Stable Gated DeltaNet-2

**TL;DR.** Linear-attention models keep a fixed-size recurrent state instead of a growing KV cache. Gated DeltaNet-2 (GDN-2) gave each channel separate control over erasing and writing, which improved in-context retrieval but made long-context training fail. The paper traces the failure to an asymmetry: the direction the model reads from when erasing differs from the direction it modifies. That makes the erase operator non-normal, so small directional gains compound across tokens and the state grows exponentially even with no new writes. The fix uses symmetric erasure (provably non-expansive) plus decay-regulated residual writing to keep write flexibility. It proves an O(T) bound on state growth, keeps chunkwise parallel training, and at about 1.6B parameters lifts 128K RULER by 6.80 points (pure recurrent) and nine-task accuracy by 0.62 (hybrid). It was the top Hugging Face paper of the day (128 upvotes).

<div class="dg-title">Asymmetric erase compounds; symmetric erase cannot grow</div>
<div class="dg-sub">The bug is in the erase step, not the write step.</div>

```mermaid
flowchart LR
  S["State S_t<br/><small>fixed-size memory</small>"] --> E{"Erase step<br/><small>read vs modify dirs</small>"}
  E -->|asymmetric| G["Non-normal operator<br/><small>gains compound</small>"]
  G --> X["State explodes<br/><small>long-context failure</small>"]
  E -->|symmetric| N["Non-expansive<br/><small>O(T) growth bound</small>"]
  N --> W["Residual write<br/><small>decay-regulated</small>"]
  W --> S2["Stable S_t+1<br/><small>+6.8 RULER 128K</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class S input
  class E loop
  class N,W core
  class S2 exit
  class G,X err
  linkStyle 1 stroke:#e03131,stroke-width:2px
  linkStyle 3 stroke:#2f9e44,stroke-width:2px
```

<div class="dg-legend">Blue is the state, amber is the erase decision, purple is the fix, green is the stable result, red is the failure path.</div>

## Key findings

- Training instability in GDN-2 comes from the erase operator, not from writes: the state can blow up with zero new information.
- Symmetric erasure makes propagation non-expansive; decay-regulated residual writing recovers the expressiveness that symmetric erase gives up.
- O(T) upper bound on state norm, chunkwise-parallel kernel retained (no training-throughput penalty claimed).
- ~1.6B models: +6.80 avg RULER at 128K (recurrent), +0.62 avg on nine downstream tasks (hybrid).

## Gaps

- Only ~1.6B parameters; no result at the 7B+ scale where hybrid linear attention ships (Ling/Ring 2.6, Nemotron 3).
- The hybrid gain is small (+0.62); the big gain is in the pure-recurrent setting, which few production models use.
- No reported end-to-end throughput or kernel timing vs GDN-2.

## How this relates to prior wiki pages

- **Fills a stability gap in the linear-attention line** on [attention-mechanisms](attention-mechanisms.md). The 08-04 [RAVEN](2026-08-04-raven-sparse-memory-routing.md) page organized the zoo by memory-write policy (dense-write-with-forgetting like DeltaNet vs sparse-write). Today's paper says the *erase* operator's geometry is a third axis that decides whether long-context training survives at all.
- **Complicates the 11-24 Canon-layers result** (Allen-Zhu: plain gated linear attention plus local mixing matches Gated DeltaNet). If richer DeltaNet variants need special erase geometry to train stably, the simpler GLA-plus-Canon recipe looks even more attractive.
- **Efficiency link.** A stable fixed-size state is the alternative to the KV cache. See [kv-cache](../inference-efficiency/kv-cache.md): every recurrent layer that trains reliably at 128K is one fewer layer paying KV memory.
