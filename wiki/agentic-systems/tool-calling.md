# Tool Use & Function Calling

Concept page for how agents invoke external tools, APIs, and code from inside an LLM-driven loop.

This page accumulates findings on:

- **Function-call interfaces** — JSON schemas, structured-output constraints, decoder-side enforcement.
- **Tool selection** — when to call which tool, learned vs hand-coded routers.
- **Permission and capability** — sandboxing, scoped credentials, dry-run modes.
- **Tool-chaining attacks** — adversarial sequences that exploit chained permissions (per the Marcus 2026-05-06 study on production agent vulnerability).
- **Tool ecosystems** — MCP, OpenAPI bindings, plugin frameworks.

Source pages tagged with this concept will accumulate at `wiki/agentic-systems/YYYY-MM-DD-<slug>.md` and link back here.

## Recent additions

- **2026-05-31 — [CoHyDE: co-training the rewriter and the encoder for tool retrieval](2026-05-31-cohyde-cotrain-rewriter-encoder-tool-retrieval.md).** Tool retrieval over large API catalogs fails on the colloquial-query-vs-technical-catalog gap. A fine-tuned dense encoder is strong on surface-matching queries but collapses on vague ones; frozen-LLM HyDE expansion is robust to vague queries but hurts well-formed ones because the LLM is catalog-unaware. CoHyDE trains both as one co-evolving loop (encoder retrained with InfoNCE on the rewriter's catalog-style hypotheticals; rewriter DPO-aligned against the encoder's retrieval scores, both warm-started on the catalog). Three rounds on a ~10k ToolBench subset beat the strongest single-component baseline by +2.5 pp NDCG@5 on standard and +6.3 pp on held-out vague queries. The retrieval bottleneck decides whether an agent even *sees* the right tool, so this is upstream of all tool-selection routing.
