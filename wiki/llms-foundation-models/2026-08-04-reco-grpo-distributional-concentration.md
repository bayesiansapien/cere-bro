# ReCo: Reweighting GRPO Against Distributional Concentration

**Source:** Kurate weekly cs.LG leaderboard #19, ai_rating 6.0/10 · [arXiv 2607.26862](https://arxiv.org/abs/2607.26862) · published 2026-07-29 · raw: [`raw/kurate/2026-08-04-cs-lg.md`](../../raw/kurate/2026-08-04-cs-lg.md)

**Authors:** Junoh Park, Junseo Hwang, Wonguk Cho, Taesup Kim

## TL;DR

GRPO (Group Relative Policy Optimization, the standard RL recipe for post-training language models: sample a group of responses per prompt, score them, and push the policy toward the better ones relative to the group) is known to reduce a base model's reasoning coverage, underperforming the base model on Pass@k when k is large. ReCo traces that to **distributional concentration** and localizes it in two specific terms of the GRPO update. At the response level, responses the base model already generates with high probability simply appear more often in the sampled group, so they dominate the group gradient by repetition. At the token level, GRPO's importance ratio scales gradients in proportion to how likely a token has become under the current policy, which reinforces already-likely tokens further. Both effects push in the same direction, toward whatever the base model was already going to say. ReCo fixes both: normalize each response's contribution by its **expected occurrence** within the rollout group, and replace the token-level importance ratio with a **variance-based ratio** that gives larger update scale to non-saturated decision points where alternative tokens are still plausible. Across Qwen2.5-Math-1.5B/7B and Llama-3.1-8B-Instruct on five math benchmarks, ReCo improves Pass@k at large k and matches GRPO at small k.

---

```mermaid
flowchart LR
  BASE[Base model<br/>reasoning coverage] --> ROLL[Sample rollout group]
  ROLL --> R1[Response-level:<br/>high-probability responses<br/>appear MORE OFTEN]
  ROLL --> R2[Token-level:<br/>importance ratio scales<br/>with current likelihood]
  R1 --> CONC[Distributional<br/>concentration]
  R2 --> CONC
  CONC --> LOSS[Pass@k drops<br/>at large k:<br/>coverage lost]
  R1 --> FIX1[ReCo: normalize by<br/>EXPECTED occurrence]
  R2 --> FIX2[ReCo: variance-based ratio,<br/>upweight non-saturated<br/>decision points]
  FIX1 --> KEEP[Pass@k improves at large k,<br/>matched at small k]
  FIX2 --> KEEP
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d
  classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81
  class BASE,ROLL input
  class R1,R2 decision
  class FIX1,FIX2,KEEP output
  class CONC,LOSS warn
```

---

## Key claims

- **The Pass@k regression is mechanistic, not mysterious, and it has two independent causes inside one update rule.** Repetition-driven group dominance and importance-ratio reinforcement both amplify high-probability content, and either alone would produce concentration.
- **Expected-occurrence normalization is the response-level fix.** If a response would appear three times in expectation, its contribution is divided accordingly, so sampling frequency stops doubling as gradient weight.
- **A variance-based ratio is the token-level fix, and the choice of statistic is the interesting part.** Instead of scaling by how likely a token now is, scale by how *undecided* the position is, which puts update magnitude where alternative choices remain live.
- **The result is asymmetric by design.** Pass@k improves at large k and is comparable at small k, meaning ReCo buys coverage without paying greedy accuracy. That is the right shape for a fix to an over-concentration problem.
- **Three models across two families, five math benchmarks.**

## Gaps

Math reasoning only, which is the domain where verifiable rewards work best and where response diversity is most easily confounded with solution-path diversity. No agentic or open-ended evaluation. The variance-based ratio replaces a well-understood term in a well-understood objective, and the abstract reports no stability or divergence analysis, which is what everyone actually worries about when the importance ratio is swapped. And Pass@k at large k is a coverage metric that only converts to value if you have a verifier at inference time, so the practical benefit is scoped to settings with one.

## How this relates to prior wiki pages

**It is the RLVR-side twin of a result [knowledge-distillation](../inference-efficiency/knowledge-distillation.md) recorded the day before, and the two prescriptions conflict.** [CriPO (08-03)](2026-08-03-cripo-rubric-rl-self-distillation.md) found that **over 57% of rubric-RL samples contain a criterion the model already satisfied whose signal was destroyed by scalar advantage aggregation**, and fixed it with self-distillation from privileged self-teachers. Both papers say the same thing structurally: **GRPO-family aggregation destroys information that was present in the rollout.** CriPO's destroyed information is per-criterion credit, ReCo's is coverage of low-probability reasoning paths.

**The conflict is with [CRPO (08-04)](../inference-efficiency/2026-08-04-crpo-contrastive-privileged-self-distillation.md), and it is a real one worth tracking.** CRPO uses predictive entropy to identify positions where the student is genuinely uncertain and, in agentic multi-turn settings, treats a subset of them as **exposure-bias artifacts to be contrasted away** because the privileged self-teacher is unreliable there. ReCo takes the same class of position, non-saturated decision points where alternatives remain plausible, and **upweights them**. Same statistic, opposite treatment. The reconciliation may be that they optimize different things: ReCo is protecting exploration coverage against a base-model prior, CRPO is protecting supervision reliability against a teacher that is confidently wrong. If so, an agentic RLVR recipe would need both signals and a way to tell the two kinds of uncertainty apart, which nobody has proposed. If not, one of them is wrong about what high entropy means.

**And it lands on [rl-for-llms](rl-for-llms.md)'s longest-running question: whether RL adds capability or reshapes it.** ReCo is evidence for reshaping, with a named mechanism, and its fix recovers coverage rather than adding any. That is consistent with the Pass@k-collapse literature the page tracks and gives it a concrete pair of culprits rather than a general suspicion.

## Related pages

- [RL for LLMs](rl-for-llms.md)
- [CriPO: rubric RL self-distillation](2026-08-03-cripo-rubric-rl-self-distillation.md)
- [CRPO: contrastive privileged self-distillation](../inference-efficiency/2026-08-04-crpo-contrastive-privileged-self-distillation.md)
- [Knowledge Distillation](../inference-efficiency/knowledge-distillation.md)
