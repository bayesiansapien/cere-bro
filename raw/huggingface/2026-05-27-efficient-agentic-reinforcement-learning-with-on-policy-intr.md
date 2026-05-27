---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.26952
url: https://huggingface.co/papers/2605.26952
arxiv_url: https://arxiv.org/abs/2605.26952
date: 2026-05-27
upvotes: 8
---

# Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge Boundary Enhancement

Agentic reinforcement learning (RL) has proven effective for training LLM-based agents with external tool-use capabilities. However, we identify that agentic RL training induces increasing redundant tool calls and blurs the model's intrinsic knowledge boundary, where the model fails to distinguish when tools are needed versus when parametric knowledge suffices. Existing solutions based on reward shaping create coarse-grained optimization targets that tend to incentivize indiscriminate tool-call suppression, leading to reward hacking. In this paper, we propose AKBE (Agentic Knowledge Boundary Enhancement), an on-policy method that dynamically probes the model's intrinsic knowledge boundary through dual-path (with-tool and no-tool) rollouts during training. We define the knowledge boundary as the per-instance determination of whether tools are required and the minimum tool calls necessary. By comparing correctness across paths, AKBE categorizes trajectories and constructs targeted supervisory signals that guide efficient tool-use patterns for each question. These signals are integrated seamlessly into the agentic RL training loop. Experiments on seven QA benchmarks demonstrate that AKBE improves task accuracy by +1.85 on average and reduces tool calls by 18% over standard agentic RL, yielding 25% higher tool productivity without any accuracy-efficiency trade-off. Further analysis suggests its plug-and-play compatibility across different RL algorithms and the mechanism of each signal category.
