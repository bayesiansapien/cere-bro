# Self Driving Products: Product Signals to Pull Requests

**Channel:** AI Engineer
**Published:** 2026-06-10
**Source:** https://www.youtube.com/watch?v=zMiSRliEzv4

## TL;DR
PostHog is shifting observability from manual dashboarding to autonomous code generation. By treating product signals (errors, session replays, logs) as triggers for background research agents, they automate the creation and refinement of pull requests. The core engineering challenge lies in normalization and grouping of noisy, heterogeneous signals into actionable "reports" without falling into structural similarity traps during embedding.

## Key Takeaways
- **Signals vs. Dashboards:** Dashboards are slow; PRs are fast. The goal is to move from "reading data" to "reviewing automated fixes" immediately after an event occurs.
- **Embedding Trap:** Naive embeddings of different data types (logs vs. Slack messages) cluster by *structure* (e.g., all JSON together) rather than *semantics*. PostHog solves this by using an LLM to generate natural language queries *from* signals before embedding.
- **Agent Loop Architecture:** Uses Claude Agent SDK in Modal sandboxes, connected via MCP (Model Context Protocol) to internal data (logs, replays) and external context (Linear, Notion).
- **Execution Strategy:** PRs are iterated upon in the sandbox until CI is green. Reviewers are assigned automatically via `git blame`.

## Architecture & Optimization Mechanics
- **Inference Pipeline:** Implements a multi-stage pipeline: Ingestion (Safety Filter) -> Normalization (Signal Weighting) -> Grouping (Query-based clustering) -> Research Agent -> Actionability Step -> Execution Sandbox.
- **"Tokens are Free" Philosophy:** During R&D, don't optimize for cost immediately. Run agents 100x to find patterns, then distill those complex agentic flows into single-shot LLM calls or specialized models once the solution space is understood.
- **Signal Weighting & Promotion:** Not every error deserves an agent. Signals are weighted and promoted to "Report" status only after crossing a cumulative importance threshold.

## Grounded Context (Web Enrichment)
As of June 2026, PostHog has formalized this vision under the **"Self-Driving Product"** category, specifically through the release of **PostHog Code**. This suite utilizes the **Model Context Protocol (MCP)** as its primary integration layer, allowing agents to bridge the gap between real-time product analytics and the developer's IDE (like Claude Code or VS Code). 

The 2026 PostHog "AI Engineering Handbook" highlights that the role of the AI Engineer has pivoted from writing boilerplate code to designing the **guardrails and evaluation systems** (LLM-as-a-Judge) that allow these autonomous loops to operate safely without human oversight for "paper-cut" style bug fixes.

## Real-World Application / Actionable Step
- **For Routing Optimization:** Amit can apply the "Signal Weighting" concept to LLM routing. Instead of routing every request, use a lightweight classifier to "promote" only complex or high-value queries to more expensive, agentic routing paths.
- **For Pruning/Quantization:** Use automated research agents to analyze kernel performance logs and automatically submit PRs for kernel optimizations or quantization parameter adjustments based on real-world inference hardware signals.
