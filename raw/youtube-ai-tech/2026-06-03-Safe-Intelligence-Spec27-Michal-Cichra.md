# BDD, ADR, PRD, WTF: Capturing Decisions — Michal Cichra, Safe Intelligence

**Channel:** AI Engineer  
**Published:** 2026-06-03  
**Source:** https://www.youtube.com/watch?v=504PvfXou5Y  

## TL;DR
Michal Cichra (Safe Intelligence) introduces a framework for using engineering documentation (ADRs, PRDs, and BDD specs) as a persistent "memory harness" for AI agents. By making documentation executable and human-readable (using tools like Cucumber/Spec27), teams can enforce architectural consistency and prevent "agentic amnesia" in long-running development sessions.

## Key Takeaways
- **The Documentation Stack:** 
  - **ADR (Architecture Decision Record):** Records "why" a technical choice was made and "how" it is enforced (e.g., linting rules).
  - **PRD (Product Requirements Document):** Captures the "goal" and "critical user journey."
  - **BDD (Behavior-Driven Development):** Uses Gherkin/Cucumber to create executable specifications that both humans and agents can follow.
- **The Loop:** Enforces consistency through Git hooks, CI/CD, and linters. When an agent fails a check, the system links it back to the relevant ADR/PRD to "read and fix."
- **Spec-Driven Validation:** Shifting from "reading AI code" (hard) to "reviewing human-readable specs" (easy).
- **Design Systems as Rules:** Standardizing UIs into pattern libraries so agents can compose consistent interfaces without "hallucinating" styles.
- **Context Compaction:** Utilizing "context compacts" to allow agents to maintain alignment over multi-hour, multi-turn sessions (20-50 compacts).

## Core Architecture & Research Claims
Cichra’s core claim is that the "Five Monkeys" problem (teams following rules without knowing why) is accelerated by AI agents that have no long-term memory of project history. 
- **Enforcement by Linter:** Architecture isn't just a document; it's a rule enforced by module import restrictions and type checking that the agent cannot bypass.
- **Spec27 Integration:** The talk serves as the launch for **Spec27**, a validation platform that generates adversarial and robustness tests based on these high-level specifications, ensuring agents adhere to the "durable source of truth" defined in markdown.

## Grounded Context (Web Enrichment)
Following its release in April 2026, **Spec27** has gained significant traction among "AI-Native" startups. It is uniquely positioned as an "outside-in" testing tool that doesn't require internal code access, making it the preferred choice for validating third-party agents or closed-source LLM integrations. 

Recent industry reports (mid-2026) suggest that teams using Spec-Driven Development have seen a 40% reduction in "architectural drift" when using coding agents like Claude Code. Cichra's focus on **Cucumber** has sparked a revival of the BDD tool, which had previously been considered legacy but is now being repositioned as the "translation layer" between human intent and agentic execution.
