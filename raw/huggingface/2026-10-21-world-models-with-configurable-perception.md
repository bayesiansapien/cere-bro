---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.648170
arxiv_id: 2610.27914
url: https://huggingface.co/papers/2610.27914
arxiv_url: https://arxiv.org/abs/2610.27914
date: 2026-10-21
---

# World Models with Configurable Perception

Real-world observations are noisy and often contain excessive task-irrelevant information. Effective world modeling and planning need to abstract observations into world state representations while filtering out irrelevant information. However, encoders in existing world models are typically non-adaptive, leading to state representations that are easily distracted by task-irrelevant information. As a result, the model may not selectively filter observations to cater to different task demands. To address this problem, we introduce ConfigWM, which realizes configurable perception through task-conditioned state extraction. Given a language description of the task at hand, ConfigWM uses it as a configuration signal to steer how visual embeddings are mapped into a task-specific state space, selectively preserving information relevant to the current task while suppressing task-irrelevant variations. Action-conditioned dynamics are then learned in this task-specific state space for planning. We evaluate ConfigWM in environments with increasing levels of distraction. While existing methods exhibit substantial declines in planning success rate as the environments become increasingly noisy, ConfigWM remains comparatively stable and outperforms the strongest competing method by 22.3% on average across diverse environments. Consistent gains in physical-quantity probing (+0.365 Pearson r) and distracted-to-clean retrieval (+75.5%) further indicate that ConfigWM learns states that preserve task-relevant information while remaining robust to distractors, supporting reliable world modeling and planning in noisy worlds. Project Page: https://configwm.github.io
