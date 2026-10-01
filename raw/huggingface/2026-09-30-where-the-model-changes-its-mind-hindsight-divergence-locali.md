---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36864
url: https://huggingface.co/papers/2609.36864
arxiv_url: https://arxiv.org/abs/2609.36864
date: 2026-09-30
---

# Where the Model Changes Its Mind: Hindsight-Divergence Localization for Efficient Reinforcement Learning with Verifiable Rewards

Group-relative methods for reinforcement learning with verifiable rewards (RLVR) learn from differences in rollout outcomes. Independently sampling complete trajectories is costly and does not explicitly explore the decision space at critical positions. Feedback on a completed trajectory can reveal which earlier choices the policy reconsiders, suggesting where to sample alternative continuations. We introduce Hindsight-Divergence Localization (HDL), which uses hindsight-induced changes in token log-likelihoods to select branch points. HDL generates a small number of complete root trajectories and fills each training group with continuations from the selected positions under the original task context. Each continuation reuses its root prefix and contributes policy updates only through its newly generated suffix, reducing generation cost while focusing additional exploration and learning on decisions after branching. Experiments with three models across math, code, and agent tasks show gains in both rollout efficiency and task performance. Compared with GRPO at matched group sizes and training steps, HDL yields up to a 2.5times reduction in generated tokens and a 1.8times speedup in rollout wall-clock time. Despite this reduced generation budget, HDL improves performance across all three domains, with gains of up to 12.5 points on agent tasks.
