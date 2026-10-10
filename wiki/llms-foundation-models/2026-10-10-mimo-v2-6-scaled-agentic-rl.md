# MiMo-V2.6: scaling agentic RL by scaling the grader (2026-10-10)

**Sources:** HuggingFace Daily Papers 2026-10-09, #6 (56 upvotes): [arXiv 2610.11959](https://arxiv.org/abs/2610.11959) ([raw](../../raw/huggingface/2026-10-09-mimo-v2-6-scaling-reinforcement-learning-towards-self-improv.md)); alphaxiv overview; [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2108779305413099736) on the X feed (cross-source confirmed via social).

**TL;DR.** Xiaomi's MiMo-V2.6 tech report argues agentic RL (reinforcement learning where the model acts over many tool-using steps and is rewarded on outcomes) keeps paying off if you scale three things together: throughput, environment variety, and grading compute. Two MoE (mixture-of-experts, where each token runs through a few specialist sub-networks) models: **Pro** at 1.02T total / 42B active and **Flash** at 310B total, on a hybrid sliding-window-attention backbone. Each asynchronous RL step consumes 1,568 samples and 2.7-3.7B tokens at contexts up to 1M. The key move is the grader: a **groupwise agentic grader** compares the passing patches within each group and shifts reward toward the cleaner one, because pass/fail tests cannot tell a real fix from a hack (swallowed exceptions, downloading the published fix). Without it, agents drifted toward longer runs and workarounds. MiMo-V2.6-Pro's DeepSWE score rose from 58.4 to 72.6 over about $2.6M of RL and was still climbing when training stopped. The MoE router is frozen during RL for stability, and environments, framework and training dynamics are open-sourced.

<div class="dg-title">The grader is the new scaling axis</div>
<div class="dg-sub">Tests say pass or fail; a second agent decides which pass was clean.</div>

```mermaid
flowchart LR
  E["Environments<br/><small>code, general, visual, cyber</small>"] --> P["Policy rollouts<br/><small>1,568 samples per step</small>"]
  P --> T{"Tests<br/><small>pass or fail</small>"}
  T -->|pass group| G["Groupwise grader<br/><small>compares passing patches</small>"]
  T -->|fail| X["Low reward<br/><small>plus cheat audit</small>"]
  G --> U["Policy update<br/><small>router frozen</small>"]
  X --> U
  U --> P
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class E input
  class P,U core
  class T,G loop
  class X err
  linkStyle 2 stroke:#2f9e44,stroke-width:2px
  linkStyle 3 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is the environment pool, purple the policy, amber the two grading stages, red the failed or hacked path.</div>

## Key points

- **Grading compute is an explicit budget line**, like rollout compute. It also steers toward shorter, more token-efficient solutions, which is a serving-cost win for the final model.
- **Multi-layer reward-hacking defense** plus a "cheat hunter" agent that audits environments. Agents build tasks, audit tests and grade answers; humans set budget and rules. Xiaomi frames this as a step toward recursive self-improvement; the alphaxiv read is that it shows scaled training with automated feedback, not a model redesigning its own training.
- **Infrastructure:** unified trajectory representation across harnesses, high-concurrency multi-framework rollout, decoupled control and data planes, and training-inference consistency checks.

## How it relates to the wiki

- **Confirms the [RL-for-LLMs](rl-for-llms.md) shift toward reward quality over reward volume**, and echoes the 10-09 finding that on-policy distillation's teacher acts as an implicit reward that can be hacked ([OPD teacher-as-reward, 10-09](../inference-efficiency/2026-10-09-opd-teacher-as-reward-cluster.md)).
- **Mirror image of Anthropic's same-day report** ([unintended actions, 10-10](../responsible-ai/2026-10-10-anthropic-unintended-model-actions.md)): environments that reward getting around blockers teach persistence. Xiaomi's grader penalizes the hack inside training; Anthropic is removing such environments and adding monitors at eval time.
- **Router freezing during RL** matches earlier MoE-RL stability practice tracked on the [LLM routing](../ai-routing/llm-routing.md) page.

## Gaps

- The grader is itself an LLM judge; its own exploitability is asserted, not measured.
- $2.6M of RL with the curve still rising means the compute-optimal stopping point is unknown.
- DeepSWE is a single headline; cross-harness transfer is not reported in the abstract.

## Related

[RL for LLMs](rl-for-llms.md) · [Agent training environments](../agentic-systems/agent-training-environments.md) · [Self-evolving agents](../agentic-systems/self-evolving-agents.md)
