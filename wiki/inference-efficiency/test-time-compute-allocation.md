# Test-Time Compute Allocation

**Concept page. Created 2026-08-16.**

The question is no longer *how much* compute to spend at inference. It is **where**. Given a fixed hardware budget and a query, which of the many places compute could go should receive the next unit: a longer chain, another parallel sample, a deeper branch off a promising prefix, a stronger model, or nothing at all.

This page exists because the wiki has accumulated at least eight results on the question without a page to hold them, which the [lint rule](../../CLAUDE.md) flags as a gap once a concept appears in three or more sources.

## The five decisions

Every result below is answering one of these, and almost none of them answer two.

| Decision | Question | Representative work |
|---|---|---|
| **Whether to spend at all** | Is this query within the model's capability? | [CaRL (08-16)](2026-08-16-carl-knowing-when-to-quit.md) |
| **When to stop** | Has this chain converged? | [PUMA (05-19)](2026-05-19-puma-semantic-preserving-early-exit-reasoning.md), [AdaSR (06-15)](2026-06-15-adasr-streaming-reasoning-hrpo.md) |
| **Where to spend, across traces** | Which partial trajectory deserves the next unit? | [Gambit (08-16)](2026-08-16-gambit-thought-level-beam-search.md) |
| **How to spend, more cheaply** | Can the same reasoning happen in a cheaper representation? | [SLPO (07-23)](2026-07-23-slpo-latent-reasoning-surrogate-policy.md) |
| **Who should spend it** | Which model, harness, or expert should get the query? | [LLM Routing](../ai-routing/llm-routing.md) |

## Current state (as of 2026-08-16)

**The across-trajectory axis just opened, and it is the first one that is a serving-stack change rather than a model change.** [Gambit (08-16)](2026-08-16-gambit-thought-level-beam-search.md), from Princeton, MIT CSAIL and Meta AI, formalises test-time reasoning as constrained compute allocation over partial trajectories and shows that the two existing paradigms fail in opposite directions. Independent parallel sampling learns nothing from a trace that collapsed at step three and is capped by KV cache pressure rather than by FLOPs. Subtractive pruning (DeepConf, STEP, Slim-SC) frees that memory and then wastes it, starving the hardware and never shifting the output distribution. Gambit adds the missing half: kill weak traces, immediately re-branch from strong prefixes, keep utilisation high. Up to **+6.7 points on HMMT-24**, **>2x throughput**, and **up to 68.5% fewer total tokens**.

**The empirical premise underneath it is worth stating separately**, because it constrains everything on this page: successful and failed reasoning trajectories share their opening steps and diverge later, so useful computation is disproportionately concentrated in **early intermediate states**. If that holds generally, then late-stage compute is systematically the least valuable compute, and every method here is really a way of noticing early.

**The whether-to-spend-at-all axis got its first serious treatment the same day.** [CaRL (08-16)](2026-08-16-carl-knowing-when-to-quit.md) documents **universal capability overreach**: models handed beyond-capability tasks produce long, expensive, specious derivations rather than stopping, and the miscalibration is systematic. Its hindsight refusal augmentation converts observed failures into refusal supervision, so the boundary is learned from where the model actually fails rather than from a difficulty heuristic. Gambit optimises within an attempt, CaRL decides whether to attempt, and nobody has composed them.

