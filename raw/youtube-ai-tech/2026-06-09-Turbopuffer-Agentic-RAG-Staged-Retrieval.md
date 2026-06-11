# RAG is dead, right? Agentic Retrieval & Staged Search

**Channel:** AI Engineer  
**Published:** 2026-06-09  
**Source:** https://www.youtube.com/watch?v=UM6sFg_jdlE  

## TL;DR
Contrary to the "RAG is dead" social media narrative, retrieval is evolving from simple one-shot vector lookups into **agentic retrieval**. Using Turbopuffer as a case study, the talk argues that embeddings serve as "cached compute," enabling agents to perform iterative, staged retrieval that reduces costs and increases accuracy in massive (trillion-token) datasets.

## Key Takeaways
- **Embeddings = Cached Compute:** Indexing codebases upfront is a one-time cost that makes subsequent agentic reasoning 10-20x cheaper/faster compared to per-session discovery (e.g., using `grep` alone).
- **Staged Retrieval:** As context windows grow, the bottleneck shifts to finding the "right million" tokens from trillions. Staged retrieval acts as a lightweight funnel.
- **Agentic Tools:** Modern RAG is no longer just vector search; it involves giving agents a toolset (BM25, vector, regex, Merkle trees) to iteratively probe context.
- **Incremental Indexing:** Cursor's use of **Merkle trees** allows for efficient syncing and indexing of large codebases by only re-embedding "diffs" across team members.
- **Performance Gains:** Semantic search implementation in Cursor led to a 23.5% increase in accuracy for their "Composer" model.

## Architecture & Optimization Mechanics
For the AI Optimization specialist, the core value is in **token-count reduction and inference efficiency**.
- **Context Window Management:** Instead of filling a 1M+ context window with raw data (expensive and noisy), staged retrieval narrows it down to high-signal chunks, preserving model attention.
- **Merkle Tree Optimization:** Using cryptographic hash trees for similarity detection between branches/codebases is a high-leverage architectural pattern to avoid redundant compute.
- **Storage-Informed Retrieval:** Turbopuffer’s architecture (built on object storage) allows for scaling to trillions of tokens while maintaining low-latency retrieval, optimizing the "retrieval" leg of the RAG pipeline.

## Grounded Context (Web Enrichment)
The "staged retrieval" mantra is reinforced by **Jeff Dean's** 2026 insight: "You don't need a trillion [tokens] at once, you need the right million." Web evidence indicates a diverging philosophy between **Claude Code** (which initially favored pure agentic `grep` for local discovery) and **Cursor** (which pioneered the dual-index semantic approach). Current benchmarks show that semantic-aware agents achieve 20%+ higher accuracy on complex, cross-file architectural questions compared to those relying solely on local search.

## Real-World Application / Actionable Step
- **LLM Routing via Retrieval:** Amit should implement a "Staged Retrieval" layer in his routing architecture. Before sending a query to a high-compute MoE model, use Turbopuffer to retrieve the "right million" tokens to determine if a cheaper, small-context model can handle the task.
- **Optimize Re-indexing:** For his model compression research projects, Amit should adopt Merkle-tree-based indexing (as seen in Cursor) to manage version-controlled artifacts, ensuring that he only re-calculates embeddings for modified layers or code chunks, significantly reducing GPU spend.
