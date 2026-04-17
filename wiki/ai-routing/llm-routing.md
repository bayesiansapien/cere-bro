# LLM Routing

Routing in LLM systems means deciding which model (or no model) should handle a given query — with the goal of minimizing cost while meeting quality requirements.

## Current State (as of 2026-04-17)

Routing is an active research and production concern. The core problem: different queries have very different difficulty levels, but most systems route everything to the same model. Smarter routing can cut cost dramatically without hurting quality on most traffic.

Three routing paradigms are emerging:
1. **Surrogate routing** — train a cheap classifier to handle easy traffic, fall back to LLM for hard cases
2. **Capability-based routing** — direct queries to different models based on task type or capability match
3. **Agent trajectory routing** — in multi-step agentic systems, optimize the path through a sequence of model calls, not just individual ones

## Key Papers

**TRACER (2026-04-17)** — Trains lightweight ML surrogates on an LLM's own production traces (free labeled data). A parity gate activates the surrogate only when it agrees with the teacher above a confidence threshold. Achieves 100% surrogate coverage on a 150-class benchmark using Claude Sonnet 4.6 as teacher. Generates interpretability artifacts for the routing boundary. → [summary](2026-04-17-tracer-llm-routing.md)

## Key Concepts

- **Surrogate model**: a cheap ML classifier trained to approximate a more expensive LLM's decisions on a specific task
- **Parity gate**: a confidence threshold that controls when the surrogate is trusted vs. when to fall back to the LLM
- **Coverage**: fraction of traffic the surrogate handles vs. falls back to the LLM
- **Production traces**: labeled input-output logs from a deployed LLM — free training data for a surrogate
- **Routing boundary**: the region of input space where the surrogate is reliable; interpretability artifacts describe this

## Open Problems

- Routing for open-ended tasks (no ground-truth labels to train surrogates)
- Multimodal routing: routing queries across text, image, and video models
- Agent trajectory routing: optimizing multi-step tool-use sequences, not just individual calls
- Dynamic routing that adapts as model capabilities and costs change

## Related Pages

- [Inference Efficiency](../inference-efficiency/knowledge-distillation.md)
- [KV Cache](../inference-efficiency/kv-cache.md)
