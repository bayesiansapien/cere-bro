---
date: 2026-04-16
source: huggingface
arxiv: 2604.13201
---

# InfiniteScienceGym: Procedurally-Generated Benchmark for Scientific Analysis

**TL;DR:** InfiniteScienceGym generates unbounded scientific analysis benchmarks from a seed — no static corpus needed. It exposes that no model exceeds 45% accuracy, recognizing unanswerable questions is a major weakness, and stronger models use tools more effectively rather than consuming more tokens.

## Key Findings

- Procedurally generates self-contained scientific repositories with realistic structure and LLM-verifiable QA — avoids publication bias and static dataset problems.
- Includes both answerable and **unanswerable questions** — testing abstention, a major weak spot.
- No proprietary or open-weight model exceeds **45% accuracy** overall.
- **Stronger models use tools more effectively** — not just more token-hungry — suggesting quality of tool use matters more than quantity.
- Benchmarks derived from published studies inherit bias; procedural generation removes this.

## Related Pages

- [Reinforcement Learning for LLMs](rl-for-llms.md)
- [../agentic-systems/agent-benchmarks.md](../agentic-systems/agent-benchmarks.md)

**Raw source:** [../../raw/huggingface/2026-04-16-infinitesciencegym-an-unbounded-procedurally-generated-bench.md](../../raw/huggingface/2026-04-16-infinitesciencegym-an-unbounded-procedurally-generated-bench.md)
