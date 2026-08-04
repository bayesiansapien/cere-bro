---
source: farmer/huggingface
farmed: 2026-08-04T09:04:58.435121+05:30
arxiv_id: 2608.01755
url: https://huggingface.co/papers/2608.01755
arxiv_url: https://arxiv.org/abs/2608.01755
date: 2026-08-04
---

# Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs

Recent Vision-Language-Action (VLA) models for autonomous driving (AD) increasingly utilize chain-of-thought (CoT) supervision to enhance the reasoning capabilities of their Vision-Language Model (VLM) components, yet existing annotation pipelines commonly expose the teacher model to the logged ground-truth (GT) future trajectory. We empirically show that this induces trajectory anchoring bias: teacher models rationalize the revealed outcome rather than infer a decision from scene evidence, producing less causally faithful CoTs and substantially more severe hallucinations, especially in causally challenging scenes. Removing the GT trajectory eliminates this shortcut, but open-ended trajectory generation entangles high-level decision-making with precise geometric synthesis and low-level dynamics. To make trajectory-level driving decisions verifiable without requiring open-ended trajectory synthesis, we introduce Autonomous-Driving Multiple-Choice Question (AD-MCQ), which casts planning as selection among explicit trajectory candidates. Taking this a step further, we propose Deferred Exposure of Future Trajectories for RLVR (DEFT-RLVR) to transform future trajectories from pre-decision anchors into post-decision verification targets. Experimental results show that DEFT-RLVR improves AD reasoning while preserving or even enhancing general visual capabilities. With VLM-only inference and controllable difficulty through candidate construction, AD-MCQ provides a flexible, scalable, and extensible foundation for future research on verifiable AD reasoning.
