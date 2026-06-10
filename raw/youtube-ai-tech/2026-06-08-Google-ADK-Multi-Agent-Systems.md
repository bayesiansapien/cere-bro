# Intro to multi-agent systems with ADK

**Channel:** Google Cloud Tech  
**Published:** 2026-06-08  
**Source:** https://www.youtube.com/watch?v=0Z0GUDakR_A  

## TL;DR
Google's **Agent Development Kit (ADK)** is a Python/TypeScript framework for building production-grade multi-agent systems. It moves away from monolithic agents to a **Hierarchical Agent Tree**, where "Coordinators" manage specialized sub-agents (e.g., Search Agent, Verifier Agent). ADK simplifies the "Agent-as-a-Tool" paradigm, allowing for more deterministic control, reduced hallucinations, and cost-optimized model routing.

## Key Takeaways
- **Agents as Tools:** The core strength of ADK is the ability to equip an orchestrator agent with other agents as tools. This allows for specialized "Expert" models (e.g., a "URL Verifier" agent).
- **Hierarchical Orchestration:** Uses a parent-sub-agent structure to manage memory and performance. A parent agent handles the goal, while sub-agents handle the "toil" of tool execution.
- **Deterministic Workflows:** ADK supports `SequentialAgent`, `ParallelAgent`, and `LoopAgent` to add software-engineering-style control to LLM reasoning.
- **A2A (Agent-to-Agent) Protocol:** A 2026 update enables ADK agents to talk to agents from other frameworks (LangGraph, CrewAI) through a standardized interface.

## Architecture & Optimization Mechanics
- **Model Routing/Selection:** ADK allows for heterogeneous model usage. Use Gemini Flash for the "Search Agent" (speed/cost) and Gemini Pro/Ultra for the "Verifier/Judge" (high-reasoning).
- **Session State Whiteboard:** Agents share a `session.state` whiteboard, preventing the need to pass the entire chat history in every turn, which optimizes token usage.
- **Control Loops:** Rather than one big loop, ADK encourages "Verify-and-Retry" loops where a "Verifier Agent" checks the output of a "Worker Agent" and triggers a re-run if deterministic criteria (e.g., HTTP 404 check) aren't met.

## Grounded Context (Web Enrichment)
ADK 2.0 (released April 2026) has introduced native support for the **Model Context Protocol (MCP)**, allowing these agent meshes to connect directly to enterprise data (BigQuery, Drive) without custom connectors. The **A2A Protocol** is now being proposed as an industry standard (RFC 9728) to allow cross-cloud agent collaboration. Companies using ADK report a 40% reduction in "agent drift" by moving from flat prompts to these hierarchical trees.

## Real-World Application / Actionable Step
- **For Amit:** Use ADK to build a **"Research-to-Wiki" pipeline**. 
- **Action:** Create a `ParallelAgent` that triggers Together AI's "U-Pipe" research analysis and Cloudflare's "Eval++" technical spec analysis simultaneously, then routes their outputs to a `JudgeAgent` for final synthesis. This leverages the **Agent-as-a-Tool** architecture to keep individual context windows small and high-signal.
