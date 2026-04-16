---
date: 2026-04-16
source: huggingface
arxiv: 2604.09409
---

# Do AI Coding Agents Log Like Humans? An Empirical Study

**TL;DR:** A study of 4,550 agentic PRs across 81 OSS repos finds AI coding agents change logging less often than humans (in 58% of repos), fail to follow explicit logging instructions 67% of the time, and leave humans acting as "silent janitors" who fix logging after the fact.

## Key Findings

- Agents exhibit **higher log density** when they do log, but log in fewer files than humans overall.
- Explicit logging instructions are rare (4.7% of PRs) and largely ineffective — agents fail constructive requests 67% of the time.
- Humans perform **72.5% of post-generation log repairs** without explicit review feedback — "silent janitor" pattern.
- Suggests deterministic guardrails (not natural language instructions) are needed for consistent agent logging behavior.

## Related Pages

- [Agent Evaluation & Benchmarks](agent-benchmarks.md)

**Raw source:** [../../raw/huggingface/2026-04-16-do-ai-coding-agents-log-like-humans-an-empirical-study.md](../../raw/huggingface/2026-04-16-do-ai-coding-agents-log-like-humans-an-empirical-study.md)
