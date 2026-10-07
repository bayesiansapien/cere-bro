---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05870
url: https://huggingface.co/papers/2610.05870
arxiv_url: https://arxiv.org/abs/2610.05870
date: 2026-10-06
---

# Certification of Real Images through Calibrated Content Authentication

Generative models can synthesize high-quality inauthentic multimedia content that is already being misused at scale. We evaluate twenty deepfake detectors against ten generators released in the last four years and find accuracy decreasing over time, from near-perfect 99.5% to 76%. Adversarial perturbations further reduce every baseline detector to below 2% accuracy, effectively inverting the detector's assigned label. We argue that this unreliability reflects a fundamental ambiguity: generators can reproduce authentic content exactly (e.g., through memorization), so content alone cannot reveal the true provenance label.For this reason, content produced by a generator must admit a faithful reconstruction by that same generator, and finding such a reconstruction makes synthetic provenance plausible and authenticity plausibly deniable.We therefore propose and evaluate a detection paradigm that outputs a calibrated prediction of whether authenticity is plausibly deniable: a faithful reconstruction by any known generator establishes plausible deniability, while calibration bounds how often content from known generators fails to be reproduced. Our evaluation shows that (i) our detector can be calibrated so that at most 1% of generated content is wrongly certified, an operating point at which most baseline detectors reach near-zero recall, including the strongest with 93% accuracy; (ii) calibrating a stricter security threshold on attacked samples preserves this bound against adaptive adversaries within the evaluated bounded-perturbation attack space, whose perturbations break every baseline, but does not cover arbitrary adversarial transformations; and (iii) post-hoc verifiability is eroding, as 1,116 of 3,000 Reddit images resist reproduction by a 2022 generator, but only 55 to 79 resist reproduction by 2024 generators.
