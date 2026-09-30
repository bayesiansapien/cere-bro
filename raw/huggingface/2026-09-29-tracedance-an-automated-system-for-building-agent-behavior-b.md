---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.928700+00:00
arxiv_id: 2609.33295
url: https://huggingface.co/papers/2609.33295
arxiv_url: https://arxiv.org/abs/2609.33295
date: 2026-09-29
---

# TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces

An agent can complete a task while exhibiting undesirable behavior during execution. Developers need tests for the specific behaviors encountered in deployment, beyond fixed benchmark suites. We present TraceDance, an agent system that constructs targeted benchmarks from deployment traces for user-specified undesirable behaviors. For efficient construction, Anchor-and-Confirm combines programmable retrieval with candidate-level confirmation by a Flash large language model (LLM), while the Anchor Synthesis Loop generates and revises specifications for custom behaviors. The benchmarks use decision-point continuation to evaluate an LLM's next turn at a recorded decision point with a behavior-specific rubric, without a reference answer or environment replay. Experiments in coding and general tool use draw on 252,557 sessions and produce 107 benchmarks with 4,125 instances, fulfilling 95.3% of build-target requests. Both human annotators confirm the requested behavior in 84% of sampled instances, and the automated grader's agreement with human pass/fail judgments is comparable to that between the annotators. Nine frontier LLMs achieve a mean pass rate of only 26.7%, showing that they still struggle to respond appropriately at the evaluated decision points. Analysis across behavior-specific benchmarks further reveals weaknesses in how current LLMs behave as agents. By turning deployment problems into targeted benchmarks, TraceDance could serve as a key component of the recursive self-improvement (RSI) loop.
