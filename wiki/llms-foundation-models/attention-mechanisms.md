# Attention Mechanisms: Linear, Local-Linear, and Optimizer Codesign

The attention read is the Transformer's core computational primitive, and after years of being structurally frozen it is now an active research surface again. Two distinct lines of work are running in parallel: improving the *recurrent rule* inside linear-attention layers (so they retain history without the quadratic cost), and improving the *estimator order* of the attention read itself. A third theme cuts across both: the optimizer is not separable from the architecture.

## Current State (as of 2026-05-31)

**Parallax: local-linear estimator made scalable, and Muon codesign.** [Parallax](2026-05-31-parallax-local-linear-attention.md) reframes softmax attention as a local *constant* estimator (a kernel-weighted mean) and upgrades it to a local *linear* estimator (Local Linear Attention, LLA), which nonparametric statistics says has a strictly better bias-variance tradeoff for associative memory. Exact LLA needs a per-query linear solve (a conjugate-gradient inner loop) that is too slow and unstable to pretrain; Parallax removes the solver by learning an extra query-like projector that probes the KV covariance directly, and ships a hardware-aware kernel that raises arithmetic intensity above FlashAttention, pushing attention from memory-bound toward compute-bound. The decode kernel matches or beats FlashAttention 2/3; pretraining at 0.6B and 1.7B shows perplexity gains under both parameter- and compute-matched controls (a Pareto improvement). The secondary headline: **Muon unlocks Parallax's capacity where AdamW does not**, claimed as the first architecture-optimizer codesign result for an attention mechanism.

This is significant on two axes. On the *estimator-order* axis, Parallax is a different and arguably deeper move than the recurrent-rule improvements below: it changes what the attention read computes, not just how the linear-layer state evolves. On the *optimizer-codesign* axis, it converges with the scaling-laws literature (see below).

## The two lines of work

```
Line 1 — recurrent rule inside linear layers (subquadratic, retain history):
   Mamba2 / GDN / KDA : state update = one step of online SGD on a latent objective
   MDN (05-11)        : add MOMENTUM to that update, parallelized without breaking causality
   Delta-Attention    : residual/delta corrections on the linear read

Line 2 — estimator order of the attention read itself:
   softmax attention  : local CONSTANT fit   (kernel-weighted mean of values)
   Parallax (05-31)   : local LINEAR fit      (better bias-variance, solver removed)

Cross-cutting — optimizer is not separable from architecture:
   Optimizer-spectral-scaling (05-23) : Muon scales rare-token rank where AdamW stalls
   Parallax (05-31)                   : Muon unlocks LLA capacity where AdamW does not
```

## Key papers

**Parallax (2026-05-31)** — Parameterized Local Linear Attention. Replaces exact-LLA's per-query CG solver with a learned covariance probe; hardware-aware kernel matches/beats FlashAttention 2/3; Pareto perplexity gains at 0.6B/1.7B; Muon-architecture codesign. → [summary](2026-05-31-parallax-local-linear-attention.md)

**MDN: Momentum DeltaNet (2026-05-11)** — Parallelizes stepwise momentum for delta linear attention without breaking causality, with a spectral-stability analysis constraining the gating. Beats Transformers, Mamba2, GDN at 400M/1.3B. The first paper this month to push the recurrent-rule substrate. → [summary](../inference-efficiency/2026-05-11-mdn-momentum-deltanet-linear-attention.md)

**Delta-Attention residuals (2026-05-20)** — Residual/delta corrections to the attention read. → [summary](2026-05-20-delta-attention-residuals.md)

**Same Architecture, Optimizer-Induced Spectral Scaling Laws (2026-05-23)** — Holding architecture and width fixed, Muon realizes near-linear hard-rank scaling on rare-token representations (β=1.02) where AdamW stalls (β=0.44); matched loss does not imply matched representation geometry. The theoretical companion to Parallax's Muon-codesign finding. → [summary](2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md)

## Key concepts

- **Local constant vs local linear estimator**: softmax attention reads a kernel-weighted *average* of nearby values (constant fit); local-linear attention fits a *line*, capturing the local gradient of the value field for better associative recall.
- **Arithmetic intensity**: FLOPs per byte of memory traffic. FlashAttention is memory-bound; Parallax deliberately raises arithmetic intensity to enter the compute-bound regime where GPU FLOPs are not bandwidth-starved.
- **Recurrent rule as online SGD**: Mamba2/GDN/KDA interpret their state update as one closed-form online-SGD step on an implicit memorization objective; momentum (MDN) is the standard SGD fix applied to that update.
- **Architecture-optimizer codesign**: the empirical finding that the right optimizer (Muon) is a function of the architecture, so ablating one while fixing the other mis-measures both.

## Open problems

- **Does the local-linear advantage survive scale and long-context retrieval?** Parallax tops out at 1.7B and reports no needle-in-haystack / RULER numbers; in-context retrieval is exactly where linear-attention substitutes historically collapse.
- **Why does Muon unlock these architectures?** The codesign effect is empirical; no mechanistic account links Muon's update geometry to the local-linear estimator or to rare-token rank.
- **Do recurrent-rule (MDN) and estimator-order (Parallax) gains compose?** Nobody has combined a momentum delta-rule with a local-linear read.

## Related pages

- [KV cache](../inference-efficiency/kv-cache.md)
- [MoE-muP scale-stable parameterization](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md)
- [RL for LLMs](rl-for-llms.md)
