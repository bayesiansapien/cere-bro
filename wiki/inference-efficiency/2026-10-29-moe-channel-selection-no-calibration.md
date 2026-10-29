# Channel selection for MoE decoding needs no calibration data

**Source:** [arXiv 2610.37386](https://arxiv.org/abs/2610.37386) · HuggingFace daily papers 2026-10-28 · raw: `raw/huggingface/2026-10-28-channel-selection-for-mixture-of-experts-decoding-needs-no-c.md`

**TL;DR.** At batch one, a MoE (mixture-of-experts) model's decode speed is set by how many routed-expert weight bytes it reads per token. Channel selectors skip the intermediate channels of each expert that contribute little to the current token. The usual recipe keeps channels above a threshold calibrated offline. This paper shows the threshold buys nothing: it does not fix the read budget (a selector calibrated for 18% reads only 12.9% on average), and per-token top-k on the same score matches or beats it in 40 of 43 comparisons, with no calibration data at all. The authors then build a reader entirely from the model's own weights: a ternary sketch screens channels, and a low-rank map recovers the contribution of skipped ones. It keeps 98.1% of full accuracy at 17.8% of routed-expert reads, and its Triton kernels run MoE blocks 1.60-1.90x faster than optimized vLLM at batch one (up to 2.69x at larger batches).

<div class="dg-title">Read fewer expert channels, decided per token</div>
<div class="dg-sub">A weight-only sketch picks the channels; a low-rank map patches what was skipped.</div>

```mermaid
flowchart LR
  T["Token state<br/><small>enters routed expert</small>"] --> S["Ternary sketch<br/><small>scores every channel</small>"]
  S -->|top-k| R["Read channels<br/><small>~18% of weights</small>"]
  S -->|skipped| L["Low-rank map<br/><small>recovers the rest</small>"]
  R --> O["Expert output<br/><small>98.1% of accuracy</small>"]
  L --> O
  S -.->|threshold| X["Unstable budget<br/><small>repetition loops</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class T input
  class S loop
  class R,L core
  class O exit
  class X err
  linkStyle 5 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is input, amber is the selector, purple are the two read paths, green is output, red is the calibrated-threshold failure mode.</div>

## Key findings
- Calibrated thresholds do not control the read budget: the number of channels passing a fixed threshold varies by input (Prox calibrated for 18% reads 12.9%).
- Top-k on the same score matches or beats threshold in 40 of 43 comparisons at 13% and 18% budgets, including all 23 generation tasks.
- Thresholds cause repetition-loop collapse on Gemma 4; top-k does not.
- Weight-only reader: 98.1% of full accuracy at 17.8% of routed-expert reads across three post-trained MoEs; 1.60-1.90x MoE-block speedup over vLLM at batch 1.

## Relation to prior wiki
- **Extends** the "protect the fragile part" thread in [model pruning and sparsity](model-pruning-sparsity.md): ThinkBit (10-28) allocated bits per layer by sensitivity; this allocates reads per token by contribution.
- **Complements** [quantization](quantization.md): channel skipping and low-bit weights both cut bytes per token and should compose, but nobody has tested them together.
- **Fits** the bandwidth framing from the 10-28 uzu/local-decode note: at batch 1 the only levers are fewer bytes per token or more tokens per read. This is the "fewer bytes" lever inside MoE experts.

## Open questions
- Does the low-rank recovery map survive 4-bit expert weights, or does quantization noise swamp it?
- At large batch, different tokens want different channels, so the union read grows. The 2.69x at larger batch suggests it holds, but the crossover batch size is not reported.
