---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.11465
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.11465
published: 2026-04-16
authors: S. Aaron McClendon, Jorge Gallego-Feliciano, Stavros Zervoudakis
---

# Three Roles, One Model: Role Orchestration at Inference Time to Close the Performance Gap Between Small and Large Agents

**arXiv:** https://arxiv.org/abs/2604.11465
**Authors:** S. Aaron McClendon, Jorge Gallego-Feliciano, Stavros Zervoudakis

## Abstract

arXiv:2604.11465v2 Announce Type: replace  Abstract: Large language model (LLM) agents show promise on realistic tool-use tasks, but deploying capable agents on modest hardware remains challenging. We study whether inference-time scaffolding alone, without any additional training compute, can improve the performance of a small model in complex multi-step environments. Operating on a single 24GB GPU, we evaluate Qwen3-8B on the AppWorld benchmark under both full-precision and 4-bit quantized configurations. Without any intervention, the raw model achieves just 5.4% (FP16) and 3.0% (AWQ) task goal completion. Guided by a systematic failure mode analysis, we introduce a three-tier inference scaffolding pipeline that deploys the same frozen model in three distinct roles: (1) a summarization model that preserves critical artifacts (tokens, credentials, API responses) while compressing dialogue history; (2) the main agent model that reasons over the compressed context; and (3) an isolated correction model that reviews and revises the agent's code output without access to conversation history, breaking repetitive failure loops. Applied to the same unmodified model, this scaffolding yields 8.9% (FP16) and 5.9% (AWQ) task goal completion, roughly doubling performance in both settings, with particularly strong gains on difficulty-1 tasks (15.8% to 26.3% FP16; 5.3% to 14.0% AWQ). On full-precision inference, our scaffolded 8B model surpasses DeepSeek-Coder 33B Instruct (7.1%) from the original AppWorld evaluation, demonstrating that structured inference-time interventions can make small models competitive with systems 4 times their size. We formalize the approach as a scaffolded policy over a frozen base model, three invocations of the same weights with different conditioning, drawing connections to test-time compute scaling and action-space shaping in reinforcement learning.
