---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36653
url: https://huggingface.co/papers/2609.36653
arxiv_url: https://arxiv.org/abs/2609.36653
date: 2026-09-30
---

# Scheduling Recursive Reasoning in Looped Transformers

Recurrent reasoning models have attracted growing attention for scaling test-time computation, typically by iteratively refining latent states with shared parameters. However, these models apply each learned update with a fixed unit scale, which can be conservative when updates make persistent progress and overly aggressive when they fluctuate, limiting the benefit of additional loops. To understand how the scale should vary along the trajectory, we first analyze the sensitivity of terminal loss to recurrent update scale. We show that its temporal average admits an exact decomposition into persistent-progress and centered-fluctuation contributions. Based on this, we introduce the Trajectory Adaptive Progress-Fluctuation Scheduler (TAPS), which tracks their balance across recurrent updates and adapts the step size online. Theoretically, we establish sufficient conditions under which TAPS reduces expected terminal loss and reaches a target quality in fewer recurrent loops. Empirically, we show that TAPS improves terminal accuracy across structured reasoning tasks without retraining. By further incorporating the progress-fluctuation principle into training, TAPS yields additional accuracy gains with up to 1.56 times wall-clock speedup at matched baseline accuracy. The broad applicability of TAPS is supported by its effectiveness across diverse recurrent architectures and inference strategies. Together, these results establish update scale as complementary control axis of recurrent inference alongside architecture and depth.
