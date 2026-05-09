---
source: HuggingFace Daily Papers
arxiv_id: 2605.05724
date: 2026-05-09
tier: 2
topics: [agentic-research, training-recipes, auto-ml, closed-loop-empirical]
---

# Auto Research with Specialist Agents Develops Effective and Non-Trivial Training Recipes

## TL;DR

Autonomous closed-loop empirical research without human-in-the-loop. Specialist agents partition the training-recipe surface, share measured lineage across trials, propose hypotheses + executable code edits + outcomes + feedback. Across 1,197 headline-run trials and 600 control trials, no humans chose proposals, edited recipes, overrode scores, or repaired failed trials. Reduces Parameter Golf validation bpb by 0.81%, raises NanoChat-D12 CORE by 38.7%, reduces CIFAR-10 Airbench96 wallclock by 4.59%.

## Why this matters

The "no human in the loop" claim is the load-bearing piece. The 38.7% NanoChat-D12 gain on CORE is large enough to take seriously. If the closed-loop generalizes, the labor model for training-recipe research changes: the human picks the search surface and writes the evaluator, the system runs the loop.

## Connections to prior wiki

- **Confirms the Evaluation-driven Scaling thread (04-22)**: same outer loop, both bet on external measurement as the steering signal.
- **Contradicts KernelBench-X (also today)** in one specific way. KernelBench-X says iterative refinement on kernel generation improves correctness but not performance. This paper says iterative refinement on training recipes improves both. The contrast is informative: training-recipe space is denser and smoother than kernel-generation space, so the refinement loop has a usable gradient signal in one but not the other.
- **Composition with [Skill1](2026-05-09-skill-curation-cluster-strata-skill1-skillos.md)**: the closed-loop here proposes recipes; Skill1 distills successful trajectories into reusable skills. The pair gives you a self-improving research system rather than a one-shot search.

## Research angle

1. The cost of 1,797 trials is real money. The cost-per-bpb-improvement number determines whether this is a research-grade or production-grade primitive.
2. Whether the gains transfer to a recipe surface the system wasn't trained on (i.e., does the specialist-agents partition generalize) is open.

## Source

- Paper: https://arxiv.org/abs/2605.05724
