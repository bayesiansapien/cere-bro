# SPOT: speculative decoding for diffusion LMs by predicting the commit order

**Source:** [arXiv 2610.22543](https://arxiv.org/abs/2610.22543) · HuggingFace daily papers 2026-10-28 · raw: `raw/huggingface/2026-10-28-on-the-spot-enhancing-speculative-decoding-for-diffusion-lan.md`

**TL;DR.** Diffusion language models (DLMs, which fill in masked positions in parallel instead of left to right) are lossless only when they commit one position per pass, which makes them slow. Speculative decoding (a cheap drafter guesses, the big model verifies in one pass) does not transfer directly, because a DLM must guess both *what* token and *where*. SPOT observes that the model's previous-pass predictions already hold the right token at over 90% of positions; what is missing is the order. A 0.62M-parameter drafter reads only the target's output distributions, predicts the commit order, proposes a tree of continuations, and the target verifies the tree in one pass by state equality. Sharing Gumbel noise between drafter and target ("coupled-noise match") keeps verification exact at any temperature. Result: up to 6.8x fewer target passes and 3.4x throughput on SDAR-8B, with the drafter transferring across six DLMs. SPOT-Sets extends the idea to threshold decoding and adds 59% throughput on top.

<div class="dg-title">The tokens are mostly known. The order is the guess.</div>
<div class="dg-sub">A tiny drafter predicts where to commit next; the big model checks a whole tree at once.</div>

```mermaid
flowchart LR
  P["Last pass<br/><small>token dists, 90% right</small>"] --> D["SPOT drafter<br/><small>0.62M, predicts order</small>"]
  D --> T["Candidate tree<br/><small>positions + tokens</small>"]
  T --> V["Target DLM<br/><small>one verify pass</small>"]
  V -->|state match| O["Committed span<br/><small>up to 6.8x fewer passes</small>"]
  V -->|mismatch| X["Rejected branch<br/><small>falls back exactly</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class P input
  class D,T loop
  class V core
  class O exit
  class X err
  linkStyle 4 stroke:#2f9e44,stroke-width:2px
  linkStyle 5 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is the free signal from the last pass, amber is drafting, purple is the target model, green is accepted output, red is rejected drafts.</div>

## Relation to prior wiki
- **Extends** [speculative decoding](speculative-decoding.md) to a new model family. The 10-28 uzu result (a tree drafter giving ~7.5 accepted tokens per weight read on an autoregressive 9B) and SPOT both win by verifying a tree, not a chain.
- **Contrasts** with the 10-22 finding that draft length must shrink as batch grows: SPOT reports only single-stream throughput, so its server-side value is untested.
- Diffusion LMs keep showing up (Kurate's "How To Build A Modern Diffusion Language Model", NVIDIA's NLD-Uni this week). Lossless acceleration is the missing piece for them to compete on serving cost.

## Gaps
Only SDAR-family block-diffusion models at 8B. No batched serving numbers, no comparison against an autoregressive model of equal quality on wall-clock.
