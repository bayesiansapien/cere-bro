---
title: "R²-OPD: reweight teacher supervision by whether the student's rollout actually succeeded"
date: 2026-10-04
sources:
  - https://arxiv.org/abs/2609.35517
  - ../../raw/kurate/2026-10-04-cs-lg.md
tags: [on-policy-distillation, knowledge-distillation, token-weighting, rlvr]
---

# R²-OPD: reward-aligned reweighting for on-policy distillation

**TL;DR.** On-policy distillation (OPD: the student generates its own answers and a stronger teacher scores every token) weights every token's correction equally. That treats "the teacher would have written something else here" as if it always helped. It doesn't: a correction can push the student off a path it was about to finish correctly, or onto one it cannot execute. R²-OPD (arXiv 2609.35517, Kurate cs.LG #10) uses two signals to reallocate supervision continuously: whether the trajectory's verified outcome agrees with the teacher's correction, and how strongly teacher and student disagree. Reward-aligned corrections get more weight; dense feedback is kept rather than hard-filtered. It **beats standard OPD on all seven math benchmarks**, by **+3.5 points average for a 1.7B student and +2.4 for 4B**, and +1.6 on code.

<div class="dg-title">Not every teacher correction deserves the same weight</div>
<div class="dg-sub">Outcome agreement decides how loud each token's correction is.</div>

```mermaid
flowchart LR
  S["Student rollout<br/><small>own trajectory</small>"] --> T["Teacher scores<br/><small>per-token preference</small>"]
  S --> V["Verifier<br/><small>was it right?</small>"]
  T --> W{"Reweight<br/><small>agreement and gap</small>"}
  V --> W
  W -->|aligned| U["Up-weight<br/><small>useful corrections</small>"]
  W -->|misaligned| D["Down-weight<br/><small>would hurt student</small>"]
  U --> G["Student update<br/><small>+3.5 pts at 1.7B</small>"]
  D --> G
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class S input
  class T,V core
  class W loop
  class U,G exit
  class D err
  linkStyle 4 stroke:#2f9e44,stroke-width:2px
  linkStyle 5 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is the student's rollout, purple the two scorers, amber the reweighting, green kept signal, red damped signal.</div>

## Key findings

- Formalizes the mismatch between local teacher preference and the student's continuation value, with sufficient conditions under which reallocation improves first-order task progress over uniform OPD.
- Highest average accuracy among compared methods in both cross-size and same-size distillation.

## How this relates to prior wiki pages

- **Fourth token-weighting answer to "which teacher tokens matter".** TIP (04-16) found most teacher tokens carry no signal and kept about 10%; SAKI (10-01) used maximal coupling to route teacher supervision only where student and teacher distributions diverge; MOPD-Router (09-29) picked a teacher per token. R²-OPD is the first on this wiki to weight by the *verified outcome* of the student's own continuation, which ties OPD to RLVR rewards. See [knowledge-distillation](knowledge-distillation.md).
- **Tension with 10-03's distillation-dynamics study**, which found KL direction and learning rate matter more than rollout policy. If learning rate shapes update sparsity, some of R²-OPD's gain could come from effectively changing the step size on misaligned tokens. Unresolved.
- **Sharpening Tax (10-03)** argued post-training mostly sharpens what the base already knows. R²-OPD's down-weighting of corrections the student "cannot reliably execute" is consistent with that: distillation helps most where the student is already close.

## Gaps

- Math and code only, 1.7B and 4B students. Needs a verifier, so it does not apply to open-ended tasks where OPD is most attractive.

**Raw source:** [Kurate cs.LG leaderboard](../../raw/kurate/2026-10-04-cs-lg.md); paper linked above.
