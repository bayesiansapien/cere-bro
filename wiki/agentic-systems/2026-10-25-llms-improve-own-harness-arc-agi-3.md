# Can LLMs improve their own harness? A controlled study on ARC-AGI-3

**Source:** arXiv [2610.30499](https://arxiv.org/abs/2610.30499) (Jens Lehmann, Sahar Vahdati; Amazon / TU Dresden, Leibniz Univ. Hannover / TIB). DAIR.AI Academy pick ([page](https://academy.dair.ai/papers/can-llms-improve-their-own-harness-a-controlled-study-on-arc-agi-3-2610.30499)), surfaced via [@omarsar0](https://x.com/omarsar0/status/2114050042705379461) · raw: `raw/twitter/feed/2026-10-25-morning-ranked.json`
**Topic:** harness engineering, self-improving agents

## TL;DR

Each frontier model writes a complete harness for ARC-AGI-3 (interactive games where the agent must discover the goal) from a fixed coding bootstrap, plays five development games, then rewrites its whole codebase twice. Every version is scored on 20 held-out games that never feed back. Across 27 lineages, first harnesses range from zero to near-ceiling, but two rewrites raise mean held-out RHAE (Relative Human Action Efficiency: level completion weighted by action efficiency against humans) by only 2.80 points, with a 95% interval of -1.44 to 7.35. Development-game gains overstate held-out gains, and revisions that cut dollar inference cost often lower the score. Human-steered harnesses still score higher.

<div class="dg-title">Most of the quality is set in draft one</div>
<div class="dg-sub">Rewrites tune to the five games the model can see, not the twenty it cannot.</div>

```mermaid
flowchart LR
  B["Fixed bootstrap<br/><small>same for every model</small>"] --> H1["Harness v1<br/><small>zero to near-ceiling</small>"]
  H1 --> D["5 dev games<br/><small>feedback visible</small>"]
  D --> H2["Rewrite x2<br/><small>whole codebase</small>"]
  H2 -->|re-scored| E["20 held-out games<br/><small>+2.8 RHAE, CI crosses 0</small>"]
  H2 -->|cheaper| X["Cost cuts<br/><small>often lower score</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class B input
  class H1,H2 core
  class D loop
  class E exit
  class X err
  linkStyle 3 stroke:#2f9e44,stroke-width:2px
  linkStyle 4 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is the shared start, purple are harness versions, amber is the visible feedback, green is the held-out score, red is the cost-cut failure mode.</div>

## Relation to prior wiki pages

- **Confirms** the 10-22 HDA audit on the [harness concept page](agent-harness-engineering.md) (about 54% of harness-evolution gains are overfitting to the search set). Two independent groups now find self-revision mostly overfits. Pattern n=2 with clean held-out splits.
- **Contrasts** with Harness Scaling (10-23: training across many harnesses transfers) and Google Cloud's specialized-harness router (10-22/24: +16 points with inheritance and a router). The difference: those had a search loop with held-out selection or RL; here the model revises open-loop from five games.
- **Cost axis:** the finding that cheaper revisions lose score matches the 10-24 harness-cost study (cost varies 3x across harnesses while pass rate barely moves) from the other side: cost cuts made by the model itself are not free.
