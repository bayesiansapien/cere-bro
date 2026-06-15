---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.14249
url: https://huggingface.co/papers/2606.14249
arxiv_url: https://arxiv.org/abs/2606.14249
date: 2026-06-15
---

# HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry

AI agent performance depends critically on the runtime harness, comprising the prompts, tools, memory, and control flow that mediate how a model observes, reasons, and acts. Yet today's harnesses remain largely hand-crafted and static: each new model or task still demands bespoke scaffolding, and the rich traces produced during execution are rarely distilled back into systematic improvement. We introduce HarnessX, a foundry for composable, adaptive, and evolvable agent harnesses. HarnessX assembles typed harness primitives via a substitution algebra, adapts them through AEGIS, a trace-driven multi-agent evolution engine grounded in an operational mirror between symbolic adaptation and reinforcement learning, and closes the harness-model loop by turning trajectories into both harness updates and model training signal. Across five benchmarks (ALFWorld, GAIA, WebShop, tau^3-Bench, and SWE-bench Verified), HarnessX yields an average gain of +14.5% (up to +44.0%), with gains largest where baselines are lowest. These results suggest that agent progress need not come from model scaling alone: composing and evolving runtime interfaces from execution feedback is an actionable and complementary lever. The complete codebase will be open-sourced in a future release.
