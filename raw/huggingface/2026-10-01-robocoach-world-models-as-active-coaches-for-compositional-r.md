---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349282+05:30
arxiv_id: 2609.39685
url: https://huggingface.co/papers/2609.39685
arxiv_url: https://arxiv.org/abs/2609.39685
date: 2026-10-01
---

# RoboCoach: World Models as Active Coaches for Compositional Robot Skills

Long-horizon robot manipulation reuses skills across many task compositions, but improving these compositions with additional end-to-end demonstrations is costly. A practical self-improving system must decide both what to teach next and where to apply that supervision. We present ROBOCOACH, a world-model-guided coaching framework that uses imagined failures to guide demonstration requests and expert updates. Its Route-Imagine-Diagnose-Improve (RIDI) loop executes reusable skill experts inside COACHWORLD, our shared action-conditioned world model, and uses a progress judge to record the first subtask that fails to complete. Aggregated records select which subtask demonstrations to acquire and which expert adapters to update. Across two simulation suites and two real-robot platforms, imagined and deployed success correlate over 22 task-policy pairs (rho = 0.840). Controlled comparisons show that our coaching method outperforms matched baselines under matched data budgets and update schedules. With only 150 additional subtask demonstrations, success rises from 13.3% to 75.0% on Franka and from 40.0% to 83.8% on AgileX. The coached experts also transfer to four held-out compositions, achieving an average success of 35.0%, compared with 0% for a shared-policy baseline updated with uniformly acquired demonstrations. Together, these results show that world models can serve as active coaches, turning imagined failures into targeted supervision for modular policy improvement. Project Page: https://robocoach-ai.github.io/
