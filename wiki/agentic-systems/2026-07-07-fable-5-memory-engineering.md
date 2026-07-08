# Claude Fable 5, Part 3: Memory Engineering

**Source:** Ken Huang / Agentic AI | **Date:** 2026-07-07

## TL;DR

Anthropic's memory tool is now GA on the Messages API, working on Claude 4+ models generally. The tool is entirely client-side: Claude issues file operations against a `/memories` directory, and your application executes them. Anthropic stores nothing. Memory poisoning is now an official attack class documented in Anthropic's "How we contain Claude" post (May 25), but the memory tool's own security docs never mention poisoning or prompt injection. A new arXiv preprint on forensic trajectory signatures for detecting memory poisoning achieves AUC 0.9904.

## The Memory Stack (Four Layers)

1. **CLAUDE.md** — frozen policy, loads every session, must stay small and earn every line
2. **Lessons directory** — distilled knowledge, one lesson per file, index loads every session, files load on demand
3. **Progress log / feature checklist** — project state, read at session start, written at session end
4. **Transcripts / artifacts** — raw evidence, never auto-load, exist so a lesson can point back at proof

Content moves up the stack only by earning it: verified outcomes update state files, state distills into lessons, and a lesson that keeps proving itself graduates into CLAUDE.md.

## Multi-Session Pattern

Anthropic's official pattern: an initializer session sets up memory files (progress log, feature checklist) before any substantive work. Every later session resumes from those files, not from a transcript. The rule: mark a feature complete "only after end-to-end verification confirms it works, not when the code is written."

## Memory Poisoning

Anthropic's "How we contain Claude" (May 25) has a subsection titled "Persistent memory poisoning." It names the surfaces: product memory, CLAUDE.md files, mounted workspaces, and state directories of scheduled and long-running agents. An injection reaching memory "reloads at every agent startup." A poisoned web page hits one session; a poisoned lesson file hits every session from now on.

The gap: the memory tool's official security section covers sensitive data, path traversal, file size, and expiration. The words "poisoning" and "prompt injection" appear nowhere on that page.

## Detection Research

Jun Wen Leong's "Forensic Trajectory Signatures for Agent Memory Poisoning Detection" (arXiv, June 29) shows that successful memory-poisoning attacks leave detectable fingerprints in an agent's tool-call sequence. A single hand-written rule hit AUC 0.9563; a 19-feature random forest hit 0.9904. Early signal, not settled defense.

## Related Wiki Pages

- [J-Space Global Workspace](../responsible-ai/2026-07-07-j-space-global-workspace.md) — memory activation layer
- [Agent Memory](../agentic-systems/agent-memory.md)
- [Fable 5 Loop Engineering](../agentic-systems/fable-5-loop-engineering.md)

## Raw Source

[Ken Huang: Claude Fable 5, Part 3: Memory Engineering](https://kenhuangus.substack.com/p/claude-fable-5-part-3-memory-engineering)