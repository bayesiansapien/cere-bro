---
source: HuggingFace Daily Papers
arxiv_ids: [2605.06642, 2605.06130, 2605.06614]
date: 2026-05-09
tier: 2
topics: [agent-skills, agent-rl, skill-curation, trajectory-abstraction, multi-turn-rl]
---

# Skill Curation Cluster: StraTA, Skill1, SkillOS

## TL;DR

Three papers, same day, same problem: how should an agent learn from its own past trajectories? Each picks a different layer of the stack.

- **StraTA (2605.06642)** abstracts trajectories into compact strategies, conditions actions on the strategy, trains both jointly via hierarchical GRPO. ALFWorld 93.1%, WebShop 84.2%.
- **Skill1 (2605.06130)** trains a single policy to co-evolve skill *selection*, *utilization*, and *distillation* from a unified task-outcome reward. Low-frequency reward trend credits selection; high-frequency variation credits distillation.
- **SkillOS (2605.06614)** decouples a frozen executor from a trainable skill-curator that updates an external SkillRepo. The curator generalizes across executor backbones and task domains.

Three layers: trajectory-level strategy (StraTA), per-policy skill loop (Skill1), external curator (SkillOS). The community is converging on persistent skill memory as the missing piece in agent RL.

## Why this matters

The bottleneck in agentic RL has been credit assignment over long-horizon trajectories with sparse outcome rewards. The week's three papers all attack this through skill abstraction, but at different granularities. The fact that three independent labs shipped the same week, all targeting the same gap, means the field has converged on the diagnosis: agents need persistent, reusable skill memory, and the open question is where in the stack it lives.

## Compositional map

```
SkillOS:    [Executor (frozen) ◄── retrieves ── SkillRepo (external) ◄── trained curator]
                                                       │
                                                       │ candidate insertion point
                                                       ▼
Skill1:     [Policy: select ──► utilize ──► distill ──► library]
                       (single policy, single reward, dual-frequency credit)
                                              │
                                              │ a single trajectory is also
                                              ▼
StraTA:     [State ──► strategy ──► action₁ → action₂ → ... → action_T ──► reward]
                          ▲                                              │
                          └── hierarchical GRPO credits both ◄───────────┘
```

StraTA gives you the per-trajectory strategy primitive. Skill1 gives you the within-policy skill lifecycle. SkillOS gives you the cross-task persistent repo. They are not competing; they are layers in the same stack. The natural composition: SkillOS-style external repo, populated by Skill1-style distillation, conditioned by StraTA-style strategy abstraction.

## Connections to prior wiki

**Confirms the [Corpus2Skill](../../agentic-systems/2026-04-18-corpus2skill-knowledge-navigation.md) (04-18), [CTX2Skill](../../agentic-systems/2026-05-05-ctx2skill-self-evolving-skills.md) (05-05), and [MedSkillAudit](../../agentic-systems/2026-05-07-medskillaudit-domain-specific-agent-skill-audit.md) (05-07) thread.** Wiki has been tracking skill curation for three weeks. Today's batch raises the count to six papers on this concept. The threshold for declaring a pattern is three. We're at six. **Persistent skill memory is now a settled open subfield, not a speculative one.**

**Connection to Claude Managed Agents "Dreaming" (Anthropic, 05-07/08).** Anthropic's Dreaming feature is the production embodiment of the same pattern: an external memory store, asynchronously updated by analyzing past sessions, attached to future sessions. Dreaming is SkillOS in production. Outcomes is the rubric layer that StraTA's strategy abstraction tries to learn. The research-to-product time on this primitive is sub-month.

**Refines a [LongAct](../../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md) (04-18) open question.** LongAct asked whether saliency profiling could run online during training. StraTA's hierarchical GRPO answers it indirectly: condition action gradients on a per-trajectory strategy, and credit assignment becomes tractable without explicit saliency profiling.

## Research angle

1. **Where does the abstraction layer live?** SkillOS argues external (separate curator, separate repo). Skill1 argues internal (single policy, single reward). StraTA argues per-trajectory (one strategy per task). All three ship empirical wins on overlapping benchmarks (ALFWorld, WebShop). The next paper is the one that runs the head-to-head with matched compute.
2. **Cross-domain generalization.** SkillOS claims the curator generalizes across executor backbones and task domains. That claim is strong and falsifiable. Whether SkillRepo learned on WebShop transfers to a coding-agent benchmark is a cleaner test of the underlying hypothesis.
3. **Composition with [EMO](../../inference-efficiency/2026-05-09-emo-pretraining-moe-emergent-modularity.md) (also today).** EMO's expert pool subset is the architectural primitive that lets a SkillRepo skill correspond to an actual model slice instead of a prompt template. EMO plus SkillOS is the candidate primitive for genuinely deployable, sliceable skill systems.

## Sources

- StraTA: https://arxiv.org/abs/2605.06642 · raw `2026-05-09-strata-incentivizing-agentic-reinforcement-learning-with-str.md`
- Skill1: https://arxiv.org/abs/2605.06130 · raw `2026-05-09-skill1-unified-evolution-of-skillaugmented-agents-via-reinfo.md`
- SkillOS: https://arxiv.org/abs/2605.06614 · raw `2026-05-09-skillos-learning-skill-curation-for-selfevolving-agents.md`
