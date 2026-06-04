---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2605.27492
url: https://huggingface.co/papers/2605.27492
arxiv_url: https://arxiv.org/abs/2605.27492
date: 2026-06-04
---

# Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems

LLM agents are rapidly evolving from coding assistants into autonomous software engineering systems. However, existing evaluation methodologies remain largely centered on static, isolated, and short-horizon benchmarks that fail to capture the dynamic complexity of real-world production workflows. As a result, benchmark performance may poorly reflect practical capability under realistic runtime environments involving long execution chains, tool interactions, dependency management, and iterative feedback loops. We thus present RAMP, a production-grounded infrastructure for assessing long-horizon software engineering agents. Built upon the YatCC integrated platform, RAMP provides a unified runtime assessment architecture through standardized orchestration and execution interfaces. RAMP introduces realistic compiler-construction workloads with serial dependencies and complex toolchain interactions, together with a staged recovery mechanism for analyzing execution behavior under partial workflow failure. The framework further incorporates utility-oriented multi-dimensional metrics that jointly evaluate outcome quality and process efficiency. We conduct runtime assessments across 15 mainstream models and observe substantial capability degradation that remains largely invisible to conventional isolated benchmarks. Task completion rates progressively collapse across serial workflows, dropping from 100% in the initial stage to only 20% in the final stage, while none of the evaluated models successfully completes the entire pipeline. Runtime analysis reveals systematic failure propagation and significant resource inefficiencies, with computational costs differing by up to three orders of magnitude among comparable models. These findings suggest RAMP advances agentic model evaluation toward continuous, runtime-observable, and production-grounded assessment.
