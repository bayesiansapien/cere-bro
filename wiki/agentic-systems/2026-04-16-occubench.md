---
date: 2026-04-16
source: huggingface
arxiv: 2604.10866
---

# OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language World Models

**TL;DR:** OccuBench covers 100 professional task scenarios across 65 specialized domains (triage, nuclear safety, customs processing, etc.) using Language World Models (LWMs) that simulate environments via LLM-driven tool response generation — solving the benchmark scarcity problem for professional domains.

## Key Findings

- **Language World Models (LWMs)**: use LLMs to simulate domain-specific tool responses, enabling benchmark creation for any profession without building real environments.
- 15 frontier models evaluated across 8 model families — no single model dominates all industries; each has a distinct occupational capability profile.
- **Implicit faults** (truncated data, missing fields) are harder than explicit errors (timeouts, 500s) because they lack overt error signals.
- Larger models, newer generations, higher reasoning effort consistently improve performance. GPT-5.2 improves by 27.5 points from minimal to maximum reasoning effort.
- Strong agents are not necessarily strong environment simulators — simulator quality is critical for LWM-based evaluation reliability.

## Related Pages

- [Agent Evaluation & Benchmarks](agent-benchmarks.md)
- [Tool Use & Function Calling](tool-calling.md)

**Raw source:** [../../raw/huggingface/2026-04-16-occubench-evaluating-ai-agents-on-real-world-professional-ta.md](../../raw/huggingface/2026-04-16-occubench-evaluating-ai-agents-on-real-world-professional-ta.md)
