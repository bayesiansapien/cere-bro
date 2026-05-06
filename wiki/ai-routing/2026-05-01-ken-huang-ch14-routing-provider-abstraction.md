---
source: raw/rss/2026-05-01-agentic-ai-chapter-14-model-routing-and-provider-abstraction-claud.md
date: 2026-05-01
url: https://kenhuangus.substack.com/p/chapter-14-model-routing-and-provider
---

# Ken Huang Ch 14: Model Routing and Provider Abstraction (Claude Code vs Hermes)

## TL;DR

The most detailed public cross-harness comparison of routing implementation. Claude Code bakes routing into a TypeScript compile-time layer — four providers, static selection logic, single fallback model, `stripSignatureBlocks` for fallback replay. Hermes treats routing as a first-class runtime concern — API format auto-detection, ordered fallback chains, live context-window discovery from OpenRouter, per-turn smart routing to cheaper models. Two coherent threat models, opposite tradeoffs.

## Mechanism comparison

```
Claude Code (compile-time):               Hermes (runtime):
  getMainLoopModel()                        api_mode auto-detected from URL
  getRuntimeMainLoopModel()                 fallback_chain: ordered list
    - plan mode → lighter model               advances on each failure
    - context >200K → larger window        fetch_model_metadata():
  FallbackTriggeredError catch               OpenRouter, 1hr TTL cache
    → stripSignatureBlocks()                  context window per model
    → single fallback model                switch_model():
  Static rules, resolved at startup          in-place, no session restart
                                           choose_cheap_model_route():
                                             per-turn, conservative
                                             160 char / 28 word limits
```

### `stripSignatureBlocks` — the subtle critical detail

Extended thinking produces cryptographically signed blocks that are model-specific. Replaying a conversation with signed blocks to a different model triggers API rejections. Claude Code strips these automatically on fallback before retrying. Most hand-rolled fallback implementations miss this.

### Hermes smart routing — intentionally conservative

```python
def choose_cheap_model_route(user_message, routing_config):
    # Hard limits: long text, multi-line, code, URLs → primary model
    if len(text) > 160: return None
    if text.count("\n") > 1 or "```" in text: return None
    # Keyword check: debug, implement, analyze, docker → primary model
    if words & _COMPLEX_KEYWORDS: return None
    return cfg.get("cheap_model")
```

False negative (simple query → expensive model) costs cents. False positive (complex query → cheap model) costs analyst time. Conservative is correct.

## Key design decisions and their implications

| Dimension | Claude Code | Hermes |
|-----------|-------------|--------|
| Routing time | Compile-time (startup) | Runtime (per turn) |
| Fallback | Single model, uniform | Ordered chain, consumes on failure |
| Context window | Hardcoded (200K trigger) | Live from OpenRouter (1hr cache) |
| Model switch | Not supported mid-session | `switch_model()` in-place |
| API format | 4 explicit providers | Auto-detect from URL |
| Credential safety | TS types + permission gates | Regex strip on every error path |

## Relation to prior wiki knowledge

**Continues Ch 13 (MCP integration, May 1)**: [2026-05-01-mcp-claude-vs-hermes-chapter13.md](../agentic-systems/2026-05-01-mcp-claude-vs-hermes-chapter13.md). The three-chapter pattern is now clear: Claude Code is minimal-by-design with safety delegated to humans (types, permission gates, static files); Hermes is first-class runtime subsystems with safety delegated to scanners (regex strip, fallback chain validation, 80+ pattern security scanner).

**Directly fills a gap in [llm-routing.md](./llm-routing.md)**: Prior routing concept page covers academic query-level routing (RouteLLM, LLM-Blender, cascade classifiers). Ch 14 is the first source covering *production harness-level* routing — how the decision actually gets made in deployed agent loops, including the fallback plumbing and credential handling that academic papers never mention.

**Connects to Step-level optimization** ([2026-05-02-step-level-optimization-computer-use-agents.md](./2026-05-02-step-level-optimization-computer-use-agents.md)): Both papers answer "when to use cheap vs expensive model for an agentic task." Ch 14 (Hermes `choose_cheap_model_route`) makes the decision at the *turn level* based on input complexity. Step-level optimization makes the decision at the *step level* based on trajectory history. Together: a complete two-level routing hierarchy for agentic systems — turn-level routing for provider selection, step-level routing for model escalation within a trajectory.

**MCP server selection gap noted explicitly**: Ch 14 surfaces that when 10 MCP servers expose overlapping capabilities, today the agent picks "whichever first." This is an explicit routing problem — latency-aware, cost-aware, capability-coverage-aware routing over MCP servers is the obvious gap. Ch 13 was about session management; Ch 14 names MCP routing as the next open thread.

## Open questions / Research angle

1. **Cross-server credential flow in Hermes** — per-call stripping is defensive but doesn't prevent earlier tool calls from leaking secrets into the conversation that a later server then reads. Typed credential capabilities scoped to (agent, server, time) tuples would be defense-in-depth.
2. **MCP server routing** — treat MCP server selection as a routing problem. Capability coverage, latency, cost, and freshness are the obvious routing signals.
3. **Fallback chain + KV cache** — when Hermes exhausts one fallback and rebuilds the client, does KV cache persist across the switch? Today: no. The interaction between fallback-chain routing and KV cache state is uncharacterized.
4. **Two-level composition**: turn-level smart routing (Hermes) + step-level cascade (step optimization paper) have never been composed in a single agent. The interaction effects could be nonlinear.

## Links

- Raw: [raw/rss/2026-05-01-agentic-ai-chapter-14-model-routing-and-provider-abstraction-claud.md](../../../raw/rss/2026-05-01-agentic-ai-chapter-14-model-routing-and-provider-abstraction-claud.md)
- Related: [llm-routing.md](./llm-routing.md) · [2026-05-01-mcp-claude-vs-hermes-chapter13.md](../agentic-systems/2026-05-01-mcp-claude-vs-hermes-chapter13.md)
