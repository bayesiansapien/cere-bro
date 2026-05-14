# LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues

**Date:** 2026-05-13
**Source:** [arXiv 2605.12493](https://arxiv.org/abs/2605.12493) · HuggingFace Daily Papers
**Tier:** 2. Agent memory, environment-specific experience benchmarks
**Raw:** [`raw/huggingface/2026-05-13-longmemeval-v2-evaluating-long-term-agent-memory-toward-expe.md`](../../raw/huggingface/2026-05-13-longmemeval-v2-evaluating-long-term-agent-memory-toward-expe.md)

## TL;DR

Most agent-memory benchmarks focus on user histories or short traces. LME-V2 evaluates whether memory systems help agents internalize *environment-specific* experience: interface affordances, state dynamics, workflows, recurring failure modes. 451 manually curated questions covering five memory abilities (static state recall, dynamic state tracking, workflow knowledge, environment gotchas, premise awareness), paired with history trajectories up to 500 trajectories and 115M tokens. Two methods proposed: AgentRunbook-R (RAG-based with knowledge pools for states, events, strategy notes) and AgentRunbook-C (stores trajectories as files, invokes a coding agent in a sandbox to gather evidence). AgentRunbook-C reaches 72.5% average accuracy; best RAG baseline 48.5%; off-the-shelf coding agent 69.3%. Coding-agent memory is the new Pareto front for accuracy, but at high latency cost.

## Why it matters

Two structural moves. First, the benchmark shifts the agent-memory frame from "remember the user" to "become an experienced colleague in this environment." The latter is the harder problem and the one that matters for production agentic deployments. Second, the AgentRunbook-C result argues that *coding-agent retrieval* (store trajectories as files, write code to query them in a sandbox) is materially stronger than vector RAG. This composes directly with the same day's Useful Memories paper: raw episodic storage plus coding-agent retrieval beats LLM-rewritten consolidation.

## Mechanism

AgentRunbook-R: standard RAG, but with separate knowledge pools for raw state observations, events, and strategy notes. Each pool gets retrieved separately for the downstream question.

AgentRunbook-C: store each trajectory as a file. At query time, invoke a coding agent in a sandbox to read, filter, aggregate across files. The coding agent has python and shell. The advantage: arbitrary procedural retrieval (e.g., "find all sessions where the agent reached state X then failed at step Y") which a vector index cannot express. The disadvantage: latency, because every query spawns a sandboxed coding-agent loop.

72.5% vs 48.5% is the headline. The off-the-shelf coding-agent baseline at 69.3% is the second informative number, the AgentRunbook-C structural choices (file-per-trajectory, dedicated retrieval prompt) add ~3 points on top of just letting a generic coding agent loose.

## Relation to prior wiki

- **Useful Memories Become Faulty (today, same day)** — companion paper. Useful Memories argues that LLM-rewritten consolidation hurts. LME-V2 demonstrates that file-system-plus-coding-agent retrieval works without consolidation. Together they establish the design: episodic storage, no rewrite, sandboxed-coding-agent retrieval.
- **EviMem (today HF)** — evidence-gap-driven iterative retrieval for long-term memory. Same family as AgentRunbook-C but with a different control loop (gap-driven iterative rather than coding-agent procedural). Three papers in one day arguing that procedural retrieval beats vector RAG for long-horizon agent memory.
- **AI Co-Mathematician (2026-05-09)** — interactive research workbench with persistent state. AgentRunbook-C's design pattern (file-per-experience, coding agent for retrieval) is the production-grade version of the AI Co-Mathematician's research workspace.
- **MemoryAgentBench** — referenced as part of the family this benchmark is extending. LME-V2 is the more specialized: environment-specific experience rather than general memory.

## Research angle

Three open questions. (1) AgentRunbook-C's latency cost is a serious deployment blocker; the paper does not break down per-query cost. The Pareto frontier between RAG-style cheap retrieval and coding-agent-style accurate retrieval is the natural next experiment. (2) The benchmark is built around web environments. Whether AgentRunbook-C transfers to non-web environments (CLI, scientific workflows) is open. (3) Composition with the Useful Memories paper's gated-consolidation framework: when consolidation does fire (rarely), should it consolidate within AgentRunbook-C's file system, or should it produce a separate index?

## Why Tier 2

Production-relevant benchmark plus a deployable architectural pattern. AgentRunbook-C as a retrieval design will likely become a reference point for the next quarter of agent-memory work.
