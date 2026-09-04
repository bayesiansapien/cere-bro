---
source: farmer/huggingface
farmed: 2026-09-04T08:38:35.484326+00:00
arxiv_id: 2609.01072
url: https://huggingface.co/papers/2609.01072
arxiv_url: https://arxiv.org/abs/2609.01072
date: 2026-09-04
---

# Let Confidence Change, Not the Prediction: Prediction-Preserving Repair for Post-hoc Calibration

Post-hoc calibration corrects reported confidence, yet a multiclass calibrator can also change the associated top-1 prediction. Accuracy captures only the net effect of these changes on correctness, not how often predictions change; the Top-1 Prediction Change Rate (TPCR) instead measures this frequency. We propose Calibrator-Output Repair for Top-1 Decision Preservation (CORD), the first post-fit adapter to impose exact prediction preservation by repairing the full calibrated probability vector. From the original and calibrated outputs alone, CORD determines the mass assigned to the original top-1. The calibrated conditional distribution allocates the remaining mass over the other classes, yielding a repaired vector whose own argmax recovers the original prediction. On the calibration split, CORD coordinates the repaired masses to retain the calibrated outputs' mean mass on original predictions whenever attainable. The adapter alters neither the fitted calibrator nor its direct output, fits no additional supervised map, and requires no user- or validation-tuned hyperparameter. Across CIFAR-10/100 and ImageNet-1K, CORD attains zero TPCR by construction and lowers mean ECE, NLL, and Brier relative to the corresponding direct outputs in every dataset; paired gains persist under distribution shift and across calibration-set sizes. CORD thus removes the preservation constraint from calibrator fitting and assigns exact recovery of the original decision to subsequent output repair. Our code is available at https://github.com/labhai/CORD.
