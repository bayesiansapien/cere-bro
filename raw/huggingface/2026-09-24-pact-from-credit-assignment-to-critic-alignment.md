---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.26355
url: https://huggingface.co/papers/2609.26355
arxiv_url: https://arxiv.org/abs/2609.26355
date: 2026-09-24
upvotes: 15
authors: ["Jiayan Fu", "Hang Xu", "Yong Zhang", "Zhaokai Luo", "Yao Hu", "Dongyan Zhao", "Mu Chuan"]
---

# PACT: From Credit Assignment to Critic Alignment

**Authors:** Jiayan Fu, Hang Xu, Yong Zhang, Zhaokai Luo, Yao Hu, Dongyan Zhao, Mu Chuan

**Upvotes:** 15

**Links:** [HuggingFace](https://huggingface.co/papers/2609.26355) · [arXiv](https://arxiv.org/abs/2609.26355)

Reinforcement learning has become a central component of large language model (LLM) post-training, yet token-level credit lacks a generally accepted mathematical definition, leaving its relationship to commonly used training signals unclear. We formulate three regularity conditions, namely Completeness, Prefix Consistency, and Neutrality, and prove that they uniquely determine token-level credit. This characterization provides a unified basis for explaining phenomena across existing algorithms and guides the development of an improved actor-critic training procedure. Through this lens, an ideal teacher in On-Policy Distillation (OPD) acts as an implicit critic, yielding an expected policy gradient proportional to that induced by token-level credit. Response-level REINFORCE Leave-One-Out (RLOO) signals match the expected policy-gradient contribution of token-level credit despite their coarser granularity. We further establish approximate credit sparsity under bounded outcome rewards and show how intermediate critic errors in Generalized Advantage Estimation (GAE) can become comparable to the underlying credit. These motivate Policy Aligned Critic Training (PACT), which adopts an Actor-then-Critic update order to apply importance sampling correction to critic training and better align the critic with the updated policy. In agentic mathematical reasoning, PACT achieves 72.87% average accuracy across four benchmarks, outperforming GRPO and PPO by 8.80 and 13.16 percentage points, respectively. On SWE-bench Verified, PACT achieves a pass rate of 67.4%, outperforming PPO, GRPO, and SAO by 2.4, 2.0, and 3.8 percentage points, respectively.
