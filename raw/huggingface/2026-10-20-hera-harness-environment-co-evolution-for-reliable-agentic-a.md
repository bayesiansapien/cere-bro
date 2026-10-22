---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.06563
url: https://huggingface.co/papers/2610.06563
arxiv_url: https://arxiv.org/abs/2610.06563
date: 2026-10-20
---

# HERA: Harness-Environment Co-Evolution for Reliable Agentic Abstention

Large language model (LLM) agents are increasingly capable of acting in complex tool-use environments, yet they often fail to recognize when tasks are infeasible and no valid solution exists. Recent work has formalized this reliability gap as the problem of agentic abstention, and existing approaches typically optimize a model or agent harness against a fixed set of tasks, leading to limited generalization to unseen failure modes. We introduce HERA, a framework for harness-environment co-evolution for agentic abstention. HERA consists of (i) a pipeline to automatically construct verifiable pairs of feasible and infeasible tasks by applying controlled environment mutations that transform solvable tasks into cases requiring abstention, and (ii) a co-evolution procedure in which performance failures on previous tasks are used to drive harness adaptation and generate new execution environments and tasks geared towards previous weaknesses. On held-out evaluation tasks, an evolved harness from HERA improves abstention accuracy from 61.7% to 83.3% while improving feasible-task completion from 68.3% to 76.7%, achieving the highest abstention and feasible-task completion among the compared methods. The resulting best harness transfers across 19 other LLMs, improving abstention accuracy by 15.3 percentage points on average without any model-specific optimization, and enabling smaller models to match the performance of more powerful models at an estimated 85% lower cost.
