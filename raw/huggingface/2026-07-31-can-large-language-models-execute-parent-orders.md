---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.28410
url: https://huggingface.co/papers/2607.28410
arxiv_url: https://arxiv.org/abs/2607.28410
date: 2026-07-31
---

# Can Large Language Models Execute Parent Orders?

Parent-order execution is a core problem in algorithmic trading, where the goal is to split a large order into smaller orders while reducing execution costs. Existing approaches either rely on pre-specified market assumptions that may not hold in practice, or require task-specific training that limits adaptability to new settings. To overcome these limitations, we present the first systematic study of large language models (LLMs) for parent-order execution. This extends the use of LLMs in finance from what to trade to how to execute. We propose PACE (Plan-Ahead Controlled Execution), a hierarchical framework that decomposes parent-order execution into long-horizon planning and short-horizon execution, requiring neither explicit market assumptions nor task-specific training. Experiments on Shenzhen Stock Exchange Level-1 data show that PACE outperforms TWAP, Almgren-Chriss, and learning-based baselines, exceeding the strongest baseline by 0.65 bps. Behavioral analysis reveals that LLMs make execution decisions differently from human investors: higher model confidence predicts better performance rather than worse returns, and the model trades earlier rather than procrastinating toward the deadline. These findings suggest that LLMs can complement human traders in execution decisions.
