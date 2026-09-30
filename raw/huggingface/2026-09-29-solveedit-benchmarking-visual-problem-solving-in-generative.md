---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.931625+00:00
arxiv_id: 2609.35504
url: https://huggingface.co/papers/2609.35504
arxiv_url: https://arxiv.org/abs/2609.35504
date: 2026-09-29
---

# SolveEdit: Benchmarking Visual Problem Solving in Generative Models

Machine intelligence is often evaluated through abstract reasoning problems, yet many real-world problems are visual, such as arranging objects, repairing layouts, or tracing routes. Solving these problems requires understanding a scene, inferring what must change to achieve a goal, and realizing that change without disturbing unrelated content. However, existing benchmarks mainly evaluate perception, generation, or explicitly specified transformations, leaving goal-driven visual problem solving underexplored. To bridge this gap, we introduce SolveEpIT, a benchmark for visual problem solving through scene transformation. Given an image and a goal, a model must infer a valid transformation from the request, the scene, or a visually expressed rule, then execute it while preserving unrelated content. SoLvEEDrr contains 2,728 cases. Atomic transition contracts specify required and protected conditions, enabling SoLvEScoRE to measure completion and unintended changes without a single reference output. The strongest evaluated model achieves only57.0% SolvEScore. We further introduce SolveEdiT-PLAN, a two-stage visual planner that instantiates the transition before generation. Under matched single-generation evaluation, it improves SoLvEScoRE by 9.1 points on average across three tested generators, including a gain from 57.0% to 71.6% for GPT-Image-2, without modifying the editor.
