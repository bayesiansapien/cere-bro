---
source: raw/huggingface/2026-05-02-vipo-visual-preference-optimization-at-scale.md
date: 2026-05-02
arxiv: https://arxiv.org/abs/2604.24953
---

# ViPO: Visual Preference Optimization at Scale

## TL;DR

Existing visual preference datasets have conflicting labels — images that excel on aesthetics but fail on semantic alignment get forced into a binary winner/loser label, creating contradictory gradients. ViPO creates 1M image pairs + 300K video pairs with balanced, reliable preference signals, and pairs them with Poly-DPO, which adds a polynomial confidence-calibration term. Key finding: on high-quality data, Poly-DPO collapses to standard DPO — sophistication only helps when data is noisy.

## Key findings

- Existing preference datasets have conflicting patterns from multi-dimensional quality collapse to binary labels.
- Poly-DPO adds a polynomial term to DPO that dynamically calibrates model confidence based on data quality.
- ViPO dataset: 1M image pairs (1024px, 5 categories) + 300K video pairs (720p+, 3 categories).
- On noisy data: Poly-DPO +6.87 / +2.32 over Diffusion-DPO on GenEval (SD1.5, SDXL).
- On ViPO's high-quality data: Poly-DPO → standard DPO. The polynomial term becomes unnecessary when data is clean.

## Relation to prior wiki knowledge

**N-of-2 with Semi-DPO (same day)**: Both papers diagnose the same root cause — multi-dimensional preferences collapsed to binary labels create conflicting training signal. ViPO's response: build better data. Semi-DPO's response: treat conflicting pairs as noisy unlabeled data and pseudo-label. Complementary solutions.

The deeper insight from comparing them: ViPO's finding that Poly-DPO → DPO on clean data implies that Semi-DPO's pseudo-labeling should eventually converge to clean-data DPO too, once the iterative refinement converges. The two papers predict the same long-run fixed point from different starting points.

## Links

- Raw: [raw/huggingface/2026-05-02-vipo-visual-preference-optimization-at-scale.md](../../../raw/huggingface/2026-05-02-vipo-visual-preference-optimization-at-scale.md)
- Related: [2026-05-02-semi-dpo-noisy-preferences.md](./2026-05-02-semi-dpo-noisy-preferences.md)
