# FocuSFT: Bilevel Optimization for Dilution-Aware Long-Context Fine-Tuning

**Date:** 2026-05-13
**Source:** [arXiv 2605.09932](https://arxiv.org/abs/2605.09932) · HuggingFace Daily Papers
**Tier:** 1. Long-context training, attention dilution, bilevel optimization
**Raw:** [`raw/huggingface/2026-05-13-focusft-bilevel-optimization-for-dilution-aware-long-context.md`](../../raw/huggingface/2026-05-13-focusft-bilevel-optimization-for-dilution-aware-long-context.md)

## TL;DR

The long-context capability gap is traced to a training-time problem, not an architectural one. Standard SFT on long sequences lets positional biases and attention sinks soak up the attention budget so that content tokens get starved. The weak gradient on those starved tokens means the model never learns to use them. FocuSFT is a bilevel optimization fix: an inner loop adapts lightweight fast-weight parameters to form a parametric memory that concentrates attention on relevant content, and the outer loop runs SFT conditioned on this sharpened representation. Both loops use bidirectional attention over context tokens while keeping causal masking on responses, which removes the asymmetry that creates attention sinks during training. On BABILong, up to +14 points across 4K-32K context lengths. On RULER, CWE aggregation rises 72.9 -> 81.1 at 16K. On GPQA agentic tool use, +24% relative on pass@1. Attention-sink mass drops 529x and context engagement triples.

## Why it matters

Until today, the wiki has treated long-context capability as primarily an inference-side problem: better caches (Make Each Token Count), better indexers (MISA), better drafting (Orthrus is the next-day analog). FocuSFT pushes it back to the training side, attention sinks are not just an inference artifact, they form during SFT and become baked into the gradient signal. This is the training-side complement to Make Each Token Count's inference-side claim that attention dilution is a real cost.

## Mechanism

The bilevel structure is the load-bearing piece. Inner loop: train fast-weights on each training context to form a parametric memory that biases attention toward semantically relevant tokens. Outer loop: run SFT on the model conditioned on the sharpened representation. The inner loop's fast-weights are not part of the deployed model; they exist only during training to *sharpen the gradient signal that the outer SFT loop sees*. The deployed model is a standard model with much-improved long-context behavior.

The bidirectional-attention-on-context, causal-on-response trick is the second load-bearing piece. Causal masking on the context creates a positional asymmetry that produces attention sinks at the beginning of the sequence. By using bidirectional attention on context tokens during training (causal only on the response tokens that are actually being autoregressively generated), the sink-creating asymmetry is removed. The 529x reduction in attention-sink mass is the direct readout of this design.

## Relation to prior wiki

- **Make Each Token Count (2026-05-12)** — selective KV eviction beats the full cache by reducing attention dilution. FocuSFT is the training-side counterpart, attention dilution starts during training, not at inference. The two are not redundant: even with FocuSFT-trained models, run-time eviction still helps because some dilution is task-dependent. Two papers in two days making the same diagnosis at different layers.
- **LongAct (2026-04-18)** — saliency-guided sparse RL updates: 8% on LongBench v2 by concentrating gradients only on weights tied to high-magnitude Q/K activations. FocuSFT is the same idea at the SFT stage rather than the RL stage. The pattern is now consistent: long-context training requires gradient concentration; uniform gradients are wasteful.
- **TIP (2026-04-16)** — 10% of distillation tokens carry signal. FocuSFT is the long-context-SFT analog: most positions during long-context SFT carry attention to positional sinks rather than content; concentrating the inner-loop sharpening on content tokens triples context engagement.
- **MIA Signature (2026-05-09)** — long-context activation signatures. FocuSFT's diagnosis (attention sinks dilute the training signal) is mechanistically consistent with MIA's finding that activation patterns at long context are dominated by a small set of position-specific tokens.

## Research angle

Three open problems. (1) The bilevel inner loop is expensive; the paper does not benchmark training-time cost against a strong long-context-SFT baseline at matched final quality. The right comparison is dollars per FocuSFT-quality model. (2) The bidirectional-context, causal-response masking is a structural change in how SFT is done; whether it composes with reasoning-mode training (where the entire generation is autoregressive thinking) is open. (3) Composition with FocuSFT plus Make Each Token Count is the natural next experiment: training-side sharpening plus inference-side selection. If the gains stack, the long-context cost floor drops on both axes simultaneously.

## Why Tier 1

Long-context capability has been the unresolved bottleneck for agentic and reasoning workloads. FocuSFT identifies the training-side cause of the bottleneck, gives a concrete mechanism to fix it, and shows large gains across three different long-context benchmarks. This is the training-time corollary to the inference-time long-context efficiency thread.
