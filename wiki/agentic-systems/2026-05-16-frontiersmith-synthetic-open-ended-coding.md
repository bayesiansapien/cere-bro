# FrontierSmith: Synthesizing Open-Ended Coding Problems at Scale

**Source:** HuggingFace Daily Papers · [arXiv 2605.14445](https://arxiv.org/abs/2605.14445)
**Raw:** [farmer file](../../raw/huggingface/2026-05-16-frontiersmith-synthesizing-open-ended-coding-problems-at-sca.md)
**Tier:** 2 — synthetic training data, open-ended coding, long-horizon agents

## TL;DR

LLM coding progress has concentrated on well-defined tasks (feature implementation, bug fixes, competitive programming). Open-ended coding (problems with no known optimal solution) remains weak because training data for it is scarce and expensive. FrontierSmith automates the conversion of **closed-ended coding tasks** (competitive programming seeds) into **open-ended variants** by mutating goals, restricting outputs, and generalizing inputs. A quantitative **idea divergence** metric prunes to candidates that elicit genuinely diverse approaches across different solvers. Agent-generated test cases and verifiers cover the survivors. Training on synthesized data: Qwen3.5-9B improves +8.82 on FrontierCS and +306.36 Elo on ALE-bench; Qwen3.5-27B improves +12.12 and +309.12. Synthesized problems also drive more agent turns and tokens, similar to human-curated ones.

## Why it matters

This is the third paper in three days where the model **constructs its own training substrate** instead of consuming a fixed corpus. **EvoEnv** (2026-05-15) constructs verifiable environments with solve-verify asymmetry. **EvolveMem** (2026-05-15) self-evolves retrieval configuration from failure logs. FrontierSmith evolves training problems from a closed-ended seed corpus. Three papers on the same diagnosis: the bottleneck is not the model, it is the substrate the model trains on, and substrates can be auto-generated if you have a quantitative discriminator (asymmetry condition for EvoEnv, divergence metric for FrontierSmith, failure logs for EvolveMem).

The idea-divergence metric is the operationally interesting part. Most synthetic-data pipelines that mutate seeds suffer from mode collapse: the mutated problems look superficially different but elicit the same solution strategy. FrontierSmith's divergence metric is a filter that keeps only the mutations that genuinely change the solution space. This is the same shape as the diversity scoring that worked for EvolveMem (closed-loop self-evolution): a quantitative diversity prior is doing more work than the generation step.

## Connections to prior wiki state

- **EvoEnv** ([2026-05-15](2026-05-15-evoenv-self-evolving-rl-via-environment-synthesis.md)) — solve-verify asymmetry as invariant for environment synthesis. FrontierSmith's idea-divergence-as-invariant is the problem-synthesis analogue. Both papers identify a structural quantity that lets you auto-generate at scale without quality collapse. The composition (FrontierSmith feeds EvoEnv with seed problems for environment construction) is the natural follow-up.
- **EvolveMem** ([2026-05-15](2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md)) — auto-discovers retrieval configurations via diagnosis on failure logs. FrontierSmith auto-discovers training problems via divergence on solver outputs. Both use AutoResearch-style closed-loop self-evolution.
- **Orchard 67.5% on SWE-bench Verified** ([2026-05-15](2026-05-15-orchard-open-source-agentic-framework.md)) — the agentic post-training infrastructure. FrontierSmith is one source of the **data** Orchard needs. Open-ended coding is where SWE-bench-style closed problems hit their ceiling.
- **FrontierCS / ALE-bench Elo improvements** — Elo gains in the +300 range on open-ended benchmarks are large enough that a follow-up on a frontier model (rather than Qwen3.5) is the obvious next experiment.
- **WildClawBench native runtime** ([2026-05-15](2026-05-15-wildclawbench-native-runtime-agent-benchmark.md)) — WildClawBench tasks average 8 minutes of wall-clock work. The fact that FrontierSmith-trained agents take more turns and use more tokens (similar to human-curated problems) suggests the synthesis pipeline is producing problems with realistic length, not artificially shortened ones.

## How it works

The pipeline has three stages.

**Mutation.** Starting from a competitive programming problem, FrontierSmith generates open-ended variants by (a) changing the goal (instead of "find the optimal X" ask "design a system that achieves good X under varying conditions"), (b) restricting outputs (limit what the solver can return), (c) generalizing inputs (extend to a broader input distribution).

**Idea divergence filter.** Multiple solver agents tackle each candidate problem. An idea-divergence metric quantifies how different their approaches are. Low-divergence problems are pruned (they're essentially the same problem in disguise). High-divergence problems survive.

**Test and verifier generation.** Agents synthesize test cases and verifiers for the surviving problems. Without verifiers, open-ended problems are not RL-trainable. This stage gates whether a candidate can be used downstream.

## Open problems / Research angle

- **FrontierSmith + EvoEnv composition.** FrontierSmith generates open-ended problems; EvoEnv requires verifiable environments. If FrontierSmith's test-and-verifier generation is what gives EvoEnv its solve-verify asymmetry, the two pipelines are partial-duals. The unified pipeline (problem synthesis with built-in solve-verify check) has not been written.
- **Idea-divergence beyond coding.** The divergence-metric mechanism is domain-general: it relies only on a comparable solution space. Whether it transfers to math (where solution space is well-defined), agentic workflows (where it is harder to compare), or scientific discovery (where divergence is the goal) is open.
- **Mode collapse over many generations.** If FrontierSmith is run iteratively (mutated problems become seeds for further mutation), does idea-divergence saturate? Falsifiable: a 30-day follow-up measuring divergence retention over five generations.
- **Frontier-model training.** Qwen3.5-9B and -27B benefit. Whether a frontier-tier model (Opus, GPT-5.5) benefits at the same magnitude is the load-bearing scaling question. Most synthetic-data techniques saturate above a certain model size.

## Concept tags

`synthetic-training-data` · `open-ended-problems` · `idea-divergence` · `closed-loop-synthesis` · `agentic-rl-data`
