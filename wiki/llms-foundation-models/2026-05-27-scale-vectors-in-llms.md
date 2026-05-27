# Scale Vectors in LLMs: Negligible in Size, Significant in Effect

**Source:** HuggingFace daily papers (2026-05-27, 5 upvotes) · arxiv 2605.26895
**arxiv:** [2605.26895](https://arxiv.org/abs/2605.26895)
**Date:** 2026-05-27
**Raw:** [raw/huggingface/2026-05-27-negligible-in-size-significant-in-effect-on-scale-vectors-in.md](../../raw/huggingface/2026-05-27-negligible-in-size-significant-in-effect-on-scale-vectors-in.md)
**Tier:** 2 (LLM architecture / optimization, interpretability-adjacent)

## TL;DR

Normalization layers have two parts: a deterministic normalization op (well studied) and a learnable scale vector (barely studied). This paper shows scale vectors, despite being a negligible fraction of parameters, are load-bearing: removing them substantially degrades pre-training. The theory: in Pre-Norm architectures scale vectors don't add expressivity, they improve *optimization* through a self-amplifying preconditioning effect on the following linear maps. Distinguishing Input-Norm from Output-Norm layers, the authors show weight decay helps the former and hurts the latter. They propose three lightweight fixes (branch-specific heterogeneity, better placement around linear maps, magnitude-direction reparameterization) and a unified strategy that lowers terminal loss with better scaling, at negligible overhead, validated on dense and MoE models from 0.12B to 2B under industrial token budgets.

## Key points

- **Scale vectors are an optimization tool, not an expressivity one** (in Pre-Norm): they precondition subsequent linear mappings with a self-amplifying effect.
- **Weight decay is layer-type-dependent**: beneficial for Input-Norm, harmful for Output-Norm, because the two play distinct optimization/expressivity roles.
- **Three cheap improvements** (branch-specific heterogeneity, placement, magnitude-direction reparameterization) combine into a unified strategy with consistently lower terminal loss and better scaling, negligible added cost, across dense and MoE, 0.12B-2B.

## Relation to prior wiki state

This is a pre-training optimization result that sharpens the wiki's "small structural details carry disproportionate weight" sub-theme. It rhymes with FocuSFT (05-13, attention sinks are a training-side phenomenon fixable by bilevel optimization) and the scale-stable-parameterization work ([MoE-muP](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md)): all three say the right *parameterization/normalization* choices, not just more parameters, govern training dynamics and scaling behavior. The MoE validation (0.12B-2B) ties it to the day's MoE cluster (MobileMoE, MiniMax-M2): scale-vector strategy is one more knob in the principled-MoE-training program.

## Gaps

Validated to 2B; whether the closed-form weight-decay prescription and the three fixes hold at frontier scale (100B+ MoE) is the open extrapolation question.

## Links

- [Paper](https://arxiv.org/abs/2605.26895)
- Raw: [raw/huggingface/2026-05-27-negligible-in-size-significant-in-effect-on-scale-vectors-in.md](../../raw/huggingface/2026-05-27-negligible-in-size-significant-in-effect-on-scale-vectors-in.md)
- Related: [MoE-muP](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md)
