# How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization

**Source:** Kurate cs.LG leaderboard #14, week of 2026-05-22. ai_rating 9.0/10 (highest in the week's cs.LG list). Published 2026-05-13.
**Authors:** Leena Chennuru Vankadara, Moritz Haas, Luke Hayward, Sebastian Bordt, Alessandro Breccia.
**Arxiv:** [2605.14200v1](http://arxiv.org/abs/2605.14200v1)

## TL;DR

This paper extends the maximal-update parameterization (muP) story to Mixture-of-Experts. The original muP framework, which lets you tune hyperparameters at small scale and have them transfer to large scale, was derived for dense networks. Applying it naively to MoE breaks down because the effective per-token width depends on the active expert count, not the total expert count. The "Maximally Scale-Stable Parameterization" derived in this paper gives the corrected scaling rules that hold under both width-scaling and expert-count-scaling, and shows empirically that learning rates transfer across both axes without retuning.

## Why this is a Tier 1 result

This is the cleanest mathematical statement of how to scale MoE responsibly that the wiki has tracked since the Switch Transformer / GShard era. Two specific contributions:

1. **Identifies the failure mode of naive muP in MoE.** The effective width depends on the activation pattern, not the parameter count, so a dense-network muP recipe applied to a 30B-A3B (3B active out of 30B) network behaves more like a 3B-equivalent muP than a 30B-equivalent. Vankadara et al. derive the correction.

2. **Gives an empirical recipe.** The paper claims learning rates tuned at small (e.g., 1.3B active) transfer to large (e.g., 70B-active or beyond) without retuning, across width and expert-count axes jointly. This is the practical lever: it removes a brittle and expensive hyperparameter search from the MoE training loop.

## Connections to the wiki

- The recurring 10% activation ratio across DeepSeek-V3/V4, Qwen3.6-A3B, and now Tencent Hy-MT2-30B-A3B (covered today, [2026-05-21](2026-05-21-tencent-hy-mt2-translation-quantization.md)) has been an empirical choice. If muP-MoE gives principled reasons why a particular activation ratio is scale-stable, then 10% may not be the optimal ratio, it may be a local minimum the field has settled on because they did not have the scaling recipe to explore alternatives without retuning.
- This complements the [TIP token-importance on-policy distillation work (2026-04-16)](2026-04-16-tip-token-importance-on-policy-distillation.md) which addressed where to concentrate learning signal at the token level. muP-MoE addresses where to concentrate parameter capacity across experts.
- Connects to the broader RLVR / DPO / RLHF stability story (see [DPO/RLHF conditional equivalence paper](../llms-foundation-models/2026-05-21-dpo-rlhf-conditional-equivalence.md) on the same week's Kurate). Scale-stable parameterization is the orthogonal axis: the optimization landscape is stable across model scale separately from whether the loss function is well-posed.

## Open questions

- Does the maximally scale-stable parameterization hold when expert routing is auxiliary-loss-free (e.g., DeepSeekMoE-style)?
- What happens at extreme sparsity (1% activation, e.g., a 100B-A1B model)? The dense-network muP regime stops being a good zeroth-order approximation.
- Inference-time consequence: do the scale-stable training-time parameters also produce inference-time-friendly expert utilization? Or does the scheme prioritize training stability at the expense of unbalanced runtime expert loads?

## Industrial implication

If muP-MoE delivers as advertised, the cost of training a frontier-class MoE drops measurably: hyperparameter search is the second-largest cost component after raw compute, and a transferable-recipe paper eliminates much of it. This is one of the few Tier 1 results in May 2026 that materially changes the cost frontier of training a new MoE, not just running one. Expect to see ablations and reproductions across the next 60 days.

## Cross-references

- [Tencent Hy-MT2 30B-A3B (2026-05-21)](2026-05-21-tencent-hy-mt2-translation-quantization.md)
- [TIP token-importance on-policy distillation (2026-04-16)](2026-04-16-tip-token-importance-on-policy-distillation.md)
- [DPO/RLHF conditional equivalence (Kurate cs.AI #18, 2026-05-20)](../llms-foundation-models/2026-05-21-dpo-rlhf-conditional-equivalence.md)

## Source

Raw: `raw/kurate/2026-05-22-cs-lg.md` entry #14.
