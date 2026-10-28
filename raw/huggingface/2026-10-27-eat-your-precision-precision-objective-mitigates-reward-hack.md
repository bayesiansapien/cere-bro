---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33512
url: https://huggingface.co/papers/2610.33512
arxiv_url: https://arxiv.org/abs/2610.33512
date: 2026-10-27
---

# Eat Your Precision: Precision Objective Mitigates Reward Hacking in Rubric-based RL

Rubric-based rewards enable effective reinforcement learning on non-verifiable tasks. However, because these rewards are typically defined as a weighted measure of rubric coverage, models are trained primarily to maximize a recall objective. As a result, RL-trained models produce responses that are more complete but also more verbose and contain more unnecessary or factually incorrect content, leading them to be less preferred than responses from the base model. To address this issue, we present the FORK reward, which jointly optimizes recall and a novel precision objective, which requires each unit of a model response to be both necessary and factually correct, as measured by rubric-driven necessity credits and a factual-correctness grader, respectively. Our experimental results show that FORK outperforms existing rubric-based RL methods and achieves Pareto-optimal performance that balances rubric coverage and overall response quality. Compared to the original recall-based reward, FORK substantially improves precision and reduces response length while achieving similar rubric coverage, which leads to significantly higher win rate compared to the base policy (e.g., from 10.6% to 68.0% on RubricHub-Medical and from 22.1% to 74.1% on HealthBench).
