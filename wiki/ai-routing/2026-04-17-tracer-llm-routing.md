---
source: raw/huggingface/2026-04-17-tracer-trace-based-adaptive-cost-efficient-routing-for-llm-c.md
arxiv: https://arxiv.org/abs/2604.14531
date: 2026-04-17
---

# TRACER: Trace-Based Adaptive Cost-Efficient Routing for LLM Classification

## TL;DR

Every LLM classification call already produces a labeled input-output pair. TRACER collects these production traces, trains a cheap ML surrogate on them, and routes future traffic to the surrogate when it agrees with the LLM above a confidence threshold. On a 150-class benchmark, the surrogate fully replaces the LLM teacher.

## Key Findings

- **Free training data**: production logs are an existing labeled dataset — no annotation cost
- **Parity gate**: the surrogate is only deployed when its agreement with the LLM exceeds a user-set threshold; below threshold, falls back to the LLM
- **Coverage**: 83–100% surrogate coverage on a 77-class intent benchmark depending on quality target; 100% replacement on a 150-class benchmark using Sonnet 4.6 as teacher
- **Interpretability artifacts**: TRACER generates reports describing which input regions the surrogate handles, where it plateaus, and why it defers to the LLM
- **Self-aware rejection**: on a natural language inference task where embedding representation can't support reliable separation, the parity gate correctly refuses to deploy the surrogate

## How It Works

```
Production traffic
       │
       ▼
  LLM classifier  ──────────────────────────────► answer + log (label)
       │                                                  │
       │                                          Training set grows
       │                                                  │
       ▼                                                  ▼
  TRACER surrogate  ◄──── trained on traces ────  Lightweight ML model
  (cheap, fast)
       │
  Parity gate: does surrogate agree with LLM ≥ threshold?
       │
       ├─ YES → serve surrogate response (near-zero cost)
       └─ NO  → fall back to LLM
```

## Why It Matters

This closes the loop between LLM deployment and cost reduction automatically. No manual labeling, no separate annotation pipeline — the LLM teaches the surrogate through its own production behavior. The parity gate is the safety mechanism: interpretability artifacts make the routing boundary auditable.

## Related Pages

- [LLM Routing](llm-routing.md)
