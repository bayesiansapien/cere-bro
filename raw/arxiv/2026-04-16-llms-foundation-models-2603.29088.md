---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.29088
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2603.29088
published: 2026-04-16
authors: Fabian Gloeckle, Mantas Baksys, Darius Feher
---

# WybeCoder: Verified Imperative Code Generation

**arXiv:** https://arxiv.org/abs/2603.29088
**Authors:** Fabian Gloeckle, Mantas Baksys, Darius Feher

## Abstract

arXiv:2603.29088v2 Announce Type: replace-cross  Abstract: Recent progress in large language models (LLMs) has substantially advanced automatic code generation and formal theorem proving, yet software verification has not seen comparable gains. To address this gap, we propose WybeCoder, an agentic code verification framework that enables prove-as-you-generate development, in which code, invariants, and proofs co-evolve. WybeCoder builds on a recent framework that combines automatic verification condition generation and SMT solving with interactive proofs in Lean. To enable systematic evaluation, we translate two benchmarks for functional verification in Lean, Verina and Clever, into equivalent imperative code specifications. On complex algorithms such as Heapsort, we observe consistent performance improvements as we scale our approach, synthesizing dozens of valid invariants and dispatching dozens of subgoals, ultimately producing hundreds of lines of verified code and overcoming plateaus reported in previous work. Our best system solves 74% of Verina tasks and 62% of Clever tasks at moderate compute budgets, substantially surpassing previous evaluations and paving the way for the automated construction of large-scale datasets of verified imperative code.
