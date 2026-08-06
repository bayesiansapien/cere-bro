---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.04964
url: https://huggingface.co/papers/2608.04964
arxiv_url: https://arxiv.org/abs/2608.04964
date: 2026-08-06
---

# WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models

Interactive video world models are essential for long-horizon planning and exploration, yet they suffer from compounding errors. Post-training methods such as reinforcement learning (RL) can improve these models, but they hit a verification bottleneck: for arbitrary action sequences, no ground-truth future state exists to measure long-term drift. Our key insight is that reversible action cycles make this verification possible: a sequence composed with its inverse must analytically return to the initial state, yielding annotation-free supervision on long-horizon correctness. Building on this, we introduce WorldCycle, a self-verifiable RL framework that constructs closed action cycles and their repeated executions from ordinary action sequences, and optimizes two complementary rewards: a spatial closure reward enforcing symmetry between mirrored forward and reverse segments, and a temporal consistency reward aligning states across repeated cycle executions. These rewards force the model to learn actions as consistent state operators rather than memorized temporal patterns, and extend naturally to out-of-distribution composite action cycles that the base model handles poorly. We further release CycleBench, a diagnostic benchmark for state-returning ability under complex action structures. WorldCycle reduces state returning drift by up to 44% and lifts composite-action accuracy nearly 4x over the base model, providing a vital foundation for physically grounded world models.
