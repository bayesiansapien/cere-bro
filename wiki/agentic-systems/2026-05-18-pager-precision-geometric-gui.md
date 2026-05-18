# PAGER: Bridging the Semantic-Execution Gap in Point-Precise Geometric GUI Control

**Date ingested:** 2026-05-18
**Source:** HuggingFace Daily Papers 2026-05-18
**arXiv:** [2605.15963](https://arxiv.org/abs/2605.15963)
**Tier:** 2 (agentic systems, GUI, vision-language)
**Raw:** [raw/huggingface/2026-05-18-pager-...md](../../raw/huggingface/2026-05-18-pager-bridging-the-semantic-execution-gap-in-point-precise-g.md)

## TL;DR

GUI agents trained on the dominant region-tolerant paradigm (any pixel inside the same component is a valid click) fail at precision-sensitive tasks where actions must land on specific points in continuous canvas space. Local coordinate errors cascade through dependency-driven geometric constructions, distorting downstream objects and invalidating the final output. The paper introduces PAGE Bench (4,906 problems, 224K process-supervised pixel-level GUI actions) to measure this regime. The headline diagnostic: general multimodal models achieve over 88% action-type accuracy but under 6% task success. The gap between knowing what action to take and executing it precisely is the Semantic-Execution Gap. PAGER addresses it through dependency-structured planning plus pixel-level execution, with precision-aligned RL using state-conditioned geometric feedback. Result: 4.1x higher task success than the strongest general baseline; step success rate from under 9% (GUI specialists) to over 62%.

## Why it matters

The 88% vs 6% gap is the structural story. Action-type accuracy has been the de facto GUI-agent metric for two years. The PAGE Bench result shows it is decoupled from task success in the precision-sensitive regime. This is structurally similar to the agent harness 18-point spread WildClawBench reported on 2026-05-15: when the evaluation only measures one layer of capability, agents look uniformly good despite massive deployment-relevant variation.

The Semantic-Execution Gap framing generalises beyond CAD-style geometric tasks. Any agentic task with cascading dependencies (multi-file refactors, sequential mathematical derivations, multi-step robotic manipulation) has the same structure: local accuracy is necessary but not sufficient because errors compound.

## Connection to prior wiki context

**CurveBench (2026-05-17, the nested-Jordan-curves benchmark where Gemini 3.1 Pro reaches 71.1% on Easy and 19.1% on Hard, with RLVR lifting Qwen3-VL-8B from 2.8% to 33.3% on CurveBench-Easy).** CurveBench measures structural visual reasoning. PAGE Bench measures structural visual execution. Both report large gaps; PAGER closes its gap mostly via post-training RL with state-conditioned feedback, similar in spirit to CurveBench's RLVR result. The pattern is now consistent across two benchmarks in two days: structural gaps in VLMs are post-training-learnable.

**WildClawBench (2026-05-15, the agent benchmark that measured an 18-point spread between best and worst agent harness running the same model on the same 60 long-horizon tasks).** WildClawBench made the case that harness drives benchmark numbers more than model capability does. PAGE Bench makes the case that geometric execution drives task success more than action-type accuracy does. Both papers identify that benchmark headline numbers can decouple from deployment relevance through a structural axis.

**Step-level Optimization for Computer-Use Agents (2026-05-02).** That paper introduced trajectory-aware routing for GUI agents. PAGER's dependency-structured planning is the structural-task generalisation of the same idea: route the agent's attention through the dependency graph of the task rather than treating each step as independent.

## Research angle

Falsifiable: does PAGER's recipe (dependency-structured planning + precision-aligned RL with state-conditioned geometric feedback) transfer to non-GUI structural tasks? Run the same recipe on CurveBench or on multi-file code-refactor benchmarks.

## Links

- arXiv: <https://arxiv.org/abs/2605.15963>
- Related: [CurveBench 2026-05-17](../vision-audio-video/2026-05-17-curvebench-hierarchical-topological-reasoning.md), [Step-level Optimization 2026-05-02](../ai-routing/2026-05-02-step-level-optimization-computer-use-agents.md)
