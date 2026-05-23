# Qwen3.7-Max: Alibaba's 35-hour autonomous coding agent

**Source:** The Decoder, 2026-05-23. [article](https://the-decoder.com/alibabas-latest-ai-model-ran-autonomously-for-35-hours-to-optimize-code-for-its-own-custom-chip/)

## TL;DR

Alibaba's Qwen team has released Qwen3.7-Max, a proprietary frontier model built for long-running autonomous agent tasks. In the headline demo it ran for 35 continuous hours optimizing code on Alibaba's own custom in-house inference chip. On benchmarks Qwen3.7-Max matches Claude Opus 4.6 and beats Chinese rivals DeepSeek V4-Pro and Kimi K2.6. The same model demos steering a four-legged robot, an unusual cross-domain breadth signal from a model otherwise pitched as a coding agent.

## Why this matters

Long-horizon autonomous execution is the central agentic benchmark of 2026. Anthropic's Claude has been the leader on coding agent harnesses (the controlled-experiment evidence showed harness engineering plus Opus 4.5 produced playable game code at $200 vs an unplayable $9 zero-harness output). Alibaba running a 35-hour autonomous coding agent on its own chip is the first credible Chinese match to that capability. The robot-steering demo widens the claim: the same base model is competitive on a non-coding embodied task.

The "optimizing code on its own custom chip" framing is the load-bearing detail. Alibaba is signaling that its inference chip is mature enough to run frontier-class autonomous workloads, and that the Qwen team owns the full stack from chip kernels up. That matches the broader Chinese AI strategy of vertical integration, and it is what gives DeepSeek room to make its 75 percent discount permanent the same week without bleeding to compute costs.

## Connections to prior wiki state

This is the third major Chinese frontier announcement in May 2026. DeepSeek made its 75 percent V4-Pro discount permanent today (pricing output tokens at least 34x below GPT-5.5). Kimi K2.5 underpins the Cursor Composer 2.5 release. Qwen3.7-Max adds Alibaba to that triad, with the differentiator being long-horizon agent execution rather than price or coding harness depth.

For routing: a model that holds together over 35 hours of autonomous execution is the kind of base that orchestration systems like [Maestro (today's HF paper on RL-driven model-skill orchestration)](../ai-routing/2026-05-23-maestro-rl-orchestrated-model-skill-ensemble.md) can route to as an expert. The Chinese model cohort now collectively gives non-Anthropic / non-OpenAI orchestrators a viable expert pool.

For industry economics: this is the same week Microsoft canceled its internal Claude Code licenses over token cost, Uber blew through its annual AI budget in four months, and US AI software prices jumped 20-37%. A frontier-class Chinese model that runs on Alibaba's own silicon undercuts both the cost arc and the supply arc that Anthropic's profitable Q2 forecast assumed.

## Gaps

The Decoder coverage is sparse on technical detail. We do not have the model size, architecture (dense vs MoE), training compute, context length, or licensing terms. We do not know whether Qwen3.7-Max will be open-weight (consistent with prior Qwen releases) or kept proprietary (consistent with "Max" naming and the in-house-chip optimization story). We do not have independent benchmark verification against Opus 4.6 outside Alibaba's own reporting.

## Research angle

The 35-hour autonomous run is the benchmark to watch. If reproducible on independent harnesses, it is the strongest evidence to date that long-horizon agent stability is solvable at the base-model level rather than purely at the harness level. If it requires Alibaba's specific chip-kernel codesign to hold together, then it is more a vertical-integration signal than a model capability signal.

## Raw source

[raw/rss/2026-05-23-the-decoder-alibabas-latest-ai-model-ran-autonomously-for-35-hours.md](../../raw/rss/2026-05-23-the-decoder-alibabas-latest-ai-model-ran-autonomously-for-35-hours.md)
