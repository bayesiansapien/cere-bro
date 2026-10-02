---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.346681+05:30
arxiv_id: 2609.38653
url: https://huggingface.co/papers/2609.38653
arxiv_url: https://arxiv.org/abs/2609.38653
date: 2026-10-01
---

# TERRA: Terrain-Aware Reconstruction, Retargeting and Control for Musculoskeletal Locomotion

Recent advances in musculoskeletal modeling and reinforcement learning have enabled muscle-actuated agents to reproduce increasingly complex human motions. Yet these capabilities remain largely confined to flat ground, in part because motion datasets rarely include aligned terrain geometry and because retargeting terrain interactions to complex musculoskeletal bodies is challenging. We present TERRA, an end-to-end pipeline for terrain-aware retargeting and control of musculoskeletal locomotion. From kinematic trajectories alone, TERRA combines terrain priors, estimated contacts, and negative free-space evidence to recover task-relevant support geometry. TERRA further considers anatomical, tendon-continuity, and contact constraints during retargeting. Using the resulting motion-terrain pairs from five datasets, we successfully train a single muscle-actuated control policy on 9.4 hours of diverse locomotion. Across reconstruction, retargeting, and held-out tracking benchmarks, TERRA improves terrain accuracy, sharply reduces anatomical and interaction violations, and achieves the highest observed completion rate over supported terrain families. Overall, TERRA provides a practical route from scene-less motion data to muscle-actuated locomotion over diverse non-flat terrain. Project website: https://cnai.epfl.ch/terra/
