# RPT: Reflective Prompt Tuning through Language Model Function-Calling

**arXiv:** [2605.21781](https://arxiv.org/abs/2605.21781) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.21781) · **Date:** 2026-05-31
**Raw:** [farmer file](../../raw/huggingface/2026-05-31-reflective-prompt-tuning-through-language-model-function-cal.md)

## TL;DR

Automated prompt optimization usually works one of two ways: search over many candidate prompts, or run a fixed critique-refine loop driven by individual examples or small batches. Both have a blind spot, they react to one example at a time and never form a systematic picture of *how* the prompt fails across the whole task. RPT (Reflective Prompt Tuning) reframes optimization to mimic how a human prompt engineer actually works. An LLM optimizer calls a diagnostic function that evaluates the target model over the *entire* optimization set, summarizes recurring failure modes, and returns a structured diagnostic report. The optimizer then revises the prompt using that report plus an accumulated memory of prior reports, so each edit is grounded in failure history rather than a single misfire. RPT also supports confidence-aware optimization by feeding calibration signals into both the diagnostic feedback and the final prompt selection. Across three reasoning tasks it improves over the initial prompt by up to 12.9 points, stays competitive with state of the art, and improves confidence calibration, with the largest gains on multi-hop and mathematical reasoning.

## The mechanism

```
Prior auto-prompting: react to one example / small batch ─► local critique-refine (misses systematic patterns)

RPT (function-calling reflective loop):
   LLM optimizer
       │ calls diagnostic_fn(prompt) over the WHOLE optimization set
       ▼
   structured diagnostic report  ──►  memory of prior reports (accumulated)
       │                                     │
       └──────────► revise prompt ◄──────────┘   (edits grounded in failure history)
                         │  + calibration signals (confidence-aware select)
                         ▼   repeat
```

## What problem it solves

Prompt design is labor-intensive and notoriously brittle to phrasing, formatting, and instruction order, which is why automated prompt optimization exists. But existing methods optimize myopically: a candidate search or a per-example critique loop can fix the example in front of it without noticing that the prompt systematically mishandles, say, multi-hop questions. RPT gives the optimizer a whole-set diagnostic and a memory, so it can target the recurring failure pattern instead of chasing individual errors.

## Core novelty

Using LLM function-calling to simulate the human prompt-engineer workflow: a diagnostic function that aggregates failures across the full optimization set into a structured report, plus an accumulated memory of prior reports so revisions build on diagnostic history. The confidence-aware variant folds calibration signals into both the feedback and the final selection, which is why RPT improves calibration and not just accuracy, a property most prompt-optimizers ignore.

## Key takeaways

- Diagnostic function evaluates the target model over the **entire optimization set** and returns structured, recurring-failure-mode reports, not per-example critiques.
- An **accumulated memory of prior reports** grounds each prompt revision in failure history.
- Up to **+12.9 points** over the initial prompt across three reasoning tasks; competitive with SOTA.
- **Improves confidence calibration** via calibration-aware diagnostics and selection; largest gains on multi-hop and mathematical reasoning.

## Gaps in the study

Evaluating the target model over the *entire* optimization set every iteration is the expensive part, and the paper does not report the compute cost relative to candidate-search or small-batch critique methods, so the accuracy gain's price is unclear. Three reasoning tasks is a narrow base, and the multi-hop/math concentration of gains suggests the diagnostic-report approach may help most where failures are systematic and nameable, with less to offer on tasks whose errors are diffuse. Whether the accumulated memory helps or eventually clutters the optimizer's context over many iterations is not studied.

## Relation to prior wiki state

RPT is a prompt-layer instance of a pattern the wiki has been tracking at the gradient and reward layers: locate the systematic failure and target the edit there, rather than spreading effort uniformly. Where TIP (04-16) targeted the ~10% of distillation tokens that carry signal and the LoRA Parametric Memory Law (05-29) targeted sub-threshold tokens, RPT targets recurring failure modes diagnosed across the whole set. The "use the model's own function-calling to run a structured engineering workflow" framing connects to the agentic-autoresearch thread, today's "Discovering Cooperative Pipelines" (2605.30003) has an outer-loop agent rewrite an inner pipeline's prompts and feedback functions, which is RPT's diagnostic-driven revision pushed up to the level of an autonomous researcher editing code. Both are versions of an LLM systematically improving an LLM system, with a structured diagnostic standing in for human intuition. The calibration-awareness also ties to the broader reliability thread (BeliefTrack 05-30, confidence as a control signal in Conf-KV 05-30): confidence is increasingly treated as a first-class signal to optimize, not a byproduct.

## Research angle

The decisive question is cost-effectiveness versus the alternatives: a whole-set diagnostic every iteration is expensive, and the open experiment is whether RPT's failure-history grounding beats a cheap candidate search at *matched compute*, not just matched iteration count. If RPT wins at matched compute, the structured diagnostic is genuinely worth its price; if not, it is a more interpretable but not more efficient optimizer. A second angle: because RPT improves calibration, it could be paired with a confidence-routing system (route to a stronger model only when the RPT-tuned prompt's calibrated confidence is low), turning prompt optimization and routing into a joint objective, a composition no paper has measured.

## Links

- [arXiv 2605.21781](https://arxiv.org/abs/2605.21781)
- [Discovering Cooperative Pipelines: autoresearch for social dilemmas (05-31)](../agentic-systems/2026-05-31-repot-recoverable-program-of-thought.md)
- [RL for LLMs concept page](rl-for-llms.md)
