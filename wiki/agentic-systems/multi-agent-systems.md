# Multi-Agent Systems

Concept page for systems where multiple LLM-driven agents coordinate, communicate, or compete to solve a task.

This page accumulates findings on:

- **Coordination architectures** — orchestrator/worker, peer-to-peer, hierarchical, mixture-of-agents.
- **Communication protocols** — message-passing topologies, prompt-engineered hand-offs, shared scratchpads.
- **Specialization** — heterogeneous agent pools where each model handles a sub-task it's best at.
- **Cross-agent learning** — RL signals shared across agents, curriculum design for joint training.
- **Failure modes** — drift, deadlock, and adversarial dynamics between agents.

Source pages tagged with this concept will accumulate at `wiki/agentic-systems/YYYY-MM-DD-<slug>.md` and link back here.

## Findings

### Orchestration helps at inference; joint training is fragile (2026-06-02)

Three same-day papers triangulate when multi-agent structure actually pays off:

- **MACU** ([2026-06-02](2026-06-02-multi-agent-computer-use.md)) improves the *system* through orchestration without touching the underlying agents: a manager decomposes a task into a directed acyclic graph (DAG), dispatches parallel computer-use subagents on the ready frontier, and continuously revises the DAG as findings arrive. It treats partial observability as first-class, forwarding information a downstream agent cannot re-observe. Beats single-agent baselines by 3.4–25.5% on OSWorld / Online-Mind2Web / WebTailBench / Odysseys and cuts wall-clock ~1.5x on long-horizon tasks.
- **OpenWebRL** (2026-06-02) takes the opposite route: train a *single* 4B visual web agent with online multi-turn RL to near-proprietary quality. A well-trained single agent is the strong baseline that any orchestration must beat.
- **When Does Multi-Agent RL Improve LLM Workflows?** (2026-06-02) is the cautionary voice: multi-agent gains are conditional on workflow, task, and scale, and jointly training agent roles can fall off a terminal-accuracy cliff.

Read together: multi-agent structure is a reliable *inference-time* win (MACU), but *training* a multi-agent system end-to-end is brittle, so the safer pattern today is orchestration over independently strong agents rather than joint optimization.
