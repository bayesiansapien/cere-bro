---
source: farmer/huggingface
farmed: 2026-06-18T00:00:00Z
arxiv_id: 2606.18375
url: https://huggingface.co/papers/2606.18375
arxiv_url: https://arxiv.org/abs/2606.18375
date: 2026-06-18
---

# PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation

World foundation models (WFMs) are powerful simulators, yet they predominantly operate in a single-view setting and lack the multi-view 3D consistency required for robotic manipulation. While robotic systems rely on multiple cameras (egocentric, eye-to-hand, and wrist-mounted) for policy learning, current multi-view world models simply concatenate view tokens without explicit geometric reasoning. This causes cross-view object drift, depth inconsistency, and texture misalignment. We trace these failures to two deficiencies: the absence of an explicit inter-view communication mechanism and the lack of a 3D geometric prior. We argue that resolving both simultaneously is necessary and sufficient. To address this, we present PAIWorld, a framework that augments diffusion-transformer world models via three core components: (1) Geometry-Aware Cross-View Attention blocks that establish an explicit pathway across views, (2) Geometric Rotary Position Embedding that encodes camera ray directions and extrinsic poses into the attention mechanism, and (3) Latent 3D-REPA, which distills 3D-aware features from frozen 3D foundation models to ensure 3D consistency. Built upon a DiT-based world foundation model, PAIWorld achieves state-of-the-art multi-view 3D consistency on robotic manipulation benchmarks, ranking 1st on the WorldArena leaderboard and 2nd on the AgiBot-Challenge2026 leaderboard, while enabling downstream applications such as model-based planning, world action models, and multi-view policy post-training.
