---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352558+05:30
arxiv_id: 2609.30840
url: https://huggingface.co/papers/2609.30840
arxiv_url: https://arxiv.org/abs/2609.30840
date: 2026-10-01
---

# Aligning One-Step Generative Models with Reward-Weighted Transport Distillation

One-step generators enable high-quality visual generation with a single network evaluation, but their post-training is difficult: general implicit generators provide neither tractable likelihoods nor denoising trajectories, and many rewards are non-differentiable. We introduce Reward-Weighted Transport Distillation (RWTD), a post-training method that requires only generated samples and scalar reward evaluations. Rather than aligning solely to the conventional reward-tilted reference distribution, RWTD constructs an adaptive target that mixes separately tilted current and reference distributions. The current component incorporates improvements discovered during training, while the reference component anchors the target to the pretrained generator. RWTD realizes this target through feature-space optimal transport and fixed-point regression. Theoretical analysis shows that the fixed-point distributions of RWTD interpolate between off-policy reward tilting of the reference and on-policy tilting of the current model, providing a principled approach to balancing reward adaptation with retention of prior knowledge. Empirically, RWTD substantially improves the GenEval score of the one-step SANA Sprint 1.6B backbone from 0.73 to 0.80, while separate preference alignment experiments demonstrate strong cross-reward generalization that yields balanced improvements and preservation of compositional capabilities.
