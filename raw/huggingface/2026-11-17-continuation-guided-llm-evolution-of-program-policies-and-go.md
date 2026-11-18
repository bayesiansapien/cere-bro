---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.112652+00:00
arxiv_id: 2611.19537
url: https://huggingface.co/papers/2611.19537
arxiv_url: https://arxiv.org/abs/2611.19537
date: 2026-11-17
---

# Continuation-Guided LLM Evolution of Program Policies and Goal Compilers in Craftax

Coding agents can synthesize and optimize code-based policies from simulator feedback, allowing the resulting program to act with zero inference model calls. But for long horizon tasks, two challenges arise: local improvements can hurt final success and switching to a new objective requires another expensive synthesis run. We propose a framework that first develops competence by refining the policy through a feedback cascade, moving from episode returns to hierarchical goals and belief updates which can be scored densely from simulator. In the Craftax game, a partially observed and procedurally generated environment, refinements via episode level feedback stall at <1% final-level arrival, whereas with the feedback cascade the optimized policy reaches the final stage 50% of time (28% final boss defeats). Furthermore, to make this competence reusable towards new goals, we factor the previous controller into an environment interpreter I (models, memory, skills) and a rule program p_0, and we show that coding agents can optimize a reusable goal compiler C_θ that maps structured tasks g into new rule programs p_g. Across five independent compiler searches trained only on short tasks, the resulting compilers successfully transfer zero-shot to longer tasks without any task-specific tuning nor inference-time LLM calls: continuation-scored feedback and a fixed machine with an editable program together turn a single-task competent policy into a reusable one.
  Code at: https://github.com/vicgalle/craftax-program-policies
