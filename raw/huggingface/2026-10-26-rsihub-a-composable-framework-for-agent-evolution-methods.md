---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.798966+00:00
arxiv_id: 2610.32253
url: https://huggingface.co/papers/2610.32253
arxiv_url: https://arxiv.org/abs/2610.32253
date: 2026-10-26
---

# RSIHub: A Composable Framework for Agent-Evolution Methods

Agent-evolution methods use execution feedback to improve prompts, skills, tools, and orchestration, but their implementations often rebuild the same experimental machinery. We present RSIHub, an open-source framework for building, comparing, and extending these methods on shared infrastructure. Recipes compose reusable operators and declare mutable resources; RSIHub supplies execution, evaluation, recovery, and lineage. Researchers can focus on evolution policy while evaluation stays outside the mutable surface and results remain tied to candidates and evaluation conditions. We instantiate AHE, Hyperagents, A-Evolve, and GEPA without modifying the framework core, keeping method-specific logic in recipes and operators. We evaluate them with MiniSWE and Codex on Terminal Bench 2 and τ^3 Banking under fixed model and evaluator configurations. The largest observed overall pass@1 gain is 13.5 percentage points, while method rankings vary across settings and optimization gains do not always transfer to held-out tasks. RSIHub provides a common protocol for comparing evolution policies, inspectable candidate histories, and reusable components for developing new methods.
