# PEAM: Parametric Embodied Agent Memory through Contrastive Internalization

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.27762](https://arxiv.org/abs/2605.27762) · [HuggingFace](https://huggingface.co/papers/2605.27762) · [raw](../../raw/huggingface/2026-05-28-peam-parametric-embodied-agent-memory-through-contrastive-in.md)

## TL;DR

PEAM moves embodied-agent memory from inference-time retrieval to parameter-resident skills. A slow deliberative LLM handles open-ended reasoning, while a fast parametric module (multimodal MoE-LoRA with per-category physically isolated adapters) handles reflexive execution. Failure-correction trajectory pairs are internalized through a joint behavioral-cloning and contrastive objective, so the agent learns both what succeeds and how a corrected action differs from the failed one. Two governance pieces decide what and when to consolidate: a parameterization-worthiness score for "should this experience become a skill" and a scale-free self-triggered mechanism for "consolidate now" that transfers across task distributions without re-tuning. In Minecraft, PEAM improves long-horizon performance, avoids forgetting on previously consolidated skills, and improves parametric-versus-retrieval efficiency over both retrieval-based and parametric-memory baselines.

```
PEAM dual-loop:

  Slow LLM (deliberative) ─── open-ended reasoning
              │                            ▲
              │  consolidate-worthy?       │ promote skill
              ▼                            │
  Fast parametric module:                  │
   ┌─────────────────────────┐             │
   │ MoE-LoRA, per-category  │ ──── reflexive execution
   │ physically isolated     │
   │ adapters                │
   └─────────────────────────┘

  Training: failure ─ correction pairs ─► BC + contrastive loss
```

## Key findings

- Per-category physically isolated LoRA adapters give parameter-level continual learning without catastrophic forgetting on previously consolidated skills.
- Failure as a first-class training signal (failure-correction pair) outperforms training on successes only.
- The parameterization-worthiness score decides what to internalize; the scale-free trigger decides when, without per-task tuning.
- Trigger transfers across task distributions without re-tuning, suggesting genuine generality.
- Improves long-horizon performance and parametric efficiency over retrieval and parametric-memory baselines.

## How this fits prior wiki state

PEAM continues the wiki's running agent-memory thread, where the central problem is: when does an episodic event become a procedural skill? The cluster going back includes MemForest (2026-05-26 hierarchical temporal memory), SEAL (2026-05-26 agent-environment co-evolution), SAM (2026-05-27 state-adaptive memory), SuperLocalMemory (2026-04-17), DeltaMem (2026-05-13), EvolveMem (the agent-memory cluster summary). PEAM differs in that consolidation is parametric (LoRA adapters) rather than indexed retrieval. The "physically isolated adapters" detail is what unlocks continual learning without forgetting.

The SkillOpt thread (Ken Huang, today via Gmail+RSS, plus prior page [[2026-05-25-skillopt-executive-optimizer-agent-skills]]) is the text-space analog: optimize a skill document. PEAM is the weight-space analog. Both are answers to the same question of where agent skills should live; one says "write better instructions", the other says "write better adapters". A natural composition is possible: SkillOpt-optimized prompts during the slow loop, PEAM-consolidated LoRA adapters in the fast loop.

## Related pages

- [[2026-05-25-skillopt-executive-optimizer-agent-skills]] — text-space skill optimization
- [[2026-05-26-memforest-hierarchical-temporal-agent-memory]] — hierarchical episodic memory
- [[2026-05-27-sam-state-adaptive-memory]] — state-adaptive memory in agents
- [[agent-memory]] — concept page

## Research angle

The failure-correction contrastive objective is the most transferable contribution. Most agent training pipelines today train on successes; PEAM shows the corrective delta carries information that pure imitation loses. A clean test: train an SWE-Bench agent on failure-fix pairs vs successful-PR pairs at matched data volume. If the failure-correction recipe also wins on coding, the implication is broad.
