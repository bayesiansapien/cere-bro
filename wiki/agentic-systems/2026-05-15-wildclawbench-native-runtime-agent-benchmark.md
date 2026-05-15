# WildClawBench: Native-Runtime Long-Horizon Agent Benchmark — Claude Opus 4.7 Tops Out at 62.2%

**Source:** [HuggingFace Daily Papers](https://huggingface.co/papers/2605.10912) · [arXiv 2605.10912](https://arxiv.org/abs/2605.10912)
**Date ingested:** 2026-05-15
**Tier:** 2. Agent evaluation, native-runtime benchmarks, harness sensitivity
**Raw:** [farmer file](../../raw/huggingface/2026-05-15-wildclawbench-a-benchmark-for-real-world-long-horizon-agent-evalu.md)

## TL;DR

WildClawBench is a native-runtime benchmark: 60 bilingual, multimodal, human-authored tasks across six themes, averaging 8 minutes of wall-clock time and 20+ tool calls per task. Tasks run inside reproducible Docker containers hosting an actual CLI agent harness (OpenClaw, Claude Code, Codex, or Hermes Agent) with access to real tools, not mocks. Grading is hybrid: deterministic checks, environment-state auditing for side effects, and an LLM/VLM judge for semantic verification. Across 19 frontier models the best is Claude Opus 4.7 under OpenClaw at **62.2%**. Every other model stays below 60%. Switching harness alone shifts a single model by up to **18 points**.

## What's new

Three things that previous SWE-bench-style benchmarks were missing.

**Native runtime.** Most agent benchmarks (SWE-bench Verified, GAIA, AgentBench) run synthetic sandboxes with mocked tool APIs. WildClawBench runs the actual CLI harness with real tools (filesystem, network, package managers). The agent is doing the same thing it would do in production.

**8-minute, 20-tool-call horizon.** This is the long-horizon regime where AgentLens's Lucky-Pass diagnosis bites hardest. Short-horizon benchmarks can be passed by memorization or by luck-of-the-draw on a single retry. 20 sequential tool calls is enough trajectory length that the failure modes show up.

**Harness as a first-class variable.** The 18-point shift from harness alone is the most surprising finding. The same model under OpenClaw vs Claude Code vs Codex vs Hermes can be 18 percentage points apart. The benchmark is the only one in the wiki that measures this cleanly.

## Why this matters

The agent-eval crisis the wiki has been tracking gets a sharper edge. Yesterday's [AgentLens](2026-05-14-agentlens-lucky-pass-swe-eval.md) said 10.7% of passing SWE-bench Verified trajectories are Lucky. AssetOpsBench reported public-to-hidden score correlation of −0.13. Soohak said models confidently answer ill-posed math. Today's WildClawBench adds: even when you grade with hybrid environment-state checks, frontier models cap at 62.2%, and *which harness* you pick matters more than which model.

This has direct deployment implications. If a routing system selects between Claude Opus 4.7, GPT-5.5, and Gemini 3 by SWE-bench Verified score, it is choosing on a metric that does not reflect native-runtime performance. The 18-point harness shift means the harness layer is the load-bearing component in production agent deployments, not the underlying model.

## Connections to prior wiki pages

- [AgentLens Lucky-Pass](2026-05-14-agentlens-lucky-pass-swe-eval.md) — yesterday. AgentLens measures *process* quality on SWE-bench Verified. WildClawBench measures *outcome* on native-runtime tasks. Both surface the over-aggregation problem; complementary diagnostics.
- [DAgger for LLM agents](2026-05-14-dagger-llm-agents.md) — yesterday. DAgger trains on student-and-teacher trajectories. WildClawBench is the natural eval for DAgger-trained 4B/8B agents (does the +3.9 SWE-bench Verified gain transfer to native-runtime tasks?).
- [Orchard](2026-05-15-orchard-open-source-agentic-framework.md) — also today. Orchard-SWE reports 67.5% on SWE-bench Verified. WildClawBench would put that number under native-runtime evaluation; the 5+ point gap to Opus 4.7 (62.2%) suggests Orchard's number is partly benchmark artifact.
- [MAP (Map-then-Act)](2026-05-14-map-then-act-paradigm.md) — yesterday. MAP's diagnosis is "Delayed Environmental Perception." WildClawBench's 8-minute, 20-tool-call horizon is exactly the regime where DEP bites.
- [Soohak refusal subset](../llms-foundation-models/2026-05-12-soohak-research-math-benchmark.md) — same family of benchmark-integrity work.

## Why this is Tier 2 and not Tier 1

Pure benchmark papers are Tier 2 by default. WildClawBench is upgraded toward Tier 2 importance because the harness-sensitivity finding is structurally novel and because the cap on Claude Opus 4.7 at 62.2% changes what frontier-model status means in deployment.

## Research angle

1. **Harness-as-routing-variable.** If switching harness shifts performance by 18 points, the routing decision should include the harness, not just the model. WildClawBench points at a per-task harness selector as a research direction.
2. **What is the harness actually doing?** No paper in the wiki has isolated the harness mechanism. Is it the system prompt? The tool descriptions? The interrupt/cancellation logic? Untested.
3. **Native-runtime AgentLens.** AgentLens's process labels were derived for OpenHands trajectories. Native-runtime trajectories have different state granularity (filesystem changes, network requests, process spawns). Whether the Lucky-Pass framework transfers cleanly is open.

## Why it matters

The agent-eval question has been "how do we measure pass-rate honestly." WildClawBench changes the question to: "how much of the agent is actually the harness, not the model?" If the answer is "a lot," the routing literature and the deployment literature are pointing at different objects.

## Links

- [Paper](https://arxiv.org/abs/2605.10912)
- [HuggingFace](https://huggingface.co/papers/2605.10912)
- [Raw farmer file](../../raw/huggingface/2026-05-15-wildclawbench-a-benchmark-for-real-world-long-horizon-agent-evalu.md)
- Related: [AgentLens Lucky-Pass](2026-05-14-agentlens-lucky-pass-swe-eval.md), [DAgger](2026-05-14-dagger-llm-agents.md), [Orchard](2026-05-15-orchard-open-source-agentic-framework.md), [agent-benchmarks.md](agent-benchmarks.md)
