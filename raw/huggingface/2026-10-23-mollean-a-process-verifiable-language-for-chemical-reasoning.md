---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.884841+00:00
arxiv_id: 2610.20459
url: https://huggingface.co/papers/2610.20459
arxiv_url: https://arxiv.org/abs/2610.20459
date: 2026-10-23
---

# MolLean: A Process-Verifiable Language for Chemical Reasoning

Chemical chain-of-thought can contain hallucinated structural and property claims. We thereby introduce MolLean, a process-verifiable language that grounds chemical reasoning in an explicit molecular state. A layered Lean-based kernel checks state transitions and assertions over molecular readouts, from primitive graph edits to compound transformations. Meanwhile, a typed witness protocol separates native structural checks from externally supplied measurements. We further introduce MolLean-MCP, a stateful tool interface that exposes these transitions, checks, and readouts during generation: the model receives feedback to decide its next action, and rejected actions leave the state unchanged. MolLean supports one-pass trace execution, whole-trace refinement, and interactive reasoning through MolLean-MCP. We evaluate these three modes with direct chain-of-thought on 8,800 matched examples across 12 tasks spanning molecular generation, editing, optimization, and reactions. With Qwen3.6-27B, whole-trace refinement outperforms direct chain-of-thought on all 12 tasks. MolLean-MCP complements whole-trace refinement with stepwise verification feedback, reaching better performance in reaction tasks. Together, these results highlight an executable foundation for chemical reasoning, in which explicit chemical commitments can be checked and revised rather than remaining solely in free-form explanations.
