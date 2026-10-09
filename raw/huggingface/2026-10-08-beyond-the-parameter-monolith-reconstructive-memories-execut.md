---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.311562+05:30
arxiv_id: 2610.04012
url: https://huggingface.co/papers/2610.04012
arxiv_url: https://arxiv.org/abs/2610.04012
date: 2026-10-08
---

# Beyond the Parameter Monolith: Reconstructive Memories, Executable Skills, and Residual Assembly for Language Models

Language-model systems can separate contextual computation, persistent storage, and exact execution instead of updating all capabilities through one shared parameter system. We investigate FEM-ASM, a finite-element-method-inspired organization in which independently constructed document states and deterministic executable skills contribute typed proposals to a shared language-model state. An explicit residual operator reconciles proposals attached to common interface nodes. We evaluate this organization through controlled experiments and negative results rather than claiming a physical finite-element formulation of language. An attention-free Multi-Mesh prototype learns causal language modeling but does not establish competitive general capability. A versioned store contains 52,809 reconstructive memory elements near a 1.7-billion-floating-value budget; reconstruction is incomplete, with approximately 75\% token accuracy. Support-aware lexical indices make these elements addressable under provenance-controlled query construction. For executable arithmetic, positional result observations substantially improve neural rendering relative to a repeated global result vector, and output substitutions change the model's preferred answer. A bounded attachment demonstration further measures the effect of making selected evidence available, without establishing the utility of loading an entire multi-billion-value store. The results support a separation of storage, execution, and neural coordination, while identifying unresolved limitations in question-only retrieval, unrestricted answer generation, and end-to-end efficiency.
