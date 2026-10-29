---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.995855+05:30
arxiv_id: 2610.36022
url: https://huggingface.co/papers/2610.36022
arxiv_url: https://arxiv.org/abs/2610.36022
date: 2026-10-28
---

# Learning and Reasoning with Geometry: How Generation Helps Spatial Understanding

Image and video generators can produce spatially consistent visual content, but how to use this capability to improve spatial understanding remains underexplored. We study this problem from two perspectives: geometric supervision during training and explicit geometric evidence during inference. To this end, we introduce a unified geometric understanding and generation model (GeoUG) that integrates depth and multi-view generation with spatial understanding. First, we design a multi-scale depth codec that enables metric-depth generation using a pretrained visual autoencoder, and show that joint training yields task-dependent gains in spatial understanding. Second, we introduce 3DCueBench to control geometric difficulty while balancing selected 2D cues, and find that generated depth provides larger reasoning gains on questions requiring fine-grained geometric discrimination. Building on this finding, we develop adaptive interleaved reasoning, in which GeoUG first drafts an answer and then decides whether to generate geometric evidence to confirm or revise it. We train this decision through reinforcement learning, balancing accuracy gains over retaining the draft against generation cost. GeoUG achieves circular accuracies of 97.9%, 90.8%, and 94.2% on CV-Bench-3D, 3DCueBench, and DA-2K with fewer generation calls than always generating.
