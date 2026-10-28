# OPTIC: 100x compression of per-layer embeddings (2610.31309)

**TL;DR.** Per-layer embeddings (PLE: a separate embedding vector per token *per layer*, used in Gemma's on-device E-series) are 35.2% of Gemma 4 E4B's parameters. At extreme compression, giving each token-layer vector its own few-byte code fails. OPTIC (Output-Path-fitted, Token-shared Indexed Codes) stores one quantized code tuple per token and decodes it at every layer with a small layer-specific affine decoder. Codes and decoders are fitted to the PLE output path, not to the stored vectors. At about 100x PLE compression it keeps 97.8% of the uncompressed model's performance across seven benchmarks (product quantization, the best of six baselines: 66.3%). At 594x and 1,002x it keeps 90.5% and 84.1%. On the official W4A16 release it keeps 96.9% at ~100x. GPU memory drops 29.7% at the same KV size, with at most 0.40% slowdown.

<div class="dg-title">One code per token, decoded differently at every layer</div>
<div class="dg-sub">Cross-layer sharing is where the 100x comes from.</div>

```mermaid
flowchart LR
  T["Token id<br/><small>known before layer 0</small>"] --> C["Shared code<br/><small>one tuple per token</small>"]
  C --> D1["Layer-1 decoder<br/><small>small affine map</small>"]
  C --> D2["Layer-k decoder<br/><small>small affine map</small>"]
  D1 --> O["PLE output path<br/><small>what the fit targets</small>"]
  D2 --> O
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class T input
  class C,D1,D2 core
  class O exit
```

<div class="dg-legend">Blue is the token address, purple are the shared code and per-layer decoders, green is the fitted target.</div>

## Relation to prior wiki pages
- Third compression result for token-ID-addressed tables in a week on [conditional memory embeddings](conditional-memory-embeddings.md): Conditional Program (10-22, 2-bit codes for Engram n-gram tables, 203 GB to 51 GB) and DeepSeek's Engram prefetch (10-22). OPTIC is the "compress it into HBM" route at a far higher ratio, exploiting cross-layer redundancy instead of per-row codes.
- Like RAQ-MLA (today), the fit targets the output path, not tensor reconstruction.

## Gaps
- Gemma 4 E4B only. Whether larger PLE-style tables (or Engram tables) share as much cross-layer structure is open.

Raw: [HF](../../raw/huggingface/2026-10-27-extreme-compression-of-per-layer-embeddings-via-cross-layer.md) · [arXiv](https://arxiv.org/abs/2610.31309)
