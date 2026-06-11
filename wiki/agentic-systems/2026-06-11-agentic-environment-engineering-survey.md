# Agentic Environment Engineering for LLMs: A Survey

**TL;DR.** A survey that organizes the fast-growing literature on *agentic environments* — the interactive systems LLM agents act in — around an engineering lifecycle: modeling, synthesis, evaluation, and application. It characterizes environments by eight attributes and eight domains, splits automated environment synthesis into symbolic vs neural paradigms, and frames agent-environment co-evolution along four axes (memory-centric, orchestration-centric, trajectory-centric offline, exploration-centric online) plus three environment-evolution paradigms (neural-driven, difficulty-driven, scaling-driven). It closes with future directions including Environment-as-a-Service, multi-agent environments, and neural-symbolic environments.

**Source:** HuggingFace Daily Papers · arxiv [2606.12191](https://arxiv.org/abs/2606.12191)

## Why it matters for the wiki

This survey is the map for the 06-11 substrate cluster. On the same day, [RACES](../llms-foundation-models/2026-06-11-races-composable-verifiable-environments.md) is a concrete *scaling-driven* environment-evolution method (compose verified bricks), [EvoTrainer](../llms-foundation-models/2026-06-11-races-composable-verifiable-environments.md) is *orchestration/trajectory-centric* co-evolution, [Arbor](2026-06-11-arbor-hypothesis-tree-refinement.md) is *memory-centric* (the hypothesis tree), and [DeNovoSWE](2026-06-11-denovoswe-whole-repo-generation.md) is a synthesized long-horizon environment dataset. The survey's "Environment-as-a-Service" direction is the natural endpoint of the wiki's [self-evolving agents](self-evolving-agents.md) thread: if harness and environment both become first-class, scalable objects, the agent's substrate becomes a product surface, not a research artifact.

Useful as the citation anchor when future digests need a single reference for "the agentic-environment lifecycle."

→ Raw: [`raw/huggingface/2026-06-11-agentic-environment-engineering-for-large-language-models-a.md`](../../raw/huggingface/2026-06-11-agentic-environment-engineering-for-large-language-models-a.md)
