# Confidence-Adaptive SwiGLU (κ-SwiGLU) for Mixture-of-Experts

## TL;DR

SwiGLU is the standard gated activation in modern Transformer MLPs. It pairs a SiLU gate (a smooth, sigmoid-shaped gating curve) with a linear value path, and the gate's "sharpness", how smoothly or selectively it turns on, is normally a fixed property of the activation throughout training. κ-SwiGLU (Confidence-Adaptive SwiGLU) makes that sharpness learnable and conditions it on the router's confidence in Mixture-of-Experts (MoE) models, where each token is routed through a small subset of expert MLPs. Concretely it parameterizes the SiLU sharpness coefficient as a learnable function of the router logit, so each expert gate unit can interpolate between smooth, broadly-active gating and sharp, selective gating per token, driven by how confidently the router picked that expert. Evaluated on FineWeb-Edu across MoE Transformers from 8 to 28 layers, κ-SwiGLU improves mean CORE performance while adding negligible parameters and only a small compute overhead. Code is released.

```
token ─► MoE router ─► router logits
                          │
            ┌─────────────┴───────────────┐
            ▼                              ▼
   (a) expert selection          (b) learnable κ-controller:
       (pick experts)                router logit ─► κ (SiLU sharpness)
            │                              │
            └──────────────┬───────────────┘
                           ▼  expert SwiGLU MLP uses token-specific κ
       low router confidence ─► SMOOTH gate (broadly active)
       high router confidence ─► SHARP gate (selective)  ─► output
```

## Key points

- **Gate sharpness becomes confidence-conditioned.** The SiLU sharpness coefficient is a learnable function of the router logit, so the gate sharpens when the router is confident in the expert and stays smooth when it is not, decided per token.
- **Targets the MLP, not the routing.** Unlike expert-skipping or routing-policy tweaks, κ-SwiGLU changes the activation inside the chosen expert. It is orthogonal to which experts are selected.
- **Nearly free.** Improves mean CORE across MoE Transformers of 8 to 28 layers on FineWeb-Edu while adding negligible parameters and incurring only a small compute overhead.
- **Released and reproducible.** Code at https://github.com/askerlee/kappa-swiglu.

## How this relates to prior wiki pages

κ-SwiGLU is another same-week MoE efficiency tweak alongside [dMoE](2026-06-01-dmoe-block-level-moe-diffusion-llm.md) (2026-06-01, which aggregates per-token expert distributions into one block-level distribution in diffusion LLMs, dropping uniquely-activated experts from 69.5 to 14.6 and cutting memory 76-80%), but the two operate on different MoE knobs. dMoE attacks the *memory cost of routing* (how many distinct experts a block must load); κ-SwiGLU attacks the *quality of each expert's MLP* by tying gate sharpness to routing confidence. They could compose: dMoE decides which experts load, κ-SwiGLU shapes how sharply each selected expert gates. Both reflect the wiki's recurring "use the router signal for more than expert selection" theme, where the router logit, normally just a selection score, is reused to drive a second decision. There is no standalone mixture-of-experts concept page yet; the prior MoE-efficiency entries (dMoE, plus expert-skipping and pooled-expert work) cover adjacent ground and would be the place to fold this in.

## Gaps

Evaluation is on FineWeb-Edu and the CORE metric across 8-to-28-layer models; whether the gain holds at the larger expert counts and depths of production MoEs, and on downstream task suites beyond CORE, is not shown. The improvement magnitude is reported as a mean-CORE lift but the abstract does not give the absolute delta, so how meaningful "improves mean CORE" is at scale is unclear. The interaction with load-balancing losses and router temperature, which also shape routing confidence, is not analyzed.

**Source:** [arXiv 2606.00761](https://arxiv.org/abs/2606.00761) · raw: [raw/huggingface/2026-06-02-confidence-adaptive-swiglu-for-mixture-of-experts.md](../../raw/huggingface/2026-06-02-confidence-adaptive-swiglu-for-mixture-of-experts.md)
