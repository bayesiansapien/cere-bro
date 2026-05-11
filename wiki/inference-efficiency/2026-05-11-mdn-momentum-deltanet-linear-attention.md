# MDN: Parallelizing Stepwise Momentum for Delta Linear Attention

**arXiv:** [2605.05838](https://arxiv.org/abs/2605.05838) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.05838) · **Date:** 2026-05-11
**Tier:** 1 — Linear attention / long-context architecture
**Authors:** Yulong Huang, Xiang Liu et al. (HKUST Guangzhou)
**Raw:** [farmer file](../../raw/huggingface/2026-05-11-mdn-parallelizing-stepwise-momentum-for-delta-linear-atte.md)

## TL;DR

Linear attention models like Mamba2 and GDN read each recurrent state update as one step of online SGD on a latent objective. Naive SGD updates decay information fast and converge slowly, so these models tend to forget fine-grained history. Momentum is the standard SGD fix. The problem is that strict-causal stepwise momentum (block size 1) preserves the inference semantics but is sequential, and blockwise momentum is parallel but breaks causality. MDN reorders the update coefficients geometrically to produce a chunkwise parallel algorithm for stepwise momentum that does not break causality, then uses spectral analysis of the resulting second-order recurrence to constrain the gating so the system stays stable. The Triton kernel runs at roughly the same training throughput as Mamba2 and KDA. At 400M and 1.3B params, MDN beats Transformers, Mamba2, and GDN on broad downstream benchmarks.

## What is new

Two interlocking contributions.

**Geometric reordering of stepwise momentum updates.** Stepwise momentum at block size 1 looks naively sequential because each step depends on the previous step's velocity. The geometric reordering reframes the per-token momentum update so that an entire chunk can be computed in parallel without altering the value computed at any token position. This is the same family of trick that GDN used to parallelize delta-rule updates, applied to the momentum factor.

**Spectral stability analysis.** Momentum updates introduce a second-order recurrence, which can have complex conjugate eigenvalues. Naive gating in the second-order setting destabilizes training because the eigenvalue magnitudes can drift outside the unit circle. The paper analyzes the eigenvalue structure as a function of the gate parameters and derives constraints that keep the system stable across the gating range.

The result is a linear-attention recurrence that retains fine-grained history better than the SGD-rule baselines, while training at competitive throughput.

## Why momentum is the right fix here

Mamba2, GDN, and KDA all interpret their recurrent state updates as closed-form online SGD on an implicit objective. The implicit objective is what the model is trying to memorize as it sees tokens. SGD's failure mode in this regime is the same as in optimization more broadly: rapid information decay (the gradient signal washes out fast) and slow convergence on noisy or fine-grained features. Momentum accumulates the directional component of the gradient signal across steps, which makes it especially useful when the signal you are trying to capture is consistent across many adjacent tokens (the kind of structure long-form text actually has).

The HKUST team is the first to show this concretely at LLM scale. The 400M and 1.3B parameter sweeps are enough to claim that the win is not a tiny-model artifact, and the comparison set (Mamba2, GDN, KDA, Transformer) is the right one.

## Relation to prior wiki coverage

The wiki's hybrid-architecture thread has been about composition (Nemotron3-Super, Kimi Linear) rather than substrate (the recurrent rule inside the linear layers themselves). MDN is the first paper this month to push the recurrent-rule substrate.

This composes naturally with PrfaaS (04-22), which depends on hybrid models with linear-complexity layers to make KV cache shipping affordable. If MDN's stepwise-momentum recurrence becomes the new linear-layer substrate, it makes the linear layers more useful at fixed compute, which makes the hybrid ratio that PrfaaS exploits even more favorable.

This also touches the LongAct (04-18) thread. LongAct identified high-magnitude saliency peaks in Q/K and routed RL gradients selectively to those weights. The MDN momentum mechanism is the architectural analogue: not "which weights to update during RL" but "which historical features to accumulate during inference."

## Research angle

**Composition with delta-rule plus momentum is unmeasured.** The paper compares against GDN (delta rule, no momentum) and against Mamba2 (decay rule, no momentum). The natural next sweep is delta plus momentum, or decay plus momentum, with the gating constraints from the spectral analysis tuned per rule. If the wins compose, this is the cleanest substrate-level update to linear attention in 2026.

**Larger-scale evaluation.** 1.3B parameters is enough to make the claim plausible but not yet enough to clear the bar set by the dense-attention frontier. The natural next paper is a 7B-class MDN trained on a standard tokens-per-step budget, with downstream coverage that includes long-context retrieval benchmarks specifically. Information retention should be the headline metric.

## Links

- [arXiv 2605.05838](https://arxiv.org/abs/2605.05838)
- [HuggingFace](https://huggingface.co/papers/2605.05838)
- [KV cache concept page](kv-cache.md)
