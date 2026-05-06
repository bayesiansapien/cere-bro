# Eywa: Heterogeneous Scientific Foundation Model Collaboration

**arXiv:** 2604.27351 · [paper](https://arxiv.org/abs/2604.27351) · [HF](https://huggingface.co/papers/2604.27351)
**Tier:** 2 — multi-agent / heterogeneous foundation models
**Raw:** [../../raw/huggingface/2026-05-01-heterogeneous-scientific-foundation-model-collaboration.md](../../raw/huggingface/2026-05-01-heterogeneous-scientific-foundation-model-collaboration.md)

## TL;DR

Agentic LLM systems use language as the universal interface — which limits applicability to scientific domains where domain-specific foundation models (chemistry transformers, protein FMs, materials FMs) operate on non-linguistic data. **Eywa** wraps these specialized models with a language-model reasoning interface so an LLM can guide inference over non-text modalities. Three deployment modes: drop-in single-agent (EywaAgent), multi-agent integration (EywaMAS), and a planner-orchestrated heterogeneous system (EywaOrchestra) that dispatches across traditional and Eywa agents. Improves performance on structured / domain-specific tasks while reducing reliance on pure language reasoning.

## Why this is the right framing

Agentic AI has been mostly a language-tool-call composition. But many high-value scientific tasks need a *predictive* foundation model — AlphaFold-style protein FMs, materials FMs, climate FMs — that takes non-text input. Wrapping them as "agents" via a thin language interface is the natural next step, and Eywa is the first paper to formalize the dispatch logic.

The interesting design choice: **the LLM doesn't have to understand the foundation model's internals — only its API.** This makes Eywa an instance of *language as a universal control plane* over heterogeneous compute. Pair this with MCP (Ken Huang Ch 13, today's RSS) and you have a complete picture: MCP is the protocol, Eywa is the multi-modal extension where some "tools" are themselves heavy foundation models.

## Connection to prior wiki

- **MCP integration (Ken Huang Ch 13, 05-01)** — MCP standardizes the agent → tool interface. Eywa is what happens when one of those "tools" is a 10B-parameter scientific FM with its own input modality. The two papers compose: MCP provides the connection, Eywa provides the language-bridging shim.
- **Heterogeneous Multi-Agent Organisations / "Skills to Talent" (04-28)** — argued for typed skill-to-agent dispatch. Eywa makes the same argument across modality boundaries (LLM ↔ scientific FM) instead of within text-only multi-agent systems.
- **GLM-5V-Turbo (04-30) MMTP** routes visual content through a shared `<|image|>` token. Eywa routes domain-specific content through a language-mediated agent interface. **Two different layers of the same routing thesis** — within-model (GLM-5V) and across-model (Eywa).
- **AI routing concept page** — Eywa is a *cross-model* routing system where the routed entities are foundation models with different input modalities. This is a new branch of the routing taxonomy that the concept page should track.

## Open problems

1. **Reliability of the language interface to specialized FMs.** When the LLM mis-specifies inputs to a protein FM, how does the system recover? The paper mentions planner-based orchestration but doesn't characterize failure modes.
2. **Latency.** Heavy scientific FMs (millions of FLOPs per query) plus an LLM orchestrator means each step has serious cost. Eywa's economics depend on the LLM's call frequency to the FM being low. This intersects with the SemiAnalysis (today) thesis on token economics: only viable if scientific-FM inference is cheap relative to LLM inference.
3. **Composition with KV cache.** When EywaOrchestra calls the same scientific FM repeatedly across an agent trajectory, can it cache embeddings or intermediate representations? The paper does not address this; it is the obvious efficiency optimization.

## Research angle

The genuinely novel contribution is treating *foundation models as agents inside a multi-agent system, routed via a language planner*. This is the inverse of the standard view (LLM is the agent, FM is just a tool). For Tier 1 routing research, Eywa is a meaningful data point: **the routing layer can sit above heterogeneous foundation models, not just over LLM SKUs**. Whoever publishes the first scientific-task benchmark where a small router-LLM beats a frontier monolithic LLM by routing to specialized FMs has the cleanest follow-up.
