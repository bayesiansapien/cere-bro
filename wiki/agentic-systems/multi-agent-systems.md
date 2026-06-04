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

### Streaming reasoning steps cuts latency AND raises accuracy (2026-06-04)

[StreamMA](2026-06-04-streamma-streaming-multi-agent-reasoning.md) (arxiv 2606.05158) changes the communication protocol rather than the agents: instead of generate-then-transfer (where end-to-end latency scales linearly with pipeline depth), it streams each reasoning step downstream as soon as it is generated, pipelining adjacent agents. The counterintuitive result is that pipelining also improves *effectiveness*: reasoning quality is non-uniform, early steps are more reliable than later ones, so working from reliable early steps prevents error-prone late steps from misleading downstream agents. The paper gives the first closed-form joint analysis of stream/serial/single protocols (ordering stream > serial > single, plus a speedup bound and cost ratio) and reports +7.3 pp average (+22.4 on HMMT 2026) across eight benchmarks, two frontier models (Claude Opus 4.6, GPT-5.4), and three topologies. It also surfaces a **step-level scaling law**: more per-agent reasoning steps improve both effectiveness and efficiency, a scaling axis orthogonal to and composable with agent count.

This strengthens the 06-02 verdict below: StreamMA is a pure inference-time win that changes *when* partial results flow (one of this page's named axes, communication protocols), complementing [MACU](2026-06-02-multi-agent-computer-use.md)'s restructuring of *what* gets dispatched. The "early steps more reliable" finding echoes the reasoning-efficiency line ([PUMA](../inference-efficiency/2026-05-19-puma-semantic-preserving-early-exit-reasoning.md) 05-19, late reasoning tokens add little), turned into a communication rule. Open question: on tasks where the answer only crystallizes late, forwarding early steps could propagate a wrong frame, and that failure boundary is unmapped. The step-level scaling law is a routing lever (trade steps-per-agent against agent-count under a latency budget) the [llm-routing](../ai-routing/llm-routing.md) thread should pick up.

### Orchestration helps at inference; joint training is fragile (2026-06-02)

Three same-day papers triangulate when multi-agent structure actually pays off:

- **MACU** ([2026-06-02](2026-06-02-multi-agent-computer-use.md)) improves the *system* through orchestration without touching the underlying agents: a manager decomposes a task into a directed acyclic graph (DAG), dispatches parallel computer-use subagents on the ready frontier, and continuously revises the DAG as findings arrive. It treats partial observability as first-class, forwarding information a downstream agent cannot re-observe. Beats single-agent baselines by 3.4–25.5% on OSWorld / Online-Mind2Web / WebTailBench / Odysseys and cuts wall-clock ~1.5x on long-horizon tasks.
- **OpenWebRL** (2026-06-02) takes the opposite route: train a *single* 4B visual web agent with online multi-turn RL to near-proprietary quality. A well-trained single agent is the strong baseline that any orchestration must beat.
- **When Does Multi-Agent RL Improve LLM Workflows?** (2026-06-02) is the cautionary voice: multi-agent gains are conditional on workflow, task, and scale, and jointly training agent roles can fall off a terminal-accuracy cliff.

Read together: multi-agent structure is a reliable *inference-time* win (MACU), but *training* a multi-agent system end-to-end is brittle, so the safer pattern today is orchestration over independently strong agents rather than joint optimization.

## Communication and reliability (2026-06-04)

- **Streaming beats generate-then-transfer (StreamMA, [06-04](2026-06-04-streamma-streaming-multi-agent.md))**: the standard "each agent finishes its chain, then hands off" pattern makes latency scale linearly with depth. [StreamMA](2026-06-04-streamma-streaming-multi-agent.md) streams each reasoning step downstream as it is produced, pipelining adjacent agents. Counterintuitively it also *improves accuracy*: early reasoning steps are more reliable than late ones, so downstream agents working off reliable early steps avoid being misled by error-prone late steps. It introduces a **step-level scaling law** (more steps-per-agent improves both effectiveness and efficiency), a new axis orthogonal to and composable with agent-count and topology scaling. +7.3pp avg / +22.4pp max across 8 benchmarks on Claude Opus 4.6 and GPT-5.4.
- **Span-level error localization (DRIFT/TELBench, [06-04](2026-06-04-drift-telbench-span-error-localization.md))**: final-answer evaluation cannot tell you *which* part of a long deep-research trajectory corrupted the answer. [DRIFT](2026-06-04-drift-telbench-span-error-localization.md) is a claim-centric auditor that tracks agent claims, checks each against trajectory evidence, and flags unsupported/conflicting spans on the answer path (+30pp first-error accuracy). TELBench (1,000 instances from 2,790 real trajectories) is the benchmark. Process-level reliability, the agent-trajectory analogue of CoT span-level analysis.
