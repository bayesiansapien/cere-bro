# How to design a multi-agent system that skips the LLM

**Channel:** Google Cloud Tech  
**Published:** 2026-06-06  
**Source:** https://www.youtube.com/watch?v=Fzd0BWMH65s  

## TL;DR
Casey West (Google Cloud) presents "Race Condition," a multi-agent system that scales to 1,000+ autonomous agents by utilizing the **`before_model_callback`** to bypass LLM calls for deterministic tasks. By separating reasoning (AI) from execution (code), the system achieves massive scale (up to 10,000 agents) with minimal token costs and sub-second latency, using **Redis** for distributed session management.

## Key Takeaways
- **Hybrid Architecture:** Use the LLM for high-level judgment and algorithm selection, but use deterministic code for execution (e.g., pathfinding, math, or repetitive protocols).
- **The Intercept Trick:** The `before_model_callback` in the Google **Agent Development Kit (ADK)** intercepts execution before the LLM is called. If the task is procedural, the callback returns a result directly, skipping the AI inference.
- **Scalable State:** Standard `InMemorySessionService` fails at scale. The project uses a **Redis session service** from the `google-adk-community` repo to share state across 50+ Cloud Run instances.
- **NP-Hard Routing:** Route planning for a 26.2-mile marathon is solved via a deterministic "Spine & Sprout" algorithm (Dijkstra-based) rather than letting an LLM hallucinate coordinates.

## Architecture & Optimization Mechanics
- **Model vs. Logic Separation:** The "Planner Agent" uses Gemini for reasoning (which landmarks to visit), while the "Runner Agents" (autopilot) use 100% deterministic code to move. This means adding more runners adds **zero additional tokens**.
- **Latency Optimization:** By using `before_model_callback` and Redis, agent turns complete in milliseconds rather than seconds, which is crucial for real-time simulations.
- **Server-Side Ticks:** Borrowing from game development, the simulator uses a "tick" system to manage the state of 1,000 independent agent sessions synchronously.

## Grounded Context (Web Enrichment)
The "Race Condition" demo was a centerpiece of the **Google Cloud Next '26** Developer Keynote. It showcased the maturity of the **ADK (Agent Development Kit)**, positioning it as a competitor to frameworks like LangChain or AutoGen for enterprise-grade, high-scale deployments.

The use of **Redis for session pruning** is a critical optimization for long-horizon agents. By pruning old event history and preventing "blob growth" in the session state, the system maintains performance even as sessions reach hundreds of turns. This is directly relevant to anyone building "perpetual agents" that need to maintain state for days or weeks.

## Real-World Application / Actionable Step
- **Optimize Routing Harness:** For Amit's LLM routing research, he should implement a `before_model_callback` to check if a query can be answered via a cache or a simpler deterministic tool (like a calculator or local DB) before sending it to a frontier model.
- **Action:** Explore the `google-adk-community` repository for the **Redis Session Service** to replace any memory-bottlenecked session stores in his current agentic projects.
