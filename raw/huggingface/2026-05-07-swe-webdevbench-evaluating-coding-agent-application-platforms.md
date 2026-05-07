---
source: farmer/huggingface
farmed: 2026-05-08T00:00:00Z
arxiv_id: "2605.04637"
url: https://huggingface.co/papers/2605.04637
arxiv_url: https://arxiv.org/abs/2605.04637
date: 2026-05-07
---

# SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies

The emergence of AI application-building platforms that convert natural language descriptions into deployed full-stack applications ("vibe coding") has created a new evaluation challenge: existing benchmarks assess code generation or issue-solving on developer-facing tasks, but do not measure whether AI systems can function as complete software agencies—understanding business intent, clarifying ambiguities, making sound architectural decisions, writing secure code, and handling iterative modifications.

We introduce SWE-WebDev Bench, a 68-metric evaluation framework organized across three orthogonal dimensions (Interaction Mode: ACR/AMR × Agency Angle: PM/Engineering/Ops × Complexity Tier: T4/T5) with a four-tier judging taxonomy. The framework distinguishes App Creation Requests (ACR) from App Modification Requests (AMR)—the first benchmark to separately evaluate creation and modification competencies. We introduce the Canary Requirement methodology: 80 culturally-specific, domain-embedded test requirements that distinguish genuine comprehension from template matching.

Evaluating six platforms (Lovable, Replit Agent, Vercel v0, QwikBuild, Emergent, Base44) across three business domains (EdTech, Field Service, FinTech-AI), we uncover four recurring shortcomings: (1) The Specification Bottleneck: inference quality varies 3.5× across platforms, with most skipping requirement elicitation; (2) Frontend-Backend Decoupling: polished UIs mask absent backend infrastructure; (3) The Production Readiness Cliff: no platform exceeds 60% engineering score, and post-generation effort varies 5×; (4) Widespread Security Failures: no platform exceeds 65% Security Score against a 90% target. Preliminary AMR analysis reveals that modification systematically degrades quality, with surviving requirements showing 3× the loss rate of new requirements.

We release the benchmark as a living community resource to enable researchers and platform builders to diagnose and address gaps in AI app-building systems.
