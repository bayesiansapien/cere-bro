---
title: "Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention"
date: 2026-05-29
arxiv: https://arxiv.org/abs/2605.29548
source: huggingface
tier: 1
topic: llms-foundation-models
---

# Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention

> The reason bigger models learn rare and complex tasks that small ones don't is not raw capacity. It's **gradient interference**: small models allocate their neurons to high-frequency or low-complexity tasks, then their gradient updates on those tasks keep overwriting the rare-task features before they consolidate.

```
Small model (data-induced competition over neurons):

  Common tasks    ► loud gradients ► overwrite rare-task features each step
  Rare tasks      ► tiny gradients ► get erased before consolidation
  Result: rare/complex tasks remain unlearned even with INFINITE data

Large model (gradient interference reduced):

  Common tasks    ► already well-learned ► gradients become weak/small
  Rare tasks      ► accumulate slowly without overwrite
  Result: rare/complex tasks finally learned

Validated end-to-end on:
  ── Synthetic mixture-of-tasks (controlled frequency × complexity grid)
  ── OLMo models from 4M → 4B params on novel-task pretraining
       only the largest OLMo models learn the infrequent + complex tasks
       larger models embed more features in their representations
       larger models show less gradient interference between tasks
```

## TL;DR

Power-law scaling already mathematically implies that a larger model can learn a part of the data distribution a smaller model cannot, even with infinite training data. This paper validates that claim and identifies the *mechanism*: data-induced competition over neurons. Smaller models allocate their neurons to high-frequency or low-complexity tasks, so their solutions perform poorly on rare and complex tasks **even when the architecture can express the desired task**. The bottleneck is not capacity in the parameter-count sense; it is *gradient interference*. Larger models allocate enough resources to common tasks that the gradient updates for those common tasks become small in magnitude, which means rare-task features accumulate without being overwritten. Validated on a synthetic mixture-of-tasks setup with monotonic scaling curves, then end-to-end with OLMo pretraining from 4M to 4B parameters on novel tasks of varying frequency and complexity. Larger OLMo models learn the infrequent and complex tasks and exhibit measurably less gradient interference and richer task-feature representations.

## Why this matters for Tier 1

Scaling laws are normally framed as "more parameters → lower loss." This paper recasts the right-hand side: larger models reduce *interference*, not just increase fit. The implication is operational. **You cannot fix rare-task underperformance with more data, only with bigger models or with interference-reducing tricks** (sparse mixtures, MoE expert routing, gradient masking). This is the most useful theoretical result for production training mixture design in months.

The interference framing also explains a long-running puzzle: why do small models trained on long-tail data sometimes do *worse* than the same model trained on a balanced mix? Because the long-tail-task gradients are dominated by the head, gradient interference is maxed out, and rare features never consolidate. The remedy is either size up or actively suppress head gradients (which is what MoE routing achieves implicitly when experts specialize).

## Connection to today's other papers

This pairs directly with **How LoRA Remembers** (2026-05-29, the paper that derived the Parametric Memory Law and identified a 0.5-probability phase transition for token-level verbatim recall). The Memory Law lives at *finetuning recall* time; Why Larger Models Learn More lives at *pretraining capacity* time. Both end with the same operational claim: gradient is the scarce resource, and you fix model behavior by sending more gradient to the tokens or tasks that need it. The MoE literature converges from a third angle (route expert capacity by task).

## Connections to prior wiki

- **TIP** (2026-04-16, token-importance on-policy distillation): the per-token, on-policy version. Most tokens carry no signal; rare tokens carry most of it.
- **LongAct** (2026-04-18, long-context gradient signal in first 5 percent of tokens): the length-axis version.
- **Nemotron3 Super hybrid MoE** (2026-04-21): an architectural cure for the same interference problem. Capacity-interference theory predicts MoE wins where rare-task capacity matters most.
- **C2 rubric reward modeling** (2026-04-18) + **TempO test-time training** (2026-04-22): the rare-task-loss-recovery side.
- **Compliance vs sensibility reasoning controllability** (2026-05-02): tasks that "exist in the model but are not surfaced" — capacity interference is one mechanism by which that happens.

## Research angle

The synthetic mixture-of-tasks framework is the right tool. Open empirical questions:
1. Does activation sparsity (MoE) measurably reduce the interference signature versus dense pretraining at matched parameter count? The paper hints yes but a head-to-head was not done.
2. At what frequency × complexity grid cell does interference start to dominate? If it can be characterized empirically, you can predict in advance which long-tail tasks your training mix will fail to capture.
3. Are reasoning-chain tasks (math, code) "rare-and-complex" in this framing? If so, the theory predicts that small models will hit a wall on reasoning even with optimal data — which matches the empirical pattern of reasoning emerging only at 7B+.
