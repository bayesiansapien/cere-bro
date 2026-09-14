# Benchmark Radar: a living database and search engine for AI benchmarks

**arXiv:** [2609.11115](https://arxiv.org/abs/2609.11115) · **HF Daily Papers:** [page](https://huggingface.co/papers/2609.11115) · **Date:** 2026-09-14
**Raw:** [farmer file](../../raw/huggingface/2026-09-14-benchmark-radar-a-living-database-and-search-engine-for-ai-b.md)

## TL;DR

Benchmark Radar is infrastructure rather than a method: a continuously updated, searchable catalog of AI benchmarks that also tracks **where each benchmark was used and what was scored on it**. Daily discovery runs across 37 sources (13 direct connectors plus 24 first-party research and engineering feeds), pulling in benchmark papers, repositories, datasets and releases. The catalog holds **1,283 source records drawn from 4 benchmark catalogs and 12,916 numeric score observations across 790 records**, alongside mentions in model cards and technical reports and per-benchmark score histories. It keeps source identities and citations attached so a reader can inspect the evidence behind a number rather than taking it on faith. Shipped artifacts: a web dashboard with a leaderboard, a Pareto view of score against measured usage, saturation and trend views, daily feeds, downloadable evidence, and a CLI for offline queries.

## Why it matters more than a benchmark paper usually does

The two analyses the authors run on their own catalog are the point. **Benchmark saturation** (how many benchmarks have ceilinged) and **adoption trends** (which ones are actually used versus merely published) are both questions the field discusses constantly and measures almost never. The Pareto view of score against *measured use* is the useful primitive: it separates benchmarks that are hard from benchmarks that are merely obscure.

The honesty about **the limits of score comparison** matters too. Reported scores are conditioned on prompt format, decoding settings, harness, few-shot count and evaluation code version, and cross-paper comparison silently assumes those match. Retaining source identity and citation is what makes that auditable.

## How this relates to what the wiki already knows

**It is the tooling answer to a measurement problem this wiki has named repeatedly.** The [agent benchmarks page](agent-benchmarks.md) has recorded that agentic evaluations are harness-dependent, most sharply in [Raschka's 09-10 observation](../llms-foundation-models/2026-09-10-raschka-looped-transformers-recurrent-depth.md) that models are tuned against one primary harness so cross-model agent scores are not comparable. Benchmark Radar does not fix that, but it makes the conditions visible, which is the precondition for fixing it.

**It also lands on the verification gap that today's other sources named independently.** The [route-by-task piece (09-14)](../ai-routing/2026-09-14-route-by-task-open-vs-frontier.md) cites an August 2026 Morph analysis finding that essentially all open-model benchmark scores are vendor self-reported, with none of the tracked SWE-bench Verified entries independently verified. A catalog that carries the citation and the score history alongside every number is exactly the instrument that claim calls for. **A benchmark index and a verification gap arriving in the same day's sources is not coincidence; it is the field noticing that its scoreboard is unaudited.**

## Gaps

Coverage is a function of the 37 sources, and the abstract does not report recall against any independent list of benchmarks, so it is unknown what fraction of the space the catalog sees. 12,916 numeric observations across 790 records averages about 16 scores per benchmark, which is thin for trend analysis on any individual one. And a living database's value depends entirely on whether it stays live, which no paper can establish.

## Related pages

- [Agent benchmarks](agent-benchmarks.md)
- [Agent harness engineering](agent-harness-engineering.md)
