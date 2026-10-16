---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.228305+05:30
arxiv_id: 2610.19729
url: https://huggingface.co/papers/2610.19729
arxiv_url: https://arxiv.org/abs/2610.19729
date: 2026-10-15
---

# A Diagnostic Study of World-Space Human Recovery Under High Camera Dynamics

Monocular world-space human recovery methods excel on current benchmarks, but these rarely include fast camera motion. We introduce the K-Pop stress test, broadcast dance videos that combine fast, large camera motion with dense multi-person choreography. Leading methods produce plausible per-frame meshes on these videos, yet their world-space trajectories drift far from the performers' stage positions. Through a systematic diagnosis, we show that the camera and human estimates each remain self-consistent, and that the drift appears when they are combined at mismatched scales. Each is recovered at its own scale, so a mismatch between the two can turn camera motion into human drift that grows with camera displacement and becomes severe in broadcast dance videos. We derive a closed-form correction that estimates this mismatch and applies one scale to all performers, removing the drift while keeping their relative positions in one shared world frame. It requires no retraining and works with existing backends. Combined with physical constraints, the correction yields stable world-space reconstruction for choreography modeling, scene editing, data generation, and virtual reshooting.
