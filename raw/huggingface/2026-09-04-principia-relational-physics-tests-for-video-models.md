---
source: farmer/huggingface
farmed: 2026-09-04T10:50:04.492861
arxiv_id: 2609.04200
url: https://huggingface.co/papers/2609.04200
arxiv_url: https://arxiv.org/abs/2609.04200
date: 2026-09-04
---

# Principia: Relational Physics Tests for Video Models

Evaluating physical reasoning in video models is difficult because absolute motion measurements depend on frame rate, object scale, and camera calibration, all of which are often ambiguous or unavailable in generated video. We propose a different approach. When two objects in the same scene obey the same physical law, their motions must satisfy predictable relationships, and these relationships hold independent of calibration. We introduce Principia, a benchmark that evaluates Newtonian physics through relational consistency between paired objects. Principia spans eight phenomena - gravity, restitution, friction, rotational inertia, projectile motion, momentum, pendulum, and mass-spring oscillation - across translational, rotational, collisional, and oscillatory dynamics, using real-world scenes recorded under controlled protocols. We also introduce a calibration-independent consistency score that quantifies physical violation directly in image space. Across thousands of generations from six state-of-the-art video generators, no model exceeds 0.42 on Principia despite all scoring around 0.8 on VBench. Vision-language models are evaluated on their ability to detect relational physics violations, with the best model achieving only 67% accuracy and most performing near chance level.
