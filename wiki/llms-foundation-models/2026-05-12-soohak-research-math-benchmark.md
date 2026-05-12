# Soohak: Mathematician-Curated Research-Level Math Benchmark

**Date:** 2026-05-12
**Source:** HuggingFace Daily Papers
**arXiv:** [2605.09063](https://arxiv.org/abs/2605.09063)
**Tier:** 2 — Reasoning / benchmarks / evaluation

## TL;DR

A 439-problem benchmark authored from scratch by 64 mathematicians, designed to measure research-level math capability rather than olympiad-style step-by-step reasoning. Two subsets. On the **Challenge subset**, frontier models reach Gemini-3-Pro 30.4%, GPT-5 26.4%, Claude-Opus-4.5 10.4%. Open-weight leaders (Qwen3-235B, GPT-OSS-120B, Kimi-2.5) are all under 15%. On the **refusal subset**, no model exceeds 50%, identifying refusal-on-ill-posed-problems as a distinct capability target that no current model directly optimizes for. Public release deferred to late 2026 to delay contamination.

## Why it matters

After IMO gold-medal performance was reached, "olympiad accuracy" stopped being a meaningful frontier signal. Soohak is the cleanest attempt yet to ask whether frontier models can advance the frontier of mathematical knowledge itself rather than execute textbook reasoning faster. The refusal subset is the more interesting half. Research mathematicians spend large amounts of their time recognizing when a problem is ill-posed. Models that confidently produce false proofs on ill-posed problems are not just inaccurate, they are unreliable as research collaborators. No model exceeds 50% on this subset.

## How it relates to prior wiki state

- **Gowers GPT-5.5 Pro Math (2026-05-10).** Gowers reported strong informal-math performance from GPT-5.5 Pro. Soohak quantifies the headroom: 30% on a curated frontier suite is a long way from research-grade. Both readings can be true: GPT-5.5 is genuinely useful for working mathematicians, *and* there is a large gap to research-level autonomy.
- **AI Co-Mathematician (2026-05-09).** The agentic-mathematics paper from last week argued for collaboration patterns. Soohak provides the evaluation harness against which those patterns can be tested.
- **AI Scientists Produce Results Without Reasoning Scientifically (Kurate cs.AI #5).** Different domain, same diagnosis: current models output confident answers in regimes where they should refuse. Soohak's refusal subset operationalizes that critique for math.
- **PhilosophyBench (2026-05-03).** Both papers probe whether frontier models recognize the limits of their own reasoning. PhilosophyBench probes ethical divergence, Soohak probes mathematical ill-posedness. Two specific instances of a general claim: current frontier reasoning is over-confident at the meta-cognitive layer.

## Research angle

The refusal subset is the trainable surface. The standard RL post-training pipeline rewards confidence on correct answers and penalizes confident wrong answers, but does not reward calibrated abstention on ill-posed inputs. Adding ill-posed problems with abstain-as-correct labels into the post-training mix is a tractable experiment, and the prediction would be that current frontier models can be moved from ~30% on the refusal subset to >70% with relatively modest data, because the mechanism (recognize ill-posedness, output abstention) is already in the model's repertoire on other tasks. Whether that transfer holds is the empirical question worth a 90-day follow-up.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2605.09063)
- [HuggingFace page](https://huggingface.co/papers/2605.09063)
- Raw source: [raw/huggingface/2026-05-12-soohak-a-mathematician-curated-benchmark-for-evaluating-rese.md](../../raw/huggingface/2026-05-12-soohak-a-mathematician-curated-benchmark-for-evaluating-rese.md)

## Related wiki pages

- [Gowers on GPT-5.5 Pro Math](2026-05-10-gowers-gpt55-pro-math.md)
- [AI Co-Mathematician](../agentic-systems/2026-05-09-ai-co-mathematician.md)
- [PhilosophyBench: ethical divergence](2026-05-03-philosophy-bench-ethical-divergence.md)
