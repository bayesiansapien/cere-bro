---
source: farmer/huggingface
farmed: 2026-06-07T04:51:04Z
arxiv_id: 2606.03092
url: https://huggingface.co/papers/2606.03092
arxiv_url: https://arxiv.org/abs/2606.03092
date: 2026-06-07
---

# The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs

Inference-time scaling has emerged as a critical avenue for enhancing Large Language Models' performance, yet real-world deployment is constrained by strict computational budgets. In this work, we formulate inference budget allocation as a global constrained optimization problem governed by economic principles. By modeling per-query reasoning utility with a shifted-surge function, we derive an optimal allocation policy based on a global shadow price that equilibrates marginal utility under resource scarcity. Based on this theory, we propose Constrained Latent-utility Equilibrium Allocation for Reasoning (CLEAR). It performs rational abandonment and reallocates resources from insolvent queries to solvable queries near their emergence thresholds.
  Extensive experiments on several reasoning tasks with different traffic streams demonstrate that CLEAR significantly improves the Pareto frontier of total token cost versus mean accuracy. In resource-scarce regimes, CLEAR achieves up to a 3x improvement in global accuracy compared to uniform allocation.
