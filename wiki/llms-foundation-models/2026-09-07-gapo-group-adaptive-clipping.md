# GAPO: Group Adaptive Clipping Policy Optimization

**Source:** HuggingFace Daily Papers, 2026-09-07 · [arXiv 2609.00444](https://arxiv.org/abs/2609.00444) · [raw](../../raw/huggingface/2026-09-07-group-adaptive-clipping-policy-optimization.md)

**TL;DR.** Group-relative policy optimization, the family of methods behind most reinforcement learning with verifiable rewards, clips the importance-sampling ratio at a **fixed boundary for every rollout**. GAPO identifies what that costs. A rare correct rollout on a hard problem and one of many correct rollouts on an easy problem get clipped at comparable rates, even though they carry completely different amounts of learning signal. Rollouts from low-success groups naturally have **larger importance-sampling ratios** and therefore stronger gradient signal for exploring and solving genuinely new problems, and a fixed clip suppresses exactly those. GAPO makes the clipping boundary a function of the rollout's advantage, justified by a reverse-KL trust-region argument that rollouts carrying more learning signal deserve proportionally more update headroom. It is a **plug-in change to the clipping threshold only**: no reward shaping, no new hyperparameter regime, the standard PPO/GSPO surrogate preserved. Across Qwen and Llama models it improves **both Pass@1 and Pass@k** over fixed clipping and advantage-shaping baselines on math and coding benchmarks where the base model's pass rate is low.

```mermaid
flowchart LR
  G[Rollout group<br/>same problem] --> A{Group success<br/>rate}
  A -->|high, easy problem| E[Small IS ratio<br/>weak signal]
  A -->|low, hard problem| H[Large IS ratio<br/>strong exploration signal]
  E --> FC[Fixed clip<br/>same boundary]
  H --> FC
  FC --> SUP[Rare correct rollouts<br/>disproportionately clipped]
  H --> GC[GAPO: clip boundary<br/>scaled to advantage]
  GC --> HEAD[More update headroom<br/>where signal is largest]
  HEAD --> PK[Pass@1 and Pass@k<br/>both improve]
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d
  class G input
  class A,GC decision
  class H,HEAD,PK output
  class E,FC,SUP warn
```

## Relation to prior wiki state

**Pass@k improving alongside pass@1 is the specific thing this wiki has been waiting for, and it makes GAPO the third member of a pattern that now crosses the threshold.** Three results in five days modify the *magnitude* of a per-position or per-rollout update based on a signal about how informative that update is, and all three do it to protect diversity rather than to chase accuracy:

- **[IDA-OPD (09-03)](../inference-efficiency/2026-09-03-ida-opd-influence-directed-distillation.md)** labels each distillation update entropy-expanding or entropy-contracting using a signed first-order proxy, and shrinks the contracting ones. Its diagnosis, **diversity distillation failure**, is that pass@1 improves while pass@k plateaus because concentrating supervision concentrates the student's output distribution.
- **[Cliff (09-03)](2026-09-03-cliff-process-rewards-first-mistake.md)** locates the first mistake in an RLVR rollout and assigns positive token-level advantages before it and negative after, beating on-policy distillation by 15% and standard GRPO by 7% with only modestly capable teachers.
- **GAPO (09-07)** scales the clip boundary with advantage so that rare correct rollouts on hard problems are not suppressed at the same rate as abundant correct ones on easy problems.

**The shared claim, now nameable: the unit of policy improvement is the individual update, and its size should be set by how much that update tells you rather than by a global constant.** Three papers, three subfields (distillation entropy, process-reward design, trust-region clipping), no cross-citations.

**It also answers the [RL for LLMs](rl-for-llms.md) page's five-month diversity-collapse cluster from a new direction.** That page recorded on 09-05 that [Locked at the Entrance](2026-09-05-locked-at-the-entrance-rlvr-breadth.md) localized the loss of breadth: RLVR contracts coverage by up to 67%, concentrated at the first move, so parallel sampling from an RLVR-trained policy draws from a distribution that was narrowed exactly where the draws matter. Six prior interventions were read there as fixes proposed without knowing where the damage happened. **GAPO is the first to name a concrete mechanism inside the optimizer that would produce that contraction**: fixed clipping systematically suppresses the low-success rollouts, and low-success rollouts are precisely the ones that would have kept a non-dominant first move alive. Whether GAPO's pass@k gain actually restores entrance coverage rather than breadth further down the trace is the measurement that would connect the two, and it is not reported.

## Gaps

Gains are demonstrated "on math reasoning and coding benchmarks where the pass rates by the base model are relatively low," which is the regime the method is designed for and also the regime where a method that boosts rare-rollout updates has the most room. **The high-base-pass-rate regime is where an adaptive clip could plausibly destabilize training, and it is not reported.** No wall-clock or step-count overhead is quoted, though an advantage-dependent threshold should be nearly free. And no entropy or coverage measurement is given, so the mechanism's claimed effect on exploration is inferred from pass@k rather than observed directly.

## Related

- [RL for LLMs](rl-for-llms.md) · [Knowledge distillation](../inference-efficiency/knowledge-distillation.md) · [RISE (09-07)](../inference-efficiency/2026-09-07-rise-self-extrapolating-distillation.md)
- [Daily digest 2026-09-07](../daily-digest/2026-09/2026-09-07.md)
