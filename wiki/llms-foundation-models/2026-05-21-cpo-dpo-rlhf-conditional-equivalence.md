# CPO: Conditional Equivalence of DPO and RLHF, and a Provable-Alignment Fix

**Source:** HuggingFace Daily Papers 2026-05-21 · arXiv 2605.20834 · [paper](https://arxiv.org/abs/2605.20834) · [raw](../../raw/huggingface/2026-05-21-conditional-equivalence-of-dpo-and-rlhf-implicit-assumption.md)
**Topic:** llms / alignment / RLHF

## TL;DR

DPO (Direct Preference Optimization) was sold as theoretically equivalent to RLHF with a simpler implementation. The paper proves the equivalence is conditional: it holds only under an implicit assumption that is frequently violated in practice, namely that the RLHF-optimal policy must prefer the human-preferred response. When the assumption fails, DPO optimizes relative advantage over the reference policy rather than absolute alignment with human preferences, leading to pathological convergence where policies decrease DPO loss while preferring the dispreferred response. Constrained Preference Optimization (CPO) augments RLHF with explicit constraints to restore provable alignment.

## What is new

The result clears up two years of "why does DPO sometimes go wrong" empirical reports. The failure mode is named precisely: DPO is a soft-margin ranking with potentially negative target margins, which means the optimum can be a policy that ranks the dispreferred response above the preferred one as long as the relative advantage over the reference policy goes the right way. The geometric interpretation through soft-margin ranking is the cleanest description of DPO's failure boundary the wiki has seen.

CPO restores provable alignment by adding explicit constraints to RLHF that force the policy to prefer the human-preferred response (the assumption DPO implicitly relies on but does not enforce). The implementation cost is the constraint enforcement; the theoretical gain is provable alignment with human preferences rather than conditional alignment with the reference policy's preferences.

## Why it matters

The DPO-versus-RLHF debate has dominated alignment infrastructure choices since 2024. Many production stacks moved to DPO for the simplicity. The paper is a structured warning that the simplicity was the cost: DPO's implementation simplicity hides an alignment-correctness assumption that production systems do not enforce. CPO offers a path that keeps the implementation tractable while restoring the alignment guarantee.

The conditional-equivalence framing is the more transferable contribution. Any future "X is equivalent to Y under simpler implementation" claim now has a test to apply: what is the implicit assumption that makes the equivalence work, and is it enforced in the simpler implementation?

## Research angle

Three threads. First, CPO's constraints reintroduce some of the complexity DPO was selected to avoid; the question is whether the constraint set can be enforced at near-DPO-implementation cost via projection or Lagrangian methods. Second, the conditional-equivalence framing should be applied to other "simpler-alternative" claims in alignment: GRPO versus PPO, RLOO versus full PPO, DAPO versus GRPO. Each has a similar pattern (drop the simulation, drop the value model, drop the clipping) and each implicitly assumes something the production setup may not enforce. Third, this composes with today's RELEX result that RLVR is rank-1 extrapolation along a fixed direction: if the direction is wrong (in DPO's case, optimizing relative advantage instead of absolute alignment), all the extrapolation does is walk further in the wrong direction faster.

## Related wiki pages

- [RELEX rank-1 RLVR extrapolation (2026-05-21)](2026-05-21-relex-rank1-rlvr-extrapolation.md)
- [Unlearnability RLVR (2026-05-21)](2026-05-21-unlearnability-rlvr.md)
- [AntiSD (2026-05-20)](2026-05-20-antisd-anti-self-distillation-pmi-divergence-ascent.md)
