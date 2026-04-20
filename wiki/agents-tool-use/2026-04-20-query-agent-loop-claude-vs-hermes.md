---
date: 2026-04-20
source: raw/rss/2026-04-20-agentic-ai-chapter-3-the-query-agent-loop-claude-code-vs-hermes-ag.md
url: https://kenhuangus.substack.com/p/chapter-3-the-query-agent-loop-claude
tier: 2 — Agent Systems / Architecture
---

# Chapter 3: The Query/Agent Loop — Claude Code vs. Hermes Agent

## TL;DR

A side-by-side architectural comparison of the agent loop in Claude Code (TypeScript, async generator) vs. Hermes Agent (Python, synchronous). The key comparison: Claude Code's loop is a state machine with 7 named continue sites that prevent runaway retry spirals; Hermes uses a dual-gate budget (iteration count + shared IterationBudget counter) that threads safely across parent/child agent trees.

## Key Findings

**Claude Code's 7 continue sites (state machine approach):**
```
collapse_drain_retry        → cheapest: archive messages, no API call
reactive_compact_retry      → medium: summarize old history via fast model  
max_output_tokens_escalate  → single-shot: raise token ceiling to 64K
max_output_tokens_recovery  → multi-turn: inject "resume without recap" message
stop_hook_blocking          → inject hook errors and retry
token_budget_continuation   → warn model it's near budget
next_turn                   → happy path: tools ran, loop continues
```

The `transition` field is the key: it records WHY the loop continued, so the next iteration can make an informed recovery decision. This prevents the common failure mode of infinite retry spirals where the loop keeps retrying the same failed path.

**Hermes' IterationBudget (shared resource approach):**
```python
# Thread-safe shared counter across parent + all child agents
class IterationBudget:
    def consume() → bool   # atomic increment, returns False if exhausted
    def refund() → None    # used for programmatic tool calls that don't count
```

The budget resets per conversation turn, not per session — so subagent usage doesn't carry over. The `refund()` method allows programmatic tool calls (internal utilities, not user-facing actions) to be excluded from the budget count.

**Streaming vs. synchronous:** Claude Code is an async generator that yields events in real time (text appears character-by-character). Hermes returns a final string when done. The streaming design is architectural: async generators compose naturally, so the entire call stack from API response to UI is non-blocking and incremental.

**Context compression:** Hermes fires the ContextCompressor when token usage crosses 50% of context window, before the API call. Claude Code's collapse/compact sites handle this as recovery from near-overflow rather than preventive. Different philosophies: preventive (Hermes) vs. reactive (Claude Code).

## This Builds on the 04-17 and 04-19 Claude Code Analyses

The wiki has now accumulated three deep dives on Claude Code architecture:
- 04-17: First look at the loop and surrounding systems (ML permission classifier, 5-layer compaction)
- 04-19: Reverse engineering comparison with OpenClaw (harness design matters more than model)
- 04-20: Detailed state machine analysis of the 7 continue sites

The cumulative picture: production agent reliability is determined almost entirely by recovery behavior — what the loop does when things go wrong, not what it does on the happy path.

## Relations to Prior Wiki Pages

- **2026-04-17-claude-code-architecture.md**: First architectural analysis, established the 5 surrounding systems
- **2026-04-19-claude-code-architecture.md**: Reverse engineering, OpenClaw comparison, harness design finding
- **GTA-2 (04-20)**: GTA-2 found that execution harness design matters more than model capability. The Claude Code state machine details here explain mechanistically *why* harness design dominates.

## Raw Source

→ [raw/rss/2026-04-20-agentic-ai-chapter-3-the-query-agent-loop-claude-code-vs-hermes-ag.md](../../raw/rss/2026-04-20-agentic-ai-chapter-3-the-query-agent-loop-claude-code-vs-hermes-ag.md)
