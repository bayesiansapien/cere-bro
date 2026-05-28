# Verus-SpecGym: Agentic Environment for Specification Autoformalization

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.26457](https://arxiv.org/abs/2605.26457) · [HuggingFace](https://huggingface.co/papers/2605.26457) · [code](https://github.com/formal-verif-is-cool/verus-spec-gym) · [raw](../../raw/huggingface/2026-05-28-verus-specgym-an-agentic-environment-for-evaluating-specific.md)

## TL;DR

Formal verification of AI-written code only helps if the formal spec actually matches what the user meant. Verus-SpecGym studies whether LLM agents can do that translation reliably. Verus-SpecBench is 581 spec-writing tasks derived from Codeforces problems and targeting Verus, a Rust verifier. Verus-SpecGym is the matching agentic environment, where the model interacts with Verus, bash, and the filesystem to develop and check specs. Evaluation works by extending Verus's exec_spec mechanism so generated specs can run as Rust code, then testing them against official Codeforces tests plus adversarial "hacks" (edge cases competitors wrote to break wrong solutions). Gemini 3.1 Pro solves 77.8% of tasks, other frontier models 51.1 to 57.8%, and open-source models 21.5 to 25.5%. Failure modes are concrete: model-generated specs omit important input assumptions, accept incorrect outputs, or reject valid ones. LLM-as-a-judge evaluation misses 26% of the failures the executable evaluator catches.

```
Standard formal-verif loop:                    Verus-SpecGym:
  user problem ─► spec ─► code + proof          user problem ─► agent in env
                  ▲          ▲                                    │
                  hand-written by expert                          ├ runs Verus
                  (expensive bottleneck)                          ├ runs bash
                                                                   ├ executes spec as Rust
                                                                   ├ tested vs Codeforces hacks
                                                                   ▼
                                                              spec graded by behavior
```

## Key findings

- 581 spec-writing tasks; targets Verus, the Rust verifier; specs evaluated by execution against Codeforces tests and adversarial hacks.
- Frontier-model ceiling: Gemini 3.1 Pro 77.8%; other frontier 51 to 58%; OSS 21 to 26%.
- Concrete failure modes: missing input assumptions, accepting incorrect outputs, rejecting valid ones.
- LLM-as-a-judge misses 26% of the failures the executable evaluator catches.
- Spec autoformalization is within reach for frontier agents on problems where they can already write correct code, but remains brittle.

## How this fits prior wiki state

The 26% LLM-judge miss rate is the same finding ScientistOne ([[2026-05-28-scientistone-chain-of-evidence]]) reports today on the research-manuscript side. CoE Audit catches failures that LLM judges miss; Verus-SpecGym's exec_spec evaluator catches spec failures LLM judges miss. Two independent papers in one day report the same operational result: judge-model evaluation under-reports failure when an executable check is available.

Verus-SpecGym also touches the cost-discipline cluster from yesterday. Specification autoformalization is the upstream half of any verified-coding agent stack; if specs are wrong 22 to 49% of the time even on problems the agent can otherwise solve, then verified-coding pipelines need an extra verification layer aimed at the spec itself, not just the implementation. That extra layer is exactly the executable evaluator this paper proposes.

## Related pages

- [[2026-05-28-scientistone-chain-of-evidence]], same finding on the research-manuscript side
- [[2026-05-28-omniverifier-m1]], symbolic verification with rule-based RL rewards
- [[2026-05-27-agent-token-consumption]], token economics in agentic coding
- [[code-generation]], concept page

## Research angle

The 26% gap between LLM-judge and executable evaluation suggests the field's "agent-as-judge" pipelines are systematically over-reporting agent quality whenever an executable check exists but is not used. The natural follow-up is a survey of agentic benchmarks: which of them rely on LLM judges where an executable evaluator could exist, and what does the corrected score look like. The other open question is whether spec autoformalization scales: 581 Codeforces problems are competitive-programming shape, and whether the same agents can write Verus specs for production Rust code at industrial scale is untested.
