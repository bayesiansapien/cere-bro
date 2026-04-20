---
date: 2026-04-20
source: raw/huggingface/2026-04-20-gta-2-benchmarking-general-tool-agents-from-atomic-tool-use.md
arxiv: https://arxiv.org/abs/2604.15715
tier: 2 — Agent Benchmarks / Tool Use
---

# GTA-2: Benchmarking General Tool Agents from Atomic Use to Open-Ended Workflows

## TL;DR

GTA-2 reveals a capability cliff: frontier models already fail below 50% on atomic (single-step) tool use, and nearly all fail on open-ended multi-step workflows, with top models at 14.39% success. The key finding is that execution harness design matters more than the underlying model — Manus and OpenClaw frameworks substantially boost workflow completion beyond what model capability alone predicts.

## Key Findings

**Two-tier benchmark:**
- **GTA-Atomic**: short-horizon, closed-ended, single-tool precision tasks (inherited from GTA-1)
- **GTA-Workflow**: long-horizon, open-ended, multi-tool coordination tasks

**Results:**
- Frontier models: below 50% on GTA-Atomic
- Top models on GTA-Workflow: 14.39% success
- Advanced frameworks (Manus, OpenClaw): substantially better than same model without framework

**Evaluation mechanism for open-ended tasks:** Recursive checkpoint-based evaluation — decomposes the open-ended objective into verifiable sub-goals. Each sub-goal can be independently checked. This solves the binary success/fail problem for tasks with no single correct output.

**Harness design matters:** The finding that the execution framework matters more than the model is the most consequential result. This shifts focus from model capability to scaffolding architecture — consistent with the Claude Code analysis (04-17, 04-19) showing that the while-loop is trivial; the surrounding systems determine real-world performance.

## Connection to Prior Agent Benchmarks

This is the third agent benchmark in the wiki this week:
- OccuBench (04-16): 100 professional task scenarios, Language World Models
- DR3-Eval (04-18): deep research benchmark with static corpus sandboxes
- GTA-2 (04-20): tool use from atomic to workflow, real queries + deployed tools

Together they're converging on the same finding from different angles: **models can't yet complete realistic multi-step tasks reliably.** OccuBench found this in professional tasks. DR3-Eval found this in research tasks. GTA-2 finds it in tool-use workflows. Three papers, same measurement, three weeks.

## Relations to Prior Wiki Pages

- **Claude Code architecture (04-17, 04-19)**: GTA-2 validates the architecture observation — harness design is the differentiator. Claude Code's ML-based permission system, 5-layer compaction, and extensibility mechanisms are exactly the kinds of harness features GTA-2 shows matter.
- **VAKRA (04-16)**: VAKRA documented tool-use failure modes. GTA-2 quantifies the performance gap those failure modes produce at scale.
- **Exploration/Exploitation (04-16)**: GTA-2's workflow failures map to the exploit-too-early failure mode — agents commit to an approach before exploring sufficiently.

## Raw Source

→ [raw/huggingface/2026-04-20-gta-2-benchmarking-general-tool-agents-from-atomic-tool-use.md](../../raw/huggingface/2026-04-20-gta-2-benchmarking-general-tool-agents-from-atomic-tool-use.md)
