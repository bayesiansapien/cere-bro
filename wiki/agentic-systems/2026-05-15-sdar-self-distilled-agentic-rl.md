# SDAR: Self-Distilled Agentic Reinforcement Learning

**Source:** [HuggingFace Daily Papers](https://huggingface.co/papers/2605.15155) · [arXiv 2605.15155](https://arxiv.org/abs/2605.15155)
**Date ingested:** 2026-05-15
**Tier:** 2. Multi-turn agent RL, on-policy self-distillation, post-training stability
**Raw:** [farmer file](../../raw/huggingface/2026-05-15-self-distilled-agentic-reinforcement-learning.md)

## TL;DR

RL post-training for agents uses trajectory-level rewards, which is coarse supervision for long-horizon multi-turn interaction. On-Policy Self-Distillation (OPSD) helps by adding dense token-level supervision from a teacher with privileged context, but transferring it to multi-turn agents is unstable: compounding errors across turns destabilize the supervision, and skill-conditioned privileged guidance requires asymmetric treatment for negative teacher rejections. SDAR treats OPSD as a gated auxiliary objective: a sigmoid gate over detached token-level signals strengthens distillation on teacher-endorsed positive-gap tokens and softly attenuates negative teacher rejections, while RL remains the primary optimization backbone. On the Qwen2.5 and Qwen3 families across ALFWorld, WebShop, Search-QA: **+9.4% ALFWorld, +7.0% Search-QA, +10.2% WebShop-Acc over GRPO**, and it avoids the instability of naive GRPO+OPSD.

## What's new

Two ideas.

**Gated OPSD.** The token-level signal from the teacher branch is multiplied by a sigmoid gate over the policy-teacher gap. Positive-gap tokens (teacher confident, student wrong) get strong distillation; negative-gap tokens (teacher rejected, student already correct, or teacher might be wrong) get attenuated. The gate is detached so it does not introduce additional gradient pathways.

**RL primary, OPSD auxiliary.** Naive GRPO+OPSD treats the two objectives equally and destabilizes. SDAR keeps RL as the primary backbone (the trajectory-level reward is the signal that matters) and uses OPSD only as gated dense feedback on the way to that reward. This is the same architectural pattern as the [Extrapolation Cliff](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md): selective use of the dense teacher signal, gated by a structural quantity.

## Why this matters

SDAR is the multi-turn agent version of the dense-vs-sparse signal thread the wiki has been tracking on the distillation side. [TIP](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md) said only 10% of distillation tokens carry signal. [LongAct](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md) said sparse RL updates dominate dense. [The Extrapolation Cliff](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md) gave a closed form for when dense distillation breaks. SDAR is the structurally same prescription applied to multi-turn agents: gate the dense signal by a learned-or-derived quantity.

The 9-10% gains over GRPO are practical headline numbers, but the more interesting result is that SDAR *avoids the instability* of naive GRPO+OPSD. Naive composition of two strong post-training methods often blows up; the gate is what makes the composition stable. That stability result generalizes.

## Connections to prior wiki pages

- [The Extrapolation Cliff](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md) — yesterday. Closed-form clip-safety threshold for OPD with structured outputs. SDAR is the multi-turn agent analogue with a learned gate. The Cliff says "above λ-star, format collapses;" SDAR says "for tokens above the policy-teacher gap threshold, attenuate." Same shape of prescription.
- [TIP](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md) — selective distillation: 10% of tokens. SDAR is the multi-turn version.
- [LongAct](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md) — sparse RL updates dominate dense. SDAR is the multi-turn corroboration.
- [DAgger for LLM agents](2026-05-14-dagger-llm-agents.md) — yesterday. DAgger interpolates student-teacher trajectories at the turn level. SDAR gates per-token distillation within a trajectory. Two papers in two days on selective supervision for multi-turn agents.
- [G-Zero](../llms-foundation-models/2026-05-12-g-zero-verifier-free-self-play.md) — formal bound for verifier-free self-play. SDAR's gating mechanism deserves the same kind of theoretical analysis.

## Research angle

1. **Online λ-star scheduler + SDAR gate.** The Cliff gives a closed-form for OPD; SDAR uses a learned gate for multi-turn OPSD. The natural composition: derive a closed-form gate from the Cliff's three observables (p, b, c) extended to multi-turn settings. This is a one-paper rewrite.
2. **Gate-as-routing-signal.** If positive-gap tokens are where dense supervision helps, the gate signal can drive routing decisions across teacher models in a fleet.
3. **SDAR composed with EvoEnv.** EvoEnv constructs environments with solve-verify asymmetry; SDAR trains agents with gated OPSD. Combining the environment-construction loop with the gated post-training is the natural next experiment.

## Why it matters

The agent RL recipe is starting to converge. Multi-turn agents need (a) selective per-token supervision (SDAR), (b) stable verifiable environments (EvoEnv), (c) credit-assigned trajectory pools (Orchard), (d) honest evaluation (WildClawBench). Four pieces; they all dropped in one batch.

## Links

- [Paper](https://arxiv.org/abs/2605.15155)
- [HuggingFace](https://huggingface.co/papers/2605.15155)
- [Raw farmer file](../../raw/huggingface/2026-05-15-self-distilled-agentic-reinforcement-learning.md)
- Related: [Extrapolation Cliff](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md), [DAgger](2026-05-14-dagger-llm-agents.md), [TIP](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md), [LongAct](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md)
