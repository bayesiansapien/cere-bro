---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.996831+05:30
arxiv_id: 2610.33245
url: https://huggingface.co/papers/2610.33245
arxiv_url: https://arxiv.org/abs/2610.33245
date: 2026-10-28
---

# AdaPRA: Process Reward Agents with Adaptive Rubrics for Data Science

Data science agents can automate end-to-end machine learning workflows, yet they remain far from competitive on human leaderboards. Agents make process errors such as insufficient exploration, unsound validation, coding bugs, and poor use of a fixed budget (re-running the same exploratory data analysis and baseline models in every attempt). We propose AdaPRA to address these issues: a persistent coding agent harness that accumulates knowledge across attempts on the same task, with rubric-guided process supervision that identifies and corrects errors. Our process reward agent audits the agent's trajectory and workspace by executing checks, and adapts its rubrics to each task. We find that rubrics seeded from easier tasks generalize to harder tasks, with rubric adaptation further improving performance. With five attempts per task, AdaPRA improves an 80B Qwen model's leaderboard percentile by 24.5 points on DSPredict-Easy and 14.8 points on DSPredict-Hard while reducing process errors. We also show that supervision with rubrics mined from one base model's runs improves another (DeepSeek-V3.2), and that AdaPRA beats DataPRM, a competitive PRM for data science. We also share our code for reproducibility.
