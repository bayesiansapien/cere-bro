---
title: "Understanding Positional Embeddings in Modern LLMs (Sebastian Raschka, Ahead of AI)"
date: 2026-11-16
source: Ahead of AI (RSS + Gmail), amplified on X by @rasbt
topic: llms-foundation-models
---

# How modern LLMs encode position, and where they skip it

**TL;DR.** Raschka's long tutorial builds positional encoding from first principles and then surveys what 2026 open-weight models actually do. Attention without position information cannot tell "the red fox jumps over the gray fox" from the swapped sentence. A causal mask gives implicit order but cannot tell a gap of one token from a gap of ten. GPT-2 adds a learned vector per position before the first block. That does not scale: at a 100K context the table would be over 22% of GPT-2 Medium's weights. Modern models use RoPE (rotary position embedding, which rotates query and key vectors by an angle set by position, inside every attention layer). The 2026 trend is to use *less* RoPE: partial RoPE, NoPE layers, and learned relative biases.

<div class="dg-title">Position moved from the input to inside attention, and is now being thinned out</div>
<div class="dg-sub">Each step trades a little explicit position signal for cheaper or longer context.</div>

```mermaid
flowchart LR
  A["Learned absolute<br/><small>GPT-2, fixed length</small>"] --> R["Full RoPE<br/><small>rotate every q,k pair</small>"]
  R --> P["Partial RoPE<br/><small>rotate a subset</small>"]
  R --> N["NoPE layers<br/><small>causal mask only</small>"]
  R --> B["Relative bias<br/><small>added to scores</small>"]
  P --> L["Long context<br/><small>better extrapolation</small>"]
  N --> L
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class A input
  class R core
  class P,N,B loop
  class L exit
```

<div class="dg-legend">Blue is the original method, purple is today's default, amber are the 2026 variants, green is what they aim for.</div>

## Key points

- **Partial RoPE.** MiniMax-M3 rotates 64 of 128 dimensions per head. That halves the precomputed sine/cosine tables (128 MiB saved at 1M context in BF16), but the KV cache still stores full keys and values. A cited 1B-8B study found rotating about 10% of features gave similar loss to full RoPE, though full RoPE won some evaluations. Raschka's verdict: "hardly worth it."
- **NoPE layers.** The causal mask alone can encode position (a uniform-attention feature equals one over prefix length). In the original NoPE study, a 107M model length-generalized best on ten toy tasks. SmolLM3 skips RoPE in every fourth of 36 layers and its authors credit that with better long context.
- **Learned relative bias.** Thinky's Inkling adds a learned relative-position bias to attention scores in both sliding-window and global layers.

## How it relates to prior wiki pages

- **KV cache link.** Raschka is explicit that partial RoPE does not shrink the KV cache. Methods that compress keys (see [kv-cache](../inference-efficiency/kv-cache.md)) interact with the position scheme, because rotated and unrotated dimensions compress differently.
- **Fills a gap.** The wiki tracks long-context and hybrid attention papers but had no page on the position layer itself. This is the reference for it.

## Links

- Article: https://magazine.sebastianraschka.com/p/understanding-positional-embeddings
- Post: https://x.com/rasbt/status/2121958665989083253
- Raw: `raw/rss/2026-11-15-ahead-of-ai-*.md` · `raw/gmail/2026-11-16-newsletters.md`
