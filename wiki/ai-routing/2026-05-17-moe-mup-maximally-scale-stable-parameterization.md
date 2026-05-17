# MoE-muP: How to Scale Mixture-of-Experts (From muP to the Maximally Scale-Stable Parameterization)

**Source:** Kurate cs.LG #13 weekly leaderboard (ai_rating 9.0/10, score=1611, win_rate=85.0%)
**Authors:** Leena Chennuru Vankadara, Moritz Haas, Luke Hayward, Sebastian Bordt, Alessandro Breccia (Gatsby UCL, Amazon, Tübingen)
**arxiv:** [2605.14200](https://arxiv.org/abs/2605.14200)
**Date:** 2026-05-13 (surfaced via Kurate on 2026-05-17)
**Raw:** none (Kurate-only; not in HuggingFace top this week)
**Tier:** 1 (routing, MoE scaling, hyperparameter transfer)

## TL;DR

Modern Mixture-of-Experts (MoE) models add three new scaling axes on top of the classical width and depth: the number of experts M, the per-expert width Ne, and the routing sparsity K (how many experts each token activates). The Maximal Update Parameterization (muP, Yang et al. 2022) makes hyperparameters transfer across width for dense models, but it breaks in subtle ways inside MoE because the router, expert update statistics, and active-parameter count are coupled and interact non-commutatively across the new axes. The authors derive, using muP and Dynamical Mean Field Theory (DMFT), a Maximally Scale-Stable Parameterization (MSSP) that holds feature dynamics, prediction dynamics, and learning-rate transfer invariant across the full combinatorial space of M, Ne, K, N, L co-scaling regimes. The result is the first scaling-law framework that applies to the actual architectures shipping in 2026: Kimi K2.6, DeepSeek V4, GLM-5.1, Gemma 4 26B-A4B, Qwen3.6-35B-A3B.

## Key findings

1. **muP is necessary but not sufficient for MoE.** Naively applying width-muP to the expert blocks leaves router gradients miscalibrated and active-parameter-count drift uncontrolled. The paper identifies which specific muP rules fail and which optimizer-state interactions cause the failure.
2. **Co-scaling is non-commutative.** Scaling M then Ne does not produce the same trained model as scaling Ne then M, even at matched FLOPs. The combinatorial space of co-scaling regimes has distinct fixed points, and the right hyperparameter prescription depends on the regime.
3. **MSSP prescriptions are derived in closed form.** Initialization variance, learning rate, weight decay, and routing-temperature schedules are given as explicit functions of (M, Ne, K, N, L). Empirically the prescription holds across optimizers (the paper covers SGD, Adam, and Adafactor families) rather than being tied to one.
4. **Concurrent work (Jiang et al. 2026) is narrower.** The paper distinguishes itself from a concurrent MoE-muP proposal by covering a broader set of optimizers and by repairing specific muP shortcomings in MoEs that the concurrent paper does not address.

## Relation to prior wiki state

This paper does two things at once for the wiki's running threads.

**It is the theoretical complement to the BEAM thread (05-16).** BEAM ([summary](../ai-routing/2026-05-16-beam-binary-expert-activation-masking-moe.md)) reframed per-token K from a fixed serving-time constant into a learned binary mask. MoE-muP makes the orthogonal move: it asks how K, the average active count, should be scaled with M and Ne to keep the training dynamics well-defined as the model gets bigger. BEAM optimizes K within a fixed scale; MoE-muP makes the scale itself principled. Together they remove two of the three load-bearing arbitrary choices in MoE training (the fixed top-K rule and the per-axis tuning of hyperparameters); the third (expert assignment regularization) remains an open axis.

**It is the foundational layer under the open-model wave that landed this weekend.** Sebastian Raschka's Gmail-starred 05-17 post (Recent Developments in LLM Architectures, [raw/gmail/2026-05-17-starred.md](../../raw/gmail/2026-05-17-starred.md)) catalogs the architectural diversity now shipping: Gemma 4's KV sharing plus per-layer embeddings, Laguna XS.2's layer-wise attention budgeting, ZAYA1-8B's compressed convolutional attention, DeepSeek V4's mHC and compressed attention. Every one of those models is a MoE. The fact that the four labs converged on similar architectural patterns despite no public scaling theory for MoEs to guide them is itself evidence the field has been operating on folk knowledge. MoE-muP is the first paper that lets a new lab choose those hyperparameters in advance rather than by expensive empirical sweep.

**It addresses LLMs Gaming Verifiers (Kurate cs.LG #10, ai_rating 6.8, 04-16) from the other side.** That paper showed RLVR breaks when scale changes the verifier's leverage. MoE-muP gives the upstream tool: if training dynamics are scale-invariant, the verifier-policy game has predictable transfer properties.

## Why it matters

Frontier MoE pre-training runs cost tens of millions of dollars. Each hyperparameter sweep that has to be re-run at the target scale is most of that budget. muP for dense models cut the sweep cost by an order of magnitude. MoE-muP extends that economic logic to the architecture every frontier lab is actually shipping. If the closed-form prescription transfers cleanly to ZAYA1-class and DeepSeek-V4-class training runs, the next generation of MoEs will be tuned at 1B and trained at 1T with no re-sweep. The most likely test is a public proxy-scale sweep + extrapolation paper from a frontier lab in the next 60-90 days.

## Research angle

1. **MoE-muP + BEAM joint formulation.** BEAM trains a per-token binary mask under a fixed expected K. MoE-muP prescribes how to scale the expected K with M and Ne. The composition is unwritten: a BEAM-trained model where the average mask count follows the MoE-muP schedule across scales. Falsifiable: a paper reporting both (a) BEAM-style 98%+ retention and (b) MoE-muP-style hyperparameter transfer across a 10-100x scale jump on the same backbone family.
2. **MoE-muP for routing-temperature schedules.** The paper covers routing temperature; whether the prescribed schedule matches what frontier labs empirically chose (e.g. Kimi K2.6's published recipe, when it surfaces) is the easiest empirical falsifier.
3. **MoE-muP under hybrid attention.** Modern MoEs increasingly mix softmax with linear, sliding-window, or compressed-convolutional attention (the Raschka catalog). Whether the paper's MSSP holds under hybrid attention is unaddressed in the current draft.
4. **MSSP for muTransfer-with-RL.** If MoE-muP makes pre-training scale-invariant, the natural next question is whether the same DMFT machinery lets RLVR hyperparameters transfer across the same axes. Untested.

## Links

- [Paper](https://arxiv.org/abs/2605.14200)
- Raw Kurate entry: [raw/kurate/2026-05-17-cs-lg.md](../../raw/kurate/2026-05-17-cs-lg.md)
- Related: [BEAM 2026-05-16](2026-05-16-beam-binary-expert-activation-masking-moe.md), [DLR 2026-05-15](2026-05-15-dlr-dynamic-latent-routing-post-training.md), Gemma 4 / DeepSeek V4 architectures (Raschka, 05-17 Gmail): [raw/gmail/2026-05-17-starred.md](../../raw/gmail/2026-05-17-starred.md)
- Concept page: [LLM routing](llm-routing.md)
