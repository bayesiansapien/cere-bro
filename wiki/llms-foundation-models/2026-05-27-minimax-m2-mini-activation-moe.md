# MiniMax-M2: Mini Activations, Agent-Native MoE

**Source:** HuggingFace daily papers (2026-05-27, 15 upvotes) · arxiv 2605.26494
**arxiv:** [2605.26494](https://arxiv.org/abs/2605.26494)
**Date:** 2026-05-27
**Raw:** [raw/huggingface/2026-05-27-the-minimax-m2-series-mini-activations-unleashing-max-real-w.md](../../raw/huggingface/2026-05-27-the-minimax-m2-series-mini-activations-unleashing-max-real-w.md)
**Tier:** 2 (MoE foundation model + agentic systems)

## TL;DR

MiniMax-M2 is a Mixture-of-Experts model family built on the bet that a *small active footprint* can still deliver frontier real-world intelligence. The flagship has 229.9B total parameters but activates only 9.8B per token (a ~23:1 sparsity ratio). It is designed end-to-end for agentic deployment and rests on three pillars: (i) agent-driven data pipelines that produce large-scale verifiable trajectories for agentic coding and "cowork," each grounded in an executable workspace with an artifact-aligned reward; (ii) Forge, an agent-native RL system for long-horizon trajectories with windowed-FIFO scheduling, prefix-tree merging, inference optimization, and a clean training-inference-agent decoupling that supports white-box and black-box agents; (iii) the M2.7 checkpoint takes an early step toward self-evolution, autonomously debugging its own training runs and modifying its own scaffold.

```
MiniMax-M2 stack:

  agent-driven data ──► verifiable trajectories (coding + cowork)
       │                grounded in executable workspace + artifact reward
       ▼
  Forge (agent-native RL) ──► long-horizon trajectories
       │  windowed-FIFO sched · prefix-tree merge · train/infer/agent decoupled
       ▼
  229.9B total / 9.8B active MoE  ──► M2 … M2.7
       │                              M2.7: self-evolution
       ▼                              (debugs own training, edits own scaffold)
  frontier-tier on agentic coding, deep search, office tasks, reasoning
```

## Key points

- **Extreme sparsity for an agent model.** 229.9B total / 9.8B active is a deliberate "mini activation" design: cheap per-token inference (decode cost scales with active params) while keeping a large knowledge store in the inactive experts. The right serving profile for long agentic trajectories that generate many tokens.
- **Artifact-aligned, verifiable rewards.** The data pipeline grounds every trajectory in an executable workspace so the reward is checkable, the same verifiable-reward discipline QUEST (05-26) used for open deep-research agents.
- **Forge is the agent-native RL substrate.** Windowed-FIFO scheduling and prefix-tree merging are infrastructure choices for long-horizon agent rollouts, and the white-box/black-box decoupling lets it train against agents it does not fully control.
- **Self-evolution at M2.7.** Autonomously debugging training runs and editing its own scaffold is the same self-improvement signal as Self-play SWE-RL (Twitter, 05-27) and SEAL (05-26), here folded into a shipped frontier model.

## Relation to prior wiki state

MiniMax-M2 sits at the intersection of two wiki threads. On the architecture side it is another extreme-sparsity MoE in the lineage the [MoE-muP page](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md) catalogs (Kimi K2.6, DeepSeek V4, GLM-5.1, Qwen3.6-35B-A3B): 9.8B active out of 229.9B is one of the most aggressive published active-to-total ratios, and pairs with today's MobileMoE result that sparsity is the lever for matching cost to a deployment constraint (phone there, long agent trajectory here). On the agentic side, Forge plus the self-evolution checkpoint is the productized version of the "substrate around the agent" story: [Scaling the Harness (05-27)](../agentic-systems/2026-05-27-scaling-the-harness.md) argues the orchestration layer is the real design surface; MiniMax built one (Forge) and shipped a model trained inside it. The self-scaffold-editing in M2.7 is the same self-play-on-real-software direction as Self-play SWE-RL and SEAL's co-evolution.

## Why it matters

A 229.9B/9.8B open MoE tuned end-to-end for agentic coding and office tasks is a direct competitive signal against closed coding agents (Claude Code, Codex), and reinforces Nathan Lambert's Gmail thesis (05-27) that Chinese labs are specializing on open MoEs for agentic/enterprise use. The mini-activation design is the economically correct shape for agent workloads, where per-token decode cost dominates the bill (see today's How Do Agents Spend Your Money: 154:1 input:output).

## Gaps

The abstract reports frontier-tier performance without the head-to-head numbers; the self-evolution claim (M2.7 editing its own scaffold) is early-stage and not quantified. Whether the 9.8B active budget holds quality on non-agentic reasoning at the level of denser frontier models is the open question.

## Links

- [Paper](https://arxiv.org/abs/2605.26494)
- Raw: [raw/huggingface/2026-05-27-the-minimax-m2-series-mini-activations-unleashing-max-real-w.md](../../raw/huggingface/2026-05-27-the-minimax-m2-series-mini-activations-unleashing-max-real-w.md)
- Related: [MobileMoE 2026-05-27](../inference-efficiency/2026-05-27-mobilemoe-on-device-moe-scaling.md), [Scaling the Harness 2026-05-27](../agentic-systems/2026-05-27-scaling-the-harness.md), [QUEST 2026-05-26](../agentic-systems/2026-05-26-quest-deep-research-agent-synthetic-tasks.md), [MoE-muP](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md)
