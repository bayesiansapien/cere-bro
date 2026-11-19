---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.22275
url: https://huggingface.co/papers/2611.22275
arxiv_url: https://arxiv.org/abs/2611.22275
date: 2026-11-18
---

# Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration

Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically coupled interactions between humanoids, enabling coordinated decentralized control from local observations alone. At the high level, we train a vision-language planner and design a speech-based leader-follower coordination mechanism to synchronize decentralized execution without network communication. Trained with two identical humanoids, our system scales to teams of up to ten robots and generalizes to heterogeneous teams without retraining. To benchmark these capabilities, we introduce HH-Bench, comprising 12 tasks involving teams of 2 to 10 humanoids, including heterogeneous teams. Systematic evaluations show that Heave-Ho consistently outperforms baseline methods, while real-world experiments demonstrate robust decentralized collaboration across challenging tasks.
