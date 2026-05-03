---
source: raw/huggingface/2026-05-02-compliance-versus-sensibility-reasoning-controllability-llms.md
date: 2026-05-02
arxiv: https://arxiv.org/abs/2604.27251
---

# Compliance vs Sensibility: Reasoning Controllability in LLMs

## TL;DR

LLMs learn reasoning patterns (induction, deduction, abduction) so deeply during pre-training that they resist instruction-level override. When you force a model to use an "unnatural" reasoning type for a task, it prefers the task-appropriate pattern over the instruction — and still performs well, because it's using parametric memory, not actually following the instruction. The key finding: reasoning types are *linearly encoded* in middle-to-late layers, which means mechanistic interventions can increase compliance by up to 29%.

## Key findings

- Models consistently favor task-appropriate reasoning over conflicting instructions.
- High performance under "wrong" reasoning type reveals reliance on internalized parametric memory rather than instruction-following.
- This behavior scales with model size — larger models are *more* likely to override instructions with internally "correct" patterns.
- Reasoning-type conflicts produce detectable drops in confidence scores (useful as a diagnostic signal).
- Reasoning types are *linearly encoded* in middle-to-late transformer layers.
- Mechanistic intervention on those layers increased instruction-following compliance by up to 29%.

## Mechanism

```
Task: "Using deductive reasoning, classify this sentiment."
Model's internal preference: inductive (pattern-matching from examples)

Observed behavior:
  - Model uses inductive reasoning despite instruction
  - Output is high-quality (uses parametric memory)
  - Confidence score drops slightly vs. natural-pattern condition
  - Linear probes on layers 16-24 show inductive encoding, not deductive

Intervention:
  - Identify "reasoning direction" in residual stream at layer N
  - Steer toward deductive encoding
  - Compliance increases +29%, quality maintained
```

## Implications

Three downstream uses of this finding:

1. **Fine-tuning and instruction-following research** — if you're training a model to follow reasoning-type instructions, you need to target the representation layer, not just the output. Behavioral cloning on outputs misses the underlying mismatch.

2. **RAG and structured prompting** — prompts that mandate a specific reasoning approach (e.g. "use first principles") may be silently overridden. The model produces a convincing output using a different path.

3. **Mechanistic interpretability** — reasoning type as a linearly separable direction in the residual stream is a clean target for future work. This is the same family of finding as emotion directions, factuality directions, etc.

## Relation to prior wiki knowledge

This paper opens a gap in the current knowledge base: reasoning controllability has not been a concept page topic. The mechanism (parametric memory overriding instructions) is a concrete instance of the broader instruction-following brittleness that the safety literature documents, but it's the first paper to localize it to reasoning-type encoding specifically.

The linear-encoding finding parallels interpretability work on factuality (04-18 cluster), but applied to reasoning mode rather than factual content.

## Open questions

1. Does the 29% compliance gain from mechanistic intervention generalize across reasoning types, model families, and task domains?
2. Can the confidence-score drop from reasoning conflicts be used as a real-time signal in production (e.g. to flag unreliable outputs)?
3. How does this interact with chain-of-thought prompting? CoT presumably reinforces the model's natural reasoning type.

## Links

- Raw: [raw/huggingface/2026-05-02-compliance-versus-sensibility-reasoning-controllability-llms.md](../../../raw/huggingface/2026-05-02-compliance-versus-sensibility-reasoning-controllability-llms.md)
