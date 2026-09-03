# Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation

**TL;DR.** Sampled-token on-policy distillation is the cheap version of distillation: the student generates, and you only ask the teacher for its log-probability on the single token the student actually sampled, instead of its full-vocabulary distribution. It works on pass@1 and quietly fails on pass@k, a failure the authors name **diversity distillation failure**: the student gets better at its first answer while never inheriting the teacher's ability to find several different correct answers. This paper explains it with **First-Order Local Entropy Influence**, a signed first-order proxy that decomposes each update's effect on entropy into two factors, the teacher-student log-probability gap and the student's local probability structure, and shows entropy collapse traces to identifiable **negative-influence positions**. The fix, **IDA-OPD**, keeps entropy-expanding updates as they are and replaces only the entropy-contracting ones with divergence-adaptive advantage shrinkage. It needs nothing beyond the sampled-token teacher log-probability. Result: pass@k improves consistently, pass@1 broadly holds at vanilla levels, and it matches the strongest teacher-informed methods at strictly lower cost.

**Source:** [HuggingFace Daily Papers](https://huggingface.co/papers/2608.29846) · [arXiv 2608.29846](https://arxiv.org/abs/2608.29846) · BiliBili Inc., UNC Chapel Hill, USTC, Shanghai University of Finance and Economics · [raw](../../raw/huggingface/2026-09-03-influence-directed-distillation-solving-the-diversity-bottle.md)

```mermaid
flowchart LR
  S[Student rollout] --> TOK[Sampled token]
  TOK --> TQ[Teacher log-prob<br/>sampled token only]
  TQ --> INF{First-Order Local<br/>Entropy Influence}
  INF -->|signed positive<br/>entropy-expanding| KEEP[Keep update as-is]
  INF -->|signed negative<br/>entropy-contracting| SHRINK[Divergence-adaptive<br/>advantage shrinkage]
  KEEP --> OUT[pass@k improves<br/>pass@1 held]
  SHRINK --> OUT
  ALT[Prior fix:<br/>full-vocabulary Forward KL] -.->|restores diversity<br/>but deletes the cost saving| EXP[Expensive]
  ALT2[Prior fix:<br/>global entropy bonus] -.->|untargeted| BLUNT[Hits good updates too]
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d
  classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81
  class S,TOK,TQ input
  class INF decision
  class OUT,KEEP output
  class EXP,BLUNT warn
  class SHRINK,ALT,ALT2 aux
```

---

## What problem it solves

On-policy distillation trains the student on its own generations under teacher supervision. Full-vocabulary OPD matches the student's whole output distribution to the teacher's at every position, which is accurate and expensive. **Sampled-token OPD** cuts the cost to almost nothing by requesting the teacher's log-probability for one token per position, the one the student sampled. That is the version that scales, and it is the version in wide use.

Its failure is specific and has a signature. **Pass@1 improves while pass@k plateaus.** The student learns to produce the teacher's most likely answer and loses the teacher's spread. For anything downstream that samples multiple attempts, which is every reasoning pipeline that uses best-of-n, self-consistency, or verifier reranking, that is the capability you were paying for.

The two existing repairs both give something up. **Teacher-informed** methods reintroduce richer teacher signal, top-K distributions or full-vocabulary Forward-KL objectives (AOPD, EOPD, divergence-based criteria), which restores diversity by re-paying the cost that sampled-token OPD existed to avoid. **Student-side** methods keep the cost low by inflating the student's entropy globally, via entropy bonuses, relaxed heavy-tailed credits, or reinforcing negative samples, but they are blunt: they push entropy up everywhere without identifying which updates were destroying it.

## The core novelty

The mechanism, not the fix. **First-Order Local Entropy Influence** is a signed first-order proxy for how a given update will move the student's entropy, and it factorizes into two interpretable quantities: the **teacher-student log-probability gap** at that position, and the **student's local probability structure** there. Because it is signed, every update can be labelled entropy-expanding or entropy-contracting before it is applied, which turns "distillation collapses diversity" from an aggregate observation into a per-position property. The paper then links entropy contraction empirically to **negative-influence positions**, so the diagnosis is localized rather than global.

IDA-OPD is the minimal intervention that follows: leave entropy-expanding updates untouched, and replace entropy-contracting ones with **divergence-adaptive advantage shrinkage**, scaling the update down in proportion to the divergence rather than discarding it. Crucially the whole thing runs off the sampled-token log-probability that vanilla OPD already fetches, so it is **precise like the teacher-informed methods and cheap like the student-side ones.** That is the actual contribution: it dissolves the trade-off rather than picking a side of it.

## Key results

- **Pass@k improves consistently** on reasoning-oriented distillation, which is the metric the whole failure mode was defined by.
- **Matches the strongest teacher-informed methods at strictly lower cost.** No top-K, no full-vocabulary Forward KL.
- **Pass@1 broadly maintained** at vanilla sampled-token OPD levels, so the diversity is not bought by giving back accuracy.
- Requires **only the teacher's sampled-token log-probability**, meaning it is a drop-in change to an existing sampled-token OPD training loop rather than a new pipeline.

## How this relates to prior wiki pages

**It opens a fifth axis on the selective-supervision program that [knowledge-distillation.md](knowledge-distillation.md) has been tracking all year, and it is the first one about the objective rather than the data.** That page records four axes so far: **which tokens** to supervise (TIP, 04-16, which found most teacher-generated tokens carry no learning signal and roughly 10% suffice, through TA-OPD, TrOPD, FiRe-OPD, SG-OPD, to [R2-OPD (08-25)](2026-08-25-r2-opd-reasoning-progress-filtering.md)); **which layer** (OPRD, 06-05, align hidden states and bypass the LM head); **which trajectories** ([OPDVR (08-26)](2026-08-26-opdvr-distillation-verifiable-reward.md), keep only trajectories with verifiable reward); and **which teacher** ([QAH (08-26)](2026-08-26-quantization-aware-healing.md)). IDA-OPD adds **which updates**, selected by their signed effect on entropy. Every prior axis asks what to learn from. This one asks what a given update does to the student's distribution, which is a different question and the first that is measured on the student side rather than the teacher side.

**It also changes what the program is optimizing.** All four earlier axes were sharpening a single answer, and the entire family is evaluated on accuracy. IDA-OPD is the first result on this page whose target is **pass@k**, and it reveals that the selective-supervision program has a systematic blind spot: filtering supervision to the highest-signal tokens is exactly the operation that concentrates the student's distribution. **Selectivity and diversity are in tension, and no paper in the earlier thread measured the cost.** That is a retroactive question mark over a year of results, and it is the most useful thing this paper does for the wiki.

**It is the third consecutive result in this family to depend on an auxiliary estimator, and the first where the estimator is actually derived.** [knowledge-distillation.md](knowledge-distillation.md) generalized a warning on 08-26: R2-OPD's progress-reward model and VoI-MoLE's reducibility estimator are both unvalidated learned models with no sensitivity ablation, so "every method in this family depends on a second estimator nobody has validated." First-Order Local Entropy Influence is different in kind. It is a **closed-form first-order proxy with an interpretable factorization**, not a trained network, so it can be reasoned about analytically. Whether the first-order approximation holds where it matters is a fair question; whether it is a black box is not. That is a real methodological improvement on its own neighbourhood.

**Cross-thread with today's [Cliff (09-03)](../llms-foundation-models/2026-09-03-cliff-process-rewards-first-mistake.md).** Both papers convert a per-position diagnosis into **signed token-level advantages** and both work by treating positions asymmetrically rather than reweighting uniformly: Cliff splits a rollout at the first mistake and assigns positive advantage to the correct prefix and negative after, IDA-OPD splits updates by entropy sign. Two papers on one day arriving at signed, position-local advantage shaping from unrelated starting points (RLVR reward design and distillation entropy) is a convergence on the *unit of credit assignment*, and neither cites the other.

## Gaps

- **First-order only.** The proxy is explicitly first-order, and entropy dynamics over a full training run are not. No evidence is offered that the approximation stays faithful late in training when the student's local probability structure has moved substantially from where the proxy was calibrated.
- **Shrinkage, not removal, and the schedule is unreported.** Divergence-adaptive shrinkage has a functional form and presumably a hyperparameter. How sensitive the result is to it is the obvious ablation and the abstract does not mention one.
- **"Broadly maintains" pass@1 is a hedge.** It says there are cases where pass@1 degrades. Which cases, and by how much, decides whether this is a free improvement or a trade.
- **Reasoning-oriented distillation only.** Diversity matters differently in open-ended generation, and there is no evidence outside reasoning benchmarks.
- **No teacher-scale sweep.** Whether the entropy-contraction problem gets worse as the teacher-student gap widens is directly predicted by the mechanism (the log-probability gap is one of the two factors) and is not tested.

## Industrial implication

Anyone running sampled-token OPD to compress a frontier model into a servable one is currently shipping a student that is quietly worse at best-of-n than its teacher, and if their eval is pass@1 they cannot see it. The immediate action is cheap: **add pass@k to the distillation eval, and if the plateau is there, IDA-OPD is a loop-level change rather than a pipeline rebuild.** This matters most for the tiered-serving architectures that the rest of this week's results are making practical, because a small model that inherits a large model's context ([Cross-Model KV Sharing, 09-02](2026-09-02-cross-model-kv-sharing.md)) but not its solution diversity will fail exactly on the hard queries that were routed to it as a cost saving.

## Related

- [knowledge-distillation.md](knowledge-distillation.md) — concept page, the selective-supervision axes
- [R2-OPD (08-25)](2026-08-25-r2-opd-reasoning-progress-filtering.md) · [OPDVR (08-26)](2026-08-26-opdvr-distillation-verifiable-reward.md) · [QAH (08-26)](2026-08-26-quantization-aware-healing.md)
- [Cliff (09-03)](../llms-foundation-models/2026-09-03-cliff-process-rewards-first-mistake.md) — the same signed-advantage move from the RLVR side
