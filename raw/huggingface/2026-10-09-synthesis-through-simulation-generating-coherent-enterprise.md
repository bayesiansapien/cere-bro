---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.417766+00:00
arxiv_id: 2610.10549
url: https://huggingface.co/papers/2610.10549
arxiv_url: https://arxiv.org/abs/2610.10549
date: 2026-10-09
---

# Synthesis Through Simulation: Generating Coherent Enterprise Data via Scalable Agent-System Interaction

Tool-calling agents have become central to enterprise AI, yet training and evaluating them at scale remains severely constrained due to business and legal restrictions on enterprise systems, data, and database schemas. Tabular data synthesis offers a natural alternative, but its effectiveness is fundamentally limited by structural validity and schema availability, while procedure-based approaches yield the opposite weakness, typically lacking distributional fidelity without per-domain authoring. We introduce **Synthesis Through Simulation** (STS), a **schema--free** data synthesis paradigm in which an LLM agent generates data by executing operations against policy-enforcing APIs within simulated enterprise environments. Because data is generated through the same environment that defines what is valid, STS guarantees structural validity by construction while decoupling validity enforcement from distribution modeling, allowing each to be addressed independently. The **Generalist Populator** (GP), STS's domain-agnostic agent, addresses the remaining challenges of distributional fidelity and synthesis scalability: GP achieves **0.88** average marginal fidelity and **100\% constraint satisfaction** across all ten environments *without access to DB schemas*, while statistical synthesizers are inapplicable to seven due to necessary seed data requirements, and schema-privileged agents fail 82\% of trajectories on airline environment's tightly coupled workflows due to brittle task composition. We open-source the full framework, all ten environments, and generated datasets at https://github.com/SAP/synthesis-through-simulation.
