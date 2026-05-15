# Orchard: Open-Source Agentic Modeling Framework — 67.5% SWE-bench Verified at 30B

**Source:** [HuggingFace Daily Papers](https://huggingface.co/papers/2605.15040) · [arXiv 2605.15040](https://arxiv.org/abs/2605.15040)
**Date ingested:** 2026-05-15
**Tier:** 2. Agentic systems, open-source training infrastructure
**Raw:** [farmer file](../../raw/huggingface/2026-05-15-orchard-an-open-source-agentic-modeling-framework.md)

## TL;DR

Orchard is an open-source agentic training framework with a Kubernetes-native environment service (Orchard Env) that provides reusable sandbox lifecycle primitives, plus three recipe pipelines (SWE, GUI, Claw) on top. Headline: Orchard-SWE on a 30B-A3B-Thinking backbone hits **64.3% on SWE-bench Verified after SFT, 67.5% after SFT+RL**, setting a new open-source SOTA at this scale. Orchard-GUI gets 74.1% / 67.0% / 64.0% on WebVoyager / Online-Mind2Web / DeepShop with only 0.4K distilled + 2.2K open-ended training tasks on a 4B VLM. Orchard-Claw hits 73.9% pass@3 on Claw-Eval with the ZeroClaw harness using just 0.2K synthetic tasks.

## What's new

Three structural decisions, in order of importance.

**Harness-agnostic Kubernetes-native environment layer.** Most open agent frameworks ship a vertical stack (one harness, one model, one task type). Orchard Env separates sandbox lifecycle from agent harness. Trajectory distillation, on-policy RL rollouts, and evaluation all run against the same thin K8s service. Adding a new harness (Codex, Claude Code, Hermes) does not require re-implementing the environment.

**Credit-assignment SFT.** The 107K trajectories distilled from MiniMax-M2.5 and Qwen3.5-397B include a mix of resolved and unresolved tasks. The SFT recipe learns from "productive segments" of unresolved trajectories instead of discarding them, then applies Balanced Adaptive Rollout for sparse-reward RL. The SFT vs SFT+RL jump (64.3% → 67.5%) is the empirical case for adding RL on top.

**Per-recipe specialization with shared infrastructure.** SWE (107K distilled trajectories + RL), GUI (0.4K + 2.2K), Claw (0.2K) all use Orchard Env underneath. The data-efficiency varies by domain (GUI and Claw are 100-1000x lower data than SWE) but the framework is the same.

## Why this matters

Two reasons.

First, the open-source SWE-bench Verified frontier at the 30B scale jumps from the high-50s (Devstral, OpenHands) to 67.5%. That number is competitive with several closed-source SWE agents. The reproducibility framing ("scalable agentic modeling" with open infra) is real if the K8s service and recipes land.

Second, Orchard-Claw introduces "Claw-Eval" and the ZeroClaw harness, which are new evaluation infrastructure for personal-assistant agents (email, calendar, productivity workflows). This is the explicit response to the OpenClaw category that emerged from NVIDIA's claw blog last week, and that the wider deployment-services thread has been pointing at.

## Connections to prior wiki pages

- [DAgger for LLM agents](2026-05-14-dagger-llm-agents.md) — yesterday's paper hit 27.3% SWE-bench Verified at 4B and beat published 8B SWE-agents. Orchard hits 67.5% at 30B. The two papers are not directly comparable on scale, but both are training-side recipes for agentic gain. DAgger interpolates student-teacher trajectories at the turn level; Orchard's credit-assignment SFT learns from productive segments. Different mechanisms, same prescription (train on the data the deployed agent will see).
- [AgentLens Lucky-Pass evaluation](2026-05-14-agentlens-lucky-pass-swe-eval.md) — yesterday's eval-side paper says 10.7% of passing SWE-bench Verified trajectories are Lucky. Orchard's 67.5% is a pass-rate number. Whether Orchard-SWE's trajectory quality holds under AgentLens process labels is the natural follow-up evaluation.
- [WildClawBench](2026-05-15-wildclawbench-native-runtime-agent-benchmark.md) — also today. WildClawBench is a native-runtime benchmark where Claude Opus 4.7 only hits 62.2%. Orchard's 67.5% is on the older Verified benchmark; running Orchard-SWE on WildClawBench is the next data point.
- [MinT million-scale LoRA serving](../inference-efficiency/2026-05-14-mint-million-scale-lora-serving.md) — MinT covers the *serving* side of multi-policy fleets. Orchard covers the *training* side. The composition: train policies with Orchard, serve them with MinT.

## Research angle

1. **Credit-assignment SFT generalization.** The "learn from productive segments of unresolved trajectories" idea is structurally similar to DAgger's "interpolate student and teacher" and to the Extrapolation Cliff's "clip below λ*." All three are forms of selective supervision on partially-failed trajectories. A unifying frame for this family is unwritten.
2. **Cross-harness transfer.** Orchard-SWE was trained against OpenHands-style harnesses. WildClawBench shows switching harness alone shifts a single model by up to 18 points. The empirical question: does Orchard-SWE generalize to Hermes / Codex / Claude Code harnesses, or does it overfit to OpenHands?
3. **Open-infra reproducibility.** The big open question for the field is whether the Kubernetes-native environment service is what enables the gain, or whether the credit-assignment SFT recipe is. An ablation that runs the recipe without Orchard Env (or vice versa) is the only way to tell.

## Why it matters

The open-source SWE-bench leaderboard just got a 10+ point jump at 30B. The framework is open. If reproducible, the open-source agent stack closes most of the gap to closed-source SWE agents.

## Links

- [Paper](https://arxiv.org/abs/2605.15040)
- [HuggingFace](https://huggingface.co/papers/2605.15040)
- [Raw farmer file](../../raw/huggingface/2026-05-15-orchard-an-open-source-agentic-modeling-framework.md)
- Related: [DAgger for LLM agents](2026-05-14-dagger-llm-agents.md), [AgentLens](2026-05-14-agentlens-lucky-pass-swe-eval.md), [WildClawBench](2026-05-15-wildclawbench-native-runtime-agent-benchmark.md)
