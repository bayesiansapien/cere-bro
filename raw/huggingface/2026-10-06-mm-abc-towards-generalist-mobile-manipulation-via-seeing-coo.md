---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.35652
url: https://huggingface.co/papers/2609.35652
arxiv_url: https://arxiv.org/abs/2609.35652
date: 2026-10-06
---

# MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining

Mobile manipulation extends robot interaction beyond a fixed kinematic workspace by making the reachable region itself controllable. This flexibility introduces two central challenges: spatially grounded perception under continuous ego-motion and coordinated control of heterogeneous arm and base actions. Existing approaches strengthen geometry through explicit 3D representations or predictive world models, and often decouple mobility and manipulation into separate action streams. We argue that effective mobile manipulation requires not only decoupling, but also representations that support efficient cross-stream collaboration. We present MM-ABC, a foundation model built around Seeing, Coordinating, and Imagining Arm-Base Collaboration. MM-ABC combines sparse multi-level VLM features for spatial perception; a training-only future branch that uses world imagination and geometric intent as extra supervision, strengthening perception and manipulation-intent prediction and improving the overall learning signal; and MM-APT, which coordinates separate manipulation and mobility streams through masked joint attention and clean-action x-prediction. In controlled ablations, replacing clean-action prediction with velocity prediction lowers success on RoboCasa365 composite-seen tasks from 32.8% to 29.2%, and removing future supervision or multilevel conditioning causes larger drops. We pretrain MM-ABC on 5,000+ hours of heterogeneous robot data spanning 400K+ episodes, 12 datasets, and 17 embodiments. Experiments cover EBench, RoboCasa365, ManiSkill-HAB, LIBERO, LIBERO-Plus, and real-world mobile manipulation. MM-ABC achieves 44.71% success on EBench, 61.2% on RoboCasa365, 99.1% on LIBERO, 82.8% on LIBERO-Plus without perturbation training, and 83% mean success on five real-world tasks.
