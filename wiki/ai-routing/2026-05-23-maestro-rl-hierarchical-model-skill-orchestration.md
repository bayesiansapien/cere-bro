# Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles

**Date:** 2026-05-23
**Arxiv:** [2605.22177](https://arxiv.org/abs/2605.22177)
**HF papers:** [https://huggingface.co/papers/2605.22177](https://huggingface.co/papers/2605.22177)
**Code:** [github.com/jinyangwu/Maestro](https://github.com/jinyangwu/Maestro)
**Raw source:** [farmer/huggingface](../../raw/huggingface/2026-05-23-maestro-reinforcement-learning-to-orchestrate-hierarchical-m.md)

## TL;DR

Maestro is an RL-trained 4B orchestrator that picks at each step whether to call an external expert, which model-skill pair to invoke, and when to stop. Across ten multimodal benchmarks it reports 70.1% average, ahead of GPT-5 (69.3%) and Gemini-2.5-Pro (68.7%). Crucially, the learned policy generalizes to out-of-domain experts not seen in training: augmenting the registry with new experts gives 59.5% on four challenging out-of-domain benchmarks, ahead of all closed-source baselines. Outcome-based RL, no step-level supervision.

## Why this matters

The wiki has been tracking the routing thread since the 05-01 Ken Huang chapter on routing-with-provider-abstraction, through the 05-08 Netflix state-of-routing piece, the 05-11 CARE bi-level routing for MoE continual learning, the 05-11 Conductor orchestration paper by Sakana, and the 05-15 RouteProfile work. Most of these route between LLMs at the model level. Maestro routes one level deeper: between (model, skill) pairs in a two-tier registry. This is the same architectural move that the 05-18 MM-Skills paper made for visual agents (skill-packages with mounted instructions) but with outcome-based RL replacing prompted module-selection. Two papers in five days establishing a hierarchical (model × skill) routing surface is a pattern.

## Mechanism

A two-tier registry: a set of frozen expert models, and a skill library indexed under each model. A 4B policy LLM observes the task state at each step and emits one of three actions: invoke an external expert, select a (model, skill) pair, or terminate. The policy is trained by outcome-based RL using rollouts on the training tasks: positive reward when the orchestrated trajectory solves the task, no reward otherwise. No step-level supervision and no per-skill reward shaping.

The unusual finding is OOD generalization. The policy learned with one set of experts in the registry generalizes when new experts (different model families, different skill types) are added. This is the property that distinguishes a real routing policy from a memorized lookup table.

## Key takeaways

- 4B orchestrator achieves 70.1% average on ten multimodal benchmarks (math reasoning, chart understanding, high-resolution perception, domain-specific analysis).
- Beats GPT-5 (69.3%) and Gemini-2.5-Pro (68.7%) at headline accuracy.
- OOD: augmenting registry with unseen experts yields 59.5% on four challenging benchmarks, ahead of all closed-source baselines.
- Outcome-based RL, no step-level supervision. Code public.

## Gaps

The 4B orchestrator beating GPT-5 is a frontier-model claim that wants ablations on which benchmarks drive the average. If the 70.1% is concentrated on benchmarks where GPT-5 is known to underperform (chart understanding, domain-specific perception), the headline overstates the result. The paper does not yet report latency / cost economics of the orchestrated stack, which is the dimension that decides production adoption. Composition with the 05-11 CARE bi-level routing (which routes between MoE experts in a continual-learning setting) is not addressed.

## Related wiki pages

- [LLM Routing](./llm-routing.md) — the parent concept page.
- [Conductor / Sakana (2026-05-11)](2026-05-11-conductor-sakana-orchestrating-frontier-models.md) — orchestrating frontier models via a smaller policy.
- [CARE bi-level routing (2026-05-11)](2026-05-11-care-bi-level-routing-moe-continual-learning.md).
- [RouteProfile (2026-05-15)](2026-05-15-routeprofile-llm-profile-design-space.md).
- [MM-Skills (2026-05-18)](../agentic-systems/2026-05-18-mmskills-multimodal-skill-packages-visual-agents.md) — skill-package framing for visual agents.

## Research angle

The OOD generalization claim is the load-bearing one. If it holds at scale, the routing policy becomes a transferable artifact: train once on one registry, deploy on any registry. That would make routing a separable middleware product, not a per-stack engineering job. The next-quarter falsifier: does the OOD result hold when the augmented experts come from completely different modality families (audio, video, code), or only when they are variations of the trained-on multimodal families? Maestro reports OOD inside multimodal; cross-modality is the harder test.
