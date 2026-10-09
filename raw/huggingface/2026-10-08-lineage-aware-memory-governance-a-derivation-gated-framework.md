---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.312085+05:30
arxiv_id: 2610.07258
url: https://huggingface.co/papers/2610.07258
arxiv_url: https://arxiv.org/abs/2610.07258
date: 2026-10-08
---

# Lineage-Aware Memory Governance: A Derivation-Gated Framework for Privacy-Preserving Column-Level Access Control in Enterprise AI Agents

Enterprise AI agents that share a memory store face two unaddressed risks: sensitive data can leak through legitimately computed results the requester could not derive, and departments can silently compute a same-named key performance indicator (KPI) through conflicting logic. Existing agent-memory systems (e.g., MemGPT, Zep, A-MEM) gate retrieval by content, ownership, and role, not derivation, missing a cached insight that embeds a forbidden column. We introduce the Analytical Memory Unit (AMU), a memory schema that attaches a full derivation (lineage) graph to every cached result, gated by a retrieval policy that serves a hit only when the requester is authorised for every column touched. Provided lineage recording is complete, we prove by construction that the policy blocks retrieval of results derived from a sensitive column outside the requester's permissions, at O(n) worst case -- a conditional design guarantee, not an empirical claim, that excludes derived features encoding sensitive information without naming their source. Eliminating measured leakage required 75-90% recorded lineage completeness, so we treat 90% as a conservative deployment target. Across six experiments, lineage-gated retrieval removes the 18.8-25.5% cross-department leakage naive content-gated memory suffers, keeping 81.5-82.6% of memory reuse at 13.8 microsecond worst-case overhead. A real-agent proof-of-concept with LLM-generated SQL is consistent with the guarantee: zero leaks over 9 round-trips, two conflicts caught automatically -- though a feasibility demonstration, not evidence of production viability. This offers a practical governance layer for shared agent memory, complementing source-layer access control and supporting EU AI Act compliance.
