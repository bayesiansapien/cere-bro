# InteractWeb-Bench: Multimodal Agents under Non-Expert User Instructions

**arXiv:** 2604.27419 · [paper](https://arxiv.org/abs/2604.27419) · [HF](https://huggingface.co/papers/2604.27419)
**Tier:** 2 — agent benchmarks (interactive, multimodal)
**Raw:** [../../raw/huggingface/2026-05-01-interactweb-bench-multimodal-agent-blind-execution-website-generation.md](../../raw/huggingface/2026-05-01-interactweb-bench-multimodal-agent-blind-execution-website-generation.md)

## TL;DR

Existing website-generation benchmarks assume idealized inputs (well-structured, information-rich). Real users give ambiguous, incomplete, or contradictory low-code instructions, and frontier multimodal agents fall into **"blind execution"** — they generate code that satisfies their misreading of the instruction without ever asking for clarification. **InteractWeb-Bench** introduces four user-agent personas + persona-driven instruction perturbations grounded in requirements-engineering defect taxonomies, and an interactive environment with a unified action space (Clarify, Implement, Verify, Submit). Result: frontier MLLM agents remain trapped in blind execution.

## Why blind execution matters

This is the first benchmark to *explicitly grade clarifying behavior*. Most agent benchmarks reward final-result correctness and ignore intermediate uncertainty management. InteractWeb-Bench treats the **decision to ask vs guess** as a first-class evaluation dimension. Frontier agents that score well on static benchmarks fail here because they default to immediate execution rather than uncertainty-aware interaction.

This generalizes well beyond website generation. Any agent deployed to real users (where instructions are inherently ambiguous) faces the same trade-off: clarify (annoying but safe) vs guess (fast but error-prone). Most current systems guess.

## Connection to prior wiki

- **Claw-Eval-Live (05-01)** found 66.7% pass rate on workflow tasks. InteractWeb-Bench reveals one likely contributor: agents don't ask for clarification when they should. Two benchmarks today, complementary diagnoses.
- **MERRIN (04-16) / OccuBench (04-16)** showed agents struggle on ambiguous/noisy multimodal evidence. InteractWeb-Bench formalizes this as an *interaction* failure rather than a *retrieval* failure.
- **AVR / Adaptive Visual Reasoning (04-20)** introduced an explicit "ask for more info" action. InteractWeb-Bench is the natural benchmark for evaluating that line of work.
- **VAKRA (04-16)** characterized agent reasoning failure modes; "blind execution" is a clean, quantifiable instance Vakra would predict.

## Research angle

The four-action space (Clarify/Implement/Verify/Submit) is a useful primitive for agent harness design. The natural next paper: **a router that learns to call Clarify based on instruction-ambiguity signal**, trained on InteractWeb-Bench. Routing within an agent's action space is a Tier 1 intersection (action-trajectory routing) — clarify-vs-execute is fundamentally a routing decision.

## Open problems

- The four user-agent personas may not capture real-user heterogeneity. Real low-code users have wildly different ambiguity profiles. Persona generalization is the next test.
- Clarification cost is not modeled. Asking-too-often is also a failure mode in deployment; the benchmark needs a clarification-budget axis.
