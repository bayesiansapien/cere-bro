---
source: farmer/huggingface
farmed: 2026-06-03T06:14:02Z
arxiv_id: 2606.03102
url: https://huggingface.co/papers/2606.03102
arxiv_url: https://arxiv.org/abs/2606.03102
date: 2026-06-03
---

# Small RL Controller, Large Language Model: RL-Guided Adaptive Sampling for Test-Time Scaling

Test-time scaling improves the reasoning performance of large language models but incurs substantial cost in both total computation and latency. Existing adaptive sampling methods partially mitigate this issue by dynamically deciding when to stop sampling, yet they typically rely on heuristic rules or rely on distribution assumptions. In this work, we formulate adaptive sampling as a Markov decision process (MDP). We train a lightweight sampling controller with reinforcement learning (RL) to jointly balance answer correctness, latency, and computation cost. At each round, the controller decides to stop sampling or to acquire additional samples. Our method is lightweight which only relies on statistics of final answers, and can be trained and deployed on CPU. We further show that the resulting framework admits an interpretation as the Lagrangian relaxation of a constrained optimization problem with explicit budget constraints. Experiments against strong baselines such as ASC and ESC show that our method achieves improved trade-offs among answer correctness, sampling rounds, and total samples required.
