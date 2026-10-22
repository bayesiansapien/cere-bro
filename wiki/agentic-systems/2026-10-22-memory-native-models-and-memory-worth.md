# Memory has a price: MemT-1.0, TokenWorth, Anti-Persistence, and self-evolving agents as continual learners

**Sources:** HuggingFace daily papers 2026-10-20/21: [MemT-1.0: Towards Memory-Native Evolution, 2610.26825](https://arxiv.org/abs/2610.26825); [Remembering Has a Price (TokenWorth), 2610.26453](https://arxiv.org/abs/2610.26453); [More Memory, Worse Agents (Anti-Persistence), 2610.27406](https://arxiv.org/abs/2610.27406). Via X feed: [Are Self-Evolving Agents Continual Learners?, 2610.25858](https://arxiv.org/abs/2610.25858) (Google DeepMind / Mila). Raw: `raw/huggingface/2026-10-2[01]-*` matching slugs.

## TL;DR

- **MemT-1.0** builds memory into the model instead of the context: Gated DeltaNet-2 layers update a token-level memory state within each turn, and **Mixture-of-Storage** scales capacity. Two models: Nano (36B-A3B on a Qwen3.6-35B-A3B base, 10M dynamic memory) and Flash (288B-A17B on a DeepSeek-V4-Flash base, 336M dynamic memory), trained on 34B tokens. At a 128K-token history, Nano gives **~1.86x end-to-end speedup and 66x less persistent storage than a full-context KV cache**, beats parametric-memory baselines and stays competitive with RAG.
- **TokenWorth**: under tight generation, interaction and memory budgets, sophisticated lifelong-memory methods do no better than simple retrieval or no memory at all. Retrieving a relevant-but-useless memory burns scarce context. TokenWorth learns a query-dependent "memory worth" from sparse execution feedback and uses it for both retrieval and bounded memory management. Highest success with the fewest output tokens on three LifelongAgentBench environments.
- **More Memory, Worse Agents**: storing abstractions (rules, summaries, skills) lets errors reproduce: a faulty rule shapes new trajectories, which are re-abstracted into the same faulty rule. **Anti-Persistence** stores only trajectories and outcomes and rebuilds task guidance on demand, then discards it. Higher held-out success.
- **Continual learners?** ReasoningBank, GEPA and Meta-Harness on four drifting task streams: more plasticity always costs stability. Self-modifying methods make global edits to a shared prompt that interfere with unseen tasks; similarity-based memory localizes updates but suffers retrieval collisions when similar queries need conflicting workflows.

## How this relates to prior wiki pages

- **MemT extends the 10-19 Memorilla line on [kv-cache](../inference-efficiency/kv-cache.md)** (16 query-specific memory tokens replace a long cache). Memorilla compresses into soft tokens at the input; MemT compresses into a recurrent state inside the model. Both trade exact recall for size, and neither reports exact-recall tests in the abstract.
- **Confirms the 10-16 "Scaling Discovery Requires Forgetting" result on [self-evolving-agents](self-evolving-agents.md)** (wiping research-agent history beat keeping it). Anti-Persistence and the continual-learner audit are now three papers saying accumulated agent memory degrades by default. Pattern threshold reached (n=3).
- **TokenWorth is the memory-side twin of today's decision-model audit** ([decision models](../ai-routing/2026-10-22-decision-models-good-judgment-bad-advice.md)): relevance (or offline ranking skill) is not usefulness. Both need feedback-learned value, not similarity.
- See [agent-memory](agent-memory.md).

## Gaps

- MemT: abstract does not report needle-style exact recall at 128K; 1.86x speedup is end-to-end for Nano only.
- TokenWorth and Anti-Persistence: benchmarks are mid-sized; no production agent traces.
