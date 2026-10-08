---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2609.39870
url: https://huggingface.co/papers/2609.39870
arxiv_url: https://arxiv.org/abs/2609.39870
date: 2026-10-07
---

# Magic-W0: A Structured World-Action Foundation Model for Physical Intelligence

World-action models (WAMs) augment robot policies with action-conditioned environment dynamics, yet existing approaches largely rely on future observation reconstruction or generic latent prediction and lack structured, control-oriented world representations tightly coupled with action generation. We introduce Magic-W0, a world-action foundation model that jointly models structured physical state evolution and continuous actions. Magic-W0 represents interaction as a Structured World Transition consisting of Current State, Transition, and Future State. Current State combines vision-language context with Current 3D Geometry; Transition is represented by 3D Motion capturing action-induced three-dimensional changes; and Future State is represented by Future Semantics describing task-relevant outcomes. To couple prediction and control, we propose a layer-aligned world-action interaction architecture in which evolving action hypotheses condition world-transition prediction, while predicted world representations continuously inform action generation. Magic-W0 is pre-trained on large-scale egocentric human manipulation, UMI, real-robot, and simulation data, with latent supervision for geometry, 3D motion, and future semantics from pre-trained visual models. Inference-time interventions show that structured world representations respond systematically to changes in candidate actions and that action-related information propagates through shared 3D representations into future semantic predictions. On RoboDojo-Sim, Magic-W0 achieves an average Score of 27.10, the highest among the compared WAMs. Across multiple real-robot tasks, it also demonstrates strong downstream performance after fine-tuning with limited downstream data, supporting generalization and rapid adaptation.
