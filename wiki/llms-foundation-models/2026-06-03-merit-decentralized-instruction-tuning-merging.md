# MERIT: Decentralized Instruction Tuning — Conflict-Aware Splitting and Weight Merging

**Date:** 2026-06-03
**Source:** HuggingFace Daily Papers
**arXiv:** [2606.01717](https://arxiv.org/abs/2606.01717) · code: [naver-ai/merit](https://github.com/naver-ai/merit)
**Tier:** 2 — Instruction tuning, model merging, decentralized training

## TL;DR

Instruction tuning aligns LLMs (including multimodal ones) to many user intents, but scaling to heterogeneous data mixtures hits two walls at once: gradient interference between dissimilar tasks, and bandwidth-heavy synchronization across compute. MERIT asks whether both can be solved together by training parts of the mixture *independently* and reconciling them once in parameter space. A local quadratic theory inside a shared flat loss basin yields three results: weight merging gives a curvature-weighted variance reduction; splitting the mixture along the top PCA conflict axes maximizes that gain along high-curvature directions; and merging additionally acts as spectral filtering with implicit norm regularization. The recipe: estimate dataset-level gradient conflicts, partition the mixture along the top PCA conflict axes, fine-tune each partition independently with zero inter-partition communication, then merge once via token-weighted averaging. On Qwen2.5-VL-3B with 136 Vision-FLAN tasks it lifts the 8-benchmark average from 54.3 (joint training) to 57.0; the same recipe scales to a 7B model on a 1.6M-example, 176-source mixture, matching or beating centralized joint training at minimal overhead, and transfers to text-only FLAN.

```
heterogeneous instruction mixture
        │
        ▼  estimate dataset-level gradient conflicts
   PCA conflict axes ─► partition mixture
        │
   ┌────┴────┬─────────┬──────────┐
   ▼         ▼         ▼          ▼
 part 1    part 2   part 3   …  part k     (fine-tune INDEPENDENTLY,
   │         │         │          │          no inter-partition comms)
   └────┬────┴────┬────┴────┬─────┘
        ▼ merge ONCE via token-weighted averaging
   = curvature-weighted variance reduction
     + spectral filtering / implicit norm regularization
```

## Key findings

1. **One move, two bottlenecks.** Conflict-aware splitting plus single merge attacks gradient interference *and* synchronization bandwidth together, rather than treating them as separate problems.
2. **Theory inside a shared flat basin.** Merging = curvature-weighted variance reduction; PCA-aligned conflict splitting maximizes the gain along high-curvature directions; merging also spectrally filters and implicitly regularizes the norm.
3. **Beats joint training.** 54.3 → 57.0 on the 8-benchmark Vision-FLAN average at 3B; scales to 7B on a 1.6M-example, 176-source mixture, matching or exceeding centralized joint training; transfers to text-only FLAN.
4. **Communication-free fine-tuning.** Each partition trains with no cross-partition communication, which is the property that makes it decentralized and cheap.

## Relation to prior wiki state

MERIT and today's [Local Perturbation Theory for multi-domain RL](2026-06-03-local-perturbation-multi-domain-rl-interference.md) are a same-day pair on the same disease — cross-task interference — from opposite ends. Local Perturbation explains *why* the conflict concentrates in a low-dimensional shared subspace (active-route second-order damage); MERIT *uses* a low-dimensional conflict structure (top PCA axes) to split data so the independent fine-tunes do not collide, then merges. The shared-conflict-subspace (Local Perturbation) and top-PCA-conflict-axes (MERIT) may literally be the same object, which is the cleanest unification the day offers.

It extends the wiki's model-merging line. [Model Merging Scaling Laws](2026-05-12-model-merging-scaling-laws.md) (05-12) found merging gains fall ~1/k with a capacity-dependent floor; [Geometry Conflict / GCWM](2026-05-12-geometry-conflict-continual-post-training.md) (05-12) merged via Wasserstein barycenters using covariance geometry; [Weight Disentanglement / Task Arithmetic](2026-04-22-weight-disentanglement-task-arithmetic.md) (04-22) studied when task vectors compose; [Darwin evolutionary merging](2026-05-15-darwin-family-evolutionary-merging.md) (05-15) searched merge configurations. MERIT's contribution is to make the *split* conflict-aware before the merge, with a curvature-variance-reduction account of why merging helps. It is also a decentralized-training story (independent partitions, single merge), which connects to the broader efficiency thread of removing synchronization cost.

## Research angle

1. **Is MERIT's PCA conflict axis the same as Local Perturbation's conflict subspace?** A single estimate of the cross-task conflict subspace could drive the MERIT split and a Local-Perturbation-style rollback for recovery. Testing whether the two subspaces coincide is the obvious experiment.
2. **Conflict-aware split for RL, not just SFT.** MERIT is instruction tuning. Whether the same PCA-conflict split stabilizes parallel multi-domain *RL* (the MAI-Thinking-1 split-then-merge setting) is unexplored.
3. **Dynamic re-partition.** The split is computed once. As the model state evolves the conflict geometry shifts (per Geometry Conflict), so a re-partition schedule could recover the gains a static split leaves on the table.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2606.01717) · [code](https://github.com/naver-ai/merit)
- [HuggingFace page](https://huggingface.co/papers/2606.01717)
- Raw: [raw/huggingface/2026-06-03-decentralized-instruction-tuning-conflict-aware-splitting-an.md](../../raw/huggingface/2026-06-03-decentralized-instruction-tuning-conflict-aware-splitting-an.md)
- Concept page: [RL for LLMs](rl-for-llms.md)
- Related: [Local Perturbation Theory 06-03](2026-06-03-local-perturbation-multi-domain-rl-interference.md) · [Model Merging Scaling Laws 05-12](2026-05-12-model-merging-scaling-laws.md) · [Geometry Conflict 05-12](2026-05-12-geometry-conflict-continual-post-training.md)
