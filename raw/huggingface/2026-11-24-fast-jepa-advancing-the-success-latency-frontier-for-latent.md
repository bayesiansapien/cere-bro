---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.928522+00:00
arxiv_id: 2611.25927
url: https://huggingface.co/papers/2611.25927
arxiv_url: https://arxiv.org/abs/2611.25927
date: 2026-11-24
---

# Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models

Latent world models predict the outcomes of action sequences, but comparing candidate plans through recursive rollout remains expensive at test time. We introduce Fast-JEPA, a latent world model planning framework that advances the success-latency Pareto frontier of predictive search. Fast-JEPA reorganizes predictive computation to support effective action-sequence search at low planning cost. It constructs a goal-directed plan to guide search and directly predicts the outcomes of complete candidates for efficient comparison, avoiding recursive state rollout during refinement. Across PushT, Reacher, Cube, and TwoRoom, Fast-JEPA achieves 96.50% average success rate with 2.41x faster planning than INTACT. Search-budget sweeps show that its competitive success and low latency extend across candidate counts and refinement depths. We further introduce DynaGoal, a benchmark for evaluating world-model planning under dynamic out-of-distribution conditions, execution deadlines, and controlled response delays. Fast-JEPA achieves average success rates of 73.83% on DynaGoal-Shift and 87.67% on DynaGoal-Deadline, demonstrating the practical value of low-latency predictive planning under changing control conditions and execution-time constraints. Our code is available at https://github.com/Sofilyzia/Fast-JEPA.
