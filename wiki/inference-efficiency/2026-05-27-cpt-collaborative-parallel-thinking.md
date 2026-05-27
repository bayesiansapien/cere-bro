# CPT: Collaborative Parallel Thinking for Efficient Test-Time Scaling

**Source:** HuggingFace daily papers (2026-05-27, 17 upvotes) · arxiv 2605.27030
**arxiv:** [2605.27030](https://arxiv.org/abs/2605.27030)
**Date:** 2026-05-27
**Raw:** [raw/huggingface/2026-05-27-share-more-search-less-collaborative-parallel-thinking-for-e.md](../../raw/huggingface/2026-05-27-share-more-search-less-collaborative-parallel-thinking-for-e.md)
**Tier:** 2 (inference efficiency, test-time scaling)

## TL;DR

Test-time scaling (TTS, spending extra inference compute to explore more of the solution space) usually runs parallel reasoning branches in isolation, so each branch privately rediscovers things other branches already found, wasting search steps. CPT (Collaborative Parallel Thinking) is a training-free framework that lets branches share discoveries during search: it extracts compact intermediate findings from ongoing branches, keeps a deduplicated query-level information pool, and broadcasts pool entries back through each branch's input context so later steps reuse what others found instead of re-deriving it. On HMMT and AIME (hard math benchmarks), CPT sets a better accuracy-latency Pareto frontier than strong baselines across rollout budgets and model scales.

```
Isolated parallel TTS:              CPT (search-time sharing):
  branch A ─┐                        branch A ─┐ extract findings
  branch B ─┤ each rediscovers        branch B ─┤──► dedup info pool ──► broadcast
  branch C ─┘ same facts              branch C ─┘    back into each branch's context
  ⇒ redundant exploration            ⇒ less re-search, better accuracy/latency
```

## Key points

- **Information isolation is the waste.** Branch-private intermediate discoveries force redundant exploration; sharing them shortens the search needed to assemble complete decision information.
- **Training-free.** CPT operates at inference via context broadcasting and a deduplicated pool, so it drops onto existing models without retraining.
- **Better accuracy-latency Pareto** than strong parallel-TTS baselines on HMMT and AIME, across rollout budgets and model scales.

## Relation to prior wiki state

CPT is a cost-efficiency result and pairs with the day's cost cluster. Where [How Do AI Agents Spend Your Money (05-27)](../agentic-systems/2026-05-27-agent-token-consumption.md) showed that accuracy peaks at intermediate token spend and naive "think longer" is wasteful, CPT is a concrete mechanism for getting more accuracy per token by removing redundant re-exploration. It is also the parallel-reasoning analogue of [DarkForest (05-27)](../agentic-systems/2026-05-27-darkforest-controlled-communication-multi-agent.md), which cuts multi-agent communication to reduce token cost 6.5x: both attack the cost of agents/branches talking, but from opposite directions, DarkForest by *limiting* raw exchange to avoid error propagation, CPT by *adding* structured exchange to avoid redundant search. The tension between them (when does sharing help versus hurt?) is the open question. Conceptually CPT continues the wiki's "allocate compute proportionally to information density" theme: don't spend search steps on information already discovered.

## Why it matters

TTS is now standard in reasoning models, and parallel rollouts are expensive. A training-free way to improve the accuracy-latency frontier ships immediately into reasoning-model serving. The result also reframes parallel TTS as a coordination problem, not just a sampling problem.

## Gaps

Evaluated on math (HMMT, AIME) where intermediate findings are cleanly extractable; whether compact-finding extraction and deduplication work on open-ended or multi-modal reasoning, where "a discovery" is fuzzier, is untested.

## Links

- [Paper](https://arxiv.org/abs/2605.27030)
- Raw: [raw/huggingface/2026-05-27-share-more-search-less-collaborative-parallel-thinking-for-e.md](../../raw/huggingface/2026-05-27-share-more-search-less-collaborative-parallel-thinking-for-e.md)
- Related: [How Do AI Agents Spend Your Money 2026-05-27](../agentic-systems/2026-05-27-agent-token-consumption.md), [DarkForest 2026-05-27](../agentic-systems/2026-05-27-darkforest-controlled-communication-multi-agent.md)
