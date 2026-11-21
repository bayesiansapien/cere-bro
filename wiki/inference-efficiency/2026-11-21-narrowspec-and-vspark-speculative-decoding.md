# NarrowSpec and VSpark: two cheaper drafters for speculative decoding (2611.23835, 2611.22666)

**TL;DR.** Speculative decoding lets a small draft model guess several tokens, and the big target model checks them all in one pass. Two papers on 11-20 make the drafter cheaper in different ways. **NarrowSpec** shows that drafters that read the target's hidden states (DFlash, EAGLE-3) do not need the target's hidden width. Their whole residual stream can run at half or a quarter width and keep most of the acceptance rate. For DFlash, the output adapter folds into the borrowed vocabulary projection, so logits are unchanged up to rounding. On Qwen3-8B (NVFP4) and GPT-OSS-20B (MXFP4) in SGLang, end-to-end decoding is 1.06-1.12x faster on B200 and 1.13-1.44x faster on a DGX Spark (GB10) at batch 1, and up to 1.21x at large batch. No narrow drafter is slower than full width. **VSpark** brings speculative decoding to vision-language-action robot models, where many different action tokens mean almost the same motion, so near-miss drafts get rejected. It trains the drafter on rollouts with calibrated action noise, aligns it to the VLA's hidden features rather than its tokens, and reuses the target's predictions along rejected drafts. It reaches 1.28-2.10x lossless speedup on four VLAs.

<div class="dg-title">Shrink the drafter, keep the verifier</div>
<div class="dg-sub">The target still checks every token, so the drafter can lose width as long as acceptance holds.</div>

```mermaid
flowchart LR
  H["Target hidden states<br/><small>read by the drafter</small>"] --> D["Narrow drafter<br/><small>half or quarter width</small>"]
  D --> F["Folded projection<br/><small>adapter merged into vocab</small>"]
  F --> G["Draft tokens<br/><small>several per step</small>"]
  G --> V{"Target verifies<br/><small>one forward pass</small>"}
  V -->|accepted| O["Output<br/><small>up to 1.44x on GB10</small>"]
  V -->|rejected| D
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class H input
  class D,F,G core
  class V loop
  class O exit
  linkStyle 5 stroke:#2f9e44,stroke-width:2px
  linkStyle 6 stroke:#f08c00,stroke-width:2px
```

<div class="dg-legend">Blue is the target's state, purple is the drafter, amber is verification, green is the result.</div>

## Why NarrowSpec's gain is largest on the small box
On a memory-bandwidth-limited device like GB10, every byte the drafter reads costs latency, so halving its width is close to halving its cost. On B200 the drafter is already a small share of step time. That is why the same change gives 1.44x on a DGX Spark and 1.12x on a B200.

## Relation to prior wiki pages
- **Third drafter-input paper in three days.** DNeo (11-19) argued parallel drafters need better target features; NarrowSpec shows the drafter can be thinner as long as it reads those features. Both say the target's hidden state, not the drafter's capacity, carries the signal. See the [speculative decoding page](speculative-decoding.md).
- **VSpark extends** feature-aligned drafting (the OPRD / hidden-state matching idea from 06-05) to action tokens, and its continuation reuse rhymes with re-speculation in the FPGA inference-chip post circulating on X this week.
- Pairs with the quantized targets trend: NarrowSpec tests on NVFP4 and MXFP4 targets, so it composes with [quantization](quantization.md).

## Gaps
- NarrowSpec reports temperature 0; acceptance at sampling temperatures used in chat is not shown.
- VSpark's lossless claim is about tokens; whether near-equivalent actions could be accepted (lossy but safe) is left open.

## Sources
- [NarrowSpec](https://arxiv.org/abs/2611.23835) · [VSpark](https://arxiv.org/abs/2611.22666) · raw: `raw/huggingface/2026-11-20-narrowspec-draft-hidden-width-need-not-match-the-target-in-s.md`, `raw/huggingface/2026-11-20-vspark-speculative-decoding-for-autoregressive-vision-langua.md`

Concept pages: [speculative decoding](speculative-decoding.md)
