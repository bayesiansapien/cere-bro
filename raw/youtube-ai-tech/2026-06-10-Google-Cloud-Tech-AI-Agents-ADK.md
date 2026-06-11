# What are AI agents? (Google ADK Tutorial)

**Channel:** Google Cloud Tech
**Published:** 2026-06-10
**Source:** https://www.youtube.com/watch?v=Zqno_vux6d8

## TL;DR
AI agents are software systems that move beyond simple generation to reasoning, planning, and autonomous action based on the ReAct framework. Google's Agent Development Kit (ADK) provides a structured way to build these systems using patterns like Sequential, Reactive, and Deliberate/Planning agents, featuring built-in "LoopAgents" for automated retry and validation logic.

## Key Takeaways
- **Agent Patterns:** 
    - **Sequential:** Predictable, step-by-step assembly lines.
    - **Reactive:** Decides in-the-moment based on state (flexible but no plan).
    - **Deliberate/Planning:** Sketched plans with dependencies (e.g., travel booking).
- **Core Architecture:** Built on the cycle of Reasoning -> Acting -> Observing -> Adjusting.
- **Shared State:** ADK utilizes a "shared state" where agents (like a Blog Planner) save outputs (e.g., `blog_outline`) for subsequent agents (like a Blog Writer) to pick up.
- **Self-Correction:** "LoopAgents" wrap sub-agents and validation checkers, enabling up to 3 retries if the output doesn't meet strict criteria (e.g., "markdown outline must have 4-6 sections").

## Architecture & Optimization Mechanics
- **ADK 2.0 Components:** Native support for `SequentialAgent`, `ParallelAgent`, and `LoopAgent`. These abstractions allow for higher-level orchestration without manual state management.
- **Root Agent Pattern:** A "Blogger" root agent orchestrates sub-agents (Planner, Writer) which are exposed as tools. This encapsulates complexity and provides a clean interface for the end-user.
- **Validation as Guardrails:** By using "Validation Checkers" (LLM-as-a-Judge) within loops, the system ensures output quality before proceeding, reducing the cumulative error rate in multi-step pipelines.

## Grounded Context (Web Enrichment)
As of mid-2026, the **Google ADK (Agent Development Kit)** has been integrated into the broader **Gemini Enterprise Agent Platform**. ADK 2.0 now supports **Model Context Protocol (MCP)** natively, allowing agents to connect to Google Cloud services (BigQuery, Spanner) with zero boilerplate. 

A significant 2026 update is the **"Four-Rung" development model**, where ADK sits at the code-first tier, supported by **Antigravity 2.0** for visual debugging and orchestration. Furthermore, ADK has become "Provider Agnostic," supporting not just Gemini, but also Claude, Ollama, and vLLM, which is critical for Amit's LLM routing research.

## Real-World Application / Actionable Step
- **For LLM Routing:** Implement the "LoopAgent" pattern to verify the quality of a routed response. If a cheaper model (Gemini Flash) fails a validation check, the LoopAgent can automatically "retry" by routing the same prompt to a more capable model (Gemini Pro/Ultra) in the next iteration.
- **Deployment:** Use the `ADK web` CLI command to visualize agent traces and identify where reasoning bottlenecks occur in your optimization pipelines.
