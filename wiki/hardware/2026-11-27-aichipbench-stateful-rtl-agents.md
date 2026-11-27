---
title: "AIChipBench: coding agents building LLM decoder hardware fail on stored state"
date: 2026-11-27
source: https://arxiv.org/abs/2611.33093
raw: ../../raw/huggingface/2026-11-26-aichipbench-benchmarking-llm-agents-for-automated-ai-acceler.md
tags: [hardware-design, rtl, accelerators, coding-agents, benchmarks]
signal: HuggingFace 11-26
---

# AIChipBench

**TL;DR.** Agents write synthesizable RTL (register-transfer-level hardware code) for quantized Qwen3.5, Gemma 3/4 and Llama 3.2 decoders, checked against an integer reference that fixes both the outputs and the stored state at every decoding step. The hard part is state: a decoder carries state between tokens, so a wrong update can leave this token right and corrupt one several tokens later. Across 9,136 attempts by four coding agents, pointing feedback at the first state mismatch raised acceptance by 25.0-46.9 points in all 12 agent-task cells and halved agent-hours per accepted design. But 45 of 69 accepted designs failed within 32 steps when regraded on new sequences.

<div class="dg-title">Passing the output test is not passing the design</div>
<div class="dg-sub">State-level feedback is what moves acceptance; held-out sequences expose the rest.</div>

```mermaid
flowchart LR
  A["Coding agent<br/><small>writes decoder RTL</small>"] --> T["Public tests<br/><small>fixed budget</small>"]
  T -->|output only| F1["Weak signal<br/><small>state bugs hidden</small>"]
  T -->|first state mismatch| F2["Strong signal<br/><small>+25 to +47 points</small>"]
  F2 --> A
  A --> H["Held-out grading<br/><small>resets, stalls, synthesis</small>"]
  H --> X["45 of 69 fail<br/><small>within 32 steps</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class A core
  class T loop
  class F1,X err
  class F2 exit
  class H input
  linkStyle 2 stroke:#2f9e44,stroke-width:2px
  linkStyle 3 stroke:#f08c00,stroke-width:2px
```

<div class="dg-legend">Purple is the agent, amber is the test loop, green is the feedback that works, red is what still fails.</div>

## Key findings

- Difficulty lives in stored state (KV and decode registers), not arithmetic.
- First-state-mismatch feedback beats output-only feedback in every one of 12 agent-task cells, +25.0 to +46.9 points, and halves agent-hours per accepted design.
- 45 of 69 accepted designs fail on fresh sequences within the 32 steps the tests required: development tests are far too short.
- More than a third of speed-up attempts on a correct design (second track, near-fixed area) end without one.
- Overall ranking: Sol 5.6 and Fable 5.1 above Astra 6 and Opus 5.5, stable across all 200 random instance splits.

## How it relates to prior wiki pages

- **Same lesson as KernelBench-style agent work** (KernelShift, 11-25): agents recombine known idioms and stall on new abstractions; here the new abstraction is cross-step state.
- **Mirrors Anthropic's Rust migration** (11-26): tests said 98% done while production parity was 25%. Both say the verifier, not the generator, is the bottleneck.
- **Confirms** the 11-26 Looking Ahead call that agent benchmarks need repeated-run and held-out reliability numbers: 65% of accepted designs fail held-out.

## Gaps

Small edge-scale decoders only; no timing closure on a real process node; four agents.

Related: [gpu-kernels](../inference-efficiency/gpu-kernels.md) · [agent-benchmarks](../agentic-systems/agent-benchmarks.md) · [compute-economics](compute-economics.md)
