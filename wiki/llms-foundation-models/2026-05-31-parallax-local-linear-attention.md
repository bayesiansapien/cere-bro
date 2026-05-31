# Parallax: Parameterized Local Linear Attention for Language Modeling

**arXiv:** [2605.29157](https://arxiv.org/abs/2605.29157) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.29157) · **Date:** 2026-05-31
**Authors:** Yifei Zuo (Northwestern), Dhruv Pai (Tilde Research), Zhichen Zeng (UW), Alec Dewulf, Shuming Hu (Tilde), Zhaoran Wang (Northwestern)
**Raw:** [farmer file](../../raw/huggingface/2026-05-31-parallax-parameterized-local-linear-attention-for-language-m.md)

## TL;DR

Softmax attention is, viewed through the test-time regression lens, a local *constant* estimator: each query reads a kernel-weighted average of values around it. Local Linear Attention (LLA) upgrades that to a local *linear* estimator, which nonparametric statistics says has a strictly better bias-variance tradeoff for associative memory. The catch is that exact LLA solves a linear system per query (a conjugate-gradient inner loop), which is too slow and numerically fragile to pretrain at scale. Parallax removes the solver entirely: it learns an extra query-like projector that probes the KV covariance directly, places the result in a family of attention variants parameterized by bandwidth / probe / affine structure, and ships a hardware-aware kernel that raises arithmetic intensity above FlashAttention (pushing attention from memory-bound toward compute-bound). The prototype decode kernel matches or beats FlashAttention 2/3 across batch sizes and context lengths. Pretrained at 0.6B and 1.7B, Parallax shows consistent perplexity gains that survive both parameter-matched and compute-matched controls (a genuine Pareto improvement), and the gains transfer downstream. The headline secondary finding: Muon unlocks Parallax's capacity in a way AdamW does not, the first clean demonstration of architecture-optimizer codesign for an attention mechanism.

## The mechanism

```
Softmax attention   : value ≈ local CONSTANT fit around the query   (kernel-weighted mean)
Local Linear Attn   : value ≈ local LINEAR  fit around the query   (better bias-variance)

Exact LLA (too slow):
  query q ─► solve  Σ x = μ   per query  (conjugate-gradient inner loop) ─► estimate
            └ Σ = local KV covariance, μ = local mean ┘   T·L·d memory access

Parallax (no solver):
  query q ──────────────► softmax-style read ─┐
  learned probe  p(q) ──► probes KV covariance ┼─► affine combine ─► estimate
                          (replaces the solve)  ┘
  + hardware-aware kernel: higher arithmetic intensity than FlashAttention
    (attention becomes compute-bound, not memory-bound)
```

## What problem it solves

The core computational primitive of the Transformer, attention, has been structurally frozen while everything around it (optimizers, data, MoE routing) has been re-engineered. Efficient-attention research has mostly chased *sub*quadratic cost (linear attention, SSMs like Mamba, DeltaNet) and accepted a quality hit on in-context retrieval, or it has optimized the existing softmax primitive without changing it (FlashAttention). LLA is a rare proposal that changes the primitive in a direction that is provably *more* expressive rather than merely cheaper, but nobody had scaled it because the per-query linear solve is both expensive (an iterative solver needs `T·L·d` memory traffic versus `2·L·d` for one attention pass) and numerically unstable. Parallax is the first paper to make the local-linear estimator trainable at LLM pretraining scale.

## Core novelty

Two things. First, the solver elimination: instead of solving `Σx = μ` per query, Parallax learns a second query-like projector that directly probes the KV covariance, turning an iterative numerical routine into a single learned forward op. That move also defines a *family* of attention mechanisms indexed by bandwidth (how local the fit is), probe construction, and affine structure, with softmax attention sitting at one corner. Second, the hardware-aware algorithm deliberately increases arithmetic intensity so that attention shifts into a compute-bound regime where modern GPU FLOPs are not starved by memory bandwidth, which is why the decode kernel can match FlashAttention 2/3 despite doing more math per token.

## Key takeaways

- Local-linear estimator (better bias-variance for associative memory) made scalable by replacing the per-query CG solver with a learned covariance probe.
- Decode kernel **matches or beats FlashAttention 2/3** across diverse batch sizes and context lengths, by raising arithmetic intensity into the compute-bound regime.
- Pretrained at 0.6B and 1.7B: consistent perplexity gains throughout pretraining, **persisting under both parameter-matched and compute-matched controls** (Pareto improvement, not a parameter-count artifact).
- **Muon unlocks Parallax's capacity**; AdamW does not realize the same gain. Claimed as the first empirical architecture-optimizer codesign result for attention.

## Gaps in the study

Largest scale is 1.7B, well below the dense-attention frontier where retrieval behavior and long-context degradation actually bite; the in-context retrieval weakness that plagues linear-attention variants is exactly the regime not yet stress-tested at length. The Muon-unlocks-Parallax phenomenon is reported empirically without a mechanistic account of *why* the optimizer matters for this architecture specifically. No long-context retrieval benchmark (needle-in-haystack, RULER) is reported, which is the make-or-break axis for any attention replacement.

## Relation to prior wiki state

Parallax sits at the intersection of two threads the wiki has been tracking. The linear-attention substrate thread runs through MDN (05-11, the first paper this month to parallelize stepwise *momentum* inside the delta-linear recurrence without breaking causality) and Delta-Attention residuals (05-20). Those papers improve the *recurrent rule* inside linear layers; Parallax instead upgrades the *estimator order* of the attention read itself (constant → linear), a different and arguably deeper axis. The more striking connection is to the optimizer-codesign thread: "Same Architecture, Optimizer-Induced Spectral Scaling Laws" (05-23) showed that Muon realizes near-linear hard-rank scaling (β=1.02) on rare-token representations where AdamW stalls (β=0.44), arguing the optimizer determines effective capacity. Parallax's finding that Muon, not AdamW, unlocks its capacity is the same claim arriving from the architecture side: the two papers together say optimizer choice and architecture choice are not separable design decisions. This also rhymes with MoE-muP (05-17, re-confirmed on Kurate cs.LG #14 at ai_rating 9.0), which made MoE scale-up principled by fixing the parameterization; Parallax does the analogous thing for the attention primitive.

## Research angle

The open question is whether the local-linear estimator's advantage *grows or shrinks with scale*. The MDN research angle asked the same thing about momentum recurrences; here the falsifiable version is whether a 7B-class Parallax keeps the Pareto gain on long-context retrieval, the exact regime where linear-attention substitutes historically collapse. The Muon-codesign result is the more provocative lead: if the architecture-optimizer interaction is real and mechanistic (not a tuning artifact), then the right experimental unit is the (architecture, optimizer) pair, and the field's habit of ablating one while fixing the other is systematically mis-measuring both. A clean follow-up: measure Parallax's FFN spectral ranks under Muon vs AdamW and check whether the codesign benefit shows up as the same rare-token hard-rank scaling the 05-23 paper isolated.

## Links

- [arXiv 2605.29157](https://arxiv.org/abs/2605.29157)
- [MDN momentum delta-linear attention (05-11)](../inference-efficiency/2026-05-11-mdn-momentum-deltanet-linear-attention.md)
- [Optimizer-induced spectral scaling laws (05-23)](2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md)
- [MoE-muP scale-stable parameterization (05-17)](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md)
