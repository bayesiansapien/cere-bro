# Agent Evaluation & Benchmarks

A growing ecosystem of benchmarks specifically designed for agentic AI — measuring not just accuracy but exploration/exploitation, long-horizon task completion, tool use, robustness, and professional domain coverage.

## Current State (as of 2026-04-18)

Standard LLM benchmarks underserve agents. The field has been building agent-specific eval frameworks across several dimensions: decision-making quality, professional domain coverage, multimodal grounding, and robustness under fault injection.

## Key Benchmarks

**OccuBench (2026-04-16)** — 100 tasks across 65 professional domains using Language World Models (LWMs) to simulate environments. Key finding: no single model dominates all industries; implicit faults are hardest. → [summary](2026-04-16-occubench.md)

**Exploration/Exploitation Measurement (2026-04-16)** — Policy-agnostic metric for explore/exploit errors in LM agents on 2D grid environments. Reasoning models perform best; harness engineering meaningfully improves both dimensions. → [summary](2026-04-16-exploration-exploitation-lm-agents.md)

**GameWorld (2026-04-16)** — 34 browser games, 170 tasks, state-verifiable outcomes for MLLM game agents. Best models still far below human. → [summary](../multimodal/2026-04-16-gameworld-multimodal-game-agents.md)

**MERRIN (2026-04-16)** — Search-augmented agent benchmark with noisy multimodal web evidence. Average accuracy 22.3%; agents over-rely on text modalities. → [summary](../multimodal/2026-04-16-merrin-multimodal-retrieval.md)

**InfiniteScienceGym (2026-04-16)** — Procedurally generated scientific analysis benchmark. No model exceeds 45%; abstention on unanswerable questions is a key weakness. → [summary](../llms-foundation-models/2026-04-16-infinitesciencegym-benchmark.md)

**DR3-Eval (2026-04-18)** — Deep Research Agent benchmark. Static per-task corpus sandboxes with evidential sources, confounding documents, and noise. Reverse-constructed questions (derived from verified evidential docs) ensure every task is answerable. Multi-dimensional scoring: recall, factual accuracy, citation coverage, instruction following, depth. State-of-the-art models still struggle. → [summary](2026-04-18-dr3-eval-deep-research-benchmark.md)

## Patterns Across Benchmarks

- Reasoning models consistently outperform base models on agentic tasks
- Over-exploration is a common failure mode in strong models
- Professional/domain-specific tasks expose different weaknesses than general benchmarks
- Deterministic environment generation (OccuBench, InfiniteScienceGym) removes publication bias

## Related Pages

- [GUI Agents](gui-agents.md)
- [Multi-Agent Systems](multi-agent-systems.md)
