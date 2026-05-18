# MMSkills: Multimodal Skills for General Visual Agents

**Date ingested:** 2026-05-18
**Source:** HuggingFace Daily Papers 2026-05-18
**arXiv:** [2605.13527](https://arxiv.org/abs/2605.13527)
**Tier:** 2 (agentic systems, multimodal, skill libraries)
**Raw:** [raw/huggingface/2026-05-18-mmskills-...md](../../raw/huggingface/2026-05-18-mmskills-towards-multimodal-skills-for-general-visual-agents.md)

## TL;DR

MMSkills argues that visual-agent skill packages need to be multimodal, not text-only. Each MMSkill is a compact state-conditioned package: a textual procedure plus runtime state cards plus multi-view keyframes. The packages are derived from public non-evaluation interaction trajectories via an agentic generator that performs workflow grouping, procedure induction, visual grounding, and meta-skill auditing. At inference time a branch-loaded agent inspects state cards and keyframes in a temporary branch, aligns with the live environment, and distills structured guidance for the main agent. Across GUI and game-based visual-agent benchmarks, MMSkills consistently improve both frontier and smaller multimodal agents.

## Why it matters

The dominant skill-library pattern in agentic systems is text-only: skills are stored as natural-language procedures or executable code. MMSkills is the first wiki entry that treats procedural knowledge as inherently multimodal. For a visual agent, "click the save button" is incomplete; the agent must recognise the save button visually under the specific layout of the moment. State cards (snapshots of recognised UI configurations) and keyframes (visual references for procedure steps) are the missing layers.

The branch-loaded inference pattern is the second contribution. The main agent does not carry the full multimodal context, which would explode the image-token budget. The temporary branch consults the package, aligns with the live environment, and emits structured text guidance back to the main agent. This is a routing pattern: heavy multimodal evidence on a side branch, light textual guidance on the main path.

## Connection to prior wiki context

**ctx2skill (2026-05-05, the self-evolving skill-library paper).** ctx2skill grew text-only skills from context. MMSkills extends the skill substrate to multimodal. The wiki now has three skill-library entries: corpus2skill (2026-04-18, knowledge navigation), ctx2skill (2026-05-05, self-evolving), MMSkills (today, multimodal). The trajectory is from text retrieval to text self-evolution to multimodal package.

**Branch-loaded inference and the routing surface.** The main-agent + side-branch pattern echoes the Conductor (2026-05-11, Sakana's RL-trained orchestrator) and Step-level Optimization for Computer-Use Agents (2026-05-02) frame. In all three, the cheap path is the default and a specialised path is invoked under specific signals. MMSkills routes by skill-relevance; Conductor routes by task complexity; Step-level Optimization routes by progress signal.

**CurveBench / WildTableBench / MemEye-MemLens cluster (2026-05-15 and 2026-05-17).** Those papers identified the VLM structural-representation gap (Gemini 3.1 Pro at 71.1% on CurveBench Easy and 19.1% Hard, 1 of 21 frontier VLMs above 50% on WildTableBench). MMSkills addresses the same gap from the deployment side: rather than training the VLM to represent structure better, supply structured multimodal evidence at inference time. Whether MMSkills closes the CurveBench gap as effectively as RLVR (which lifted Qwen3-VL-8B from 2.8% to 33.3% on CurveBench-Easy) is an open evaluation.

## Research angle

1. **Cross-benchmark transfer.** The paper evaluates on GUI and game benchmarks. Whether MMSkill packages generalise to CurveBench / WildTableBench (structural visual reasoning) would test whether the multimodal-skill abstraction is fundamental or harness-specific.
2. **Skill-package staleness.** UI layouts and game states evolve. The state cards and keyframes encode a moment in time. How fast packages need to be refreshed and whether stale packages actively hurt is the production-deployment question.

## Links

- arXiv: <https://arxiv.org/abs/2605.13527>
- Related: [ctx2skill 2026-05-05](2026-05-05-ctx2skill-self-evolving-skills.md), [Conductor 2026-05-11](../ai-routing/2026-05-11-conductor-sakana-orchestrating-frontier-models.md)
