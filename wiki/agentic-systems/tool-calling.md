# Tool Use & Function Calling

Concept page for how agents invoke external tools, APIs, and code from inside an LLM-driven loop.

This page accumulates findings on:

- **Function-call interfaces** — JSON schemas, structured-output constraints, decoder-side enforcement.
- **Tool selection** — when to call which tool, learned vs hand-coded routers.
- **Permission and capability** — sandboxing, scoped credentials, dry-run modes.
- **Tool-chaining attacks** — adversarial sequences that exploit chained permissions (per the Marcus 2026-05-06 study on production agent vulnerability).
- **Tool ecosystems** — MCP, OpenAPI bindings, plugin frameworks.

Source pages tagged with this concept will accumulate at `wiki/agentic-systems/YYYY-MM-DD-<slug>.md` and link back here.
