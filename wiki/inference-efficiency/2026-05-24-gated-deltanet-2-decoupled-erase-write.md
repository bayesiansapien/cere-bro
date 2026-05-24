# Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

**Source:** HuggingFace daily papers, [arXiv 2605.22791](https://arxiv.org/abs/2605.22791). NVIDIA (Hatamizadeh, Choi, Kautz).
**Date:** 2026-05-24
**Tier:** 1 (linear attention, long-context efficiency)

## TL;DR

Gated DeltaNet-2 is the next step in the delta-rule linear-attention family. Prior delta-rule models (DeltaNet, Gated DeltaNet, Kimi Delta Attention / KDA) use a single scalar gate to control both how much old content is erased on the key side and how much new content is written on the value side. The authors argue this scalar coupling is a modeling restriction because erasing and writing operate on different axes of the recurrent state. Gated DeltaNet-2 splits the gate into a channel-wise erase gate `b_t` (key side) and a channel-wise write gate `w_t` (value side), reducing to KDA when both gates collapse to the same scalar and to Gated DeltaNet when the decay also collapses. At 1.3B parameters trained on 100B FineWeb-Edu tokens, it beats Mamba-2, Gated DeltaNet, KDA, and Mamba-3 variants on language modeling, commonsense reasoning, and retrieval. The advantage is most pronounced on long-context RULER needle-in-a-haystack, in both pure recurrent and hybrid settings.

## Key findings

- The single-scalar gate in delta-rule models was hiding a two-axis update. Decoupling the axes gives strictly better fast-weight memory updates without changing the asymptotic compute envelope.
- Channel-wise gating on both the erase and write paths is the right granularity. A scalar erase plus channel-wise write, or vice versa, is strictly dominated.
- The chunkwise WY algorithm absorbs the channel-wise decay into asymmetric erase factors, so the parallel-training cost matches the prior generation.
- Multi-key RULER retrieval is the benchmark that exposes the difference. On standard language-modeling perplexity the gap is real but small; on long-context retrieval the gap opens up.

## Why this matters

The delta-rule line (DeltaNet → Gated DeltaNet → KDA → MDN → GDN-2) is the most active corner of efficient sequence modeling. Each step has been a single-mechanism refinement: data-dependent decay (Mamba-2), targeted delta-rule overwriting (DeltaNet), gated decay (Gated DeltaNet), channel-wise forgetting (KDA), momentum updates (MDN, 2026-05-11). GDN-2 is the first to decouple the gate functionally rather than just refining the same gate. That makes it the most interpretable update so far: erase and write are now separately controllable, which opens space for asymmetric training objectives.

The most consequential implication is for hybrid models. PrfaaS-style production stacks (Kimi Linear, MiMo-V2-Flash, Qwen3.5-397B) are linear-attention-heavy because the cache footprint is the binding constraint on cross-datacenter KV transport. If GDN-2 closes more of the quality gap with full attention while keeping the constant-memory decoding, the hybrid ratio shifts toward more linear-attention layers, which directly compounds into KV transport savings.

## Research angle

The decoupling is now a programmable substrate. The natural extension is to ask whether the erase and write gates should be supervised differently during training — for example, RL-style outcome supervision on the write gate (commit only useful content) and curriculum supervision on the erase gate (forget less when sequence is short, more when sequence is long). The wiki has seen this kind of decoupled supervision argument before: LongAct (2026-04-18, the paper that restricted RL gradient updates to high-saliency activations) on the gradient side, and FocuSFT (2026-05-13) on the attention-sink side. GDN-2 opens the same surface in the recurrent-state update itself.

A second open question is whether the channel-wise decoupling generalizes to attention-side architectures rather than recurrent-state ones. The same single-scalar-controls-two-things observation should apply to any attention variant with a learned gate, and the corresponding two-axis decoupling could yield similar gains.

## Related

- [KV Cache](kv-cache.md) — concept page, MDN line.
- [MDN: Momentum DeltaNet (2026-05-11)](kv-cache.md#key-papers) — momentum-update line in the same family.
- Hybrid architectures: prior wiki entries on Kimi Linear / MiMo-V2-Flash via PrfaaS.

Code: [NVlabs/GatedDeltaNet-2](https://github.com/NVlabs/GatedDeltaNet-2).

## Raw source

[`raw/huggingface/2026-05-24-gated-deltanet-2-decoupling-erase-and-write-in-linear-attent.md`](../../raw/huggingface/2026-05-24-gated-deltanet-2-decoupling-erase-and-write-in-linear-attent.md)
