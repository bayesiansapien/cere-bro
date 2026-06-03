# A Local Perturbation Theory for Cross-Domain Interference and Recovery in Multi-Domain RL

**Date:** 2026-06-03
**Source:** HuggingFace Daily Papers
**arXiv:** [2606.02398](https://arxiv.org/abs/2606.02398)
**Authors:** Lei Yang, Deyi Xiong (TJUNLP Lab, Tianjin University), Siyu Ding (Baidu)
**Tier:** 2 — Multi-domain RL, continual post-training, interference mechanism

## TL;DR

RL post-training lifts an LLM on one domain (math, code, QA, creative writing) but training on one domain usually drags down the others. The standard explanations — catastrophic forgetting, global gradient conflict — are incomplete: the paper shows substantial interference happens even when the full-model gradients are nearly orthogonal, so it cannot be a whole-model phenomenon. The real story is local. Single-domain RL makes sparse, small-magnitude edits with weak overlap among the top-changed neurons, yet different domains still share active *computation routes*, and on those shared routes the update direction decides whether two domains help or hurt each other. Under a local perturbation model, the paper proves later-domain training harms an earlier domain mainly through a second-order damage term that, given the sparse-route structure, concentrates in a low-dimensional shared conflict subspace. The payoff is recovery: a short domain refresh contracts the harmful component on that subspace. After Code→Math→QA→CW, a brief Re-Math refresh recovers Math from 57.66 to 66.04 while preserving the others (best average 66.39), and a training-free rollback on a sparse proxy conflict-coordinate set partially restores Math with no retraining.

```
Why orthogonal gradients still interfere:

  Domain A update ─┐         shared active route
  Domain B update ─┘────►  ┌──────────────────────┐
   (≈ orthogonal in        │ same neurons used by   │
    full param space)      │ both at inference time │
                           └──────────┬────────────┘
                                      ▼
            2nd-order damage term concentrates in a
            LOW-DIM shared conflict subspace
                                      │
            ┌─────────────────────────┴─────────────────────┐
            ▼                                                ▼
   short domain "refresh"                     training-free rollback on
   contracts harmful component                sparse proxy conflict coords
   (Math 57.66 → 66.04)                       (partial Math restore)
```

## Key findings

1. **Interference is local, not global.** It occurs even under near-orthogonal full-model gradients, so the explanatory variable is the shared active computation route, not the full gradient.
2. **Sparse small edits, shared routes.** Single-domain RL changes few neurons by small amounts with little overlap; the damage flows through routes both domains *use*, where update direction sets synergy vs conflict.
3. **A provable second-order damage term in a low-dim subspace.** The harm to an earlier domain concentrates in a low-dimensional shared conflict subspace, which is what makes targeted recovery feasible.
4. **Two recoveries.** A short domain refresh contracts the harmful component (Math 57.66→66.04, others preserved); a training-free rollback on a sparse proxy conflict-coordinate set partially restores the degraded domain with zero retraining.

## Relation to prior wiki state

This is the RL-side, mechanistic sibling of [Geometry Conflict](2026-05-12-geometry-conflict-continual-post-training.md) (05-12), which explained catastrophic forgetting in continual post-training as a covariance-geometry misalignment between a new task's update and the evolving model state, fixed by Wasserstein-barycenter merging. Both reject the global-gradient-conflict story; both localize the damage to a structured low-dimensional object (Geometry Conflict's covariance misalignment, Local Perturbation's shared conflict subspace). Read together they triangulate the same phenomenon from weight-space geometry and from active-route perturbation. [Model Merging Scaling Laws](2026-05-12-model-merging-scaling-laws.md) (05-12, gains from merging fall ~1/k with a capacity-dependent floor) is the macroscopic shape; Local Perturbation gives a mechanism for why each added domain interferes more.

It pairs directly with today's [MERIT](2026-06-03-merit-decentralized-instruction-tuning-merging.md), which attacks the *same* multi-domain interference but on the instruction-tuning / merging side: MERIT splits the data mixture along top PCA conflict axes and merges once, while Local Perturbation explains why the conflict lives in a low-dimensional subspace in the first place and offers a post-hoc rollback on it. The diagnosis (low-dim conflict subspace) and the prescription (split / refresh / rollback along it) are two halves of one story arriving the same day. It also extends the wiki's "operational targets are sparse and locatable" thread ([rl-for-llms](rl-for-llms.md)) from *where the signal is* to *where the damage is* — both turn out to be sparse and locatable.

## Research angle

1. **Predict the direction of forgetting, not just the magnitude.** If the conflict-subspace signal says *which* prior capability will degrade (as Geometry Conflict's open question also asked), recovery becomes targeted before training, not reactive after.
2. **Online conflict-coordinate monitoring.** The training-free rollback implies a sparse proxy coordinate set can be tracked cheaply. A controller that watches those coordinates during sequential training and applies micro-rollbacks online is the obvious extension.
3. **Unify with MERIT's PCA split.** MERIT's top PCA conflict axes and this paper's shared conflict subspace may be the same object. If so, a single subspace estimate could drive both the data split (MERIT) and the recovery rollback (here).

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2606.02398)
- [HuggingFace page](https://huggingface.co/papers/2606.02398)
- Raw: [raw/huggingface/2026-06-03-a-local-perturbation-theory-for-cross-domain-interference-an.md](../../raw/huggingface/2026-06-03-a-local-perturbation-theory-for-cross-domain-interference-an.md)
- Concept page: [RL for LLMs](rl-for-llms.md)
- Related: [Geometry Conflict 05-12](2026-05-12-geometry-conflict-continual-post-training.md) · [Model Merging Scaling Laws 05-12](2026-05-12-model-merging-scaling-laws.md) · [MERIT 06-03](2026-06-03-merit-decentralized-instruction-tuning-merging.md)
