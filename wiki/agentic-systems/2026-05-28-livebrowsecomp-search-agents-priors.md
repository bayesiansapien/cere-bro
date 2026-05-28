# LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28721](https://arxiv.org/abs/2605.28721) · [HuggingFace](https://huggingface.co/papers/2605.28721) · [raw](../../raw/huggingface/2026-05-28-livebrowsecomp-are-search-agents-searching-or-just-verifying.md) · [dataset](https://huggingface.co/datasets/Forival/LiveBrowseComp)

## TL;DR

LLM search agents do not actually search the web most of the time. They use the web to verify what they already know. On BrowseComp, agents answer up to 44.5% of questions correctly with no tools at all; more than half of their search queries are generated from internally produced hypotheses rather than retrieved leads; and when answer-supporting evidence is removed from the index, agents perform worse than the closed-book baseline. The authors call this Intrinsic Knowledge Dependence (IKD). LiveBrowseComp is a new benchmark of 335 human-authored questions whose answers depend on facts published within 90 days before benchmark construction, drawn from six updated sources, filtered to exclude globally salient events. On LiveBrowseComp, every evaluated agent scores below 2% closed-book, search-augmented scores drop by 25-40 points relative to BrowseComp, and prior model rankings stop predicting performance.

```
BrowseComp (static benchmark):
  agent answer ────► [intrinsic knowledge: 44.5%]
                    │                         │
                    └──► [verification search]┘  ← agent uses web as a fact-check
                          most queries come from internal hypotheses

LiveBrowseComp (90-day fresh facts):
  agent answer ────► [intrinsic knowledge: <2%]
                          │
                          └──► [must genuinely search]
                                 25-40pp drop, ranking inversion
```

## Key findings

- Up to 44.5% of BrowseComp questions are answerable without tools, so high scores conflate memorization with retrieval.
- More than half of generated search queries come from internally produced hypotheses, not retrieved leads.
- Removing answer-supporting evidence makes search-augmented agents perform worse than closed-book agents — strong evidence that retrieval is being used to confirm rather than discover.
- On LiveBrowseComp (fresh 90-day facts), all agents fall under 2% closed-book accuracy and 25-40pp lower with search than they scored on BrowseComp.
- The previously stable model rankings on BrowseComp invert on LiveBrowseComp, so leaderboard position was reflecting training-cutoff coverage as much as search ability.

## How this fits prior wiki state

This connects directly to the eval-rigor cluster that has been forming: AI Research Agents Narrow Scientific Exploration (today, same finding from a different angle — agents recombine the prior they have rather than venturing out), Chartographer (today — VLMs fail counterfactual charts they previously solved), HRBench (today — switching strategies have different effectiveness regimes), and back to ITBench-AA (yesterday, frontier models <50% on enterprise IT tasks). A pattern is now established: static benchmarks have been overstating capability across at least four distinct task types this week (browse, chart QA, reasoning-mode switching, enterprise IT). The mechanism is the same in all cases — the benchmark reuses inputs the model has effectively memorized, and "with tools" inflates the score by giving the model a way to re-derive the answer it already had.

This also retroactively explains a result on yesterday's How Do AI Agents Spend Your Money study: that paper found accuracy peaks at intermediate token cost. If a chunk of test items are answerable from priors, extra search rounds just add noise.

## Related pages

- [[2026-05-28-ai-research-agents-narrow-exploration]] — same memorization-vs-search frame, ideation side
- [[2026-05-27-agent-token-consumption]] — accuracy peaking at intermediate cost
- [[2026-04-18-dr3-eval-deep-research-benchmark]] — deep-research evaluation rigor
- [[agent-benchmarks]] — concept page

## Research angle

The 25-40pp drop combined with the ranking inversion is a serious result for any production retrieval system tuned on BrowseComp-style benchmarks. The follow-up that matters: how much of the "with-search" gain on standard benchmarks is verification vs discovery, decomposed per model. If the verification share is ≥50% for the top models, then "search agent capability" as currently reported is mostly a training-data-cutoff variable rather than a retrieval-skill variable. That would imply a clean direction for designing search-specific RL signals that reward evidence-grounded answers over hypothesis-confirming ones.
