---
source: raw/huggingface/2026-05-02-learning-noisy-preferences-semi-supervised-direct-preference-optim.md
date: 2026-05-02
arxiv: https://arxiv.org/abs/2604.24952
---

# Semi-DPO: Learning from Noisy Preferences via Semi-Supervised DPO

## TL;DR

Binary preference labels for images hide multi-dimensional quality tradeoffs — an image can win on aesthetics but lose on semantic alignment, yet is labeled simply "winner." This creates contradictory gradient signals. Semi-DPO treats conflicting pairs as noisy unlabeled data: train on clean consensus pairs first, then use that model to generate pseudo-labels for the conflicting pairs, iterate. No extra annotation, no explicit reward model.

## Key findings

- Multi-dimensional preferences (aesthetics, detail, semantic alignment) collapsed to binary labels introduce conflicting gradients into DPO training.
- Semi-DPO separates pairs into "clean" (consistent across dimensions) and "noisy" (conflicting).
- Train on clean subset first → pseudo-label noisy pairs → iterate refinement.
- Significant improvement in aligning with complex human preferences vs standard DPO.
- No additional annotation or explicit reward models required.

## Relation to prior wiki knowledge

**N-of-2 with ViPO (same day)** — [2026-05-02-vipo-visual-preference-optimization.md](./2026-05-02-vipo-visual-preference-optimization.md). Same diagnosis, different treatment. ViPO solves by collecting better data; Semi-DPO solves by cleaning noisy data. Together they confirm the conflicting-label problem is a known gap now being attacked from both ends simultaneously.

## Links

- Raw: [raw/huggingface/2026-05-02-learning-noisy-preferences-semi-supervised-direct-preference-optim.md](../../../raw/huggingface/2026-05-02-learning-noisy-preferences-semi-supervised-direct-preference-optim.md)
- Related: [2026-05-02-vipo-visual-preference-optimization.md](./2026-05-02-vipo-visual-preference-optimization.md)
