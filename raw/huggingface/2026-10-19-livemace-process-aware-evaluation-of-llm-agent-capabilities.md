---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.09872
url: https://huggingface.co/papers/2610.09872
arxiv_url: https://arxiv.org/abs/2610.09872
date: 2026-10-19
---

# LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets

Evaluating agents by outcomes alone can obscure the capabilities that produce them. This problem is especially pronounced in evolving environments, where outcomes reflect a closed-loop interaction between agent behavior and changing external conditions. We introduce LiveMACEBench, a process-aware benchmark that uses live financial markets as a naturally evolving testbed for persistent LLM agents. Five frontier LLMs operate along continuous trajectories under matched Tool Use, Persistent Memory, Rule Following, and Multi-Agent Collaboration configurations. We evaluate them through both realized outcomes and mechanism-specific diagnostics derived from complete decision traces. Across 30 days of live evaluation, we find a pronounced outcome-capability gap: realized returns often diverge from capability-specific measurements, and similar outcomes can arise from markedly different patterns of mechanism use. Trace-level diagnostics further expose distinct bottlenecks across capabilities, demonstrating that mechanism access, effective mechanism use, and downstream performance are not interchangeable measures of agent capability. LiveMACEBench makes this distinction measurable, turning live markets from a performance leaderboard into a diagnostic environment for agent capability
