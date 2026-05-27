# Trajel: Auditing Trajectory-Level Hallucinations in Multi-Agent Workflows

**Source:** HuggingFace daily papers (2026-05-27, 4 upvotes) · arxiv 2605.24219
**arxiv:** [2605.24219](https://arxiv.org/abs/2605.24219)
**Date:** 2026-05-27
**Raw:** [raw/huggingface/2026-05-27-beyond-final-answers-auditing-trajectory-level-hallucination.md](../../raw/huggingface/2026-05-27-beyond-final-answers-auditing-trajectory-level-hallucination.md)
**Tier:** 2 (responsible-ai, agentic)

## TL;DR

Most hallucination benchmarks grade only the final answer, missing failures born in intermediate Thought-Action-Observation steps. Trajel is a dataset and framework for auditing trajectory-level hallucinations in multi-agent industrial workflows, built on a five-type taxonomy (factual, referential, logical, procedural, scope-based) over expert-annotated traces from AssetOpsBench. Benchmarking supervised detectors at subtask, trajectory, and long-context levels, it finds the most common failure modes are invisible to final-answer benchmarks, nearly half of hallucinated trajectories mix multiple types, and detectors with high binary accuracy still miss the subtlest types. Trajectory-aware detection significantly beats post-hoc final-output verification.

## Key points

- **Final-answer benchmarks hide the real failures.** Errors that originate mid-trajectory often don't change the final answer's surface plausibility but corrupt the process.
- **Five-type taxonomy** (factual, referential, logical, procedural, scope) with expert annotations; ~half of bad trajectories exhibit multiple types simultaneously.
- **Trajectory-aware detection > post-hoc verification**, making taxonomy-grounded, step-level evaluation necessary for safe agent deployment.

## Relation to prior wiki state

Trajel extends the measurement-crisis thread the wiki named on 05-26. [Faithfulness Metrics Don't Measure Faithfulness (05-26)](2026-05-26-faithfulness-metrics-meta-evaluation.md) showed that CoT-faithfulness metrics perform near chance against ground truth; Trajel makes the parallel point one level up, for *agent trajectories*: final-output checks miss the intermediate hallucinations, and you need step-level ground truth to catch them. Two benchmarks in two days arguing the field's safety-evaluation infrastructure measures the wrong surface. It also operationalizes the "verification-and-governance layer" that [Scaling the Harness (05-27)](../agentic-systems/2026-05-27-scaling-the-harness.md) names: trajectory-level auditing is exactly the harness-level evaluation (trajectory quality, not one-shot success) that paper calls for.

## Gaps

Built on AssetOpsBench (industrial-operations traces); whether the taxonomy and detector results transfer to coding or research agents is open. Detection still misses the subtlest types even at high binary accuracy.

## Links

- [Paper](https://arxiv.org/abs/2605.24219)
- Raw: [raw/huggingface/2026-05-27-beyond-final-answers-auditing-trajectory-level-hallucination.md](../../raw/huggingface/2026-05-27-beyond-final-answers-auditing-trajectory-level-hallucination.md)
- Related: [Faithfulness Metrics 2026-05-26](2026-05-26-faithfulness-metrics-meta-evaluation.md), [Scaling the Harness 2026-05-27](../agentic-systems/2026-05-27-scaling-the-harness.md)
