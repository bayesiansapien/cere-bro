---
source: farmer/huggingface
farmed: 2026-09-22T11:38:12.626404+05:30
arxiv_id: 2609.23986
url: https://huggingface.co/papers/2609.23986
arxiv_url: https://arxiv.org/abs/2609.23986
date: 2026-09-22
---

# Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents

Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \method, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6times speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.
