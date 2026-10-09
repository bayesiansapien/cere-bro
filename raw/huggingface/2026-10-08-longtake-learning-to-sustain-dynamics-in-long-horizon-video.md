---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.313377+05:30
arxiv_id: 2609.38562
url: https://huggingface.co/papers/2609.38562
arxiv_url: https://arxiv.org/abs/2609.38562
date: 2026-10-08
---

# LongTake: Learning to Sustain Dynamics in Long-Horizon Video Generation

World models, game simulators, and long-take video creation require coherent scene evolution and sustained dynamics over extended durations. Autoregressive (AR) video diffusion provides a natural framework for long-horizon generation, yet extended rollouts often become near-static or lose visual quality. We hypothesize that these failures reflect the limited guidance provided by short-video supervision on how ongoing scene dynamics develops over longer durations. This motivates us to introduce LongTake, a two-stage training pipeline built around Long-Horizon Teacher Forcing (TF) on curated real long videos. Long-Horizon TF trains the AR model to predict later frames conditioned on long ground-truth video prefixes, extending direct supervision beyond the short training horizon. This supervision is designed to help the model sustain dynamics and preserve visual quality during long-horizon generation. Our central finding is that this training stage strengthens direct initialization for distribution matching distillation (DMD) under student self-rollout, without the intermediate few-step distillation stage used in standard pipelines. Under the same five-second DMD training setup, our initialization yields substantially higher dynamic degree than short horizon TF initialization on 30-second rollouts at comparable aesthetic quality, and surpasses the evaluated baselines in both measures. Hybrid DMD further reuses this teacher to extend supervision to later frames of the self-rollout while retaining bidirectional joint supervision over the initial window. On long-horizon self-rollouts, LongTake lies on the Pareto front of dynamic degree and aesthetic quality, and Hybrid DMD attains the highest dynamic degree among evaluated methods at both 30s and 60s.
