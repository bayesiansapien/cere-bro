---
source: raw/huggingface/2026-05-02-vipo-visual-preference-optimization-at-scale.md, raw/huggingface/2026-05-02-learning-noisy-preferences-semi-supervised-direct-preference-optim.md
date: 2026-05-02
arxiv: https://arxiv.org/abs/2604.24953, https://arxiv.org/abs/2604.24952
---

# ViPO + Semi-DPO: Two Same-Day Attacks on Noisy Visual Preferences

## TL;DR

Two papers, same day, same problem: visual preference data is multi-dimensional (aesthetics + detail fidelity + semantic alignment), but datasets give a single binary label. Reducing the multi-dim signal to one bit creates conflicting gradients in Diffusion DPO. **Semi-DPO** treats consensus pairs as clean and conflicting pairs as noisy unlabeled; trains on the clean subset, then iteratively pseudo-labels the noisy half. **ViPO** scales the data: 1M image pairs at 1024px + 300K video pairs at 720p+ across eight categories. Their **Poly-DPO** adds a polynomial confidence calibration to the DPO objective. The most striking finding from ViPO: *when applied to the high-quality ViPO data, Poly-DPO collapses to standard DPO* — sophisticated optimization stops mattering once the data is clean.

## Key findings

**Semi-DPO**
- Theoretical result: binary reduction of multi-dim preferences induces *conflicting gradient signals* in Diffusion DPO.
- Treats consistent pairs as clean, conflicting pairs as noisy unlabeled.
- Two-stage: consensus-filtered SFT, then iterative pseudo-labeling.
- No additional annotation, no explicit reward model.

**ViPO + Poly-DPO**
- Data: 1M image pairs (1024px, 5 categories) + 300K video pairs (720p+, 3 categories).
- Poly-DPO adds polynomial confidence calibration over standard DPO.
- On *noisy* baselines: +6.87 (SD1.5) and +2.32 (SDXL) GenEval gains over Diffusion-DPO.
- On *ViPO* (clean): Poly-DPO ≡ standard DPO. Optimizer no longer helps.

## The single most important finding (across both papers)

**Data quality and optimizer sophistication trade off.** When data is clean, you don't need a fancier objective. When data is noisy, you do. The two papers describe the same trade-off from opposite ends — Semi-DPO leans on optimizer sophistication (semi-supervised pseudo-labeling) to extract signal from a noisy dataset; ViPO/Poly-DPO leans on data scale and quality and finds the optimizer trick redundant.

## Relation to prior wiki knowledge

**Generalizes the cross-architecture distillation pattern (05-01, six papers in three weeks).** That thread converged on: *engineer the channel between mismatched models*. The visual-preference thread is converging on a structurally similar claim: *engineer the channel between the multi-dimensional preference signal and the binary DPO objective*. Two of the three engineering choices (Semi-DPO's consensus filter, ViPO's data balancing) are exactly the same primitive — separate clean from conflicting, train on clean, fix the conflicting half last.

**Aligns with the LenVM (05-01) lesson.** LenVM showed length lives in token-level value heads — the operational quantity is fine-grained, not sequence-level. The visual-preference papers say preference is multi-dimensional and per-pair, not scalar. Both findings push the field toward *richer per-example targets and cleaner per-dimension supervision*.

**Pairs with Edit-R1 (05-01)** which used a verifier-based RL reward model with principle-level scoring on image edits — a *structured* reward to replace the scalar judge. The data side (Semi-DPO + ViPO) and the reward side (Edit-R1) are the same critique from two angles: scalar judgments lose information.

## Open questions / Research angle

1. **Per-dimension preference labels released?** ViPO has multi-category data but the public release scheme isn't fully clear. Per-dimension labels would let downstream researchers train multi-channel DPO directly.
2. **Does Poly-DPO ≡ DPO on clean data generalize beyond visual?** If yes, the entire rich-objective DPO literature has a quiet null result waiting on better data. Worth testing.
3. **Cross-modality.** The two papers treat image and video; audio preferences are next. The Nemotron 3 Nano Omni release (05-02) provides an open omni backbone — first audio-DPO at scale on open weights is the obvious follow-up.

## Links

- Raw ViPO: [raw/huggingface/2026-05-02-vipo-visual-preference-optimization-at-scale.md](../../raw/huggingface/2026-05-02-vipo-visual-preference-optimization-at-scale.md)
- Raw Semi-DPO: [raw/huggingface/2026-05-02-learning-noisy-preferences-semi-supervised-direct-preference-optim.md](../../raw/huggingface/2026-05-02-learning-noisy-preferences-semi-supervised-direct-preference-optim.md)
- Related: [2026-05-01-edit-r1-verifier-rl-image-editing.md](./2026-05-01-edit-r1-verifier-rl-image-editing.md) · [2026-05-01-lenvm-token-level-length-value-model.md](../inference-efficiency/2026-05-01-lenvm-token-level-length-value-model.md)
