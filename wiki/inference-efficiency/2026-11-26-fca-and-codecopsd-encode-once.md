---
title: "Encode once: Factorized Context Attention reuses one KV cache for all spans; CodecOPSD prunes 66% of conditioning tokens"
date: 2026-11-26
source: https://arxiv.org/abs/2611.32423
raw: ../../raw/huggingface/2026-11-25-factorized-context-attention-from-emulated-to-native-grid-pr.md
raw2: ../../raw/huggingface/2026-11-25-on-policy-codec-distillation-for-efficient-all-in-one-video.md
tags: [kv-cache, block-sparse-attention, long-context, token-pruning, video-diffusion, self-distillation]
signal: HuggingFace 11-25
---

# Encode once: FCA and CodecOPSD

**TL;DR.** Two efficiency papers remove repeated work on the input side. FCA notices that "grid probing" (asking a frozen model the same question about many short spans of a long input, a training-free trick that recovers accuracy) is just an attention mask applied from outside. It runs that mask natively: encode the input once into a KV cache, then read every span as a masked sequence in one batched pass. CodecOPSD borrows the video-codec idea of "only encode what changed" to drop redundant conditioning tokens in video diffusion.

<div class="dg-title">Grid probing was attention all along</div>
<div class="dg-sub">FCA turns many re-encoded prompts into one cache plus a block-sparse mask.</div>

```mermaid
flowchart LR
  I["Long input<br/><small>book, video, image</small>"] --> K["KV cache<br/><small>encoded once</small>"]
  K --> M["Block masks<br/><small>local + strided spans</small>"]
  M --> P["Stair positions<br/><small>stay in trained range</small>"]
  P --> B["One batched pass<br/><small>all spans read</small>"]
  B --> A["Answer<br/><small>grid accuracy, less cost</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class I input
  class K,B core
  class M,P loop
  class A exit
```

<div class="dg-legend">Blue is the input, purple is the model's own cache and pass, amber are the mask and position tricks, green is the answer.</div>

## Factorized Context Attention ([2611.32423](https://arxiv.org/abs/2611.32423))

- Training-free block-sparse attention. Encodes the input once into the KV cache, reads all local and strided spans as masked sequences in one batched forward, and uses a **stair position schedule** so every span stays inside the model's trained position range (this is what lets it extend reach past the context window).
- Matches grid probing's accuracy and reach on long video, long-context text and image grounding "at a fraction of its cost", gaining about 10 points over standard full-context reading in the reported settings.

## CodecOPSD ([2611.31184](https://arxiv.org/abs/2611.31184))

- In all-in-one video diffusion, every condition (identity, scribble, depth map, motion video) is tokenized and appended, so conditioning dominates compute.
- Step 1: **codec-based token pruning** keeps only tokens a classical codec would consider new information. Step 2: **on-policy self-distillation** trains a DiT adapter to follow that pruning pattern without quality loss.
- Across 16 condition modalities: **66% of condition tokens pruned on average, ~2x faster denoising, up to 73% smaller cache in KV-cache mode**. Benefit grows with more conditions, frames and resolution, and it transfers to other pretrained image/video models.

## Relation to prior wiki pages

- **Extends** the [KV cache](kv-cache.md) page's "build the cache once, read it many ways" line: MemOnce (11-24) stored a tiny memory and rebuilt the KV cache on demand; FCA keeps one cache and changes the mask. Both treat the cache as the reusable artifact and the read pattern as the variable.
- **Confirms** the 05-19 CompactAttention page (block-union KV selection during chunked prefill) that block-sparse reads over a shared cache match dense accuracy when the blocks are chosen well.
- CodecOPSD is the video counterpart of the token-pruning results on the [model pruning](model-pruning-sparsity.md) page, and a third "on-policy self-distillation" use this month (after OPRD and CSPD on 11-25).

## Gaps

- FCA: exact cost ratio vs grid probing and vs a native long-context baseline is "a fraction" in the abstract.
- CodecOPSD's main results are on the authors' own video model.

Raw: [FCA](../../raw/huggingface/2026-11-25-factorized-context-attention-from-emulated-to-native-grid-pr.md) · [CodecOPSD](../../raw/huggingface/2026-11-25-on-policy-codec-distillation-for-efficient-all-in-one-video.md)
