# Multi-Agent Computer Use (MACU)

**Source:** HuggingFace Daily Papers · [arXiv 2606.01533](https://arxiv.org/abs/2606.01533)
**Raw:** [raw/huggingface/2026-06-02-multi-agent-computer-use.md](../../raw/huggingface/2026-06-02-multi-agent-computer-use.md)
**Date:** 2026-06-02

## TL;DR

Computer-use agents (CUAs, agents that drive a desktop or browser by clicking and typing) are deployed today as single serial agents, which is bad for long-horizon tasks that want decomposition, parallelism, and re-planning. MACU proposes a manager model that decomposes a task into a directed acyclic graph (DAG) of nodes with dependencies, dispatches parallel CUA subagents on the ready frontier, and continuously revises the DAG (adding, canceling, rewriting nodes) as findings arrive. It treats the partially observable environment as first-class: information a downstream agent cannot re-observe is retained and passed forward through the manager and DAG. MACU beats strong single-agent baselines by 3.4–25.5% on OSWorld, Online-Mind2Web, WebTailBench, and Odysseys, and cuts wall-clock ~1.5x on the long-horizon Odysseys benchmark.

## Diagram

```
Single CUA:   one serial agent ─► stuck on long-horizon tasks, slow, no parallelism

MACU:
  Manager ─► decompose task into a DAG (nodes + dependencies + goals)
          ─► dispatch PARALLEL CUA subagents on the ready frontier
          ◄─ subagents return findings (esp. non-re-observable info)
          ─► continuously REVISE DAG (add / cancel / rewrite nodes)
  ─► +3.4–25.5% on OSWorld / Online-Mind2Web / WebTailBench / Odysseys
  ─► ~1.5x faster wall-clock on Odysseys (long-horizon)
```

## Key points

- **DAG-structured planning with live revision.** The manager encodes dependencies as a DAG and rewrites it as new information arrives, rather than committing to a fixed plan.
- **Partial observability handled explicitly.** Information that downstream agents cannot re-observe (a one-time popup, a transient state) is captured and forwarded through the DAG — a concrete answer to a known CUA failure mode.
- **Parallelism buys both accuracy and speed.** 3.4–25.5% accuracy gains plus ~1.5x faster wall-clock on long-horizon web navigation.
- Code and interactive visualizations released at jykoh.com/multi-agent-computer-use.

## Relation to prior wiki knowledge

MACU is one of three agentic papers today and sits in tension with the third. OpenWebRL (2026-06-02, online multi-turn RL trains a single 4B visual web agent to near-proprietary quality) improves the *single* agent through training; MACU improves the *system* through orchestration, leaving each CUA as-is. "When Does Multi-Agent RL Improve LLM Workflows?" (2026-06-02) is the cautionary third voice: multi-agent gains are conditional on workflow, task, and scale, and jointly training roles can fall off a terminal accuracy cliff. Read together, the three say multi-agent structure helps at inference (MACU) but is fragile to train end-to-end (the workflow-scaling paper), while a well-trained single agent (OpenWebRL) is a strong baseline that orchestration must beat. See [multi-agent-systems.md](multi-agent-systems.md) and [gui-agents.md](gui-agents.md).

Related: [multi-agent-systems.md](multi-agent-systems.md) · [gui-agents.md](gui-agents.md) · [agent-benchmarks.md](agent-benchmarks.md)
