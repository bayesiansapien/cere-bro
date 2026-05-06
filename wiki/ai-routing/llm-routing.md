# LLM Routing

Routing in LLM systems means deciding which model (or no model) should handle a given query — with the goal of minimizing cost while meeting quality requirements.

## Current State (as of 2026-05-04)

Routing is an active research and production concern operating on **three distinct axes** that the May 2026 batch makes explicit:

1. **Query-level routing** — given a query, pick a model. TRACER (04-17) is the canonical surrogate-routing example.
2. **Provider/tier routing inside a harness** — pick provider, model, fallback chain, cheap-vs-primary tier per turn. Ken Huang Ch 14 (05-01) is the most concrete public read.
3. **Step-level (trajectory) routing** — in multi-step agentic systems, pick the model *per step* based on signals from the trajectory itself. Step-level Optimization for Computer-Use Agents (05-02) is the first concrete mechanism.

Stacked, the three axes form a routing surface: which provider × which tier × which model per step. The wiki has now seen at least one concrete paper / harness analysis on each axis.

Three routing paradigms remain operative:
1. **Surrogate routing** — cheap classifier handles easy traffic, fall back to LLM for hard cases (TRACER).
2. **Capability-based routing** — direct queries to different models based on task type or capability match (cheap-model heuristics in Hermes are the production form; learned variants are open).
3. **Agent trajectory routing** — in multi-step agentic systems, optimize the path through a sequence of model calls, not just individual ones (Step-level Optimization).

## Key Papers / Posts

**TRACER (2026-04-17)** — Trains lightweight ML surrogates on an LLM's own production traces (free labeled data). A parity gate activates the surrogate only when it agrees with the teacher above a confidence threshold. Achieves 100% surrogate coverage on a 150-class benchmark using Claude Sonnet 4.6 as teacher. Generates interpretability artifacts for the routing boundary. → [summary](2026-04-17-tracer-llm-routing.md)

**Ken Huang Ch 14 — Routing and Provider Abstraction (2026-05-01)** — Cross-harness comparison of how Claude Code and Hermes implement routing. Claude Code: compile-time provider abstraction, single fallback model, signature-stripping on retry. Hermes: runtime API-mode auto-detection, ordered fallback chain, live OpenRouter context-window discovery (cached 1 h), `switch_model` mid-session, conservative `choose_cheap_model_route`. The most detailed public read of production routing engineering. → [summary](2026-05-01-ken-huang-ch14-routing-provider-abstraction.md)

**Step-level Optimization for Computer-Use Agents (2026-05-02)** — Event-driven cascade for GUI agents: small policy by default, escalate to frontier model when learned monitors detect a Stuck pattern (progress stalled) or a Milestone (semantically significant checkpoint). Trajectory-aware routing inside the agent. Modular, no retraining. The first concrete mechanism for the trajectory-level axis. → [summary](2026-05-02-step-level-optimization-computer-use-agents.md)

**Ken Huang Ch 15 — Structured Output (2026-05-02)** — Cross-harness comparison of schema-constrained generation. Both Claude Code and Hermes converge on tool-use forcing as the portable mechanism. Claude Code: `SyntheticOutputTool` with Ajv compile, schema-identity caching, retries excluded from agent tool budget, child agents have it stripped. Hermes: `extract_structured()` with portable tool-choice forcing, plus JSONL trajectory format as infrastructure-level structured output. Schema support is a per-model capability — a sub-axis of routing the Hermes flag exposes but no router yet consumes. → [summary](../agentic-systems/2026-05-02-ken-huang-ch15-structured-output.md)

**Xiaomi MiMo-V2.5-Pro (2026-05-03)** — Open-weight long-horizon coding model claiming 40-60% fewer tokens per task than Claude Opus 4.6. The pricing axis shifts from "capability ceiling" to "tokens-per-task." Mechanism not disclosed; candidates include MoE sparsity, LenVM-style length value heads, CoPD-style distillation, RL chain-of-thought truncation. *Tokens-per-task is a routing-relevant signal regardless of mechanism — a router can prefer a model that is 50% as expensive at 95% of the quality.* → [summary](../ai-industry/2026-05-03-xiaomi-mimo-25-pro-open-weight-coding.md)

## Key Concepts

