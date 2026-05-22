# Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

**Source:** HuggingFace daily papers, 2026-05-22.
**arxiv:** [2605.22791](https://arxiv.org/abs/2605.22791)
**Authors:** Ali Hatamizadeh, Yejin Choi, Jan Kautz. NVIDIA.

## TL;DR

Linear attention replaces the unbounded KV cache of softmax attention with a fixed-size recurrent state, getting linear-time sequence mixing and constant-memory decoding. The hard problem is editing the compressed memory without scrambling existing associations. Delta-rule models (DeltaNet, Gated DeltaNet, Kimi Delta Attention / KDA) subtract the current read before writing a new value, with KDA adding channel-wise decay for sharper forgetting. But the active memory edit in all of them uses a single scalar gate to control two operations: how much old content to erase on the key side and how much new content to commit on the value side. Gated DeltaNet-2 separates those roles with a channel-wise erase gate and a channel-wise write gate. It reduces to KDA when both gates collapse to the same scalar, and to Gated DeltaNet when the decay also collapses. At 1.3B parameters trained on 100B FineWeb-Edu tokens, it achieves the strongest overall results among Mamba-2, Gated DeltaNet, KDA, and Mamba-3 variants across language modeling, commonsense reasoning, and retrieval. Its advantage is most pronounced on long-context RULER needle-in-a-haystack benchmarks.

## Why this is Tier 1

NVIDIA shipping a delta-rule linear-attention paper that beats Mamba-3 is the strongest signal yet that the post-transformer architecture race is in active production, not just academic. The decoupled-erase-and-write trick is the most theoretically principled improvement to delta-rule models since Mamba-2 introduced data-dependent decay. Three things to internalize:

1. **The single scalar gate was the hidden ceiling on delta-rule capacity.** Erasing old content (key-side operation) and committing new content (value-side operation) act on different axes of the recurrent state. Tying them with a single scalar was a modeling restriction nobody had named precisely until now.

2. **Gated DeltaNet-2 is a strict generalization.** It reduces to KDA when both gates collapse to the same scalar, and to Gated DeltaNet when decay also collapses. So there is no quality regression risk: the new architecture is a superset.

3. **Long-context RULER multi-key retrieval is where it wins.** This is the benchmark where linear-attention models have historically lost most decisively to full-attention. NVIDIA's claim that Gated DeltaNet-2 closes that gap is the actual news.

## The mechanism

```
DeltaNet:           subtract current read, write new value, no gate
Gated DeltaNet:     add a learned scalar decay gate β_t
KDA:                add channel-wise decay (sharper forgetting per channel)
Gated DeltaNet-2:   decouple into channel-wise erase gate + channel-wise write gate

State update at step t:
  S_t = S_{t-1} ⊙ (1 - G_erase_t k_t k_t^T) + G_write_t k_t v_t^T

  where G_erase_t and G_write_t are channel-wise (vector, not scalar)
        and act on different sides of the rank-1 update
```

## Why this matters now

The wiki has been tracking the post-transformer architecture race since Mamba. The state-of-the-art at the start of 2026 was Mamba-2 (data-dependent decay), DeltaNet (delta-rule overwrite), Gated DeltaNet (added decay gate), and KDA (channel-wise decay). The Mamba-3 paper (released earlier this year, the exponential-trapezoidal-discretization + complex-state + MIMO formulation) was the dense network reply. Gated DeltaNet-2 from NVIDIA is the delta-rule reply to Mamba-3, and it wins on the benchmarks that mattered.

This matters for two reasons:

1. **Inference economics.** Constant-memory decoding is the holy grail for serving long-context workloads. If Gated DeltaNet-2 is competitive with full-attention on retrieval, the constant-memory decode side closes the practical-deployment gap.

2. **NVIDIA architecture co-design.** NVIDIA shipping a model architecture paper, not a kernel paper, signals that the company is positioning hardware-aware architecture as a strategic moat. The next-generation Rubin and Vera SKUs will likely be designed to accelerate linear-recurrent state-space operations as a first-class workload, not just dense attention.

## Numbers

- 1.3B parameters, 100B FineWeb-Edu tokens.
- Strongest overall across language modeling, commonsense reasoning, retrieval.
- Advantage most pronounced on long-context RULER multi-key retrieval.

## Open questions

- How does Gated DeltaNet-2 scale to 7B / 30B / 70B? Mamba-2 had scaling-law surprises at 30B-class.
- Does the channel-wise gating compose with Mixture-of-Experts? The interaction with expert routing is not addressed.
- Whether NVIDIA's next hardware generation includes silicon-level support for the channel-wise gating asymmetric erase factor.

## Industrial implication

If reproductions hold and Gated DeltaNet-2 scales, the architecture race has a credible challenger to full-attention transformers, and one that NVIDIA is now invested in. The wiki's `inference-efficiency` concept page should be updated to reflect that linear-recurrent state-space architecture is no longer just "competitive on perplexity" but also "competitive on retrieval."

## Cross-references

- [KVServe (2026-05-22)](2026-05-22-kvserve-adaptive-kv-compression-disaggregated-serving.md)
- [RTPurbo / Full Attention Strikes Back (2026-05-22)](2026-05-22-rtpurbo-full-attention-sparse-transfer.md)
- [WorldKV (2026-05-22)](2026-05-22-worldkv-world-memory-retrieval-compression.md)
- [Delta Attention Residuals (2026-05-20)](../llms-foundation-models/2026-05-20-delta-attention-residuals.md)

## Source

Raw: `raw/huggingface/2026-05-22-gated-deltanet-2-decoupling-erase-and-write-in-linear-attent.md`.
