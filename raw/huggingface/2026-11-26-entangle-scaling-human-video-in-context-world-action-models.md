---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.903711+00:00
arxiv_id: 2611.28732
url: https://huggingface.co/papers/2611.28732
arxiv_url: https://arxiv.org/abs/2611.28732
date: 2026-11-26
---

# Entangle: Scaling Human-Video In-Context World-Action Models across Unseen Tasks and Contexts

In-context learning (ICL) enables foundation models to perform unseen tasks from context without parameter updates. In robotic manipulation, a human video provides the context that specifies how a task should be performed. However, scaling human-video ICL on world-action models (WAMs) faces two challenges: task-level human-robot pairs are not temporally aligned with robot actions, and standard action losses allow policies to rely on initial-scene or task-identity shortcuts rather than tracking the context. We present Entangle, an in-context world-action model that maps a single human video and current robot observations to future visual states and executable actions. To scale temporally aligned training data, we convert recorded robot videos into matched human contexts via video-to-video generation, supplemented by real paired recordings. For model training, we combine variable-length video windows with an intra-task contrastive objective that distinguishes the paired action trajectory from other executions of the same task, preventing task-identity shortcuts. Without task-specific fine-tuning, Entangle improves steadily as aligned training data scales, reaching an average score of 83.5/100 across six unseen tasks on an Astribot S1 robot, and achieves a 69.5% average success rate on seven unseen RoboTwin tasks, outperforming Zero-WAM by 22.6 percentage points. Under Context-OOD, although trained only on scene-aligned pairs, Entangle transfers context-specified behaviors across rearranged layouts and substituted tools. Project page at https://entangle-robotics.github.io/
