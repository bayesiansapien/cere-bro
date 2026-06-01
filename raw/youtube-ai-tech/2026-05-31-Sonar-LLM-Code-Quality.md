# Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar

**Channel:** AI Engineer  
**Published:** 2026-05-31T18:00:21Z  
**Source:** https://www.youtube.com/watch?v=NuePCNMpWGc  

## TL;DR
Prasenjit Sarkar from Sonar discusses the limitations of relying purely on functional correctness (pass rates) to judge LLM-generated code. Utilizing the Sonar LLM Leaderboard, which evaluates models against 4,444 Java assignments, he reveals that while LLMs successfully generate working code, they simultaneously introduce massive technical debt, verbosity, and security vulnerabilities that prevent the code from being enterprise-ready out of the box.

## Key Takeaways
- Foundational models pass basic functional correctness benchmarks (e.g., SWE-bench), but these tests ignore maintainability, security, and architectural discipline.
- Sonar's evaluation found that high-performing models can be extremely verbose—for instance, generating over a million lines of code for 4,444 assignments, increasing technical debt.
- Some leading models, like Claude Sonnet 4.6, generated high rates of security vulnerabilities (e.g., 300 security issues per million lines of code).
- Sonar introduces the ACDC framework (Agent-Centric Development Cycle: Guide, Verify, Solve) to clean code in real-time.
- SonarQube's agentic analysis acts as an open beta tool to automatically detect and remediate flaws in LLM-generated code before commits.

## Core Architecture & Research Claims
- **Cognitive & Cyclomatic Complexity:** LLMs often produce code that is structurally complex (many branches) and cognitively difficult for humans to maintain.
- **Data Poisoning Effects:** Insecure code examples present in training datasets get regurgitated by models.
- **The Productivity Paradox:** While the overall number of bugs per model might be decreasing in newer iterations, the models are introducing more complex, subtle logic vulnerabilities that are harder to detect manually.

## Grounded Context (Web Enrichment)
Web results corroborate Sonar’s ongoing mission to address the "trust gap" in AI-generated code. Prasenjit Sarkar's ACDC framework (Augment, Clean, Deliver, Control) underscores that developers must transition from "Code Authors" to "Code Curators." Sonar's LLM Leaderboard insights show that different models exhibit distinct "coding personalities." For example, some prioritize security while being verbose, while others act as rapid prototypers but introduce massive technical debt. 

Furthermore, external research aligns with Sonar's warnings about security regressions: while newer models (like Claude 4 and Gemini 3) solve complex functional problems better, they can simultaneously introduce severe security vulnerabilities (like hard-coded credentials or path-traversal injections). SonarQube Enterprise is being heavily positioned as the essential continuous monitoring layer to catch these AI "blind spots" before they hit production.