# The Unlearnability Phenomenon in RLVR for Language Models

**Source:** HuggingFace Daily Papers 2026-05-21 · arXiv 2605.16787 · [paper](https://arxiv.org/abs/2605.16787) · [raw](../../raw/huggingface/2026-05-21-the-unlearnability-phenomenon-in-rlvr-for-language-models.md)
**Topic:** llms / RLVR / reasoning
**Authors:** Yulin Chen, He He, Chen Zhao (NYU, NYU Shanghai)

## TL;DR

Among hard examples a model initially fails on, a substantial subset stays unlearnable under RLVR even when correct rollouts (sequences of actions leading to a correct answer) are present in the training batch. Existing optimization tricks (clipped higher gradients, removing KL penalties for exploration, entropy adjustments, finer credit assignment) and sampling tricks (dynamic sampling, curriculum learning) do not resolve unlearnability. Cross-example gradient analysis shows unlearnable examples have a fundamental representation issue: low gradient similarity with the rest of the examples, and ungeneralizable reasoning patterns. Data augmentation does not improve gradient similarity, so the failure is representational rather than optimization-driven.

## What is new

The implicit assumption underlying RLVR pipeline design has been: presence of positive reward implies learning. The paper invalidates that assumption empirically. The diagnostic move is cross-example gradient similarity. If example X has a gradient that does not point in a similar direction to the gradients of examples the model has already learned, the gradient updates for X cannot find anchor representations, and X stays unlearnable. Data augmentation cannot rescue this because augmentation does not change the underlying representation; if the representation is wrong, more variations of the same wrong representation do not help.

This is the first systematic characterization the wiki tracks of unlearnable data in RLVR training as a representation phenomenon, distinct from sparse-reward issues (the Sparse-to-Dense thread), from credit-assignment issues (AntiSD, CEPO), and from exploration issues (the DAPO line).

## Why it matters

The composition with RELEX (today's companion paper) is the load-bearing claim. RELEX shows that on examples RLVR helps, the direction of help is fixed in the first 15% of training and the rest is extrapolation along a rank-1 trajectory. Unlearnability shows that on examples RLVR does not help, even more rollouts and better optimization will not help, because the representation is wrong. Together: RLVR is a thin amplifier on top of a fixed pre-trained representation. The capabilities it can produce are bounded by what the pre-trained representation can grow into, in the direction the pre-trained representation already points.

For deployment economics this changes the question. If you cannot grow new capabilities via RLVR, then the bottleneck becomes pre-training data and curriculum, not the RLVR setup. The PreRL line (2026-04-16, RL inside the pre-training space) and Bitter Lesson for Data Filtering (2026-05-19, on the limits of data filtering at scale) become the foreground.

## Research angle

The diagnostic is gradient similarity. Three follow-on threads. First, can the gradient-similarity test be applied at inference time, before RLVR training even starts, to predict which hard examples are worth including in the rollout set? If yes, RLVR rollout budgets can be allocated only to examples whose gradients point in a usable direction. Second, if unlearnable examples need a representation change, the question becomes: what is the smallest pre-training change that converts an unlearnable example into a learnable one? Three candidate axes: more pre-train tokens with related concepts, targeted SFT on related solutions before RLVR, or representation engineering (steering vectors) at RLVR rollout time. Third, the unlearnability characterization gives the wiki the first principled answer to why some hard math problems remain unsolved after RLVR runs longer than they were ever supposed to. The "we just need more compute" framing has empirical pushback.

## Related wiki pages

- [RELEX rank-1 RLVR extrapolation (2026-05-21)](2026-05-21-relex-rank1-rlvr-extrapolation.md)
- [AntiSD (2026-05-20)](2026-05-20-antisd-anti-self-distillation-pmi-divergence-ascent.md)
- [PreRL: RL in pre-train space (2026-04-16)](2026-04-16-prerl-rl-in-pretrain-space.md)
- [RLVR weak supervision / reasoning faithfulness (2026-04-21)](2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md)
