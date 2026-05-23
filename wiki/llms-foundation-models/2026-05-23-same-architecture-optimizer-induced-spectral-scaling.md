# Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws

**Source:** HuggingFace daily papers, 2026-05-23.
**arxiv:** [2605.21803](https://arxiv.org/abs/2605.21803)

## TL;DR

Scaling laws have treated the optimizer as a fixed training detail. This paper shows that assumption misses a fundamental axis of representation scaling. Using eigenspectra of FFN representations (measured through soft and hard spectral ranks), the authors find that the same Transformer architecture realizes markedly different spectral scaling laws under different optimizers. Holding architecture and width fixed, AdamW exhibits weak hard-rank scaling (β=0.44) on rare-token representations, where learning is known to be hardest. Muon achieves linear scaling (β=1.02) in the same regime: a 2.3x increase in scaling exponent. This is not reducible to validation loss: AdamW configurations can match low-rank Dion variants in perplexity under extended training while exhibiting sharply different spectral geometry, demonstrating that matched loss does not imply matched representation structure. The paper argues for optimization as a first-class axis of representation scaling and motivates optimizer-architecture co-design.

## Why this matters

Most of the scaling-law literature (Chinchilla, the Muon paper, the muP MoE paper from this week's Kurate top-20) treats the optimizer as a knob you set once and forget. This paper says the optimizer determines what *capacity* you actually get from a given parameter count. Two models with the same architecture and width can realize different effective capacity depending on the optimizer.

The headline observation: Muon's β=1.02 vs AdamW's β=0.44 on rare-token hard-rank scaling: is mechanism-level evidence that Muon is not just a faster optimizer; it builds qualitatively different representations. This is consistent with the empirical observation that Muon-trained models have outperformed AdamW-trained models at matched compute on tail-distribution benchmarks (the rare-token result is the formal version of this).

The "matched loss does not imply matched representation structure" claim is the more philosophical one. Validation loss is a scalar, and two configurations can hit the same scalar through completely different representational geometries. The downstream implications (fine-tuning behavior, OOD generalization, retrieval quality) are then divergent.

## Connections to prior wiki state

This is the natural complement to the [Kurate cs.LG #14 muP-to-MoE paper (How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization, 05-13)](../). Both papers attack scaling-law parameterization, but from different angles. muP-MoE asks how to make the parameterization scale-invariant; this paper asks how the optimizer-induced spectral geometry differs across choices that pre-test as equivalent under loss.

It also informs the [Forecasting Downstream Performance with Proxy Metrics paper from today (2605.18607)](../inference-efficiency/2026-05-23-proxy-metrics-forecast-downstream.md): proxy metrics derived from next-token distributions are basically representation-quality proxies that bypass the validation-loss bottleneck. The optimizer-spectral-scaling result here gives a theoretical reason why proxy metrics work where loss fails: loss is a scalar that collapses representational geometry; spectral statistics preserve it.

## Gaps

The comparison is AdamW vs Muon vs Dion. Lion, Schedule-Free, and Sophia are missing. The eigenspectra analysis is on FFN representations only. Whether attention-side representations show the same optimizer dependence is not addressed. The claim that this is "more important than architectural effects" is supported by ablations against attention-rank and positional-encoding interventions, but those are not exhaustive.

## Research angle

If the optimizer determines effective spectral capacity, the right move is to choose the optimizer for the downstream task, not for the validation loss. The open question: can you predict downstream task performance from the spectral statistics of the trained representation? If yes, this becomes a practical model-selection tool (cheap-to-compute proxy that beats loss-based selection). If no, the result is theoretically interesting but operationally limited.

A deeper question: representation geometry depends on optimizer and on data. Whether spectral scaling exponents are a stable function of (optimizer, architecture) or also depend on data distribution is the natural follow-up.

## Raw source

[raw/huggingface/2026-05-23-same-architecture-different-capacity-optimizer-induced-spect.md](../../raw/huggingface/2026-05-23-same-architecture-different-capacity-optimizer-induced-spect.md)
