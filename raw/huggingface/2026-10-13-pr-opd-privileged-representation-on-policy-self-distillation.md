---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2609.36642
url: https://huggingface.co/papers/2609.36642
arxiv_url: https://arxiv.org/abs/2609.36642
date: 2026-10-13
---

# PR-OPD: Privileged Representation On-policy Self-Distillation for Agentic Reinforcement Learning

Language-model agents are usually trained by reinforcement learning from one reward per episode, and privileged self-distillation enriches it by letting the same policy, given a skill, teach its skill-free self through token probabilities. However, we identify two phenomena that question this channel. Invisible Advantage: a skill in context lifts WebShop success from 42.2% to 56.2%, yet changes the probabilities of fewer than a quarter of the sampled tokens. Much to Align: a skill changes the hidden states of over 80% of response tokens, in a way that linear probes can trace back to the specific skill. To exploit this, we propose Privileged Representation On-policy Self-Distillation (PR-OPD). After a GRPO warm start, the policy writes a hindsight skill for each trajectory, re-reads its own responses with that skill as a stop-gradient teacher, and aligns its projected hidden states to the teacher's at every layer alongside the reward objective, with no external skill library, separate teacher, or inference overhead. On ALFWorld and WebShop with two backbones, PR-OPD achieves the best overall results in every setting, improving over GRPO by up to 4.7 points in ALFWorld success and 14.0 points in WebShop accuracy. Code is available at https://github.com/balibata/PR-OPD.
