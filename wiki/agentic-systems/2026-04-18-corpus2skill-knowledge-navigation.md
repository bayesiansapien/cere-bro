# Corpus2Skill: Don't Retrieve, Navigate

**Date:** 2026-04-18  
**Tier:** 2 — Agents / RAG  
**arXiv:** [2604.14572](https://arxiv.org/abs/2604.14572)  
**Raw:** [source](../../raw/huggingface/2026-04-18-dont-retrieve-navigate-distilling-enterprise-knowledge-into.md)

## TL;DR

Standard RAG treats the model as a passive consumer of search results — it sees retrieved chunks but never the full structure of the knowledge base. Corpus2Skill compiles the document corpus into a hierarchical skill tree offline, then lets an agent navigate the tree at query time like a filesystem: start at the root, drill into topic branches, backtrack if needed, retrieve full documents by ID. Beats RAPTOR and agentic RAG on WixQA (enterprise customer-support QA benchmark).

## Key Findings

- **Offline compilation:** Documents are iteratively clustered and summarized by an LLM, materializing as a tree of progressively finer summaries — root = entire corpus, leaves = individual document summaries.
- **Active navigation:** At serve time, the agent gets the root view and calls skill functions to drill into branches or retrieve documents. It can backtrack if a branch is unproductive. It reasons over where to look, not just what to return.
- **Results:** Outperforms dense retrieval, RAPTOR (tree-structured retrieval), and agentic RAG baselines across all quality metrics on WixQA.

## What RAG Gets Wrong

RAG assumes the retrieval step is solved: the right chunks appear in the context, the model synthesizes them. In practice, multi-hop questions require evidence scattered across branches of the knowledge space. The model can't ask for more context mid-answer; it's stuck with what the retriever surfaced. Corpus2Skill replaces passive retrieval with active exploration: the agent knows the shape of the knowledge space and can navigate it.

The key insight is that the hierarchy is compiled *once* and reused for all queries. The navigation cost at serve time is just a few tree traversal steps. This makes it feasible even for large corpora.

## Research Angle

- How does the compiled hierarchy age? If the document corpus is updated, how much recompilation is needed?
- Corpus2Skill is a form of offline KV compression for RAG — the summaries at each level compress many documents into navigable representations. What's the information loss?
- Connection to agent routing: Corpus2Skill's tree navigation is a form of hierarchical routing across knowledge domains.

## Related Pages

- [Claude Code Architecture](2026-04-17-claude-code-architecture.md)
- [VAKRA: Agent Tool-Use Failure Modes](2026-04-16-vakra-agent-reasoning-failure-modes.md)
- [Agent Benchmarks](agent-benchmarks.md)
