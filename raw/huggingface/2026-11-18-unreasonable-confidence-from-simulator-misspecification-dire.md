---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.20321
url: https://huggingface.co/papers/2611.20321
arxiv_url: https://arxiv.org/abs/2611.20321
date: 2026-11-18
---

# Unreasonable Confidence from Simulator Misspecification: Directional Robustness on the SPEED+ Sim-to-Real Benchmark

Vision-based navigation systems for orbit must be trained almost entirely on synthetic imagery, because real labelled images of a given spacecraft in flight rarely exist. Benchmarks like SPEED+ are built for that situation: the training set comes from a simulator, and the test sets are real images of a satellite mockup under two kinds of lighting. That simulator approximates how light reflects off mylar and aluminium, and like every scientific simulator it is misspecified. Its error is radiometric, since it misses the specular highlights, hard shadows and sensor saturation common in real images. We probe the resulting synthetic-to-real gap, the central risk for such systems, with a deliberately simple monocular pose estimator. In a 2x2 study of backbone adaptation and photometric augmentation, trained on synthetic images and tested on both real hardware-in-the-loop domains, we find three things. (1) The model does not know it is failing: regions conformally calibrated to 90% on synthetic data cover only 9-15% of rotation errors on sunlamp and 21-38% on lightbox, so a wrong pose carries the confidence of a correct one. (2) Transfer is asymmetric: scaling data and features improved synthetic rotation error from 1.65 to 1.03 rad but moved the harshly lit sunlamp domain by only 0.05 rad, under twice its seed s.d., whereas adapting the backbone's last stage carried 63-83% of its extra synthetic gain to both real domains. (3) Once the backbone adapts, augmentation helps only in the direction it models: our photometric stack improved the diffusely lit lightbox domain from 1.17 to 0.99 rad on every seed but moved sunlamp no more than seed-to-seed variation, while with the backbone frozen it helped sunlamp more. Every post-review experiment was pre-registered, and the code, per-image predictions and pre-registration record are at https://github.com/lokindoo/spacecraft-pose-estimation.
