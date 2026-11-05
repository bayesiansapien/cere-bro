---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.366171+05:30
arxiv_id: 2610.41366
url: https://huggingface.co/papers/2610.41366
arxiv_url: https://arxiv.org/abs/2610.41366
date: 2026-11-04
---

# What We Keep of What We Forget: Replacement Operators and Routing Semantics in Training-Free MoE Expert Pruning

Training-free expert pruning makes two decisions: which experts to remove, and what the layer computes when its router still selects a removed expert. Published methods change both at once. Holding the mask fixed, we compare replacement operators from three families on OLMoE, DeepSeek-V2-Lite and Moonlight, with Granite as a fourth router, using paired, multiplicity-corrected tests. The largest effect is a choice usually left implicit: the survivors' gate scale. On routers trained without top-k renormalization, renormalizing the survivors' gates, a common implementation choice, costs 0.8-8.5 points and reverses whether rerouting beats MoNE's mean-output replacement; on two routers trained with renormalization, the trained scale wins at 50% pruning. We introduce the tilted novice, a closed-form low-rank map of the pruned expert's input whose rank-0 case is MoNE's constant. At 50% pruning it adds 1.2-1.8% parameters and gains 3.45 and 1.37 points over the constant on OLMoE and Moonlight, stable across calibration draws and largely unchanged by 4- and 3-bit quantization. No operator dominates: trained-scale rerouting is best on DeepSeek-V2-Lite, and a partial copy of each pruned expert is statistically indistinguishable from the tilted novice on two models. Evaluation can change conclusions: at 25% pruning MoNE's constant keeps 92-97% of dense multiple-choice accuracy but only 5-65% of GSM8K and 0-17% of code scores, and the calibration domain moves the mask 4-9 times more than resampling. We propose a five-item reporting checklist.
