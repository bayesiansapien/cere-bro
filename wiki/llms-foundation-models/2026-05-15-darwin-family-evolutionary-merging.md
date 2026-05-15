# Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Reasoning

**Source:** [HuggingFace Daily Papers](https://huggingface.co/papers/2605.14386) · [arXiv 2605.14386](https://arxiv.org/abs/2605.14386)
**Date ingested:** 2026-05-15
**Tier:** 2. Model merging, training-free post-training, cross-architecture composition
**Raw:** [farmer file](../../raw/huggingface/2026-05-15-darwin-family-mri-trust-weighted-evolutionary-merging-for-trainin.md)

## TL;DR

Training-free evolutionary merging of large language models via gradient-free weight-space recombination. Three ideas: (i) a **14-dimensional adaptive merge genome** for fine-grained component- and block-level recombination; (ii) **MRI-Trust Fusion** balancing diagnostic layer-importance signals with evolutionary search via a learnable trust parameter; (iii) an **Architecture Mapper** for cross-architecture breeding between heterogeneous model families. Flagship Darwin-27B-Opus hits **86.9% on GPQA Diamond**, ranking #6 of 1,252 evaluated models, and beats its fully trained foundation model **without any gradient-based training**. Across 4B-35B scales, Darwin models improve over their parents, support recursive multi-generation evolution, and can combine Transformer- and Mamba-based components.

## What's new

Three structural moves.

**14-dimensional merge genome.** Most evolutionary merging operates at the parameter or layer level. Darwin's genome operates at the component level (attention heads, MLP blocks, layer norms, etc.) across the 14 dimensions. This gives the search a finer addressable space than typical weight-averaging or DARE-style recipes.

**MRI-Trust Fusion.** MRI here refers to diagnostic layer-importance signals from interpretability tooling. The merge balances these signals against the evolutionary search via a learnable trust parameter. Empirically the trust parameter weighs interpretability signals where they are reliable and falls back to evolutionary search where they aren't.

**Cross-architecture breeding.** The Architecture Mapper enables merging Transformer and Mamba components. The flagship 27B-Opus result combines both. This is the first cross-architecture merge result in the wiki and a notable architectural primitive: hybrid Mamba+Transformer models constructed via merging rather than from-scratch training.

## Why this matters

GPQA Diamond at 86.9% on a *training-free* merge is remarkable. The model ranks #6 globally; this is competitive with leading frontier models and well above its fully-trained foundation. If reproducible, the cost economics of post-training reasoning models shift: an evolutionary search budget replaces a multi-million-dollar RL post-training run.

The cross-architecture result is the more structurally interesting piece. The wiki has tracked hybrid Mamba-Transformer architectures ([MDN](../inference-efficiency/2026-05-11-mdn-momentum-deltanet-linear-attention.md), [Nemotron-3 Super](../inference-efficiency/2026-04-21-nemotron3-super-hybrid-moe.md)) and Mamba-only models. Until now, the only way to build hybrid models was from-scratch training. Darwin's Architecture Mapper makes hybrid construction a post-hoc operation on existing checkpoints. This composes with [WriteSAE](../responsible-ai/2026-05-14-writesae-sae-recurrent-state.md) (interpretability for hybrid architectures) and Forcing-KV-style head-role analysis (compress hybrid heads by role).

## Connections to prior wiki pages

- [WriteSAE](../responsible-ai/2026-05-14-writesae-sae-recurrent-state.md) — reaches state-space and hybrid models. Darwin builds hybrid models without retraining. Both treat hybrid Mamba+Transformer as the architecture-of-interest.
- [TIDE: Cross-Arch Diffusion Distillation](../inference-efficiency/2026-04-30-tide-cross-arch-diffusion-distillation.md) — cross-architecture distillation. Darwin is the cross-architecture *merging* version. Two papers in two weeks on cross-architecture composition.
- [SU-01](2026-05-15-su-01-gold-olympiad-reasoning-30b.md) — also today. Gold-medal IMO via 200 RL steps on a single 30B model. SU-01 specializes via training; Darwin specializes via merging. Two paths to compact-reasoning frontier performance.
- [Shadowpeft Centralized Layer Space](../inference-efficiency/2026-04-22-shadowpeft-centralized-layer-space.md) — adapter-space composition. Darwin is the full-weight composition analogue.

## Research angle

1. **Darwin composed with EvoEnv.** EvoEnv constructs verifiable environments for self-improvement; Darwin merges checkpoints without training. The composition: evolve environments and merge models in tandem. This is the closest thing to "RSI as engineering discipline" the wiki has tracked.
2. **Trust-parameter generalization.** The MRI-Trust mechanism balances interpretability signals against search. Whether this trust framework transfers to RL post-training, adapter selection, or routing decisions is the obvious next question.
3. **Recursive merging stability.** The paper claims recursive multi-generation evolution. Whether the merged model drifts (Cliff-style format collapse, capability loss) under many generations is the natural ablation.

## Why it matters

Training-free gold-medal-tier reasoning from existing checkpoints is the kind of result that changes economics. If the GPQA 86.9% number reproduces and the cross-architecture breeding stabilizes, post-training stops being a from-scratch operation and becomes a search over the existing model ecosystem.

## Links

- [Paper](https://arxiv.org/abs/2605.14386)
- [HuggingFace](https://huggingface.co/papers/2605.14386)
- [Raw farmer file](../../raw/huggingface/2026-05-15-darwin-family-mri-trust-weighted-evolutionary-merging-for-trainin.md)
- Related: [TIDE](../inference-efficiency/2026-04-30-tide-cross-arch-diffusion-distillation.md), [WriteSAE](../responsible-ai/2026-05-14-writesae-sae-recurrent-state.md), [SU-01](2026-05-15-su-01-gold-olympiad-reasoning-30b.md), [Nemotron-3 Super](../inference-efficiency/2026-04-21-nemotron3-super-hybrid-moe.md)
