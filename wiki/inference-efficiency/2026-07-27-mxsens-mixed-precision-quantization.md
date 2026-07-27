# MXSens: Sensitivity-Aware Mixed-Precision Quantization

**Source:** Kurate weekly cs.LG #17 (ai_rating 5.5/10, farmer-inferred tier 1), absent from HuggingFace | **arXiv:** [2607.17733](https://arxiv.org/abs/2607.17733) | **Raw:** [Kurate cs.LG](../../raw/kurate/2026-07-27-cs-lg.md)
**Authors:** Simla Burcu Harma, Danila Mishin, Zhengyuan Su, Ayan Chakraborty, Elizaveta Kostenok et al.

## TL;DR

A sensitivity-aware mixed-precision quantization method for LLM inference: rather than applying one bit-width uniformly, MXSens measures which parts of the network actually degrade under low precision and spends the bit budget accordingly. Surfaced today by the first fresh Kurate weekly leaderboard in six weeks (see the connector note in the [2026-07-27 digest](../daily-digest/2026-07/2026-07-27.md)), and the highest-ranked entry the farmer's keyword heuristic classified into the efficiency tier. This page is a stub built from leaderboard metadata and the title-level claim; the paper has no alphaxiv overview yet and was not covered by HuggingFace, RSS, or social today.

## Why it is worth tracking

The wiki's quantization thread has converged on one idea from several directions: **uniform precision is the wrong default because sensitivity is not uniform.** The disagreement is about which axis the non-uniformity runs along.

- [Mix-Quant (05-21)](2026-05-21-mix-quant-phase-aware-quantization.md) split along the **inference-phase** axis: NVFP4 for prefill, which is empirically robust to quantization error in agentic workloads, and BF16 preserved for decode, where error compounds across a long autoregressive trajectory. Up to 3x prefill speedup.
- [OSCAR (05-21)](2026-05-21-oscar-extreme-kv-cache-quantization.md) and [TurboQuant (04-22)](2026-04-22-turbo-quant-kv-cache-quantization.md) split along the **cache-versus-weights** axis, pushing KV cache to extreme low precision while leaving weights alone.
- [Channel-wise vector quantization (05-26)](2026-05-26-channel-wise-vector-quantization.md) splits along the **channel** axis.
- MXSens splits along a measured **sensitivity** axis, which is the most general of the four and subsumes the others in principle: phase, cache-versus-weights, and channel are all specific hypotheses about where sensitivity lives, whereas measuring it directly does not presume.

That generality is also the reason to be skeptical until the numbers are read. Sensitivity-aware mixed precision is an old idea in the quantization literature, and the recurring problem is that the sensitivity metric is expensive to compute, unstable across calibration sets, or produces a bit assignment that no kernel can execute efficiently. A mixed-precision layout that hardware cannot serve at the promised throughput is a paper result rather than a deployment.

## What to check when the full text is read

1. **What is the sensitivity metric and what does it cost?** Hessian-based, gradient-based, or empirical-perturbation, and whether it needs a calibration pass proportional to model size.
2. **Is the resulting layout kernel-friendly?** Blackwell's MXFP formats have specific block structures. A per-layer or per-block assignment that maps onto them is deployable; an arbitrary per-tensor assignment is not.
3. **Does it compose with Mix-Quant's phase split?** These are orthogonal in principle, and nobody has stacked them.
4. **Is sensitivity measured on the right workload?** Mix-Quant's central finding was that agentic workloads have a different sensitivity profile than chatbot workloads. A sensitivity measurement calibrated on short-context benchmarks would mis-assign bits for agentic serving.

## Caveat on this page

Metadata-level entry, not a read of the paper. The Kurate ai_rating is 5.5/10, which is below the leaderboard median today, and the tier-1 classification comes from the farmer's title keyword match on "quantization" rather than from an assessment of the contribution. Treat the ranking as weak evidence. Flagged here so the next efficiency ingest in this area has the pointer.

## Related pages

- [KV Cache](kv-cache.md) — concept page
- [Mix-Quant: phase-aware NVFP4](2026-05-21-mix-quant-phase-aware-quantization.md)
- [OSCAR: extreme KV cache quantization](2026-05-21-oscar-extreme-kv-cache-quantization.md)
- [VisCo: visual token compression](2026-07-27-visco-visual-token-compression.md)
