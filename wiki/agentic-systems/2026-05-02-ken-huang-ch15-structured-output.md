# Ken Huang Ch 15 — Structured Output and Schema-Constrained Generation

**Source:** Ken Huang / Agentic AI Substack
**Raw:** [raw/rss/2026-05-02-agentic-ai-chapter-15-structured-output-and-schema-constrained-gen.md](../../raw/rss/2026-05-02-agentic-ai-chapter-15-structured-output-and-schema-constrained-gen.md)
**URL:** https://kenhuangus.substack.com/p/chapter-15-structured-output-and
**Date:** 2026-05-02
**Tier:** 1 — agent harness architecture

## TL;DR

Fifth chapter of Ken Huang's Claude-Code-vs-Hermes series (after Ch 8 memory, Ch 12 skills, Ch 13 MCP, Ch 14 routing). Both harnesses solve schema-constrained output through *tool-use forcing* — wrap the JSON schema as a fake tool, force the model to call it. Claude Code: `SyntheticOutputTool` with Ajv compile, identity-cached by schema reference (~110ms → ~4ms on 80-call workflows), `MAX_STRUCTURED_OUTPUT_RETRIES=5`, structured-output retries don't eat the agent's tool budget, child agents have the synthetic tool stripped from their tool list. Hermes: `extract_structured()` with provider-agnostic tool-choice forcing, JSONL-format trajectory output as infrastructure-level structured output via `batch_runner.py` parallel `multiprocessing.Pool`.

## Key claims

- **Tool-use forcing is the portable structured-output mechanism.** Both harnesses converge on it — they reuse the model's already-trained tool-calling reliability rather than depending on provider-specific JSON-mode flags.
- **Claude Code's `SyntheticOutputTool` design details:**
  - `SYNTHETIC_OUTPUT_TOOL_NAME = 'StructuredOutput'`
  - Ajv compiled once and identity-cached per schema object reference; 80-call workflows go from ~110ms to ~4ms total Ajv overhead
  - `MAX_STRUCTURED_OUTPUT_RETRIES` defaults to 5, env-overridable
  - `error_max_structured_output_retries` is a typed result subtype distinct from "max turns" or "budget exceeded"
  - Hook (`registerStructuredOutputEnforcement`) prevents stop without calling the synthetic tool
  - `SYNTHETIC_OUTPUT_TOOL_NAME` is filtered from agent subtools — child agents don't inherit the parent's output contract
- **Hermes's structured-output design details:**
  - `ModelCapabilities.structured_output` flag gates which mechanism is available per model
  - Validation feedback as conversation messages (richer self-correction context vs Claude Code's tool-call exception)
  - `batch_runner.py` runs structured extraction across thousands of inputs in parallel via `multiprocessing.Pool`; `_normalize_tool_stats()` enforces fixed schema across JSONL batch entries — *infrastructure-level* structured output, not just model-level

## Why this matters for cere-bro

Continuation of the most detailed public production-harness reference series available. Three things this chapter clarifies that prior chapters did not:

1. **Structured output is a routing decision, too.** Hermes's `ModelCapabilities.structured_output` flag is a per-model feature; routing to a model that lacks it requires a different mechanism. This is a sub-axis of Ch 14 routing.
2. **The retry budget is composed.** Structured-output retries are excluded from the regular tool-call budget in Claude Code. The agent's tool budget × structured-output retry budget × Hermes's per-turn fallback chain × Step-level Optimization escalation budget all interact. No paper has written down the joint budget composition.
3. **Trajectory format as structured output is the unstated infrastructure thesis.** Hermes's JSONL trajectory is itself a structured-output contract. This is what makes downstream RL post-training, replay, and evaluation tractable. *Trajectory-as-structured-output is the precondition for trajectory-aware routing,* which Step-level Optimization (05-02) formalizes one level up.

## Connections to prior wiki pages

- **Ken Huang Ch 14 — Routing (05-01)** — direct continuation. Ch 14 formalized provider/tier routing; Ch 15 formalizes the output-shape constraint orthogonal to routing.
- **Ken Huang Ch 13 — MCP (05-01)** — MCP servers expose tools whose input schemas are themselves structured-output contracts. Ch 15's mechanism applies one level up: forcing the *agent's reply* to follow a schema.
- **Step-level Optimization (05-02)** — the Stuck/Milestone monitors read trajectory format. JSONL trajectory schema enables monitor training.
- **Synthetic Computers at Scale (05-01)** — synthetic-environment training depends on structured trajectory schemas; Ch 15's batch runner is the engineering analog for parallel data generation at scale.

## Research angles

- **Schema-aware routing.** A router that knows model A supports `response_format` natively but model B requires tool-use forcing has more options at the dispatch layer. Hermes's flag exists; nobody has built the router that consumes it.
- **Trajectory-format standardization.** ShareGPT-format JSONL is the de facto standard, but no formal schema with tool-call provenance, KV-cache markers, or retry-budget annotations exists. The first standardized trajectory schema would unlock cross-harness replay and benchmarking.
- **Joint-budget composition.** Tool-budget × output-retry-budget × fallback-chain-depth × step-level-escalation-budget. These are independent today; an agent that exhausts one but has slack in another should rebalance. Operations research problem nobody has formalized.
