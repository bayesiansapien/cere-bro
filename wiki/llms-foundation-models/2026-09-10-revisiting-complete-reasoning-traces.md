# Revisiting complete reasoning traces: the middle of a trajectory carries almost no signal

**Source:** HuggingFace Daily Papers (6 upvotes) · [Paper](https://arxiv.org/abs/2609.07103) · [Code](https://github.com/naver-ai/revisiting-trace) · [raw](../../raw/huggingface/2026-09-10-revisiting-complete-reasoning-traces-for-post-training.md)

## TL;DR

Post-training on pre-collected reasoning trajectories is standard practice, and those trajectories are long because real reasoning takes detours. NAVER AI asks whether the length is doing any work. Their pilot finds that **full trajectories provide only limited benefit while partial trajectories remain effective even under heavy truncation.** Two independent analyses explain why: attention-based inspection shows intermediate tokens receive little weight in producing the final answer, and controlled token-removal studies show deleting them barely moves reasoning quality. The interpretation is that given the trajectory's **endpoints**, a model can internally infer the missing steps from knowledge it already has, so supervising those steps teaches it something it does not need. Training on endpoints alone produces consistent, measurable changes in reasoning behaviour and also improves downstream reinforcement learning and on-policy distillation.

## Key points

- **Two orthogonal probes reach the same conclusion**, which is what makes this more than an ablation. Attention analysis is correlational; controlled token removal is causal. Both point at the intermediate span.
- **"Endpoints" is a cheap intervention.** No new loss, no reweighting scheme, no teacher model. Truncate, keep the ends, train.
- **The gain extends past SFT.** Endpoint training also improves RL and on-policy distillation stages downstream, which suggests it is changing what the model learns rather than just what it memorizes.
- **Directly relevant to cost:** reasoning traces are the most expensive supervised data to collect and the most expensive to train on, and this says most of each one is waste.

## How this relates to prior wiki pages

**It is the fifth paper in three weeks arguing that training signal is concentrated in a small fraction of tokens, and at this point the pattern is established rather than emerging.** [TIP](../inference-efficiency/knowledge-distillation.md) found most teacher-generated tokens carry no distillation signal and roughly 10% suffices. [IDA/OPD (09-03)](../inference-efficiency/2026-09-03-ida-opd-influence-directed-distillation.md) selected distillation targets by influence rather than uniformly. [TG-OPD (09-08)](../inference-efficiency/2026-09-08-tgopd-prompt-level-teacher-gating.md) gated the teacher at the prompt level, deciding *whether* to consult it at all. [One-Example On-Policy Distillation (09-04)](../inference-efficiency/2026-09-04-one-example-on-policy-distillation.md) pushed the extreme case. This paper adds the *positional* version: not which examples, not which tokens by importance, but **which region of a trajectory**, and its answer is the ends. Five independent groups, one claim: **uniform supervision over generated text is wasteful, and the field has converged on selective training.**

**It cuts against the on-policy-correction result from [Co-Evolving Harnesses (09-10)](../agentic-systems/2026-09-10-co-evolving-harnesses-on-policy-correction.md), which found that training a weak model on an expert's complete trajectories under an evolved harness regressed performance on all seven tasks by 4 to 30 points, and fixed it by having the expert rewrite only the single failing turn.** Both papers say complete trajectories are the wrong training unit. They disagree about which part to keep: this paper keeps the endpoints and discards the middle; Co-Evolving Harnesses keeps the weak model's own middle and replaces one turn. The reconciliation is that they are solving different problems (redundancy versus style mismatch), but the shared conclusion is strong: **nobody should be training on complete trajectories by default, and the burden of proof has flipped.**

**It gives a mechanism to a question [rl-for-llms.md](rl-for-llms.md) has carried about why long chains of thought help at inference but not proportionally in training.** If intermediate tokens are inferable from endpoints given the model's internal knowledge, then a long trace at inference time is doing computation, while a long trace in training data is mostly restating what the model can already derive. That is a clean distinction and it explains the asymmetry.

## Gaps

The claim that models "internally infer missing steps" is an interpretation of two negative results, not a demonstrated mechanism, and it would fail on problems where the intermediate steps encode genuinely new information rather than derivable structure. Benchmarks are not enumerated in the abstract. And "heavy truncation" is not quantified, so the practical recipe (how much middle to cut) is unspecified.

## Related

- [RL for LLMs](rl-for-llms.md) · [Knowledge distillation](../inference-efficiency/knowledge-distillation.md) · [Test-time compute allocation](../inference-efficiency/test-time-compute-allocation.md)
