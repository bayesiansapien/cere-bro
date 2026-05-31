# In-Writing: Thinking Before Constraining (A Unified Decoding Framework)

**arXiv:** [2601.07525](https://arxiv.org/abs/2601.07525) · **HF Daily Papers:** [page](https://huggingface.co/papers/2601.07525) · **Date:** 2026-05-31 (resurfaced on HF)
**Code:** https://github.com/Nokia-Bell-Labs/InWriting
**Raw:** [farmer file](../../raw/huggingface/2026-05-31-thinking-before-constraining-a-unified-decoding-framework-fo.md)

## TL;DR

There is a standing tension in LLM decoding. Free-form generation gives rich reasoning but unverifiable, unstructured output. Constrained decoding (forcing the output to match a grammar or JSON schema) guarantees a parseable format but, when the constraint is applied from the first token, it can interrupt the model mid-thought and degrade reasoning. In-Writing resolves this in a single generation call: the model reasons freely first, and structured decoding only switches on after the model emits a trigger token, explicitly decoupling the reasoning phase from the formatting phase. The paper's technical contribution is trigger-token strategies that virtually eliminate "premature triggering," the failure where constrained decoding clamps down while reasoning is still in progress. Across classification and reasoning datasets, In-Writing beats state-of-the-art by up to 27% over natural generation.

## The mechanism

```
Constrained-from-start (bad):  [CONSTRAIN ▓▓▓▓▓▓▓▓▓]  ← grammar clamps token 1, reasoning crippled
Free-form (unverifiable):      [ reason freely .......... ] ← no structure, hard to parse

In-Writing (one call, two phases):
  [ free-form reasoning ............ ] ⟨TRIGGER⟩ [ CONSTRAINED structured output ]
                                         │
                          trigger-token strategy prevents PREMATURE triggering
                          (clamping before reasoning is done)
```

## What problem it solves

Production systems need machine-parseable output (JSON, a label set, a schema) but also need the model's full reasoning to get the answer right. The two requirements have been in conflict: turn on the grammar early and reasoning suffers; leave it off and you cannot reliably parse the result, needing brittle post-hoc extraction. In-Writing gets both in one pass by sequencing them rather than forcing them simultaneously.

## Core novelty

The trigger-token mechanism that cleanly separates an unconstrained reasoning phase from a constrained formatting phase *within a single decode*, plus the analysis showing the trigger strategies "virtually eradicate" premature triggering. Prior hybrid approaches either made two separate calls (reason, then format) or accepted that early constraints hurt reasoning; In-Writing makes the phase transition a learned/triggered event inside one generation.

## Key takeaways

- Single-call hybrid: free-form reasoning then structured decoding after a trigger token, decoupling reasoning from formatting.
- Trigger-token strategies **virtually eliminate premature triggering** (constraints interrupting active reasoning).
- Up to **+27% accuracy over natural generation** across classification and reasoning tasks.
- Code released (Nokia Bell Labs).

## Gaps in the study

The headline "+27% over natural generation" is measured against unstructured free-form output, not against the strongest two-call reason-then-format baseline, so the gain over a well-engineered pipeline (rather than over naive generation) is less clear. The evaluation is classification and reasoning tasks where the structured target is relatively simple; whether the single-call phase transition holds for deeply nested schemas or long structured outputs (where premature triggering has more chances to fire) is untested. Trigger-token reliability under adversarial or out-of-distribution prompts is not characterized.

## Relation to prior wiki state

In-Writing is the decoding-layer entry in the wiki's structured-output thread. Ken Huang Ch 15 (05-02) documented how Claude Code and Hermes both converge on tool-use forcing as the portable structured-output mechanism, and flagged that schema support is a per-model capability. In-Writing attacks the same goal (reliable structured output) from a different layer: instead of forcing a tool call, it sequences an unconstrained then a constrained phase inside one decode. It also connects to the reasoning-versus-format tradeoff that runs through the agentic pages, where premature commitment to a format is a known failure mode, and it rhymes with RePoT (today) in spirit: both are about not destroying a partially-correct generation, RePoT by resuming from a verified prefix, In-Writing by not clamping the format before the reasoning is complete. The "decouple reasoning from the structured commitment" move is the decoding analog of the broader pattern that mixing two objectives prematurely produces conflicting gradients (the dimension-collapse diagnosis from the reward-modeling papers).

## Research angle

The sharp open question is whether the trigger-token phase transition can be made *adaptive* rather than a single switch: hard problems might need to re-enter free-form reasoning after partially emitting structure (interleaving reasoning and formatting), which a one-shot trigger cannot express. A multi-trigger version that toggles between reasoning and constrained phases on demand would be the natural generalization, and it would let the model "step out" of a schema to reason about a hard field before committing. Measuring In-Writing against a strong two-call reason-then-format baseline on deeply nested schemas is the experiment that would establish whether the single-call framing is a genuine win or a convenience.

## Links

- [arXiv 2601.07525](https://arxiv.org/abs/2601.07525)
- [Ken Huang Ch 15: structured output (05-02)](../agentic-systems/2026-05-02-ken-huang-ch15-structured-output.md)
- [RePoT: recoverable program-of-thought (05-31)](../agentic-systems/2026-05-31-repot-recoverable-program-of-thought.md)
