---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.298641+00:00
arxiv_id: 2611.06483
url: https://huggingface.co/papers/2611.06483
arxiv_url: https://arxiv.org/abs/2611.06483
date: 2026-11-05
---

# What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?

While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth K and interaction depth T via Pass@(K,T), we show that trajectory-level RL advantages depend on sufficient turn budgets, diminishing significantly when budgets tighten. Besides, agentic RL does not uniformly elevate single-step decision quality; rather, its strength concentrates in error recovery and long-horizon resilience. To mitigate the deployment risks caused by this budget dependence, we provide a preliminary discussion on the benefits and limitations of process supervision signals and introduce BudgetMix RL as an alternative that varies interaction budgets during training. Experiments demonstrate that BudgetMix RL achieves robust performance across diverse execution settings. Project Page: https://rethinking-agentic-rl.github.io/
