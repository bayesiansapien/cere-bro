---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.03219
url: https://huggingface.co/papers/2611.03219
arxiv_url: https://arxiv.org/abs/2611.03219
date: 2026-11-03
---

# Can Coding Agents Sustain Continual Evolution without Forgetting?

Recently, harness self-evolution has emerged as an important paradigm for improving agent performance. Prior studies show that evolving the agent harness can effectively enhance agent capabilities without modifying the foundation model's parameters. We find that existing approaches largely study agent evolution on a single task. In practice, coding agents may need to handle multiple task types over time. Whether an agent harness can continuously evolve across multiple tasks without suffering from catastrophic forgetting remains an important open question.
  In this paper, we investigate this open question through a comprehensive empirical study of continual harness self-evolution. We organize three software engineering task datasets into six different evolution directions and apply two representative harness evolution methods to perform continual evolution along these directions. Our experimental results show that evolution on a subsequent dataset can substantially undermine the performance on previously seen datasets. For example, with DeepSeek-V4-Flash-0731, Meta-Harness improves its performance on SWE-Bench to 94.0% after evolution. However, after further evolution on FeatureBench, its performance on SWE-Bench drops to 32.0% by the fifth round, corresponding to a 66% relative decrease. Finally, based on our experimental findings, we identify several insights, providing directions for the continual self-evolution of agent harnesses. Code is available at https://github.com/THU-Agent/continual-harness-evolution.
