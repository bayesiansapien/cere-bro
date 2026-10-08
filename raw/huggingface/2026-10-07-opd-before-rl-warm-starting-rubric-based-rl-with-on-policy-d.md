---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.02781
url: https://huggingface.co/papers/2610.02781
arxiv_url: https://arxiv.org/abs/2610.02781
date: 2026-10-07
---

# OPD Before RL: Warm-Starting Rubric-Based RL with On-Policy Distillation

Many useful language-model tasks cannot be evaluated by exact outcome verification. Rubric-based reinforcement learning (RL) addresses this issue by scoring open-ended responses against explicit criteria. However, because the reward is assigned after the complete response, the training signal does not directly identify which individual decisions contributed to the final score. We propose a two-stage training framework that uses rubrics first as privileged teacher context for dense token-level supervision, then as rewards for further RL. In the first stage, rubric-privileged on-policy distillation (RP-OPD), a student without access to the rubric matches a rubric-aware teacher's next-token distributions at student-generated prefixes. In the second stage, RL directly optimizes the rubric reward and improves beyond the observed distillation plateau. We evaluate the framework on health and science tasks using open-weight models. Across HealthBench, ResearchQA, and RubricHub Science, we compare post-training methods and vary the amount of SFT or RP-OPD training before RL, finding that our two-stage framework achieves the highest scores among the methods evaluated. RP-OPD + RL shows limited signs of reward hacking on RubricHub Science, whereas the SFT + RL baseline increasingly receives high rewards for claims of rubric compliance without providing the required content. These findings support using rubrics to guide on-policy distillation before applying rubric-based RL.
