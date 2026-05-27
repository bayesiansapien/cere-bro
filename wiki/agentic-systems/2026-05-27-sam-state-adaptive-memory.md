# SAM: State-Adaptive Memory for Long-Horizon Reasoning Agents

**Source:** HuggingFace daily papers (2026-05-27, 2 upvotes) · arxiv 2605.24468
**arxiv:** [2605.24468](https://arxiv.org/abs/2605.24468)
**Date:** 2026-05-27
**Raw:** [raw/huggingface/2026-05-27-sam-state-adaptive-memory-for-long-horizon-reasoning-agent.md](../../raw/huggingface/2026-05-27-sam-state-adaptive-memory-for-long-horizon-reasoning-agent.md)
**Tier:** 2 (agentic systems, agent memory)

## TL;DR

Long-horizon agents act over histories full of thoughts, tool calls, observations, and partial conclusions, and the hard part is not just that the history is long but that the piece needed now may sit far back and only become relevant later. Truncation, compression, and retrieval all ignore how access should *adapt to the agent's evolving state*. SAM casts long-horizon reasoning as state-adaptive memory: it consolidates the ongoing interaction into compact memory cues while keeping the raw trajectory pages for intent-driven recall. The cues are not replacements for history; they are lightweight handles that let the agent reconstruct temporally distant information on demand, without retraining the backbone. The memory module is optimized with expert-guided supervision plus RL, aligned to trajectory-level utility. On BrowseComp, BrowseComp-ZH, WideSearch, and HLE, SAM beats strong baselines across diverse agent backbones.

```
SAM memory:

  interaction stream ──► compact memory cues (lightweight handles)
        │                         │ aligned to trajectory utility
        │                         │ via expert supervision + RL
        ▼                         ▼
  raw trajectory pages ◄── intent-driven recall (reconstruct distant info on demand)
  (kept, not discarded)         when current state needs it
        backbone unchanged (no retraining)
```

## Key points

- **State-adaptive, not fixed compression.** The decision of what past context to surface is conditioned on the agent's current need, rather than a static truncation/summary computed once.
- **Cues as handles, not replacements.** Raw trajectory pages are preserved; the compact cues are pointers that let the agent reconstruct distant detail when intent demands, avoiding the lossy-summary failure mode.
- **Backbone-frozen.** SAM is a standalone module trained with expert-guided supervision and RL on trajectory-level utility, so it drops onto existing agent models without retraining them.
- **Consistent gains** across BrowseComp, BrowseComp-ZH, WideSearch, HLE on multiple backbones.

## Relation to prior wiki state

SAM is the third agent-memory framing in two days, and the contrast is the interesting part. [MemForest (05-26)](2026-05-26-memforest-hierarchical-temporal-agent-memory.md) made memory a write-efficient time-indexed forest (a *data structure* move). [Language Models Need Sleep (05-27)](../inference-efficiency/2026-05-27-language-models-need-sleep.md) made consolidation an offline iterative pass that folds context into SSM fast weights (a *weight-level* move). SAM makes recall *state-conditioned*: the same separation of "compact handle vs full raw page" but with the retrieval decision driven by the agent's evolving intent rather than a fixed index or a one-shot consolidation. All three refuse the flat-global-summary baseline, and all three decouple memory construction/recall from the base forward pass, exactly the decoupling [Scaling the Harness (05-27)](2026-05-27-scaling-the-harness.md) names as the "trustworthy memory" bottleneck of the agent harness. The "keep raw pages, summarize into handles" design also rhymes with SkillEvolBench's (05-26) finding that distilled abstractions under-transfer versus raw-trajectory reuse: SAM hedges by keeping both.

## Why it matters

For multi-step search and research agents, where the relevant fact often surfaces many steps after it was seen, state-adaptive recall is the difference between an agent that loses the thread and one that holds it. Because SAM is backbone-frozen and trained as a module, it is the kind of memory layer a harness can adopt without retraining the underlying model.

## Gaps

Evaluated on search/browse and HLE benchmarks; whether state-adaptive recall holds on agentic coding (where the relevant context is code state, not retrieved facts) is untested. The memory module's RL training adds a moving part that the flat-summary baselines avoid.

## Links

- [Paper](https://arxiv.org/abs/2605.24468)
- Raw: [raw/huggingface/2026-05-27-sam-state-adaptive-memory-for-long-horizon-reasoning-agent.md](../../raw/huggingface/2026-05-27-sam-state-adaptive-memory-for-long-horizon-reasoning-agent.md)
- Related: [MemForest 2026-05-26](2026-05-26-memforest-hierarchical-temporal-agent-memory.md), [Language Models Need Sleep 2026-05-27](../inference-efficiency/2026-05-27-language-models-need-sleep.md), [Scaling the Harness 2026-05-27](2026-05-27-scaling-the-harness.md)
