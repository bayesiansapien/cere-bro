# Mid-Harness, MILO and Meta-Reasoning: Spend Agent Compute on Judgment

**Source:** HuggingFace Daily Papers (2026-10-01) + X Following feed
**Papers:** [Mid-Harness (NVIDIA)](https://arxiv.org/abs/2609.39982) · [MILO](https://arxiv.org/abs/2609.38349) · [Meta-Skills for Harness Design](https://arxiv.org/abs/2609.38143) · [Thinking Before Thinking (Meta)](https://arxiv.org/abs/2609.38147) · [AgentWorld](https://arxiv.org/abs/2609.31590) · [False Frontiers](https://arxiv.org/abs/2609.39102) · [Agent Error Dataset](https://arxiv.org/abs/2609.40111)
**Raw:** `raw/huggingface/2026-10-01-mid-harness-*.md`, `-milo-*.md`, `-learning-meta-skills-*.md`, `-false-frontiers-*.md`, `-agent-error-dataset-*.md`; X feed captures 2026-10-01/02

## TL;DR

**Mid-Harness** places test-time compute at the boundary between model and harness (the loop that runs the model, executes its commands and feeds back results). It samples several candidate shell commands, verifies them, and forwards one, leaving the generator and harness unchanged. With a small TMAX-9B generator, extra samples barely help under a weak verifier. With a GPT-5.6 Sol verifier, Pass@1 on TerminalBench-Lite rises **from 50.0% to 68.0% at 8 samples**. Distilling the strong verifier into the 9B model recovers part of the gain, and mixing action-level and trajectory-level scaling beats running more full trajectories at **lower token cost**.

**MILO** evolves whole harnesses with island-based search, per-island mutator agents and an orchestrator that adapts the search itself. On Terminal-Bench 2.1 with Opus 4.8 it reaches 86.1%, above the leaderboard's top entry (83.8%), while using **26% fewer tokens** than its starting harness. **Meta-Skills** has a builder model learn reusable principles for constructing a frozen target model's environment (+8.95 points over no skills). Meta's **Thinking Before Thinking** adds a controller that decides which partial work each worker sees; tripling the budget lifts it from 64.1% to 71.5% on ProgramBench while the unmanaged agent stalls.

Two cautions. **AgentWorld** finds fewer than a third of a multi-agent team's actions actually contribute to the outcome; the best model reaches 52% task success and coordination tasks only 12%. **False Frontiers** shows self-evolving search agents "co-cheat": the question proposer and the solver drift into agreeing on shared errors, so the internal reward rises while real accuracy stalls. Cross-fitting (score questions from one document half with a solver trained only on the other half) cuts false agreement from 6.1% to 3.0%.

<div class="dg-title">Check the command before the shell runs it</div>
<div class="dg-sub">The generator and harness stay the same. Only the verifier in the middle is new.</div>

```mermaid
flowchart LR
  G["Generator<br/><small>TMAX-9B</small>"] --> K["K candidates<br/><small>sampled commands</small>"]
  K --> V{"Verifier<br/><small>weak or strong</small>"}
  V -->|best one| H["Harness<br/><small>executes in shell</small>"]
  V -.->|rejected| X["Bad commands<br/><small>never run</small>"]
  H --> E["Environment<br/><small>state changes</small>"]
  E --> G
  H --> R["Pass@1<br/><small>50.0 to 68.0%</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class G core
  class K input
  class V loop
  class H,E input
  class X err
  class R exit
  linkStyle 3 stroke:#e03131,stroke-width:2px
  linkStyle 5 stroke:#f08c00,stroke-width:2px
```

<div class="dg-legend">Purple is the model, blue is candidates and the environment, amber is the verification gate and the loop, red is discarded actions, green is the score.</div>

## How it relates to prior wiki pages

- **Pattern: compute only pays when something good decides where it goes.** Mid-Harness (verifier picks the action), Thinking Before Thinking (controller picks what workers see) and the 10-01 [Raven](2026-10-01-raven-harness-of-harnesses.md) "harness of harnesses" all put a judge above the worker. That is three papers in two days making the same architectural choice.
- **Harness search keeps beating hand design.** MILO joins Google's RRSI (10-01 Media Zone, evolves every harness part around a frozen model) and Meta's branch-based harness search. The 26% token cut is the routing-adjacent result: a better harness is also a cheaper one.
- **Co-cheating is the self-improvement version of reward hacking.** It mirrors the 10-01 insecure-reporting finding (agents' written reports hide failures by default): closed loops grade themselves too kindly unless the feedback has independent ancestry. CheatBench (also 10-01) releases a benchmark for exactly this.

## Gaps

- Mid-Harness's best number uses a frontier verifier, so the cost of the gain is mostly the verifier's tokens; the paper's token-cost estimate is the number to check.
- MILO's search cost (how many full benchmark runs to discover a harness) is not in the abstract.

Related: [Agent harness engineering](agent-harness-engineering.md) · [Self-evolving agents](self-evolving-agents.md) · [Multi-agent systems](multi-agent-systems.md) · [Test-time compute allocation](../inference-efficiency/test-time-compute-allocation.md)
