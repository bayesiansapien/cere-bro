---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.07153
url: https://huggingface.co/papers/2605.07153
arxiv_url: https://arxiv.org/abs/2605.07153
date: 2026-05-13
---

# Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in LLMs

Reinforcement learning (RL) has achieved remarkable success in LLM reasoning, but whether it can also improve direct recall of parametric knowledge remains an open question. We study this question in a controlled zero-shot, one-hop, closed-book QA setting with no chain-of-thought, training only on binary correctness rewards and applying fact-level train-test deduplication to ensure gains reflect improved recall rather than reasoning or memorization. Across three model families and multiple factual QA benchmarks, RL yields ~27% average relative gains, surpassing both training- and inference-time baselines alike. Mechanistically, RL primarily redistributes probability mass over existing knowledge rather than acquiring new facts, moving correct answers from the low-probability tail into reliable greedy generations. Our data-attribution study reveals that the hardest examples are the most informative: those whose answers never appear in 128 pre-RL samples (only ~18% of training data) drive ~83% of the gain, since rare correct rollouts still emerge during training and get reinforced. Together, these findings broaden the role of RL beyond reasoning, repositioning it as a tool for unlocking rather than acquiring latent parametric knowledge.
