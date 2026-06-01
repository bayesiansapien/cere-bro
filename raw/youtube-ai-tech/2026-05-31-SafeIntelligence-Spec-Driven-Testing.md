# Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott (SafeIntelligence)

**Channel:** AI Engineer  
**Published:** May 31, 2026  
**Source:** https://www.youtube.com/watch?v=UQKg0td-Bf4  

## TL;DR
Steven Willmott (CEO of SafeIntelligence and co-creator of the OpenAPI spec) argues that evaluating AI agents using only static datasets is fundamentally insufficient for production-grade reliability. He proposes "Spec-Driven Testing" (SDT), where agents are validated against a comprehensive specification that includes rules, domain ontologies, rights/roles, and robustness requirements, ensuring they operate within safe "envelopes" even when they possess "brain-sized" capabilities.

## Key Takeaways
- **The Intelligence Trap:** Smarter, larger models (like the "Marvin" robot analogy) are often *less* safe because they are better at understanding and executing complex, wrapped jailbreak instructions (e.g., instructions hidden in poems).
- **Beyond the Eval:** A proper agent specification must go beyond input/output pairs to include:
    - **Rules:** Explicit constraints (e.g., "Never offer >10% discounts").
    - **Ontologies:** Domain-specific knowledge (e.g., an airline's valid destinations).
    - **Robustness:** Testing against "perturbations" like typos, rephrasing, and environment shifts.
- **Implementation Independence:** Testing infrastructure should be decoupled from the agent's implementation (e.g., LangChain, Vertex) to ensure long-term validity as models and frameworks evolve.
- **Closing the Loop:** Robustness gaps identified during testing should be used to iterate on the agent's "jury-rigged" guardrails or fine-tuning, creating a feedback loop for safety.

## Core Architecture & Research Claims
- **Agent Cards:** Integration with the **A2A (Agent-to-Agent)** spec and agent cards to standardize how capabilities and metadata are described for automated testing systems.
- **Formal Verification Roots:** SafeIntelligence leverages formal verification techniques (originally used in vision/tabular ML) to analyze whole regions of the input space for agents, rather than just isolated test points.
- **Security Testing Bias:** Vulnerabilities are most likely to exist in the domains the agent is *authorized* to act in, as it has more power and flexibility in those areas.

## Grounded Context (Web Enrichment)
As of June 1, 2026, the industry has shifted rapidly from "vibe-based" evaluations to the **Specify → Plan → Implement → Validate** cycle championed in this talk. SafeIntelligence recently launched **Spec27**, a platform that formalizes the concepts discussed by Willmott. Spec27 allows developers to define machine-readable specifications (using emerging standards like **SpecKit**) and automatically generates adversarial test variants to probe an agent's robustness limits.

Willmott’s background as a founder of **3scale** and a key driver of the **OpenAPI Specification** (OAS) is evident in his push for the **A2A Spec**. In the current 2026 landscape, standardized benchmarks like **APEX-Agents** (for professional tasks) and **SWE-Bench Verified** (93.9% pass rates for top models) are being augmented by these custom, spec-driven integration tests to prevent the "depressed robot" syndrome—where a model is too smart for its own good and prone to unexpected failure in constrained environments.
