---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.15631
url: https://huggingface.co/papers/2606.15631
arxiv_url: https://arxiv.org/abs/2606.15631
date: 2026-06-16
---

# Retrieve, Don't Retrain: Extending Vision Language Action Models to New Tasks at Test Time

Extending a vision-language-action (VLA) policy to a new task typically requires task-specific teleoperated demonstrations and per-task fine-tuning, making adaptation costly in both data collection and compute. In this paper, we show that this target-side per-task adaptation cost can be replaced by retrieval. Our retrieval-augmented policy is trained once on paired demonstrations from the target embodiment (query) and a cheaper embodiment (pool, e.g., human-hand video), then frozen. New tasks are added at deployment by appending pool-side demonstrations to a retrieval pool. The frozen policy conditions on retrieved trajectories at every control step, so new tasks are absorbed by indexing data rather than updating parameters. Fine-tuning is needed only to take on a new, unseen embodiment, not for each new task. We show that retrieval improves policies beyond a specific backbone, including standard VLA policies, but its effect is especially pronounced in Cosmos Policy, a video-generation-based world-action model (WAM). In this setting, retrieval supplies coarse task progression, while the WAM's future-image objective provides an additional visual consistency signal that strengthens the retrieval-conditioned actions. On PushT, we study how retrieval provides a reusable high-level motion prior for cross-embodiment generalization to unseen goal angles, while on RoboTwin 2.0 our method outperforms cross-embodiment baselines on unseen tasks, and we additionally demonstrate the method on a real robot.
