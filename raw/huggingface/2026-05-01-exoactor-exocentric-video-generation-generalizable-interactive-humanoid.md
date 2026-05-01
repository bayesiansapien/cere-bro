---
source: farmer/huggingface
farmed: 2026-05-01T00:00:00Z
arxiv_id: "2604.27711"
url: https://huggingface.co/papers/2604.27711
arxiv_url: https://arxiv.org/abs/2604.27711
date: 2026-05-01
---

# ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control

Humanoid control systems have made significant progress in recent years, yet modeling fluent interaction-rich behavior between a robot, its surrounding environment, and task-relevant objects remains a fundamental challenge. This difficulty arises from the need to jointly capture spatial context, temporal dynamics, robot actions, and task intent at scale, which is a poor match to conventional supervision. We propose ExoActor, a novel framework that leverages the generalization capabilities of large-scale video generation models to address this problem. The key insight in ExoActor is to use third-person video generation as a unified interface for modeling interaction dynamics. Given a task instruction and scene context, ExoActor synthesizes plausible execution processes that implicitly encode coordinated interactions between robot, environment, and objects. Such video output is then transformed into executable humanoid behaviors through a pipeline that estimates human motion and executes it via a general motion controller, yielding a task-conditioned behavior sequence. To validate the proposed framework, we implement it as an end-to-end system and demonstrate its generalization to new scenarios without additional real-world data collection. Furthermore, we conclude by discussing limitations of the current implementation and outlining promising directions for future research, illustrating how ExoActor provides a scalable approach to modeling interaction-rich humanoid behaviors, potentially opening a new avenue for generative models to advance general-purpose humanoid intelligence.
