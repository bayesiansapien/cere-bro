---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.310632+05:30
arxiv_id: 2610.05324
url: https://huggingface.co/papers/2610.05324
arxiv_url: https://arxiv.org/abs/2610.05324
date: 2026-10-08
---

# CoDance: Learning Reactive and Compliant Human-Humanoid Interaction from Video

Partnered human-humanoid interaction couples locomotion with continuous physical contact. A humanoid needs to coordinate with a person's motion while responding to interaction forces and maintaining stable and natural movement. We present CoDance, a framework for learning reactive and compliant human-humanoid interaction from video. We study partnered dancing as a challenging instantiation, where a humanoid coordinates its footsteps with a moving partner and maintains continuous two-hand contact. Given a single video of two human dancers, CoDance retargets their motions into a robot reference and a moving partner. We introduce a multi-link compliance augmentation that transforms the kinematic demonstration into force-aware training data by adapting the robot reference under structured forces at both hands. Policies trained on this data follow the observed partner while preserving the demonstrated locomotion style and responding compliantly to physical interaction. In simulation, the policies adapt their footsteps to changes in the partner and reproduce approximately 80% of the wrist displacement encoded by the augmented demonstrations. On a physical humanoid, CoDance enables sustained two-hand dancing with a human partner including repeated transitions between forward and backward motions.
