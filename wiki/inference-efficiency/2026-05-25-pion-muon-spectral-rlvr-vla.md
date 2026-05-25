# Pion: a high-pass replacement for Muon outside pretraining

**arXiv:** [2605.19282](https://arxiv.org/abs/2605.19282) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.19282) · **Date:** 2026-05-25
**Authors:** Chongyu Fan, Gaowen Liu, Mingyi Hong, Ramana Rao Kompella, Sijia Liu (Michigan State, Cisco, U. Minnesota, IBM Research)
**Raw:** [farmer file](../../raw/huggingface/2026-05-25-rethinking-muon-beyond-pretraining-spectral-failures-and-hig.md)

## TL;DR

Muon, the matrix-aware optimizer that uses Newton-Schulz iterations to drive every singular value of the momentum matrix toward one, beats AdamW on LLM pretraining but collapses in two important regimes outside pretraining: vision-language-action (VLA) fine-tuning and reinforcement learning with verifiable rewards (RLVR). The cause is the uniform whitening itself. It amplifies noise in low-rank gradients and destroys per-head specialization from prior training. Pion replaces the uniform whitening with a high-pass two-stage Promotion+Suppression step (anchor dominant singular values at 1, drive noisy tail to 0) and adds a per-head mode. On LIBERO Object with VLA-Adapter, Pion reaches 100 percent success at 1500 steps where Muon plateaus at 97.0 percent and AdamW at 32.2 percent. On Qwen3-1.7B/4B RLVR with GRPO/GMPO, Muon collapses to zero accuracy while Pion outperforms AdamW.

```
Newton-Schulz applied to momentum singular values:

  Muon (uniform whitening)             Pion (high-pass two-stage)

   σ_i ─────► 1.0  for all i           top-k σ_i ──Promotion──► 1.0
                                       tail σ_i ──Suppression─► 0.0
   amplifies noisy tail                tunable filter strength
   collapses on low-rank /
   low-SNR gradients                   ┌──────────────────────────────┐
                                       │ Per-head mode: reshape only, │
                                       │ no extra cost, preserves     │
                                       │ pretraining specialization   │
                                       └──────────────────────────────┘

  LIBERO Object @ 1500 steps:  Pion 100 pct │ Muon 97.0 pct │ AdamW 32.2 pct
```

## Key claims

- Muon's uniform spectral whitening, while a strength on full-rank pretraining gradients, becomes the failure mode when gradients are intrinsically low-rank (VLA action heads) or low-SNR (RLVR rollouts). Pushing all singular values to 1 amplifies the tail directions, which are pure noise in those regimes.
- The high-pass Newton-Schulz iteration is the diagnostic-and-fix in one move: Promotion drives the top singular values to 1; Suppression drives the tail toward 0. Filter strength is a tunable knob, so Pion can recover Muon's behavior when uniformity actually is desirable.
- Per-head mode applies updates independently across attention heads by a simple reshape, preserving the per-head specialization that pretraining built. This is critical for RLVR, where uniform whitening across heads erases the structure that the policy depends on.
- Empirically: VLA-Adapter on LIBERO Object reaches 100 percent at 1500 steps (Muon 97.0, AdamW 32.2). On a real Franka Research 3 robot with a pi_0.5 backbone, Pion outperforms both baselines across three grasp-and-place tasks. On RLVR with Qwen3-1.7B/4B and GRPO/GMPO on MATH and GSM8K, Pion outperforms AdamW where Muon collapses to zero.
- Computational cost is comparable to Muon; this is a drop-in.

## Relation to prior wiki content

Pion is the third paper in two weeks pointing at the same conclusion: optimizer choice is load-bearing for post-training, and the spectral geometry of gradients is the right design surface. The 2026-05-23 [Same Architecture, optimizer-induced spectral scaling](../llms-foundation-models/2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md) paper showed Muon achieves linear hard-rank scaling beta=1.02 on rare-token representations versus AdamW's beta=0.44 in pretraining. Pion says that same uniform-whitening mechanism becomes a liability the moment gradient geometry changes, which is exactly what happens between pretraining and RLVR or VLA. The two findings are consistent: uniform whitening is the right policy when gradients are full-rank and high-SNR, the wrong policy otherwise.

This is also the first paper to give a clean account of *why* RLVR post-training has been so brittle to optimizer choice. The community has been treating GRPO/GMPO collapse as a hyperparameter problem; Pion reframes it as a spectral mismatch between Muon's update geometry and RLVR's gradient distribution.

## Research angle

The biggest open question Pion raises is whether the high-pass mechanism generalizes to other low-SNR regimes: preference optimization, reward-model training, contrastive losses with hard-negative mining. If the failure mode is genuinely "uniform whitening + low-SNR gradients = noise amplification," then the same fix should help everywhere those two conditions co-occur. Worth a controlled study.

Second: the per-head mode is the obvious lever for MoE training, where each expert is its own specialized subspace and uniform whitening across experts would be even more destructive than across attention heads. The paper does not test MoE; this is the natural next experiment. Connects to the [MoE muP scaling](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md) work, where parameterization, not optimizer, was the failure surface.
