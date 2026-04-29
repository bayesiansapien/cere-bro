# Claude for Creative Work: MCP Connectors for Blender, Adobe, Ableton, Autodesk

**Date:** 2026-04-29  
**Sources:** [Anthropic Announcement](https://www.anthropic.com/news/claude-for-creative-work) · [AI Breakfast](https://aibreakfast.beehiiv.com) · [Adobe tweet](https://x.com/Adobe/status/2049154741544870369) · [Claude Code model config](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)  
**Raw:** raw/gmail/2026-04-29-starred.md

---

## TL;DR

Anthropic launched Claude for Creative Work on April 29, 2026: MCP-based connectors for Blender (3D/animation), Autodesk (CAD/engineering), Adobe (50+ Creative Cloud apps), and Ableton (music production). Simultaneously, Claude Code gained `/model` and `--model` flags for dynamic routing across models, and Remote Control push notifications for async task monitoring. Anthropic is expanding globally (Sydney office, Canva/Xero integrations). The Claude Opus access model changed — now opt-in even for Pro users, explicitly pricing compute-intensive usage separately.

---

## MCP Connectors

### Blender Connector

Built on Blender's Python API + MCP. Enables:
- Natural-language scene inspection ("what objects are in this scene?")
- Procedural edits via generated Python scripts
- Multi-step 3D workflows without leaving the chat interface

The key mechanism: Claude generates Blender Python API calls, MCP executes them in the running Blender instance, and returns results. This is the same pattern as Claude Code's bash tool, applied to a creative tool's scripting layer.

### Adobe Creative Cloud Integration

Adobe connected Claude to 50+ Creative Cloud apps including Photoshop and Premiere. The integration exposes the internal data layers (layer structure, timeline data, asset metadata) not just the file format. This enables multi-step production workflows across apps via natural language — e.g., "take the hero shot from Lightroom, apply the brand color grade, export a square crop for social" executing across multiple Creative Cloud apps in a single Claude request.

### Autodesk and Ableton

Autodesk integration targets CAD/engineering workflows — parametric modeling, design iteration, constraint checking. Ableton integration targets music production: pattern generation, mixing decisions, arrangement feedback. Both use MCP as the execution bridge.

The pattern across all four: Claude as the reasoning layer, MCP as the API gateway, the creative tool as the execution environment.

---

## Claude Code Changes

### Dynamic Model Routing

New `/model` slash command and `--model` CLI flag let developers route tasks to specific models per-task:
```
claude --model claude-opus-4-7 "complex architecture analysis"
claude --model claude-haiku-4-5 "generate test fixture"
```

This is explicit cost/capability routing — the same concept SemiAnalysis was measuring as "cost per task" vs "cost per token." A developer can now use Haiku for cheap, repetitive tasks and Opus for architectural decisions within the same workflow.

### Remote Control Push Notifications

Claude Code sends push notifications when long tasks finish or need input — users can leave the terminal and return when work is done. Requires the session to remain active locally (this is not a cloud-persistent agent). This addresses the main friction point for long-horizon agentic tasks: you can't just watch a terminal for 20 minutes.

---

## Opus Access Model Change

Anthropic is separating baseline Claude access from compute-intensive reasoning. Opus is now opt-in even for Pro subscribers, with explicit pricing for long-context and heavy inference workloads. This mirrors how OpenAI structured GPT-5.5's reasoning levels (xhigh/high/medium/low/non-reasoning) — the industry is converging on explicit compute budgets for users.

SemiAnalysis noted (04-24) that "Opus 4.6 Fast is the only Fast/Priority SKU that has gained real traction." The new opt-in model may reflect Anthropic's economics: most users don't need Opus-tier compute most of the time, and subsidizing it universally is expensive.

---

## Prior Context

**Connects to Claude Code Architecture (04-17, 04-19):** The `/model` and `--model` flags are the user-facing manifestation of the routing layer described in the architecture pages. Claude Code's tool execution loop now has explicit model selection at the task level, not just at the session level.

**Connects to UCP Agentic Commerce (04-29):** Same day, two different dimensions of "agents taking over structured workflows." UCP is agents in commerce; Claude Creative Work connectors are agents in creative production. The common thread: MCP as the protocol for exposing domain-specific APIs to LLM reasoning.

**Connects to Anthropic policy thread (04-17):** The Mythos policy page noted that Anthropic was restricting access to high-capability models. The Opus opt-in change is consistent — rather than restricting by policy, restrict by explicit pricing that reflects actual compute costs.

---

## Related Pages

- [Claude Code Architecture](2026-04-19-claude-code-architecture.md)
- [UCP Agentic Commerce Protocol](2026-04-29-ucp-agentic-commerce-protocol.md)
- [Claude Code vs Hermes Permissions](2026-04-23-claude-code-vs-hermes-permissions.md)
