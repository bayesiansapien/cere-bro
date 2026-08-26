---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.24696
url: https://huggingface.co/papers/2608.24696
arxiv_url: https://arxiv.org/abs/2608.24696
date: 2026-08-26
upvotes: 7
---

# On-policy Distillation with Verifiable Reward

Reinforcement Learning with Verifiable Rewards (RLVR) and on-policy distillation (OPD) have become two widely adopted paradigms for post-training large language models. However, RLVR suffers from sparse task-level feedback, while OPD provides dense token-level guidance but ignores trajectory correctness, limiting its performance to that of the teacher. Combining them is a promising direction: OPD supplies dense supervisory signals, while RLVR provides task-level correctness. Nevertheless, existing integrations often rely on weighted combination or heuristic switching, introducing extra hyperparameters and trade-offs. We propose On-policy Distillation with Verifiable Reward (OPDVR), a simple yet effective method that seamlessly combines OPD and RLVR without adding any hyperparameters. We first reformulate the implicit reward of sampled-token OPD based on trajectory correctness, then apply a ReLU gating mechanism to ensure that correct trajectories receive non-negative rewards and incorrect ones receive non-positive rewards---thereby aligning the distillation signal with task success while preserving the teacher's distributional guidance. Furthermore, our modification transforms sampled-token OPD into a proper RLVR method, making it readily combinable with any policy gradient algorithm, such as GRPO. Experiments on six reasoning benchmarks show that OPDVR consistently outperforms standard OPD. Our code is available at https://github.com/LeapLabTHU/OPDVR.
