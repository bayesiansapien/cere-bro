---
source: raw/huggingface/2026-04-17-dive-into-claude-code-the-design-space-of-today-s-and-future.md
arxiv: https://arxiv.org/abs/2604.14228
date: 2026-04-17
---

# Dive into Claude Code: Architecture Analysis

## TL;DR

A comprehensive architectural analysis of Claude Code v2.1.88 from its public TypeScript source. The core is a simple while-loop — but most of the system is everything built around that loop.

## Key Findings

- **Core loop**: simple while-loop (call model → run tools → repeat). Most complexity lives in the surrounding systems.
- **Five human values** motivating design: human decision authority, safety/security, reliable execution, capability amplification, contextual adaptability
- **Thirteen design principles** traced from values to specific implementation choices
- **Permission system**: 7 modes with an ML-based classifier for deciding what requires user confirmation
- **Context compaction**: 5-layer pipeline for managing context window limits across long sessions
- **Extensibility**: 4 mechanisms — MCP, plugins, skills, hooks
- **Subagent delegation**: built-in orchestration for spawning and coordinating subagents
- **Session storage**: append-oriented (sessions are logs, not state machines)
- **Comparison with OpenClaw**: same recurring design questions produce different architectural answers when deployment context changes

## Architecture Overview

```
Claude Code Core

  ┌─────────────────────────────────────────────┐
  │  while-loop: call model → run tools → repeat │  ← simple core
  └─────────────────────────────────────────────┘
               surrounded by:
  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐
  │  Permission  │  │  Compaction  │  │  Extensibility   │
  │  System      │  │  Pipeline    │  │  MCP/plugins/    │
  │  (7 modes +  │  │  (5 layers)  │  │  skills/hooks    │
  │  ML classify)│  │              │  │                  │
  └──────────────┘  └──────────────┘  └──────────────────┘
  ┌──────────────┐  ┌──────────────────────────────────┐
  │  Subagent    │  │  Append-oriented session storage  │
  │  Delegation  │  │  (sessions are logs)              │
  └──────────────┘  └──────────────────────────────────┘
```

## Why It Matters

This is the first systematic architectural analysis of a frontier AI coding agent. The five values → thirteen principles → implementation traces pattern is a useful framework for evaluating other agent systems. The 5-layer compaction pipeline and ML-based permission classifier are underappreciated design choices that affect reliability and safety at scale.

## Related Pages

- [GUI Agents](gui-agents.md)
- [VAKRA agent failure modes](2026-04-16-vakra-agent-reasoning-failure-modes.md)
