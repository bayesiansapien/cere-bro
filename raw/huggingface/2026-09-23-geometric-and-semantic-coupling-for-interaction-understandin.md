---
source: farmer/huggingface
farmed: 2026-09-23T05:53:04.588715+00:00
arxiv_id: 2609.25247
url: https://huggingface.co/papers/2609.25247
arxiv_url: https://arxiv.org/abs/2609.25247
date: 2026-09-23
---

# Geometric and Semantic Coupling for Interaction Understanding in 3D Scenes

Interaction understanding in 3D scenes requires a joint description of movable parts, their motion, and the regions through which they can be operated. We present Segment-Snap, which connects these outputs through the physical relationship between parts and handles. Learned predictors identify broad part surfaces and small handles. A geometric decoder uses planar and upright priors to constrain motion, then selects hinge lines using predicted handle locations, without training a motion regressor. Conversely, a joint part-and-handle predictor supplies additional handle candidates, whose motion classes are refined using containing parts. Each information transfer is applied once, without iterative feedback. On Articulate3D validation, handle guidance raises motion-gated AP from 13.74% to 40.98% at fixed masks and axes. Additional handle candidates raise handle AP from 24.63% to 29.65%; part-based class correction adds 0.98 points, and full context reaches 30.99%. Repeated training, learned-decoder controls and paired visualizations establish the benefits and limitations of combining geometric and semantic evidence for interaction understanding.
