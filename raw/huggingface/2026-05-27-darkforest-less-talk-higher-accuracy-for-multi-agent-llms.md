---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.25188
url: https://huggingface.co/papers/2605.25188
arxiv_url: https://arxiv.org/abs/2605.25188
date: 2026-05-27
upvotes: 1
---

# DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs

Multi-agent LLM systems improve reasoning by combining outputs from multiple agents, but interaction-heavy methods can introduce error propagation and high communication overhead. When agents exchange raw responses or reasoning traces, incorrect intermediate reasoning may be adopted and amplified, leading to confident but wrong consensus; multi-round communication also increases token consumption, latency, and inference cost. In this paper, we propose a controlled-communication coordination framework named DarkForest. DarkForest first keeps agents independent, so each agent produces an answer without seeing the others' outputs. It then parses the raw responses into structured candidate records, groups semantically equivalent candidates into clusters, and estimates a calibrated belief distribution over these clusters using agent reliability, confidence, parse quality, support-pattern reliability, and independence corrections. A coordinator receives only policy-permitted evidence from this belief state with controlled communication. Experiments on six reasoning benchmarks show that DarkForest achieves leading overall quality, improves the strongest baseline by up to 30.7% on benchmark metrics, and reduces token consumption by up to 6.5x compared with communication-heavy baselines.
