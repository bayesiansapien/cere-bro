# Forecasting Downstream Performance of LLMs With Proxy Metrics

**Source:** HuggingFace daily papers, 2026-05-23.
**arxiv:** [2605.18607](https://arxiv.org/abs/2605.18607)

## TL;DR

The two signals labs use to compare model candidates (cross-entropy loss; direct downstream evaluation) are both broken. Loss is poorly aligned with downstream capability; direct eval is expensive, sparse, and uninformative at early training. This paper builds proxy metrics by aggregating token-level statistics (entropy, top-k accuracy, expert token rank) from a candidate model's next-token distribution over expert-written solutions. Three settings:
1. **Cross-family model selection**: mean Spearman ρ = 0.81 (loss baseline: 0.36).
2. **Pretraining data selection**: rank 25 candidate corpora at ~10,000x less compute than direct evaluation.
3. **Training-time forecasting**: extrapolate downstream accuracy across an 18x compute horizon at roughly half the error of existing alternatives.

## Why this matters

The wiki has tracked the scaling-decision problem since the 04-17 "Model Capability Dominates Inference-Time Optimization" paper. That paper said the model's intrinsic capability ceiling matters more than inference-time tricks. This paper gives the inverse: a cheap way to estimate that ceiling without finishing training. If proxy metrics are 10,000x cheaper than direct eval and rank corpora correctly, the data-selection bottleneck dissolves. That is the bottleneck behind why open-weight labs lag closed: data selection is expensive, and only labs with budget for it converge fast.

The Spearman 0.81 vs 0.36 result is the headline. Loss-based ranking of heterogeneous models is barely better than random when comparing reasoning models trained with different recipes. Expert-trajectory proxy metrics restore meaningful ranking.

## Connections to prior wiki state

Companion to the [optimizer-induced spectral scaling laws paper (today)](2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md): both papers argue loss is a misleading scalar. The spectral paper says loss-matched configurations have different representation geometry; this paper says loss-ranked configurations have wrong downstream ranking. Together they erode the central assumption of the past five years of scaling research — that validation loss is the right north star.

Also relates to the [Bitter Lesson for Data Filtering (Kurate cs.LG #12, 2026-05-19)](../) — which argued data filtering recipes are over-engineered relative to scale. This paper says even cheap proxy metrics get pretraining-corpus ranking right, which lowers the cost of filtering decisions further.

## Gaps

The proxies depend on expert-written solutions being available. For frontier capabilities where expert-written solutions are themselves hard to construct (open-ended reasoning, AIME-level math, frontier research code), the proxy reduces to "compare next-token agreement with a small set of known-good completions." Robustness of the ranking when the expert set is small or noisy is the open question.

## Research angle

If proxy metrics replace direct eval for early-stage data selection, the cost structure of frontier-model development changes. The implicit assumption that data filtering needs frontier-scale compute to validate is wrong; you can validate at 10,000x less compute and only spend the big budget after the data is right. This is the kind of methodological shift that compounds: every lab that adopts proxy metrics gets a quarterly speedup in the experimentation loop.

## Raw source

[raw/huggingface/2026-05-23-forecasting-downstream-performance-of-llms-with-proxy-metric.md](../../raw/huggingface/2026-05-23-forecasting-downstream-performance-of-llms-with-proxy-metric.md)
