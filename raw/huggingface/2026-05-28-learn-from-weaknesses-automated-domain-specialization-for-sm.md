---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.28775
url: https://huggingface.co/papers/2605.28775
arxiv_url: https://arxiv.org/abs/2605.28775
date: 2026-05-28
---

# Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents

Computer-use agents (CUAs) have recently made substantial progress, but deploying a separate large expert for each software domain remains expensive. Small open computer-use agents are more practical specialization targets, but they remain substantially weaker and exhibit uneven domain-specific failures. A straightforward remedy is to synthesize large-scale training data for the target domain, yet we find that this naive approach yields only marginal improvements. Building on this observation, we introduce LearnWeak, an annotation-free specialization framework for small computer-use agents that uses a stronger reference agent to identify the student's weaknesses in the target domain, synthesize targeted tasks, and construct supervision automatically. LearnWeak further introduces an error-aware specialization objective that disentangles planning and execution errors, enabling more behaviorally precise updates than broad uniform supervision. On OSWorld, LearnWeak achieves average gains of 11.6 and 11.1 percentage points over EvoCUA-8B and OpenCUA-7B, respectively, across eight domains. We also validate that our student-aware dataset generation and training approaches outperform existing autonomous trajectory generation and training baselines. Our work highlights the importance of student awareness in both data synthesis and agent training, pointing toward a more principled and efficient path for specializing small computer-use agents in diverse domains.
