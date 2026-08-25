---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.13622
url: https://huggingface.co/papers/2608.13622
arxiv_url: https://arxiv.org/abs/2608.13622
date: 2026-08-25
upvotes: 12
authors: ["Yongqi Tong", "Tan Li Hui Faith", "Choy Zhen Wen Marcus", "Zhou Jin", "Kewei Fu", "Jiang-Ming Yang", "Jianshe Li", "Xin Zhang"]
---

# ARC: Fair Relative Advantage Comparison in Open-Ended Real-World Interaction

**Upvotes:** 12
**Authors:** Yongqi Tong, Tan Li Hui Faith, Choy Zhen Wen Marcus, Zhou Jin, Kewei Fu, Jiang-Ming Yang, Jianshe Li, Xin Zhang

Open-ended real-world interaction admits multiple valid behaviors: an agent may answer directly, ask for clarification, provide progress updates, or confirm before acting. This flexibility breaks a core assumption behind group-based RL: rollouts compared within a group are no longer guaranteed to be behaviorally comparable. As a result, reward-model preferences over interaction style can distort relative advantages and steer optimization toward reward-preferred behaviors rather than context-appropriate ones. We formalize this as a reward fairness problem and propose ARC (Advantage Regularization via Conditioning), a training recipe that restores fairer relative comparison through strategy-conditioned rollout grouping, together with hybrid rewards and entropy regularization. We study ARC in our proposed \inter, a novel paradigm for responsive, steerable, and execution-aware user-agent interaction that decouples user-visible communication from latent reasoning and tool use. \inter\ also provides the annotation and distillation pipeline for constructing \inter-86K, our strategy-annotated training corpus for supervised and RL training. Empirically, ARC substantially strengthens the core τ/τ^2 tool-use benchmarks, while \inter\ reduces time-to-first-token from 4.91s to 1.27s relative to a think-style baseline. Together, these results suggest that a central bottleneck in open-ended interactive learning is not only how agents are rewarded, but whether their behaviors are compared fairly in the first place. The ARC implementation and \inter-86K training data will be released.
