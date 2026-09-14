---
source: farmer/huggingface
farmed: 2026-09-14T06:17:21.172209+00:00
arxiv_id: 2608.30597
url: https://huggingface.co/papers/2608.30597
arxiv_url: https://arxiv.org/abs/2608.30597
date: 2026-09-14
---

# PLC-DPO: Posterior Label Correction in Noisy and Ambiguous Preference Optimization

Direct Preference Optimization (DPO) simplifies alignment through pairwise comparisons but assumes all observed preferences are reliable. Real data often violates this assumption, leading to reversed, weak, or ambiguous labels that cause harmful policy updates. To address this, we propose Posterior Label Correction DPO (PLC-DPO) to robustly optimize preferences by routing each pair's training signal as a clean, flip, or tie case. The key idea is to use the calibrated policy-reference margin as online evidence to take appropriate correction actions. This reframes noisy preference learning as actively correcting supervision direction and strength rather than merely filtering suspicious examples. Across 57 dataset-model-benchmark cells, PLC-DPO obtains the best mean win rate against DPO (60.5 vs. 55.5 for the next-best method). Injected-noise and tie stress tests, human disagreement analysis, and self-confirmation diagnostics further show that the routing remains stable and distinguishes flipped from weakly directional pairs.
