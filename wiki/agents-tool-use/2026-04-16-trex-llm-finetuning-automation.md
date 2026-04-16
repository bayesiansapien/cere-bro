---
date: 2026-04-16
source: huggingface
arxiv: 2604.14116
---

# TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration

**TL;DR:** TREX is a multi-agent system that automates the full LLM training lifecycle — from requirement analysis and literature research to data recipe prep and model evaluation — modeled as a search tree that reuses historical results across trials.

## Key Findings

- Two-module architecture: **Researcher** (literature/data research, strategy formulation) + **Executor** (data prep, training, evaluation).
- Multi-round experimental process as a **search tree**: enables branching exploration, result reuse, and distilling insights across iterations.
- Introduces **FT-Bench**: 10 real-world fine-tuning tasks ranging from fundamental capability optimization to domain-specific improvement.
- Key insight: treating ML experimentation as tree search lets agents avoid redundant runs and build on prior results.

## Related Pages

- [Multi-Agent Systems](multi-agent-systems.md)
- [../llms-foundation-models/fine-tuning.md](../llms-foundation-models/fine-tuning.md)

**Raw source:** [../../raw/huggingface/2026-04-16-trex-automating-llm-fine-tuning-via-agent-driven-tree-based.md](../../raw/huggingface/2026-04-16-trex-automating-llm-fine-tuning-via-agent-driven-tree-based.md)
