---
source: farmer/huggingface
farmed: 2026-08-14T11:17:27.766803
arxiv_id: 2608.12773
url: https://huggingface.co/papers/2608.12773
arxiv_url: https://arxiv.org/abs/2608.12773
date: 2026-08-14
---

# CW-BASS v2: Saturation-Aware Pseudo-Label Selection for Semi-Supervised Segmentation under Foundation-Model Teachers

Semi-supervised semantic segmentation has long turned on one question, which pseudo-labels to trust, and a generation of selection rules, dynamic thresholds, per-class curricula, soft confidence weights, answered it for the noisy, under-confident ResNet teachers of their day. Self-supervised foundation encoders change the regime: with a DINOv2 teacher, confidence saturates, so the filtering that helped a weak teacher can hurt a strong one. We propose CW-BASS v2, a saturation-aware pseudo-label selection method that reads the teacher's confidence regime rather than committing to one rule. It pairs held-out calibration, an unbiased per-class noise estimate, with a self-adaptive confidence floor that provably bounds retention away from 1, and combines them in a one-pass gate: measure the reliability of the teacher's confident set, pi_kept = Pr[correct | c >= tau], on a held-out slice, and filter strictly when it meets the confidence demanded (pi_kept >= tau), falling back to the adaptive floor otherwise. The boundary is the pre-existing operating threshold, not a value tuned to mIoU, and across six DINOv2 teachers it makes the correct strict-vs-floor call blind. CW-BASS v2 thus recovers the UniMatch V2 operating point on the saturated benchmarks by selecting strict (Pascal VOC 1/8 87.4 against its reported 87.9; Cityscapes within 0.5), and improves on it where the confident set is unreliable (pi_kept ~ 89%, ADE20K), where the floor edges ahead (+1.5 mIoU, single seed). The gate is principled because the failure it avoids is measured, not assumed: on a reliable, saturated teacher the confidence distribution's dynamic range collapses (98% of Pascal pixels >= 0.95), so an adaptive cutoff floods the retention mask and self-training decays into confirmation bias.
