---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.23041
url: https://huggingface.co/papers/2608.23041
arxiv_url: https://arxiv.org/abs/2608.23041
date: 2026-08-26
upvotes: 40
---

# AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces

LLM agents remain unreliable on long-horizon tasks, where small local failures can compound over extended interactions and lead to overall task failure. Although external harnesses can substantially improve robustness, harness design remains a manual and expensive process that requires searching over a large space of prompts, tool configurations, and control logic. We propose AutoSaddler, an automatic harness optimization framework that formulates harness improvement as an offline learning problem and iteratively updates the harness using failure signals from mini-batches. AutoSaddler combines failure-trace diagnosis, structured patch generation that treats the harness as code, and validation-based update selection. Experiments on GAIA2, SWE-Bench Pro, and Terminal-Bench 2.0 show that AutoSaddler substantially improves agent performance over the corresponding base harnesses, achieving gains of 9.0, 9.6, and 10.0 percentage points, respectively. Ablation studies further suggest that effective harness optimization benefits from three ingredients: deep debugging rather than shallow reflection, targeted modifications rather than unconstrained editing, and generalization-aware selection rather than trajectory-specific repair. Together, these results suggest that automatic harness optimization is a promising path toward more performant and reliable agent systems.
