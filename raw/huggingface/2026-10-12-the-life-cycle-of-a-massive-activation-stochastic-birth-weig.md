---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.224481+05:30
arxiv_id: 2610.00423
url: https://huggingface.co/papers/2610.00423
arxiv_url: https://arxiv.org/abs/2610.00423
date: 2026-10-12
---

# The Life Cycle of a Massive Activation: Stochastic Birth, Weight-Decay-Driven Growth, and Competitive Consolidation

Massive activations, residual-stream coordinates with magnitudes far larger than typical activations, are associated with attention sinks in transformers, but how their scale is regulated during training remains incompletely understood. Combining training-trajectory analyses and controlled interventions, we trace their emergence, growth, and consolidation. Sink-carrying channels vary across random seeds but stabilize early within each run. Over longer training, surrounding channels erode and the sink concentrates onto a few redundant carriers. Across ablations, gradient attenuation follows the sink token's collective root-mean-square magnitude rather than any single channel, making collective scale central to understanding their effects. Our central result is that weight decay causally controls the turnover of global activation scale. In controlled continuations, removing decay near the peak allows this scale to keep rising, whereas retaining it produces decline even at constant learning rate. We develop a balance model for the rise and peak of massive-activation magnitude, in which AdamW-preconditioned growth opposes weight decay. Sweeping the decay coefficient λ shifts peak timing approximately log-linearly and yields peak magnitudes scaling approximately as λ^{-1/2}, consistent with this balance. Optimizer measurements further show that preconditioning sustains the large-channel cohort against decay even when raw maintaining forces are too small to do so. Together, these findings connect the observed life cycle to scale-regulating training dynamics and establish weight decay as a training-time lever on activation magnitude.
