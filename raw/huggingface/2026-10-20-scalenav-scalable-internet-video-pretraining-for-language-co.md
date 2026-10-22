---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25690
url: https://huggingface.co/papers/2610.25690
arxiv_url: https://arxiv.org/abs/2610.25690
date: 2026-10-20
---

# ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation

We study language-conditioned local navigation, where a robot must navigate to a text-specified target visible in its initial observation and stop at the described location. End-to-end navigation policies require diverse training data to generalize across scenes, yet real-robot data is costly to collect and simulated data leaves a sim-to-real gap. Internet egocentric videos offer a scalable source of real-world navigation experience. Our key insight is to learn goal-directed visual dynamics from Internet egocentric videos, and use these dynamics to support robot action generation. To this end, we propose ScaleNav, a unified world-action framework with three-stage training. We first perform instruction-conditioned video pretraining on these videos to learn how observations evolve as the camera approaches instructed targets across diverse real-world scenes. Action alignment then uses action-labeled simulated data to train the model to predict executable action chunks. Joint fine-tuning subsequently optimizes all trainable components together for navigation. ScaleNav achieves success rates of 86.5% on a single-view adaptation of Short-Horizon OVON and 94.9% on our HabitatGS-LN benchmark, outperforming the evaluated baselines on both benchmarks. We further deploy and evaluate ScaleNav on a real quadruped robot, with results supporting the model's ability to generalize to real-world navigation. Code and videos are available at https://zju3dv.github.io/ScaleNav/