**There is a live methodological objection to the entire page.** [Sampling Luck Masquerades as Allocation Gain](http://arxiv.org/abs/2608.13087) (Kurate cs.LG #6, week of 2026-08-16) audits test-time budget allocation for neural combinatorial optimization and argues reported allocation gains are frequently the variance of drawing more samples rather than a real allocation effect. Any method that changes the effective number of independent draws, which is most of them, is exposed. Gambit's partial defence is that it reports lower *total token consumption* alongside higher accuracy, which sampling luck cannot produce, but it does not run the audit. **Nobody on this page has run it.**

**Aggregation over samples is weakening as an assumption.** [When Self-Consistency Backfires](http://arxiv.org/abs/2608.11403) (Kurate cs.AI #1 this week) finds majority vote *hurts* on the majority of hard science problems for small models, and [Are You Sure You're Sure? (08-16)](../responsible-ai/2026-08-16-instruction-tuning-confidence-lexical-diversity.md) finds instruction tuning consistently collapses cross-rationale diversity while leaving accuracy roughly unchanged. Self-consistency is the baseline nearly every result here is measured against, and two independent papers this week say the baseline is less sound than assumed, from the aggregation side and from the diversity side respectively.

## What the allocation is actually constrained by

Worth naming because papers say "compute budget" and mean different things.

- **KV cache memory**, which is what caps batch size for long reasoning contexts and is therefore the real constraint on parallel sampling. See [KV Cache](kv-cache.md).
- **Hardware utilisation**, which is what subtractive pruning sacrifices and Gambit protects.
- **Tokens**, which is what the customer is billed for, and which [does not convert cleanly to dollars across vendors](../ai-industry/2026-08-16-optima-cost-per-task-benchmarking.md): the same text can cost 34.5% more tokens under one tokenizer than another.
- **Wall-clock**, which is what an interactive product is constrained by and which almost no paper here reports.

## Open problems

1. **Run the sampling-luck audit on a reasoning benchmark.** It has been run on combinatorial optimization. Until it is run on HMMT or AIME, every allocation gain on this page has an unexamined confound.
2. **Compose the gate with the rationer.** CaRL at the door, Gambit inside. Both are cheap, both are policy-level, and the combination is unbuilt.
3. **Route on capability overreach instead of refusing.** CaRL's detector fires on "this model cannot do this," which is a routing signal, not a stopping signal. Escalating to a stronger model is strictly better than quitting for any user willing to pay, and [LLM Routing](../ai-routing/llm-routing.md) has no paper proposing it.
4. **Report wall-clock and dollars, not just tokens.** With [Optima (08-16)](../ai-industry/2026-08-16-optima-cost-per-task-benchmarking.md) shipping per-task cost and time measurement, the excuse that the instrument does not exist has expired.

## Related pages

- [KV Cache](kv-cache.md)
- [LLM Routing](../ai-routing/llm-routing.md)
- [Knowledge Distillation](knowledge-distillation.md)
- [Speculative Decoding](speculative-decoding.md)

---

## 2026-08-28: a new category, spending test-time compute on the weights

Everything else on this page allocates **inference** compute: how many samples to draw, how long to think, how to ration a fixed budget across a batch of queries. [TTPO](2026-08-28-ttpo-test-time-policy-optimization.md) (arXiv 2608.27448) spends test-time compute on **gradient updates to the model**, which this page has no prior entry for.

The mechanism in brief: sample rollouts on unlabeled test questions, take a majority-vote pseudo-label, then treat the two branches asymmetrically because **rollouts that disagree with the vote are usually wrong regardless of whether the vote was right.** Agreeing rollouts get dense on-policy self-distillation; disagreeing ones get a grouped RL penalty restricted to *confident* errors. Without labels it matches label-supervised on-policy self-distillation on five competition benchmarks and takes Qwen3-1.7B from 38.0% to 45.2%.

**The result that belongs on this page specifically is +25.2% to +36.4% "without thinking."** That is a direct substitution between two test-time budgets the field has treated as unrelated: TTPO recovers a large share of chain-of-thought's benefit by moving the spend out of generated reasoning tokens and into a weight update. If it holds, "how much test-time compute" stops being one dial and becomes an allocation problem between **reasoning tokens** and **adaptation steps**, which is the same shape as this page's existing batch-rationing results but across a boundary nobody was pricing.

**The comparison the paper owes and does not give.** Test-time training means N rollouts plus optimizer steps per test distribution. The honest baseline is spending that identical compute on more samples plus majority voting at inference, which needs no gradients, no optimizer state and no infrastructure. Until that number exists, TTPO is a capability claim at an unknown price. Note also that adapting weights at test time breaks reproducibility and complicates rollback and audit, which is why this will likely appear first in batch and offline scoring, where the adapted checkpoint can be pinned, rather than in interactive serving.

**Related on the same day:** [Evolution Strategies vs GRPO](../llms-foundation-models/2026-08-28-evolution-strategies-vs-grpo.md) is the other half of the Pass@K story. It finds GRPO exhibits entropy collapse, lifting Pass@1 while flattening Pass@K, where Evolution Strategies lifts both. That matters here because every best-of-K and agentic-sampling pipeline on this page is paid for in Pass@K, and the finding says the standard post-training recipe has been destroying the property those pipelines depend on. It also partly reframes the **AIMO 3 result (04-17)** that prompt diversity is a dead end for inference-time scaling: the narrowness AIMO 3 could not fix from the prompting side may have been created by the training algorithm. Whether an ES-trained model makes inference-time diversity methods work again is untested and cheap to test.
