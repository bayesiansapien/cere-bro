---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.14133
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.14133
published: 2026-04-16
authors: Edoardo Allegrini, Ananth Shreekumar, Z. Berkay Celik
---

# Formalizing the Safety, Security, and Functional Properties of Agentic AI Systems

**arXiv:** https://arxiv.org/abs/2510.14133
**Authors:** Edoardo Allegrini, Ananth Shreekumar, Z. Berkay Celik

## Abstract

arXiv:2510.14133v2 Announce Type: replace  Abstract: Agentic AI systems, which leverage multiple autonomous agents and large language models (LLMs), are increasingly used to address complex, multi-step tasks. The safety, security, and functionality of these systems are critical, especially in high-stakes applications. However, the current ecosystem of inter-agent communication is fragmented, with protocols such as the Model Context Protocol (MCP) for tool access and the Agent-to-Agent (A2A) protocol for coordination being analyzed in isolation. This fragmentation creates a semantic gap that prevents the rigorous analysis of system properties and introduces risks such as architectural misalignment and exploitable coordination issues. To address these challenges, we introduce a modeling framework for agentic AI systems composed of two central models: (1) the host agent model formalizes the top-level entity that interacts with the user, decomposes tasks, and orchestrates their execution by leveraging external agents and tools; (2) the task lifecycle model details the states and transitions of individual sub-tasks from creation to completion, providing a fine-grained view of task management and error handling. Together, these models provide a unified semantic framework for reasoning about the behavior of multi-AI agent systems. Grounded in this framework, we define 16 properties for the host agent and 14 for the task lifecycle, categorized into liveness, safety, completeness, and fairness. Expressed in temporal logic, these properties enable formal verification of system behavior, detection of coordination edge cases, and prevention of deadlocks and security vulnerabilities. Through this effort, we introduce the first rigorously grounded, domain-agnostic framework for the analysis, design, and deployment of correct, reliable, and robust agentic AI systems.
