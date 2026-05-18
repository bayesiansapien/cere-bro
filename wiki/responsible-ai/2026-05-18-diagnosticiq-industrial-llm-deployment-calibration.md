# DiagnosticIQ: LLM Deployment Calibration Bottleneck in Industrial Maintenance

**Date ingested:** 2026-05-18
**Source:** HuggingFace Daily Papers 2026-05-18
**arXiv:** [2605.08614](https://arxiv.org/abs/2605.08614)
**Tier:** 2 (responsible AI, deployment)
**Raw:** [raw/huggingface/2026-05-18-diagnosticiq-...md](../../raw/huggingface/2026-05-18-diagnosticiq-a-benchmark-for-llm-based-industrial-maintenanc.md)

## TL;DR

DiagnosticIQ is a 6,690-question benchmark for the rule-to-action step in industrial maintenance: given an engineer-authored symbolic monitoring rule that has triggered, recommend the correct corrective action. The benchmark is derived from 118 rule-action pairs across 16 asset types via a symbolic-to-MCQA pipeline that normalises rules to Disjunctive Normal Form and samples distractors via embeddings. Five variants probe different failure modes (Pro, Pert, Verbose, Aug, Rationale). The benchmark is hard: nine human practitioners average 45.0%, confirming specialist knowledge is required. Three findings stand out. First, the frontier has closed: the top three LLMs sit within one Macro point. Second, brittleness under distractor expansion: every model loses 13-60% relative accuracy on DiagnosticIQ Pro. Third, pattern-matching exposure: under condition inversion, frontier models still select the original answer 49-63% of the time.

## Why it matters

The headline finding is structural: **the deployment bottleneck is calibration, not capability**. Frontier models handle the template-style cases fine. They break under structural perturbation in predictable ways. For any deployment that depends on LLMs reading engineering rules, the model selection axis has flattened (top three are tied within 1 Macro point), and the discriminating axis is robustness to rule-rewriting.

The 49-63% original-answer rate under condition inversion is the most actionable finding for deployment teams. It means the model is recognising the surface pattern of the rule, not the logical content. A maintenance action that depends on a condition being true will be recommended even when the condition has been inverted. In a safety-critical setting (heavy industrial equipment) this is a deployment failure mode that cannot be patched with prompt engineering.

## Connection to prior wiki context

**Hodoscope (Kurate cs.AI #11 this week, 2026-04-13, ai_rating 7.2/10, unsupervised monitoring for AI misbehaviors).** Hodoscope is the upstream interpretability work; DiagnosticIQ is the deployment-level diagnostic surface. The composition is operational: Hodoscope identifies anomalous behaviour signatures, DiagnosticIQ provides labelled cases where the model is known to fail under perturbation.

**Value-Conflict Diagnostics (Kurate cs.AI #12 this week, ai_rating 7.0/10, alignment-faking diagnostics).** Same pattern: structural perturbation reveals brittleness that surface evaluation misses. DiagnosticIQ Aug's condition-inversion test is the industrial-deployment analog of value-conflict diagnostics' alignment-faking surface.

**Lucky-Pass rate from AgentLens (2026-05-14, the process-aware labeling system that found 10.7% of passing SWE-bench Verified trajectories are Lucky Passes where the right answer fell out for the wrong reasons).** DiagnosticIQ Aug's condition-inversion result is the rule-reasoning analog of Lucky Pass: the model gets the answer right by surface pattern matching, not by logical engagement with the rule.

## Research angle

The 13-60% relative-accuracy drop on DiagnosticIQ Pro is the diagnostic to watch. If post-training methods that target this drop (perturbation-augmented RLVR, condition-inversion-augmented SFT) close it, the deployment bottleneck moves elsewhere. If they do not, frontier LLMs are not yet ready for safety-critical industrial-rule deployment regardless of headline accuracy.

## Links

- arXiv: <https://arxiv.org/abs/2605.08614>
- Related: [Value-Conflict Diagnostics surfaced 2026-05-17 Worth Watching](../daily-digest/2026-05/2026-05-17.md)
