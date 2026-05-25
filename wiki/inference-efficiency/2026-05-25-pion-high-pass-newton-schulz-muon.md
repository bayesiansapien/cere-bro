# Pion: high-pass Newton-Schulz iteration as a Muon drop-in for VLA and RLVR

**arxiv:** [2605.19282](https://arxiv.org/abs/2605.19282) · **HF:** [papers/2605.19282](https://huggingface.co/papers/2605.19282) · **Raw:** [farmed](../../raw/huggingface/2026-05-25-rethinking-muon-beyond-pretraining-spectral-failures-and-hig.md)

## TL;DR

Muon is the matrix-aware optimizer that uses Newton-Schulz iterations to drive every singular value of the momentum matrix toward 1, achieving uniform spectral whitening. That choice is what makes Muon outperform AdamW on LLM pretraining. The authors show that uniform whitening fails in two regimes: vision-language-action (VLA) training, where action-module gradients are inherently low-rank and uniform whitening amplifies noisy tail singular vectors; and reinforcement learning with verifiable rewards (RLVR), where gradients are low-SNR and per-head specialization from prior training must be preserved. Pion is a drop-in replacement that anchors dominant singular values at 1 and suppresses noisy tail components toward 0 (a spectral high-pass), with controllable filter strength. On LIBERO Object with the VLA-Adapter backbone, Pion reaches 100% success after 1500 steps versus 97.0% for Muon and 32.2% for AdamW. On Qwen3-1.7B/4B RLVR with GRPO/GMPO, Pion outperforms AdamW on MATH and GSM8K while Muon collapses to zero.

## Why this matters

Muon was the optimizer story of 2026. The Same Architecture Different Capacity paper from 2026-05-23 ([2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md](../llms-foundation-models/2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md), which showed Muon achieves linear hard-rank scaling beta=1.02 versus AdamW's beta=0.44 on rare-token representations) established that optimizer choice changes effective spectral capacity, not just convergence speed. Pion now establishes the second-order result: the spectral *shape* matters too. Uniform whitening expands the rank-1 ceiling but injects noise into low-SNR regimes. A high-pass spectral filter preserves the rank benefit while suppressing the noise. This is the first paper to show Muon failing in a recognized post-training regime, and to propose the principled fix.

The per-head mode is the second important contribution. Pion supports an optional reshape that runs the high-pass independently per attention head, at no extra cost. The motivation is that pretrained models have head-level functional specialization, and applying a global spectral filter across all heads averages out that structure. The per-head mode preserves it. This makes Pion the first optimizer with explicit recognition that post-training is qualitatively different from pretraining and needs preserved-heterogeneity-aware updates.

## Where this fits

This connects directly to two prior threads:

- The optimizer-spectral-capacity finding ([2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md](../llms-foundation-models/2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md)) said matched loss does not imply matched representation. Pion says matched optimizer family does not imply matched spectral behavior across regimes. Together they argue that optimizer-architecture-regime is a three-way design choice.
- The MoE muP paper ([2026-05-17-moe-mup-maximally-scale-stable-parameterization.md](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md), which derived scale-stable parameterization so width and expert count compose without retuning) is the structural analog. Both papers say there is one parameterization that works at the pretraining regime, and a different one is needed once you scale or specialize. Pion adds the time dimension: the post-training regime is qualitatively different.

## Open research angles

- Pion is evaluated on Qwen3-1.7B/4B. Whether the spectral high-pass remains effective at 30B+ for RLVR (where most production RL post-training happens) is an open question.
- The interaction between Pion and the per-head MoE setting is not tested. If a model has both attention heads and expert heads to preserve, does the reshape generalize cleanly?
- Pion's filter strength is a hyperparameter. Whether a learned filter strength (per layer, per head, per training step) outperforms a fixed one is the obvious next step.

## Industrial implication

Production post-training (RLHF, RLVR, VLA fine-tuning) almost universally uses AdamW. Muon's pretraining win was supposed to migrate to post-training. Pion shows that direct migration fails and provides the fix. Frontier labs running Muon for pretraining now have a path to keep the optimizer family across the entire stack — pretrain with Muon, post-train with Pion — without paying the noise-amplification cost.
