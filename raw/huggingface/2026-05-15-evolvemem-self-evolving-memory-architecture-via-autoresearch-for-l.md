---
source: farmer/huggingface
farmed: 2026-05-15T00:00:00Z
arxiv_id: "2605.13941"
url: https://huggingface.co/papers/2605.13941
arxiv_url: https://arxiv.org/abs/2605.13941
date: 2026-05-15
---

# EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents

Long-term memory is essential for LLM agents that operate across multiple sessions, yet existing memory systems treat retrieval infrastructure as fixed: stored content evolves while scoring functions, fusion strategies, and answer-generation policies remain frozen at deployment. We argue that truly adaptive memory requires co-evolution at two levels: the stored knowledge and the retrieval mechanism that queries it. We present EvolveMem, a self-evolving memory architecture that exposes its full retrieval configuration as a structured action space optimized by an LLM-powered diagnosis module. In each evolution round, the module reads per-question failure logs, identifies root causes, and proposes targeted configuration adjustments; a guarded meta-analyzer applies them with automatic revert-on-regression and explore-on-stagnation safeguards. This closed-loop self-evolution realizes an AutoResearch process: the system autonomously conducts iterative research cycles on its own architecture, replacing manual configuration tuning. Starting from a minimal baseline, the process converges autonomously, discovering effective retrieval strategies including entirely new configuration dimensions not present in the original action space. On LoCoMo, EvolveMem outperforms the strongest baseline by 25.7% relative and achieves a 78.0% relative improvement over the minimal baseline. On MemBench, EvolveMem exceeds the strongest baseline by 18.9% relative. Evolved configurations transfer across benchmarks with positive rather than catastrophic transfer, indicating that the self-evolution process captures universal retrieval principles rather than benchmark-specific heuristics.
