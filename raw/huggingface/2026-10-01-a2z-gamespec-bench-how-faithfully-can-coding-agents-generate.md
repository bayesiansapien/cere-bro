---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349385+05:30
arxiv_id: 2609.39564
url: https://huggingface.co/papers/2609.39564
arxiv_url: https://arxiv.org/abs/2609.39564
date: 2026-10-01
---

# A2Z GameSpec-Bench: How Faithfully Can Coding Agents Generate Games from Game Design Specifications?

Delegating complete application development to coding agents requires preserving the intended design rather than simply producing plausible outputs through naive prompting. Game development provides a demanding testbed, as long-form Game Design Documents (GDDs) describe requirements that must work together across game logic, visual rendering, and player interactions. However, existing game-development benchmarks typically use compact specifications and provide limited support for evaluating interdependent requirements across these aspects in long-form GDDs. We introduce A2Z GameSpec-Bench, a benchmark of 100 long-form GDDs for evaluating end-to-end game development by agents. We measure faithfulness by checking whether the game satisfies the GDD requirements and preserves the relationships among them. Each GDD is turned into a dependency-aware contract that contains rules, constraints, and prerequisite relations. Following game-development practices, we combine source-code inspection with agent-generated test policies for scenario-based replay and adaptive playtesting. The contract remains fixed across agents and revision rounds, while judgments and evidence linked to the same requirements support consistent comparison and failure detection. Our evaluations show that current agents struggle to jointly satisfy interdependent requirements across code implementation and actual play. Requirement-specific feedback improves GDD Fidelity by 10.9% relative to self-revision after two rounds. A2Z GameSpec-Bench assesses end-to-end specification-following ability beyond implementation judgments and provides targeted feedback to support more faithful game development. Code and datasets are available at https://a2z-gamespec-bench.github.io.
