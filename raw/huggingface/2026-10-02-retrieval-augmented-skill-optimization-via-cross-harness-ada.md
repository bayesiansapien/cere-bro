---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.818662+00:00
arxiv_id: 2609.38024
url: https://huggingface.co/papers/2609.38024
arxiv_url: https://arxiv.org/abs/2609.38024
date: 2026-10-02
---

# Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation

An agent skill is a reusable, actionable natural-language artifact that guides an agent to perform a task effectively under a given harness. Recent studies have explored the optimization of agent skills, contributing to a growing collection of publicly available skills spanning diverse tasks, domains, and harnesses. Despite millions of publicly shared skills, existing skill optimization methods largely overlook this accumulated knowledge, instead relying solely on expensive agent rollouts to iteratively refine skills for a target task. To address this, we propose Retrieval-Augmented Skill Optimization (RASO), a framework that leverages an external skill corpus as prior knowledge throughout skill optimization. RASO retrieves relevant knowledge from existing skills and adapts it to the target task and harness via Cross-Harness Adaptation, accounting for mismatches in both domain and harness. RASO comprises two complementary stages: Retrieval-Augmented Skill Initialization (RASI) constructs a knowledge-grounded initial skill without requiring agent rollouts, while Retrieval-Augmented Skill Update (RASU) iteratively refines the skill by retrieving external knowledge guided by execution feedback. Across four agent benchmarks and two models, extensive experiments show that RASO consistently outperforms baselines without retrieval-augmented skill initialization and updating.
