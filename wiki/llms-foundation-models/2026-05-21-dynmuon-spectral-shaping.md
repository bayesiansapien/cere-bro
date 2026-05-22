# DynMuon: Dynamic Spectral Shaping of the Muon Optimizer

**Source:** HuggingFace Daily Papers 2026-05-21 · arXiv 2605.17109 · [paper](https://arxiv.org/abs/2605.17109) · [raw](../../raw/huggingface/2026-05-21-dynmuon-a-dynamic-spectral-shaping-view-of-muon.md)
**Topic:** llms / optimization

## TL;DR

Muon replaces the standard gradient update matrix M = U Sigma V^T with its polar factor U V^T, dropping the singular values. DynMuon generalizes this to M = U Sigma^p V^T with a tunable exponent p, treats p as a scheduled control variable, and develops a theory of how to pick p based on local curvature, gradient noise, and training stage. Across model sizes, architectures, and settings, DynMuon achieves lower validation loss than Muon at parity and reaches the same target loss in 10.6-26.5% fewer steps. The mechanism: positive p early emphasizes high-curvature directions for fast signal contraction, mildly negative p late reallocates update strength toward low-curvature directions that still contain useful signal.

## What is new

Muon has become the dominant optimizer for Transformer pre-training across labs, but its core operation (replacing Sigma with the identity) is empirically defended rather than theoretically justified. The "spectral shaping" framing makes the family explicit: Sigma^0 = Muon's polar factor, Sigma^1 = standard SGD, Sigma^{-1} = preconditioned-by-singular-values variant. With p as a tunable knob, three regimes become diagnosable: high p concentrates update energy on top singular directions, low (negative) p spreads it across the spectrum, p=0 is the special Muon case.

The theory ties optimal p to three quantities: local Hessian curvature (high curvature wants high p early), gradient noise from stochastic minibatches and label noise (more noise wants lower p), and training stage (the bias-variance tradeoff shifts as the model converges). The empirical schedule moves p from positive to mildly negative over training. Both halves of the schedule are validated against alternatives in the ablation.

## Why it matters

DynMuon is the first paper the wiki tracks that gives Muon a continuous family parameterization plus a theory of when each member of the family is optimal. The 10.6-26.5% step reduction at the same target loss is large for an optimizer-only intervention, especially given Muon was already the strong baseline. The contribution is more conceptual than the recipe: framing optimizer choice as spectral shaping opens space for further family members (per-layer p schedules, gradient-noise-adaptive p, MoE-aware p).

The wiki has tracked an active thread of architecture-and-training-recipe research: HRM-Text (today's other paper, 1B HRM trained on $1.5K compute to 60% MMLU), Delta Attention Residuals (2026-05-20, routing over sublayer deltas), Lighthouse Attention (2026-05-16, pre-training-only sparse attention). DynMuon adds the optimizer axis to that bundle. The compositions matter: Delta Attention Residuals changes the residual mixing matrix, which changes the Hessian curvature profile, which changes the optimal p schedule. Without joint tuning, the architecture-side and optimizer-side gains may not stack.

## Research angle

Three open questions. First, the optimal p schedule is universal across the architectures tested. Is the universal schedule a function of training-step count alone, or does the model size and shape change it? The paper claims robustness across scales but the relationship between p and Hessian curvature should be size-dependent. Second, can DynMuon's spectral-shaping insight extend to AdamW-class optimizers? AdamW does not have an obvious Sigma analogue, but the per-coordinate adaptive learning rates serve a similar concentrate-on-active-directions function. Third, joint architecture-plus-optimizer tuning is the implied next experiment: pre-training a model with Delta Attention Residuals plus DynMuon would test whether the spectral-shaping gains and the residual-routing gains share an underlying mechanism or are orthogonal.

## Related wiki pages

- [Delta Attention Residuals (2026-05-20)](2026-05-20-delta-attention-residuals.md)
- [Lighthouse Attention pre-train wrapper (2026-05-16)](../inference-efficiency/2026-05-16-lighthouse-attention-long-context-pretraining.md)
