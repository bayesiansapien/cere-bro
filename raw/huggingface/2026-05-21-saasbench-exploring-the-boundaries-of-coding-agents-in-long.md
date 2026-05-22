---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.17526
url: https://huggingface.co/papers/2605.17526
arxiv_url: https://arxiv.org/abs/2605.17526
date: 2026-05-21
---

# SaaSBench: Exploring the Boundaries of Coding Agents in Long-Horizon Enterprise SaaS Engineering

As autonomous coding agents become capable of handling increasingly long-horizon tasks, they have gradually demonstrated the potential to complete end-to-end software development. Although existing benchmarks have recently evolved from localized code editing to from-scratch project generation, they remain confined to structurally simplified, single-stack applications. Consequently, they fail to capture the heterogeneous environments, full-stack orchestration, and system-level complexity of real enterprise Software as a Service (SaaS) systems, leaving a critical gap in assessing agents under realistic engineering constraints. To fill this gap, we introduce SaaSBench, the first benchmark designed to explore the boundaries of AI agents in enterprise SaaS engineering. Spanning 30 complex tasks across 6 SaaS domains with 5,370 validation nodes, it incorporates 8 programming languages, 6 databases, and 13 frameworks to meticulously mirror real-world software heterogeneity. Furthermore, we design a dependency-aware hybrid evaluation paradigm tailored for complex systems with long horizons and multi-component coupling, enabling fine-grained, reproducible assessment. Crucially, our extensive experiments reveal a striking insight: the primary bottleneck for state-of-the-art agents is not generating isolated code logic, but successfully configuring and integrating a multi-component system. Over 95\% of task failures occur before agents even reach deep business logic, with models often falling victim to overconfidence and prematurely halting during foundational system setup, or getting trapped in ineffective debugging loops. We hope SaaSBench serves as a practical and challenging testbed to drive the evolution of reliable, system-level coding agents. The code is available at https://github.com/ShadeCloak/SaaSbench.
