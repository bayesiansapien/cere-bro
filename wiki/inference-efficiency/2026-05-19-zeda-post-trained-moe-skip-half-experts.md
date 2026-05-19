# ZEDA: Post-Trained MoE Can Skip Half Experts via Self-Distillation

**arXiv:** [2605.18643](https://arxiv.org/abs/2605.18643) · **HF:** [paper page](https://huggingface.co/papers/2605.18643) · **Tier:** 1 (MoE, dynamic routing, post-training compression)

## TL;DR

Existing dynamic MoE methods (input-dependent expert activation) usually rely on pre-training from scratch or task-specific adaptation, leaving the practical conversion of fully trained static MoE underexplored. ZEDA (Zero-Expert Self-Distillation Adaptation) is a low-cost framework that converts post-trained static MoE models into dynamic ones. It injects parameter-free zero-output experts into each MoE layer and adapts via two-stage self-distillation, using the original MoE as a frozen teacher and applying a group-level balancing loss. On Qwen3-30B-A3B and GLM-4.7-Flash across 11 benchmarks (math, code, instruction following), ZEDA eliminates over 50% of expert FLOPs at marginal accuracy loss, outperforms the strongest dynamic-MoE baseline by 6.1 and 4.0 points on the two models, and delivers ~1.20x end-to-end inference speedup.

## Key findings

- Static MoE pre-training picks a fixed top-K. Dynamic MoE (variable K per token) reduces compute on easy tokens by letting them skip experts entirely. Prior dynamic-MoE methods require pre-training from scratch or task-specific adaptation, so they cannot be applied to frontier post-trained static MoEs.
- ZEDA solves the architectural conversion by injecting parameter-free "zero experts" (experts that always output zero) into each MoE layer. The augmented model has K+1 routing slots per token, where the zero expert is the explicit option to skip computation.
- Two-stage self-distillation stabilises the conversion. The original frozen static MoE is the teacher. A group-level balancing loss prevents the router from collapsing all tokens onto the zero experts.
- On Qwen3-30B-A3B and GLM-4.7-Flash, ZEDA eliminates over 50% of expert FLOPs at marginal accuracy loss. It outperforms the strongest dynamic-MoE baseline by 6.1 and 4.0 points respectively.
- End-to-end inference speedup is ~1.20x; the gap between FLOP reduction (50%) and wall-clock (1.20x) is the standard MoE overhead from routing logic, expert dispatch, and load balancing on real hardware.

## Relationship to prior wiki entries

ZEDA is the fourth distinct MoE compression / routing direction the wiki has tracked in the last two weeks. The four directions are now:

1. **Pre-training scaling (MoE-muP, 2026-05-17, Vankadara et al., Kurate cs.LG #13).** Closed-form Maximally Scale-Stable Parameterization across the five MoE axes M, Ne, K, N, L. Answers: how to scale a new MoE.
2. **Per-token activation (BEAM, 2026-05-16).** Binary expert-activation masks trained end-to-end via straight-through estimator. 98%+ retention at 85% FLOP reduction. Answers: which experts to run for this token.
3. **Post-training resident-count compression (HodgeCover, 2026-05-18).** Harmonic-kernel obstruction in the simplicial Laplacian on the expert 2-complex. Answers: which experts to keep at aggressive compression.
4. **Post-training static-to-dynamic conversion (ZEDA, today).** Zero experts plus two-stage self-distillation. Answers: how to skip experts per token without retraining from scratch.

ZEDA and BEAM both decide which experts run per token, but they are not redundant. BEAM is a from-scratch training intervention; ZEDA is a post-training conversion of a frozen MoE. Frontier labs that have already shipped Gemma 4, DeepSeek V4, Kimi K2.6, and Qwen3.5 do not retrain those models from scratch. ZEDA is the post-hoc retrofit path BEAM cannot offer.

The natural composition the wiki has been calling out is now closer: a future MoE pre-trained under MoE-muP MSSP, post-training compressed via HodgeCover (resident experts), then dynamically routed via ZEDA (active experts per token) on top of BEAM-style per-token activation. The full stack would replace three independent ad-hoc choices in frontier MoE serving with three principled methods.

## Why it matters

The post-training conversion path is the deployable one. Frontier open MoE releases ship as static top-K models. Every operator running them in production wants the dynamic-MoE win without paying for a from-scratch retrain. ZEDA is the first wiki entry demonstrating that the conversion is cheap enough (two-stage self-distillation, no external teacher, no task data) to be applied as a routine post-release step. The 50% FLOP reduction at marginal accuracy loss on two distinct frontier open MoEs is the bar that makes this a candidate operational practice rather than a research curiosity.

## Research angle

- **ZEDA on the full open-MoE wave.** Apply to Gemma 4 26B-A4B, DeepSeek V4 Flash, Kimi K2.6, MiMo-V2.5-Pro. If FLOP-reduction-at-marginal-loss holds on three of four, the conversion is robust to MoE design choice. If it collapses on one specific architecture, the failure mode identifies a fragility in that MoE's expert specialisation.
- **Compose with HodgeCover.** HodgeCover removes experts at the layer level. ZEDA skips experts at the token level. The composition's diagnostic: do the two methods select overlapping experts to suppress, or orthogonal ones? If overlapping, HodgeCover's chosen-to-remove experts are also the ones ZEDA's zero-expert is replacing, and the two are partially redundant. If orthogonal, they are complementary and the stack is multiplicative.
- **Zero-expert as an alignment signal.** When the router prefers the zero expert, the model is implicitly saying this token does not need this layer's expert computation. The distribution of zero-expert routing across token types is an interpretability signal. The wiki has no prior entry where the routing distribution carried interpretability content directly.

## Source

`raw/huggingface/2026-05-19-post-trained-moe-can-skip-half-experts-via-self-distillation.md`
