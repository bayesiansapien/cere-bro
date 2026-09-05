# Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space

**arxiv:** [2608.29188](https://arxiv.org/abs/2608.29188) · **Source:** [HuggingFace Daily Papers 2026-09-05](../../raw/huggingface/2026-09-05-locked-at-the-entrance-open-inside-where-rlvr-narrows-the-so.md) · **Authors:** Qiancheng Zhou, Ruizhe Li · **Code:** [github.com/ershiyidian/early-branch-locking](https://github.com/ershiyidian/early-branch-locking)

## TL;DR

RLVR (reinforcement learning with verifiable rewards, where a programmatic checker supplies the reward signal instead of a human or a learned judge) reliably raises single-sample accuracy and reliably destroys diversity. The wiki has recorded that trade for five months without anyone saying **where inside a reasoning trajectory the breadth is actually lost**. This paper localises it, and the answer is unusually clean: **the loss is at the first move.**

The setup is what makes the claim checkable. The authors use Countdown, an arithmetic task whose solution space can be *exhaustively enumerated* into discrete "entrance families" defined by the first operand and the first operator. That converts "did the model lose a solution" from a vague diversity metric into a countable fact about which families it can still enter. Across PPO on Qwen2.5-3B and GRPO on Qwen2.5-3B-Instruct, **solution coverage falls by up to 67 percent**, and it halves even on problems the model solves at every checkpoint, so this is not a side effect of getting better at hard problems.

The localisation is the result. **Per-token likelihood shifts are 11 to 16 times larger before the first arithmetic operation than during downstream reasoning.** The policy is not being taught to execute one solution family better; it is being taught not to open the other doors. The decisive intervention proves it: supply an *unselected* entrance prefix, nothing else, and completion rates in low-access families rise by more than an order of magnitude, **0.018 to 0.212 under PPO**. The alternative solutions were still fully executable the whole time. They were simply never initiated.

Two follow-ons matter more than the diagnosis. First, **surface prompting fails to recover diversity but entrance-targeted parameter surgery works**: late-layer parameter interpolation with early checkpoints raises solution coverage by **37 percent at no loss in pass@1**. The recovery is free in compute terms, because the early checkpoints are already on disk. Second, the phenomenon **is not inevitable**. Early-step entropy collapse recurs across six math benchmarks at 7B and 14B, but an SFT baseline preserves **more than double** the coverage, and staged SFT to DPO to RLVR pipelines retain early-step entropy. The recipe, not the objective, decides whether breadth survives.

## Mechanism

```mermaid
flowchart LR
  P[Prompt] --> ENT{Entrance choice<br/>first operand + operator}
  ENT -->|family A<br/>high likelihood after RLVR| EXA[Execute solution A]
  ENT -.->|families B..N<br/>likelihood crushed<br/>11-16x larger shift here| EXB[Execute solution B..N<br/>still fully capable]
  EXA --> OK[pass@1 up]
  EXB --> COV[Coverage down up to 67%<br/>test-time scaling returns shrink]
  FIX1[Surface prompting<br/>ask for a different approach] -.->|fails| ENT
  FIX2[Supply unselected<br/>entrance prefix] -->|0.018 to 0.212| EXB
  FIX3[Late-layer interpolation<br/>with early checkpoints] -->|+37% coverage<br/>no pass@1 loss| ENT
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d
  classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81
  class P input
  class ENT decision
  class EXA,OK,FIX3 output
  class COV,FIX1 warn
  class EXB,FIX2 aux
```

## Key findings

- **Coverage falls up to 67 percent under both PPO and GRPO**, and halves even on the subset of problems solved at every checkpoint. The contraction is not explained by the model shifting to harder problems.
- **The likelihood damage is 11 to 16 times larger before the first operation** than during the rest of the trajectory. Breadth is lost at the door, not inside the room.
- **Alternative families remain executable.** Handing the model an entrance prefix it would never have chosen lifts completion in low-access families from 0.018 to 0.212 under PPO, a factor above ten.
- **Late-layer parameter interpolation with early checkpoints recovers 37 percent of coverage at no pass@1 cost**, while surface prompting recovers nothing. Diversity is a parameter-space property here, not a prompting one.
- **An SFT baseline preserves more than twice the coverage**, and staged SFT to DPO to RLVR retains early-step entropy, so the collapse is a property of the recipe rather than of reward-driven optimisation as such.

## Relation to prior wiki state

**This is the localisation the wiki's five-month diversity-collapse cluster has been missing, and it settles an argument the cluster left open.** The thread starts with [AIMO-3 (04-17)](../inference-efficiency/2026-04-17-model-capability-dominates-inference-time.md), which found that prompt diversity alone cannot close the gap between pass@1 and pass@N. [VPO (05-24)](2026-05-24-vector-policy-optimization-diverse-rl.md) attacked it at the objective, using randomly-weighted vector rewards so the policy keeps multiple modes. [N-GRPO (06-14)](2026-06-14-n-grpo-neighbor-mixing-grpo.md) mixed an anchor token's embedding with its nearest semantic neighbours, and [S2L-PO (06-15)](2026-06-15-s2l-po-small-models-explorers-grpo.md) used a smaller same-family model as a natural explorer because small models have higher policy-level diversity, for +8.8 points on AIME 24. [QuasiMoTTo (07-26)](../inference-efficiency/2026-07-26-quasimotto-qmc-test-time-scaling.md) replaced the sampler with quasi-Monte Carlo low-discrepancy draws for 25 to 47 percent fewer samples at matched pass@k. And [Evolution Strategies vs GRPO (08-28)](2026-08-28-evolution-strategies-vs-grpo.md) documented GRPO's entropy collapse directly and proposed a sequential GRPO-then-ES recipe to get pass@1 from one stage and pass@k from the other.

**Every one of those six is an intervention proposed without knowing where the damage occurs.** AIMO-3 said prompting is the wrong layer, and this paper's surface-prompting negative result confirms that precisely. VPO, N-GRPO, S2L-PO and QuasiMoTTo all inject diversity at or before sampling, which is the right side of the trajectory by this paper's account, though none of them targeted the entrance specifically. The ES result is the closest sibling: it says ES exploits reasoning capability the pretrained model already has rather than sharpening one path, and this paper supplies the mechanism for what "already has" means, since the alternative families are demonstrably still executable and merely un-initiated.

**It creates a genuine tension with [APPO (06-15)](../agentic-systems/2026-06-15-appo-agentic-procedural-policy-optimization.md), and the tension is informative rather than contradictory.** APPO's pilot analysis showed influential decision points are spread throughout the sequence rather than concentrated at tool-call boundaries, and it explicitly rejected token entropy as a reliable locator of influence. This paper finds the opposite shape: the damage is sharply concentrated at position zero, and early-step entropy is the diagnostic that travels across six benchmarks and two model scales. These are compatible if **influence and breadth are different quantities**: which step most changes the outcome of the trajectory you are on (spread out, per APPO) is not the same as which step decides how many trajectories you can reach (concentrated at the entrance, per this paper). Nobody has measured both on one task, and that experiment would settle it.

**It also lands on [test-time compute allocation](../inference-efficiency/test-time-compute-allocation.md)'s stated empirical premise.** That page records, as the constraint underneath everything on it, that successful and failed trajectories share their opening steps and diverge later, so useful computation is concentrated in early intermediate states. This paper agrees on the location and disagrees on the sign: the opening steps are where the value is, and they are also where RLVR has already destroyed the options. If both hold, then parallel sampling from an RLVR-trained policy is buying draws from a distribution that has been narrowed at exactly the point the draws matter, which would explain why so many allocation methods report diminishing returns from more samples.

## Gaps

Countdown is chosen because its solution space is enumerable, which is what licenses the coverage measurement, and it is also a task where "first operand and operator" is an unusually clean partition of solution families. Whether the entrance abstraction survives on tasks where the branch point is not the first token, such as multi-step proof or code, is untested; the six-benchmark entropy result shows the *symptom* generalises but not that the *localisation* does. The interpolation fix is reported at one interpolation schedule with no ablation on which early checkpoint to mix in or how the recovery scales with training length, and no pass@k number is reported alongside the 37 percent coverage figure, so it is unclear how much of the recovered coverage converts into usable test-time-scaling gain. The models are 3B for the main analysis, with 7B and 14B only in the entropy replication.

## Industrial implication

The immediately actionable finding is the cheapest one: **if you have RLVR checkpoints on disk, late-layer interpolation with an early checkpoint is a free pass@k recovery** that costs no training compute and, as reported, no pass@1. Any team serving best-of-n or self-consistency on top of an RLVR-trained model is currently paying for n samples out of a distribution that was collapsed at the entrance, which is the worst possible place for it to be collapsed. The second implication is a recipe recommendation with a number attached: staged SFT to DPO to RLVR retains early-step entropy where straight RLVR does not, so labs that care about sampling-based products should be able to justify the extra stage on breadth grounds rather than on vibes.

## Related pages

- [RL for LLMs](rl-for-llms.md)
- [Test-Time Compute Allocation](../inference-efficiency/test-time-compute-allocation.md)
- [Evolution Strategies vs GRPO (08-28)](2026-08-28-evolution-strategies-vs-grpo.md)
- [QuasiMoTTo (07-26)](../inference-efficiency/2026-07-26-quasimotto-qmc-test-time-scaling.md)
- [Daily digest 2026-09-05](../daily-digest/2026-09/2026-09-05.md)
