---
source: farmer/huggingface
farmed: 2026-05-23T00:00:00Z
arxiv_id: 2605.22538
url: https://huggingface.co/papers/2605.22538
arxiv_url: https://arxiv.org/abs/2605.22538
date: 2026-05-23
---

# Segment Anything with Motion, Geometry, and Semantic Adaptation for Complex Nonlinear Visual Object Tracking

Traditional visual object tracking (VOT) methods typically rely on task-specific supervised training, limiting their generalization to unseen objects and challenging scenarios with distractors, occlusion, and nonlinear motion. Recent vision foundation models, exemplified by SAM 2, learn strong video understanding priors from large-scale pretraining and offer a promising foundation for building more robust and generalizable trackers. However, directly applying SAM 2 to VOT remains suboptimal, as it does not explicitly model target motion dynamics or enforce geometric and semantic consistency across frames, both of which are essential for reliable tracking. To address this issue, we propose SAMOSA, a new tracking framework that adapts SAM 2 to complex VOT scenarios by explicitly leveraging motion, geometry, and semantic cues. Specifically, we introduce a lightweight nonlinear motion predictor to model target dynamics and guide mask selection as well as memory filtering. We further exploit semantic cues to detect target shifts and recover from tracking failures, while geometric cues are incorporated as structural constraints to improve tracking stability. In this way, SAMOSA bridges the gap between the implicit video understanding prior of SAM 2 and explicit tracking-oriented modeling. Extensive experiments show that SAMOSA consistently outperforms state-of-the-art SAM 2--based approaches on general benchmarks, demonstrates stronger generalization than supervised VOT methods, and achieves substantial gains on anti-UAV datasets, which typify complex nonlinear motion scenarios. Our code is available at https://github.com/DurYi/SAMOSA.
