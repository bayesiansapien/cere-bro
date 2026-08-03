---
source: farmer/huggingface
farmed: 2026-08-03T12:36:11.005337+05:30
arxiv_id: 2607.23802
url: https://huggingface.co/papers/2607.23802
arxiv_url: https://arxiv.org/abs/2607.23802
date: 2026-08-03
---

# From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement

Reinforcement Learning with Verifiable Rewards (RLVR) has driven recent progress in reasoning-oriented large language models (LLMs) by enabling large-scale optimization. However, its applicability remains largely limited to domains such as mathematics and coding, where correctness can be deterministically verified. Open-ended tasks instead often rely on human preferences, reward models, or LLM-based judges, introducing evaluation bias, judge capability bottlenecks, and additional inference costs.Drawing on the principle of self-supervised learning, which constructs pretext tasks to derive supervision from the data itself, we propose Reinforcement Learning with Self-Verifiable Rewards (RLSVR), a task-transformation-based training paradigm for extending RLVR to open-ended tasks. RLSVR transforms open-ended tasks into verifiable proxy environments whose internal rules and interaction outcomes automatically generate reward signals. We instantiate RLSVR with SpyRL, a multi-agent self-play environment inspired by Who Is the Spy?. Agents receive asymmetric information, complete the same target task, and vote to identify a designated spy. Because the spy identity is predetermined, voting outcomes provide fully verifiable rewards, while successful identification remains closely related to output quality. Experiments on text summarization, creative writing, and mathematical reasoning show that SpyRL outperforms existing self-improvement methods on non-verifiable tasks and yields consistent gains on verifiable reasoning tasks. These results demonstrate that task transformation can extend scalable RLVR-based self-improvement beyond inherently verifiable domains. Models and code have been released at https://github.com/wangqinsi1/SpyRL.
