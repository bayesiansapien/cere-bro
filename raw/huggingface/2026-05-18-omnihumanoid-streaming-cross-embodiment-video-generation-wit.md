---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.12038
url: https://huggingface.co/papers/2605.12038
arxiv_url: https://arxiv.org/abs/2605.12038
date: 2026-05-18
---

# OmniHumanoid: Streaming Cross-Embodiment Video Generation with Paired-Free Adaptation

Cross-embodiment video generation aims to transfer motions across different humanoid embodiments, such as human-to-robot and robot-to-robot, enabling scalable data generation for embodied intelligence. A major challenge in this setting is that motion dynamics are partly transferable across embodiments, whereas appearance and morphology remain embodiment-specific. Existing approaches often entangle these factors, and many require paired data for every target embodiment, which limits scalability to new robots. We present OmniHumanoid, a framework that factorizes transferable motion learning and embodiment-specific adaptation. Our method learns a shared motion transfer model from motion-aligned paired videos spanning multiple embodiments, while adapting to a new embodiment using only unpaired videos through lightweight embodiment-specific adapters. To reduce interference between motion transfer and embodiment adaptation, we further introduce a branch-isolated attention design that separates motion conditioning from embodiment-specific modulation. In addition, we construct a synthetic cross-embodiment dataset with motion-aligned paired videos rendered across diverse humanoid assets, scenes, and viewpoints. Experiments on both synthetic and real-world benchmarks show that OmniHumanoid achieves strong motion fidelity and embodiment consistency, while enabling scalable adaptation to unseen humanoid embodiments without retraining the shared motion model.
