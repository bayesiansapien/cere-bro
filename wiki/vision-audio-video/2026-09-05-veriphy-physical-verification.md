# VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement

**arxiv:** [2609.03153](https://arxiv.org/abs/2609.03153) · **Source:** [HuggingFace Daily Papers 2026-09-05](../../raw/huggingface/2026-09-05-veriphy-agentic-physical-reasoning-for-world-model-evaluatio.md)

## TL;DR

Video generators produce clips that look right and behave wrong. A scalar quality score cannot tell you *which* physical obligation a clip violates or *when* it broke, which is the information you would need to feed the failure back into training.

VeriPhy replaces the score with an evidence trail. A **text-only planner** reads the prompt and compiles it into **typed physical obligations** plus a statically validated execution plan, all of this before a single frame is observed, so the plan cannot be contaminated by what the video happens to show. Execution then gates and scopes declared calls to frozen low-level experts: segmentation and tracking, counting, **eleven typed physical measurements over the resulting tracks**, depth, OCR, and audio-event detection. Every action returns a **provenance-carrying evidence record** whose payload is either a typed measurement or an explicitly tagged learned state. Typed resolvers and fixed composition map the usable records to a three-valued verdict, supported, contradicted, or unknown, surfaced as plausible, implausible, or abstain.

The evaluation is anchored in a **1,500-clip corpus of human-annotated flaw records** that localise real generation failures in prompt reference, space and time. On a 149-clip core carrying **304 such records, VeriPhy accounts for 228**, against **164** for a published question-decomposition evaluator given the same clips and claims. The honest part of the paper is the third number: prompting the same backbone monolithically reaches **222**, so recall alone does not separate the architecture from a well-prompted single call. **What separates them is that each VeriPhy decision retains its evidence record and provenance**, making the traces auditable one verdict at a time and usable as an interface through which a critic verdict could be written back into generation.

## Key findings

- **228 of 304 human-annotated flaw records accounted for**, against 164 for the published question-decomposition baseline on identical clips and claims.
- **Monolithic prompting of the same backbone reaches 222**, and the paper says so. The architectural gain over a strong naive baseline is 6 records, not 64.
- **Plan-before-observation** is the structural commitment: obligations are compiled from the prompt and statically validated before any frame is read.
- **Three-valued output with an explicit abstain** rather than a forced binary, with every verdict traceable to the records that produced it.

## Relation to prior wiki state

**It is the fourth paper today arguing that a scalar score conditioned on unstated assumptions is the failure mode.** [Select, Compress, Reinvest (09-05)](../inference-efficiency/2026-09-05-select-compress-reinvest-visual-tokens.md) measured a 0.07 to 3.74 point gap between two harnesses running the same published rules at the same budget, which is larger than most reported margins in its area. The [Last Translation Benchmark (09-05)](../llms-foundation-models/2026-09-05-last-translation-benchmark.md) replaces automatic translation metrics with **handcrafted per-example verification rules** naming concrete failure cases, on the argument that automatic metrics are reward-hackable and unactionable. [OVMI (09-05)](2026-09-05-ovmi-speech-bci-common-measure.md) shows that word error rate computed only over the words a speech interface supports overstates how much of a user's intended speech it can convey. VeriPhy is the same move for physical plausibility: **stop reporting a number, start reporting which obligation broke and what evidence says so.**

This is the general form of the pattern statement the [agent benchmarks](../agentic-systems/agent-benchmarks.md) page reached on 09-04, that any benchmark reporting one number is conditioning on something it has not stated. Four papers on one day, in four unrelated modalities, independently choosing structured verdicts over scalars, is the threshold this wiki uses for declaring convergence rather than coincidence.

## Gaps

The architecture's advantage over monolithic prompting is 6 records out of 304 on a 149-clip core, which is well inside the range where a different prompt would flip the ordering, so the case for VeriPhy rests entirely on auditability rather than accuracy. The evidence pipeline depends on frozen low-level experts whose own error rates are not propagated into the three-valued verdict, so a tracking failure and a genuine physics violation may be indistinguishable in the record. The eleven typed physical measurements are a fixed vocabulary, and the corpus of obligations a text prompt can express is not. And the write-back-into-generation use is described as possible, not demonstrated.

## Related pages

- [Agent Evaluation & Benchmarks](../agentic-systems/agent-benchmarks.md)
- [Daily digest 2026-09-05](../daily-digest/2026-09/2026-09-05.md)
