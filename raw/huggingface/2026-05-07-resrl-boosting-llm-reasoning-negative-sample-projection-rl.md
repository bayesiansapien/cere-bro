---
source: farmer/huggingface
farmed: 2026-05-08T00:00:00Z
arxiv_id: "2605.00380"
url: https://huggingface.co/papers/2605.00380
arxiv_url: https://arxiv.org/abs/2605.00380
date: 2026-05-07
---

# ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning

Reinforcement Learning with Verifiable Rewards (RLVR) enhances reasoning of Large Language Models (LLMs) but usually exhibits limited generation diversity due to the over-incentivization of positive rewards. Although methods like Negative Sample Reinforcement (NSR) mitigate this issue by upweighting penalty from negative samples, they may suppress the semantic distributions shared between positive and negative responses. To boost reasoning ability without losing diversity, this paper proposes negative sample projection Residual Reinforcement Learning (ResRL) that decouples similar semantic distributions among positive and negative responses. We theoretically link Lazy Likelihood Displacement (LLD) to negative-positive head-gradient interference and derive a single-forward proxy that upper-bounds representation alignment to guide conservative advantage reweighting. ResRL then projects negative-token hidden representations onto an SVD-based low-rank positive subspace and uses projection residuals to modulate negative gradients, improving reasoning while preserving diversity and outperforming strong baselines on average across twelve benchmarks spanning Mathematics, Code, Agent Tasks, and Function Calling. Notably, ResRL surpasses NSR on mathematical reasoning by 9.4% in Avg@16 and 7.0% in Pass@128. Code is available at https://github.com/1229095296/ResRL.git.
