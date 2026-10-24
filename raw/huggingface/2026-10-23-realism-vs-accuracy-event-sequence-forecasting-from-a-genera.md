---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.888569+00:00
arxiv_id: 2610.12586
url: https://huggingface.co/papers/2610.12586
arxiv_url: https://arxiv.org/abs/2610.12586
date: 2026-10-23
---

# Realism VS Accuracy: Event Sequence Forecasting from a Generative Modeling Perspective

Event sequences are chains of random events, each described by heterogeneous (numerical and categorical) features. The problem of event sequence forecasting occurs in finance, healthcare, business process intelligence, and other fields. In this work, we study multi-horizon forecasting of event sequences as a conditional generative modeling problem. We evaluate forecasts not only for prediction accuracy, but also for distributional realism. To this end, we present a benchmark comprising metrics for both quality aspects, strong statistical baselines, recent models adapted from adjacent fields, and curated real-world datasets. Careful evaluation reveals that no method excels at both accuracy and realism, highlighting a fundamental trade-off between the two. Finally, we introduce Wasserstein BaryBooster, an algorithm that aggregates samples from a realism-strong diffusion model into a state-of-the-art predictor, demonstrating that distributional realism can be converted into prediction accuracy. Code is available at https://github.com/xaosina/event-sequence-forecasting.