- **Surrogate model**: a cheap ML classifier trained to approximate a more expensive LLM's decisions on a specific task
- **Parity gate**: a confidence threshold that controls when the surrogate is trusted vs. when to fall back to the LLM
- **Coverage**: fraction of traffic the surrogate handles vs. falls back to the LLM
- **Production traces**: labeled input-output logs from a deployed LLM — free training data for a surrogate
- **Routing boundary**: the region of input space where the surrogate is reliable; interpretability artifacts describe this
- **Fallback chain**: ordered list of (provider, model) tuples consumed in sequence on failure (Hermes); contrast with single-fallback (Claude Code)
- **API-mode auto-detection**: inferring the API contract (`anthropic_messages` / `chat_completions` / `codex_responses`) from URL and provider name rather than explicit configuration
- **Signature stripping**: removing model-specific extended-thinking blocks before retrying with a different model — required for cross-provider fallback to work
- **Stuck Monitor / Milestone Monitor**: learned signals on agent execution traces; fire when escalation to a stronger model is warranted
- **Cheap-model routing**: per-turn demotion to a cheap model when the user message is short, single-line, free of code blocks/URLs, free of complexity keywords; conservative by design

## Open Problems

- Routing for open-ended tasks (no ground-truth labels to train surrogates)
- Multimodal routing: routing queries across text, image, and video models — Nemotron 3 Nano Omni (05-02) multimodal token reduction is one upstream primitive
- Agent trajectory routing: optimizing multi-step tool-use sequences, not just individual calls — Step-level Optimization is the first concrete attempt; Claw-Eval-Live (05-01) provides the calibration data
- Dynamic routing that adapts as model capabilities and costs change
- **Cache-aware routing.** Switching models invalidates prompt cache; SemiAnalysis (05-01) showed cache hits drive blended Opus pricing to $0.99/MTok. A router that knows current cache state and routes within-cache aggressively is the obvious efficiency move; nobody has published it.
- **Reasoning-mode routing.** Compliance vs Sensibility (05-02) shows reasoning mode is a steerable linear direction. A router that picks both *model* and *forced reasoning mode* is the deeper control surface.
- **MCP server selection as routing.** Ken Huang Ch 13 (05-01) made clear that MCP server selection is an explicit routing problem; today the agent picks "whichever first."
- **Schema-aware routing.** Hermes's `ModelCapabilities.structured_output` flag (Ch 15, 05-02) is a per-model feature today; routing to a model that lacks native JSON-mode requires falling back to tool-use forcing. The router that consumes this flag does not exist.
- **Tokens-per-task pricing as routing signal.** Xiaomi MiMo-V2.5-Pro (05-03) reframes the cost axis: a router that knows which model is cheap on this query, rather than which model is cheap in general, is more valuable in long-horizon agents. Concept now has external open-weight competitive pressure.
- **Safety-as-routing-constraint.** Defense Trilemma (05-02) implies the wrapper around any single model cannot be both utility-preserving and complete. Routing across models with *uncorrelated* failure modes is a defense-in-depth mechanism the trilemma cannot constrain. Nobody has formalized this as a routing objective.

## Cross-axis composition (to track)

- **Step-level × Provider/tier**: stack the 05-02 step-level cascade with Ch 14 provider routing → two-axis routing surface inside one agent.
- **Step-level × Surrogate**: train a TRACER-style surrogate on the cheap-tier model in the cascade; 05-02 cascade only needs the small model for routine steps.
- **Trajectory routing × Claw-Eval-Live**: 05-01 noted that no single frontier model crosses 70% on Claw-Eval-Live; trajectory-aware routing is the cleanest open lever to cross it. Step-level Optimization is the first candidate mechanism.
- **Tokens-per-task × Trajectory routing**: Xiaomi MiMo-V2.5-Pro (05-03) optimizes the per-step cost; Step-level Optimization (05-02) optimizes per-trajectory routing. Composing them — a cheaper model in routine steps + Stuck/Milestone escalation — is the multiplicative efficiency play that no paper has measured.
- **Schema-aware × Provider routing**: a router that picks among providers where some support native JSON mode and others require tool-use forcing should bias toward the cheaper mechanism when both succeed. Hermes's flag is the substrate; no consumer exists.

## Related Pages

- [Inference Efficiency](../inference-efficiency/knowledge-distillation.md)
- [KV Cache](../inference-efficiency/kv-cache.md)
