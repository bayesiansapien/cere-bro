# Forecasting Downstream Performance of LLMs With Proxy Metrics

**Source:** HuggingFace daily papers, 2026-05-23.
**arxiv:** [2605.18607](https://arxiv.org/abs/2605.18607)

## TL;DR

Model-development decisions (which architecture, which corpus, which recipe) require reliable performance forecasts, but cross-entropy loss is poorly aligned with downstream capabilities and direct downstream evaluation is expensive and sparse. This paper proposes proxy metrics: aggregate token-level statistics (entropy, top-k accuracy, expert token rank) from the candidate model's next-token distribution over expert-written solutions. Across three settings, the proxies consistently outperform loss-based and compute-based baselines. (1) For cross-family model selection, they rank a heterogeneous population of reasoning models with Spearman ρ=0.81 (vs ρ=0.36 for cross-entropy loss). (2) For pretraining data selection, they reliably rank 25 candidate corpora at roughly 10,000x less compute than direct evaluation. (3) For training-time forecasting, they extrapolate downstream accuracy across an 18x compute horizon with roughly half the error of existing alternatives.

## Why this matters

This is one of the most consequential papers on model-development methodology this quarter. The bottleneck in scaling-law-driven research has been that loss does not predict capability. Teams have been running expensive downstream evaluations at multiple checkpoints because they cannot trust loss. This paper proposes that the right proxy is the model's next-token distribution *evaluated on expert trajectories*, which captures what cross-entropy loss collapses.

The 0.81 vs 0.36 Spearman correlation on cross-family ranking is the strongest result. Loss-based ranking essentially does not work across model families; the proxy works. The 10,000x compute reduction for pretraining data selection is the second-strongest: if you can rank 25 candidate corpora at 1/10,000 the cost of direct evaluation, every pretraining team should be using this proxy as their primary selection signal.

## Connections to prior wiki state

This is the empirical complement to [today's Same Architecture, Different Capacity paper (2605.21803)](../llms-foundation-models/2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md). The spectral-scaling paper showed that loss collapses representational geometry: two models with the same loss can have very different effective capacity. The proxy-metrics paper provides the practical exit: don't use loss for model selection, use proxy statistics that preserve more of the representational signal.

Together they form a complete argument. (a) Loss is the wrong scalar (spectral paper). (b) Here is the right alternative (proxy paper). The fact that both landed the same day is either coincidence or a sign of community convergence on the same diagnosis from theoretical and practical directions.

## Gaps

Proxies require expert-written solutions. For domains without authoritative reference solutions (creative writing, open-ended dialogue), the method does not apply directly. The "expert trajectories" framing also assumes that the expert is universally correct, which is a strong assumption in research domains where the right answer is contested.

The 18x compute extrapolation is at training time. Whether the proxies remain reliable for extrapolating to *much* longer training runs (100x, 1000x compute) is the open question. Scaling laws are most useful at the frontier; if the proxy is only reliable within an 18x range, it does not help the largest-scale forecasting problem.

## Industrial implication

Every team running ablations on pretraining data, architecture variants, or training recipes should consider adopting this proxy. 10,000x compute reduction on corpus ranking is a transformative budget reduction. The catch is that the proxies require expert reference solutions in the target domain, which limits adoption to domains where high-quality references exist.

## Research angle

The cleanest open question: which token-level statistics matter most, and can they be predicted from cheaper signals? The paper aggregates entropy, top-k accuracy, and expert token rank. If one of these is doing most of the work, the method can be simplified. If they are complementary, that gives a principled basis for designing more proxies.

A deeper question: do the proxies measure capability or do they measure alignment-with-expert-style? A model that solves problems correctly but in a different style than the reference might score poorly on the proxy. Untangling these is critical before this becomes the field's standard selection metric.

## Raw source

[raw/huggingface/2026-05-23-forecasting-downstream-performance-of-llms-with-proxy-metric.md](../../raw/huggingface/2026-05-23-forecasting-downstream-performance-of-llms-with-proxy-metric.md)
