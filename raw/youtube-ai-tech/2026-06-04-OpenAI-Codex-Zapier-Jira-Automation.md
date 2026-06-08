# What Codex Unlocks for Zapier: Epic-Level Automation

**Channel:** OpenAI  
**Published:** 2026-06-04  
**Source:** https://www.youtube.com/watch?v=DDnGhZ01PqM  

## TL;DR
Zapier’s engineering team uses Codex to compress weeks of research into hours by generating full-scope Jira tickets and epics with detailed instructions, utilizing the Zapier MCP and SDK for multi-source context retrieval.

## Key Takeaways
- **Compression of Effort:** Research and ticket creation that used to take weeks now takes hours.
- **Full-Scope Epics:** Codex doesn't just write tasks; it structures entire epics with detailed instructions pulled from multiple knowledge sources.
- **Unblocking Customers:** Faster internal production directly leads to faster customer solutions.

## Architecture & Optimization Mechanics
This workflow highlights the **Zapier SDK (`@zapier/zapier-sdk`)** for "code-native agents." Unlike the simple tool-calling of MCP, the SDK allows Codex to write complex logic (loops and conditionals) and make raw authenticated API requests. For an AI Optimizer, this demonstrates **High-Fidelity Task Reasoning**. The model must navigate a "reasoning tree" to determine what information is missing for a Jira epic and then programmatically query the necessary tools until the "information gap" is closed.

## Grounded Context (Web Enrichment)
Web enrichment confirms that in early 2026, Zapier launched the **"Training Grounds,"** an environment where developers can "grind" unlimited challenges to lock in their SDK skills. This indicates a shift towards a **Human-in-the-loop (HITL) fine-tuning** approach, where engineers correct Codex-generated Jira tickets to improve the model's future performance on specific organizational "dialects" of Jira usage.

Additionally, Codex’s integration with **Amazon Bedrock (April 2026)** allows Zapier to run these heavy agentic workloads closer to their existing AWS security and identity systems, reducing latency in cross-app data fetches.

## Real-World Application / Actionable Step
- **Agentic Optimization:** For Amit's work in inference optimization, analyze the **parallel tool-calling** patterns of the Zapier SDK. How does the model prioritize which API calls to make first? Can we use a "speculative execution" approach for API calls (fetching data before the model explicitly asks for it based on a "pre-fetch" probability model)?
- **Step:** Build a local script using the Zapier SDK to automate your own research-to-ticket workflow for AI optimization experiments.
