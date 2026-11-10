---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.203994+00:00
arxiv_id: 2610.35959
url: https://huggingface.co/papers/2610.35959
arxiv_url: https://arxiv.org/abs/2610.35959
date: 2026-11-09
---

# AgentBaton: Efficient Model Collaboration in Agentic Tasks

Solving long-horizon agentic tasks requires language agents to interact with their environments over multiple steps, and reliable performance often comes from the expensive capable models available through cloud providers. Meanwhile, alternative efficient models with inferior performance but a much lower cost are emerging, including lower-tier cloud models and smaller open-weights models deployable on local hardware. This raises a natural question that remains less explored than traditional query-level routing: can capable and efficient models collaborate within a single long-horizon agentic task to substantially reduce cost while preserving task accuracy? In this paper, we systematically investigate key design choices for such collaboration through model handoffs, where one model takes over from another, focusing on handoff direction and context transfer. We find that efficient-to-capable handoffs generally underperform capable-only execution with limited or even no cost reduction, whereas capable-to-efficient handoffs at suitable stages of task progress largely preserve or even improve accuracy while substantially reducing cost. These findings suggest that a one-time, simple, well-timed handoff strategy is good enough for cost-effective agent collaboration, motivating AgentBaton, a lightweight detector that learns when to hand off from recurring patterns in task progress. Across 11 model pairs and two representative benchmarks, AgentBaton reduces API costs by 65.9% on average while largely preserving task accuracy, with accuracy gains of up to 8.8 percentage points over capable-only execution. Experiments across various reasoning-effort settings further show that AgentBaton extends the empirical accuracy-cost Pareto frontier.
