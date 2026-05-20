# PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.19932](https://arxiv.org/abs/2605.19932) · [raw](../../raw/huggingface/2026-05-20-peek-context-map-as-an-orientation-cache-for-long-context-ll.md)

## TL;DR

LLM agents increasingly operate over long, recurring external contexts: document corpora, code repositories, knowledge bases. Across many invocations on the same context, existing systems preserve one of three things: the agent's trajectory, passive access to the raw material, or task-level strategies. None of them preserves what is actually most needed for repeated same-context workloads: reusable orientation knowledge about the recurring context itself. PEEK caches and maintains this orientation as a context map, a small constant-sized artifact carried in the agent's prompt that gives it a persistent peek into the external context. The map is maintained by a programmable cache policy with three modules: a Distiller that extracts transferable knowledge from inference-time signals, a Cartographer that translates the extracted knowledge into structured edits, and a priority-based Evictor that enforces a fixed token budget. On long-context reasoning and information aggregation, PEEK beats strong baselines by 6.3-34.0% while using 93-145 fewer iterations and incurring 1.7-5.8x lower cost than the state-of-the-art prompt-learning framework ACE. On context learning, solving rate and rubric accuracy improve by 6.0-14.0% and 7.8-12.1% at 1.4x lower cost than ACE. The gains generalize across LMs and agent architectures including OpenAI Codex.

## Why it matters

This is the first paper in the wiki to operationalize an agent-level orientation cache that is structurally separate from both KV cache and trajectory memory. The KV cache stores attention computations. Trajectory memory stores the agent's own past actions. The context map stores what the agent has learned about the external context (its contents, schema, useful entities, organization). Three distinct memory tiers for three distinct lifecycles. The Distiller/Cartographer/Evictor split is a clean separation of concerns that mirrors classical OS cache controller design.

## Mechanism

Three programmable modules under a fixed token budget. (1) **Distiller**: reads inference-time signals (tool returns, retrieval hits, model attention to certain spans) and decides what is transferable knowledge versus task-specific noise. (2) **Cartographer**: converts the distilled knowledge into structured edits to the map (entities, schema fields, organizational notes, useful constants). (3) **Evictor**: when the budget is full, removes lowest-priority entries to make room. The map sits in the agent's prompt as a constant-sized prefix.

## Open questions and gaps

The 6.3-34.0% range is wide. Where in the range a given workload lands (and why) is the deployment-relevant question and is not separated in the paper. The Distiller's signal selection is the load-bearing module; its behavior under adversarial or low-signal contexts is untested. Composition with KV-cache compression (Make Each Token Count, Forcing-KV) is unexplored, but the map is conceptually orthogonal to those cache-level interventions.

## Industrial implication

Agents on production codebases (Codex, Claude Code, Cursor, Devin) are the natural deployment target. The same repository gets hit thousands of times by the same agent type. A constant-sized orientation prefix that improves by 6-34% while cutting cost by 1.7-5.8x is large enough to move the production frontier. Expect this to ship inside a coding-agent platform within 60 days.

## Connections

- **Make Each Token Count (2026-05-12)** changed the KV cache from a fixed retention store to a learned eviction policy. PEEK does the analogous thing at the orientation layer.
- **CompactAttention (2026-05-19)** built the minimal block table for chunked prefill. PEEK builds the minimal orientation prefix for recurring contexts. Both are mask-as-selection-signal moves applied at different layers.
- **Context Memorization (today, 2605.18226)** externalizes the prefix as a lookup-based attention-state memory at the token-position layer. PEEK externalizes orientation as semantic edits to a structured map. Different abstractions, complementary roles.
