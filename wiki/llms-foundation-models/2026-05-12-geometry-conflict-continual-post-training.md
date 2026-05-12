# Geometry Conflict: Explaining and Controlling Forgetting in LLM Continual Post-Training

**Date:** 2026-05-12
**Source:** HuggingFace Daily Papers
**arXiv:** [2605.09608](https://arxiv.org/abs/2605.09608)
**Tier:** 2 — Continual learning / model merging / post-training

## TL;DR

The paper offers a geometric account of catastrophic forgetting in continual post-training. Each task is represented by its parameter update, and the covariance geometry of that update determines whether the next sequential update transfers or interferes. Central claim: forgetting is a *state-relative update-integration failure* that arises when the covariance geometry of a new task misaligns with the geometry of the evolving model state. The proposed method, **Geometry-Conflict Wasserstein Merging (GCWM)**, builds a shared Wasserstein metric via Gaussian Wasserstein barycenters and uses geometry conflict to gate geometry-aware correction. Data-free. Across Qwen3 0.6B-14B on domain-continual and capability-continual settings, GCWM consistently outperforms data-free baselines on retention and final performance.

## Why it matters

Continual post-training has been a benchmark game for two years (replay rates, regularization strengths, merging schemes) without a clean explanatory variable. Geometry conflict gives one: misalignment between the new task's update geometry and the current model state's geometry. That is both diagnostic (you can predict which tasks will interfere) and prescriptive (you can correct only the conflicting components). The method is data-free, which makes it deployable in continual pipelines that do not retain prior task data for privacy or storage reasons.

## How it relates to prior wiki state

- **Model Merging Scaling Laws (today).** The two papers attack the same empirical phenomenon from different ends. The scaling-laws paper observes that gains from merging fall roughly as 1/k and that the size-dependent floor decreases with model capacity. Geometry Conflict explains *why* additional experts deliver diminishing returns: as the model state accumulates updates, the probability of geometry conflict with the next task rises. Reading them together: the scaling law is the macroscopic shape, geometry conflict is the microscopic mechanism.
- **Weight Disentanglement / Task Arithmetic (2026-04-22).** That paper studied when task-vector arithmetic works. Geometry Conflict refines the answer in covariance terms: task vectors compose cleanly when their covariance geometries align with the current state. Disentanglement is a special case where geometries are nearly orthogonal.
- **TIDE (2026-05-09, every layer knows the token).** TIDE found that distillation signal is heterogeneous across layers. Geometry Conflict implies that update interference is also heterogeneous across layers (different layers have different covariance shapes). The two readings of layer-wise heterogeneity reinforce each other.
- **Distillation Panic (Lambert, 2026-05-04).** Lambert argued the field over-relied on distillation as a quick win. Geometry Conflict offers a principled axis for deciding *when* sequential updates are safe to merge versus when they will interfere, which is a stronger answer than "distill carefully."

## Research angle

Two open questions. First, does the geometry-conflict signal predict the *direction* of forgetting (which prior capability degrades), not just the magnitude? If yes, geometry-aware merging becomes targeted: the merge corrects the specific components that would otherwise lose. Second, the Gaussian Wasserstein barycenter is a strong distributional assumption. Real parameter-update distributions are heavy-tailed. The Wasserstein construction with non-Gaussian priors is the cleanest follow-up. Third (predictive): if geometry conflict generalizes, the next generation of continual-learning baselines should publish geometry-conflict scores as standard diagnostic output, the way calibration curves became standard in classification.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2605.09608)
- [HuggingFace page](https://huggingface.co/papers/2605.09608)
- Raw source: [raw/huggingface/2026-05-12-geometry-conflict-explaining-and-controlling-forgetting-in-l.md](../../raw/huggingface/2026-05-12-geometry-conflict-explaining-and-controlling-forgetting-in-l.md)

## Related wiki pages

- [Model Merging Scaling Laws](2026-05-12-model-merging-scaling-laws.md)
- [Weight Disentanglement / Task Arithmetic](2026-04-22-weight-disentanglement-task-arithmetic.md)
- [TIDE: every layer knows the token](2026-05-09-tide-every-layer-knows-token.md)
- [Distillation Panic (Lambert)](../inference-efficiency/2026-05-04-distillation-panic-lambert.md)
