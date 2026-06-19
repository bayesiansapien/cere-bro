# The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks

**Channel:** AI Engineer  
**Published:** 2026-06-18  
**Source:** https://www.youtube.com/watch?v=ObTPqBGsEbA  

## TL;DR
Moving LLM applications from prototype to production requires shifting focus away from model selection toward a robust infrastructure framework built on evaluation, tracing, and data governance. Sandipan Bhaumik from Databricks shares a five-pillar production playbook—Evaluation, Observability, Data Foundation, Orchestration, and Governance—empirically proven to resolve enterprise scalability bottlenecks such as behavioral edge-case failures, runaway duplicate API costs, and compliance risks. 

## Key Takeaways
- **The Three Core Production Gaps:** AI deployments fail due to the observability gap (inability to trace decisions), evaluation gap (lack of defined business-aligned success metrics), and governance gap (undefined accountability when AI fails).
- **The Five-Pillar Playbook:** Successful production deployment requires standardizing on five consecutive layers: Evaluation, Tracing/Observability, Data Foundation (question vs. tracking data), Multi-Agent Orchestration, and Governance.
- **Three-Tier Evaluation Framework:** Evaluation must span across three distinct layers: deterministic validation (regex, classic ML for PII/intents), non-deterministic semantic validation (LLM-as-a-judge for groundedness), and behavioral validation (inspecting multi-turn agent logic, loops, and tool-calling execution).
- **The Real Cost of Runaway Tool Calls:** While duplicate API or database calls function fine in a single-user demo environment, they become prohibitively expensive and inject high latency under production loads, demanding strict behavioral tracking and online monitoring with fallback limits.
- **Data Foundations for Non-Human Actors:** Traditional enterprise data structures were designed for forgiving human readers. Agents execute strictly against available data and amplify formatting/content errors confidently, requiring meticulous data quality and semantic metadata tagging via tools like Unity Catalog.

## Architecture & Optimization Mechanics
- **Evaluation Sequencing:** Model selection should occur late in the development lifecycle (e.g., week 7 of an 8-week timeline). Meticulously establish a living "golden evaluation dataset" derived from real human-agent transcripts first, automating test pipelines before writing application logic.
- **Orchestration Topology Selection:** 
  - *Orchestrator-Worker Pattern:* Centralized routing plane handles all state and delegates to specialized sub-agents. Provides straightforward debugging logs but introduces single-point-of-failure and latency overhead.
  - *Choreography Pattern:* Sub-agents operate autonomously via an asynchronous event/message bus, running in parallel. This dramatically reduces system latency but increases state complexity and hardens tracking.
- **Continuous Integration (CI) cost mitigations:** Running full 500+ row behavioral evaluation suites on every single prompt commit is economically non-viable. Optimize CI/CD by executing prompt modifications against a small, representative evaluation subset, deferring full suite runs to main-branch merge triggers.

## Grounded Context (Web Enrichment)
Databricks formalized the concepts from this playbook through the General Availability of the Mosaic AI Agent Framework and **Agent Bricks**. Agent Bricks provides a low-code interface designed around specialized enterprise archetypes (Knowledge Assistant, Information Extraction, Multi-Agent Supervisor), optimizing model routing and retrieval mechanics natively. 

Furthermore, Databricks resolved the exact behavioral and tool-calling evaluation bottlenecks highlighted in the playbook by introducing **Agent-as-a-Judge** and the **CLEARS** framework (Correctness, Latency, Execution, Adherence, Relevance, Safety). Agent-as-a-Judge automates the parsing of nested execution traces to verify if correct tool calls were executed, eliminating manual traversal code. For persistence and session management across complex choreography patterns, the platform relies on its Agent Memory Service powered by serverless relational backends.

## Real-World Application / Actionable Step
Amit should immediately implement a three-tier automated evaluation pipeline for his current routing and MoE optimization pipelines. Specifically, he must:
1. Stop modifying prompt/routing parameters directly in code without an evaluation framework.
2. Build a baseline "golden data library" containing at least 100-200 expert-validated edge cases.
3. Integrate an automated LLM-as-a-judge system (leveraging Databricks' Agent-as-a-Judge or custom MLflow 3.0 tracing) to measure behavioral correctness—flagging and short-circuiting any routing loops or redundant model tool invocations before code hits staging.
