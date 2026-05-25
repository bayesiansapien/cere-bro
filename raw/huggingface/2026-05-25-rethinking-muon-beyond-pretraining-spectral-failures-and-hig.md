---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.19282
url: https://huggingface.co/papers/2605.19282
arxiv_url: https://arxiv.org/abs/2605.19282
date: 2026-05-25
---

# Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR

Muon is a matrix-aware optimizer that leverages Newton-Schulz (NS) iterations to enforce spectral gradient orthogonalization by driving all singular values of the momentum matrix toward 1. While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noisy tail directions, and (ii) reinforcement learning with verifiable rewards (RLVR), where low-SNR gradients and the need to preserve per-head specialization from prior training make whitening unstable. To address these challenges, we propose Pion, a drop-in replacement for Muon that preserves its computational efficiency while replacing uniform spectral whitening with a two-stage Promotion+Suppression mechanism, which we call the high-pass NS iteration. This design induces a sharp spectral high-pass effect, anchoring dominant singular values at 1 while suppressing noisy tail components toward 0, with controllable filter strength. To preserve pretrained per-head heterogeneity, Pion also supports a per-head mode that applies updates independently across attention heads via a simple reshape, at no extra cost. In VLA training on LIBERO and LIBERO-Plus, Pion consistently outperforms both baselines across l_1-regression (VLA-Adapter) and flow-matching (VLANeXt) architectures, e.g., reaching 100% success rate on LIBERO Object after 1,500 training steps with VLA-Adapter, vs. 97.0% for Muon and only 32.2% for AdamW. The advantage of Pion further extends to a real Franka Research 3 robot with a pi_0.5 backbone under the DROID setup on three grasp-and-place tasks. In RLVR post-training on Qwen3-1.7B/4B with GRPO and GMPO, Pion also outperforms AdamW on MATH and GSM8K while Muon collapses to zero.
