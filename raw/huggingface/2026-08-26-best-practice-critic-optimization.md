---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.23566
url: https://huggingface.co/papers/2608.23566
arxiv_url: https://arxiv.org/abs/2608.23566
date: 2026-08-26
upvotes: 2
---

# Best Practice Critic Optimization

Group-based reinforcement learning methods such as GRPO for large language models avoid training a critic by sampling multiple responses for each prompt. A reliable critic could instead estimate token-level advantages from one response, but standard critic-based training recipes are often unstable. We study this instability and develop **Best Practice Critic Optimization (BPCO)**, a recipe that combines DPPO, value predictions bounded to the reward range, Monte Carlo value targets, unnormalized policy advantages, and length-adaptive generalized advantage estimation. Because the critic is used only during training, BPCO can also condition it on reward-defining information, such as a reference answer or grading rubric, that is hidden from the policy. Controlled experiments isolate the effect of each design choice. Across mathematical reasoning tasks with models ranging from 1.5B parameters to 30B-A3B mixtures of experts, BPCO improves a strong critic-based baseline consistently, and matches or exceeds a group-based baseline while sampling one response per prompt. The same recipe also improves learning with rubric-based rewards. These results show that a carefully designed critic provides a reliable alternative to group-relative advantage estimation. Code is available at https://github.com/QPHutu/golden_critic.
