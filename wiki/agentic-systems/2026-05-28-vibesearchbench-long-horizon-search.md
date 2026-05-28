# VibeSearchBench: Long-Horizon Proactive Search

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.27882](https://arxiv.org/abs/2605.27882) · [raw](../../raw/huggingface/2026-05-28-vibesearchbench-benchmarking-long-horizon-proactive-search-i.md)

## TL;DR

LLM agents score well on search benchmarks while real users find their results unsatisfying. VibeSearchBench attributes the gap to single-turn, over-specified, fixed-schema benchmark design and proposes a counter-benchmark: 200 manually curated bilingual (Chinese, English) tasks across 20 domains, where each task pairs a user persona with a schema-free ground-truth knowledge graph and is evaluated through a progressive-disclosure user simulator and graph-matching. Seven frontier models tested under ReAct and OpenClaw harnesses all remain inadequate, best F1 is 30.30.

## Key findings

- Persona + schema-free knowledge graph per task; progressive-disclosure simulation.
- 200 tasks across 20 domains, Chinese + English.
- Best F1: 30.30, substantially below standard benchmark scores.
- Failure modes: long-context reasoning, proactive intent elicitation, structured knowledge construction.

## How this fits prior wiki state

This sits with LiveBrowseComp (today), HRBench (today), and ITBench-AA (yesterday) in the eval-rigor cluster. All four say the same thing: static, single-turn, fixed-input benchmarks have been overstating agent capability and a more realistic eval shape produces a 20-40pp drop. VibeSearch's specific contribution is the progressive-disclosure user simulator that turns search into a dialogue rather than a one-shot.

## Related pages

- [[2026-05-28-livebrowsecomp-search-agents-priors]], companion eval-rigor finding
- [[2026-04-18-dr3-eval-deep-research-benchmark]], deep-research evaluation
- [[agent-benchmarks]], concept page

## Research angle

Progressive-disclosure user simulators are now a credible eval primitive. The next paper that uses one for tool-use rather than search will measure something the current benchmark stack cannot.
