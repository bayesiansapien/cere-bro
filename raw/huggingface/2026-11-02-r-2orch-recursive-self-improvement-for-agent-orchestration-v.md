---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.495669+05:30
arxiv_id: 2610.22740
url: https://huggingface.co/papers/2610.22740
arxiv_url: https://arxiv.org/abs/2610.22740
date: 2026-11-02
---

# R^2Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop

In recent years, agentic orchestration has been widely applied to solve complex human tasks. However, existing orchestration learning still faces key challenges, including hand-designed curricula, advantage collapse when a task's rollouts all reach the same outcome, and unreliable evaluation signals that judge each skill by one noisy score. To address these challenges, we propose R^2Orch, a new paradigm of Recursive Self-Play Orchestration: an inner loop of self-play that improves the orchestrator on self-chosen tasks, and an outer loop that improves how the inner loop improves. To support this paradigm, we introduce Recursive Learnability, a training objective that rewards a Proposer for choosing tasks whose rollouts keep reaching different outcomes as skills are withdrawn. Built on this objective, we further propose Skill Withdrawal, in which the outer loop withdraws each skill once a controlled evaluation within self-play shows that the orchestrator performs as well without it. Moreover, the two loops form one cycle: failures are distilled into skills, skills into parameters, and withdrawals lead the Proposer to new failures, so the orchestrator moves toward zero-skill deployment. Experimental results on twelve datasets show that R^2Orch consistently outperforms baselines across question answering, math, code, and interactive tasks. Our code is available at https://github.com/beita6969/R2Orch.
