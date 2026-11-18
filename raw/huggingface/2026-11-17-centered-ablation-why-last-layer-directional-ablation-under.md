---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.116787+00:00
arxiv_id: 2611.20148
url: https://huggingface.co/papers/2611.20148
arxiv_url: https://arxiv.org/abs/2611.20148
date: 2026-11-17
---

# Centered Ablation: Why Last-Layer Directional Ablation Under-Fires or Collapses, and a Closed-Form Fix

Directional ablation removes a hidden state's component along a "behaviour direction" while a language model runs. It is the standard way to switch a behaviour such as refusal off, but it is erratic: on some models it barely fires, on others the text collapses into repetition. We show why, and fix it. At the last residual stream, ablation is exactly a logit bias: a fixed vocabulary footprint scaled by a gate, the cosine between the hidden state and the direction. The gate is measured from the origin, but last-layer states share a large common mode far from it, so a direction that overlaps the common mode fires on benign text and under-fires on its targets. Centered Ablation (CA) projects the common mode out of the direction, in closed form. Across 8 models, CA raises attack success by 29 and 46 points where the standard recipe under-fires, cuts collapse on Gemma-2-9B from 50\% to 1\%, and preserves 12 to 40 points more benign answers on high-overlap models, 39 to 46 more than the affine offset of prior work. Two numbers computed before generation predict, on models the analysis had not seen, which gain faithfulness and which gain attack success, and a collapse index marks when text degenerates. We also show that two standard safety judges score collapsed text in opposite directions, which can fabricate a 46-point effect.
