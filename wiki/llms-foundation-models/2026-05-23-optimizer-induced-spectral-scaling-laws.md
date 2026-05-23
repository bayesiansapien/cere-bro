# Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws

**Date:** 2026-05-23
**Arxiv:** [2605.21803](https://arxiv.org/abs/2605.21803)
**HF papers:** [https://huggingface.co/papers/2605.21803](https://huggingface.co/papers/2605.21803)
**Raw source:** [farmer/huggingface](../../raw/huggingface/2026-05-23-same-architecture-different-capacity-optimizer-induced-spect.md)

## TL;DR

Scaling laws have always treated the optimizer as a fixed training detail. This paper shows that the optimizer is a first-class axis of representation scaling. Using eigenspectra of FFN representations measured through soft and hard spectral ranks, the authors hold the architecture and width schedule fixed and vary only the optimizer. AdamW gives weak hard-rank scaling (β=0.44) on rare-token (TAIL) representations. Muon gives linear hard-rank scaling (β=1.02) in the same regime. That is a 2.3x increase in the scaling exponent from the optimizer choice alone, exceeding the effect of architectural interventions (attention rank, positional encoding) the authors test.

## Why this matters

The wiki has tracked optimizer-scaling work since the 05-13 / 05-21 MoE-muP-to-Maximally-Scale-Stable-Parameterization paper (Kurate cs.LG #14, ai_rating=9.0). That paper made the architectural choice (MoE) scale-stable under muP. This paper says the optimizer itself, holding architecture fixed, induces a different scaling law. The two findings combine into a single thesis: **representation capacity is jointly determined by (optimizer, architecture, scale)**, and the conventional scaling-law setup that varies only width and data is undercounting the design space.

The matched-loss / different-spectral-geometry observation is the sharpest result. AdamW configurations can match low-rank Dion variants in perplexity under extended training, while exhibiting different spectral geometry. Loss-matched does not imply structure-matched.

## Mechanism

Spectral rank of FFN representations is measured two ways:
- **Soft rank**: continuous measure of effective dimensionality from the eigenspectrum.
- **Hard rank**: count of eigenvalues above a threshold.

The asymmetry between the two reveals not just *how much* capacity is realized but *how it is structured* across eigenmodes.

Holding everything else fixed, the rare-token (TAIL) representations are where the optimizer effect is largest, because the gradient signal there is the weakest and most sensitive to update geometry. AdamW's coordinate-wise normalization underweights these directions; Muon's orthogonalization preserves them.

## Key takeaways

- AdamW hard-rank scaling exponent: β=0.44 on TAIL.
- Muon hard-rank scaling exponent: β=1.02 on TAIL.
- 2.3x increase in scaling exponent from optimizer choice.
- Optimizer-induced spectral shifts exceed architectural interventions on attention rank and positional encoding.
- Loss-matched configurations can have sharply different representation structures.

## Gaps

Whether the larger spectral-rank scaling under Muon converts to downstream task gains is not the load-bearing finding (the paper is about representation structure). But the next-quarter question is exactly that: does the higher β translate to capability scaling, or only to representation diversity that does not show up on standard benchmarks? Composition with quantization is open: low-rank representations are easier to quantize; if Muon makes representations higher-rank, quantization tax may rise.

## Related wiki pages

- [LLMs / Foundation Models](./llms-foundation-models.md).
- [MoE muP scale-stable parameterization (2026-05-17)](../inference-efficiency/2026-05-17-raschka-llm-architecture-kv-sharing-mhc-compressed-attention.md) — see also 05-21 muP-MoE summary.
- [Bitter lesson for data filtering (2026-05-19 via Kurate)](../llms-foundation-models/) — adjacent re-evaluation of scaling assumptions.

## Research angle

If optimization is a first-class scaling axis, the next generation of scaling-law papers needs a third variable beyond (params, data). The compute-optimal frontier at fixed (params, data) may move substantially with the optimizer, and "Chinchilla-optimal" becomes optimizer-conditional. The practical implication: a lab that trains a 10B model with Muon may have richer representations than a lab that trains a 30B model with AdamW. That changes the open-vs-closed scoreboard.
