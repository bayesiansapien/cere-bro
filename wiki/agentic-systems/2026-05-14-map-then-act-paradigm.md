# MAP: a Map-then-Act paradigm for long-horizon interactive agents

**Source:** HuggingFace Daily Papers · 2026-05-14
**Paper:** [arXiv 2605.13037](https://arxiv.org/abs/2605.13037)
**Raw:** [raw](../../raw/huggingface/2026-05-14-map-a-map-then-act-paradigm-for-long-horizon-interactive-age.md)
**Tier:** 2. Agent reasoning, cognitive maps, ARC-AGI-3

## TL;DR

Current LM agents acquire environmental knowledge reactively during execution, which the paper calls Delayed Environmental Perception and identifies as an Epistemic Bottleneck. MAP proposes a plug-and-play three-stage framework that builds the environmental prior first: Global Exploration → Task-Specific Mapping → Knowledge-Augmented Execution. On ARC-AGI-3 — the benchmark where the wiki has been tracking zero-knowledge interactive reasoning — MAP enables frontier models to surpass near-zero baseline performance in 22 of 25 game environments. The accompanying MAP-2K dataset of map-then-act trajectories beats expert execution traces as training data, which is the paper's most interesting claim: understanding environments is more fundamental than imitating them.

## Why it matters

The wiki's responsible-ai and agentic-systems threads have been converging on the same point. [ARC-AGI-3 three systematic reasoning errors](../llms-foundation-models/2026-05-02-arc-agi-3-three-systematic-reasoning-errors.md) (05-02) identified the failure modes. [AutoTTS](2026-05-11-autotts-agentic-discovery-test-time-scaling.md) (05-11) automated test-time scaling discovery for one of those failure modes. MAP attacks a different failure mode at the architecture level: agents don't form world models because they conflate exploration with execution. The mechanism is Tolman-and-Gibson cognitive-map theory applied at LM-agent scale. The 22-of-25 result on ARC-AGI-3 is the strongest single-paper number on this benchmark since it was introduced.

## Mechanism

```
   ┌────────────────────────┐
   │  Global Exploration    │  env-general priors
   │  (no task in mind yet) │  affordances, layout, constraints
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │  Task-Specific Mapping │  structured cognitive map
   │  (now condition on task)│ what matters for THIS goal
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │ Knowledge-Augmented    │  grounded execution
   │  Execution             │  no trial-and-error baseline
   └────────────────────────┘
```

The shift versus ReAct / CoT / standard agent loops: in those, environmental understanding is a byproduct of action. In MAP, action is conditional on the prior map. The agent does not act until it has explored. The paper claims this matches the cognitive science framing in Gibson's affordance theory and Tolman's cognitive map theory — agents build a model first, then act inside it.

MAP-2K is the dataset: 2,000 map-then-act trajectories. Training on this set outperforms training on expert execution traces. That is the load-bearing empirical result: in long-horizon interactive settings, the demonstration that matters is *how to build the map*, not *what to do*. This is a different prescription from standard SFT (clone the expert action sequence). It is also different from DAgger ([same day, 2026-05-14](2026-05-14-dagger-llm-agents.md)), which clones expert labels at student-encountered states. MAP says: clone the *exploration policy*, not the *execution policy*.

## Connections

- **ARC-AGI-3 three systematic reasoning errors** ([2026-05-02](../llms-foundation-models/2026-05-02-arc-agi-3-three-systematic-reasoning-errors.md)) identified the three failure modes. MAP fixes one (delayed perception). The other two (premature commitment, brittle composition) are unaddressed.
- **AgentLens Lucky Pass** ([2026-05-14](2026-05-14-agentlens-lucky-pass-swe-eval.md)) measures the symptom: 10.7% of passing trajectories are chaotic. MAP attacks the cause: agents that didn't build a prior. Two papers on the same day diagnosing the same disease from opposite ends.
- **AutoTTS** ([2026-05-11](2026-05-11-autotts-agentic-discovery-test-time-scaling.md)) discovers TTS controllers. With MAP, the discovered controllers could become per-environment-after-mapping rather than environment-agnostic. The natural composition: MAP builds the environment prior, AutoTTS discovers the TTS controller conditional on that prior.
- **Corpus2Skill** ([2026-04-18](2026-04-18-corpus2skill-knowledge-navigation.md)) and **Intern-Atlas method-evolution-graph** ([2026-05-01](2026-05-01-intern-atlas-method-evolution-graph.md)) both proposed structured-environment-representation ideas for navigation. MAP is the explicit cognitive-map version at runtime, not over a corpus.

## Research angle

1. **Map persistence across tasks.** The paper builds task-specific maps. The natural follow-up: persist the global-exploration prior across tasks in the same environment, do task-specific mapping on top. That converts MAP from per-task agent design into an environment-level agent memory system.
2. **Map quality measurement.** The paper does not appear to publish a map-quality metric. AgentLens-style process labels could give one: was the exploration-stage map sufficient for the execution-stage decisions? That metric would close the loop with AgentLens directly.
3. **MAP versus DAgger.** Both papers are on the same day and both target long-horizon agent quality. MAP says clone the exploration policy; DAgger says clone the expert labels at student-encountered states. A controlled comparison on SWE-bench (DAgger's home benchmark) or ARC-AGI-3 (MAP's home benchmark) would establish which prescription dominates.

## Where it lives

Update [multi-agent-systems.md](multi-agent-systems.md) and [agent-benchmarks.md](agent-benchmarks.md) — MAP is the first cognitive-map paradigm paper in the wiki and the strongest ARC-AGI-3 result to date.
