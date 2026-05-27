# DarkForest: Controlled-Communication Multi-Agent Coordination

**Source:** HuggingFace daily papers (2026-05-27, 1 upvote) · arxiv 2605.25188
**arxiv:** [2605.25188](https://arxiv.org/abs/2605.25188)
**Date:** 2026-05-27
**Raw:** [raw/huggingface/2026-05-27-darkforest-less-talk-higher-accuracy-for-multi-agent-llms.md](../../raw/huggingface/2026-05-27-darkforest-less-talk-higher-accuracy-for-multi-agent-llms.md)
**Tier:** 2 (agentic systems, multi-agent, cost)

## TL;DR

Multi-agent LLM systems combine multiple agents' outputs to reason better, but interaction-heavy designs propagate errors (one agent adopts another's wrong reasoning, producing confident-but-wrong consensus) and run up token cost, latency, and inference bills. DarkForest keeps agents independent first (each answers without seeing others), then parses raw responses into structured candidate records, clusters semantically equivalent candidates, and estimates a calibrated belief distribution over clusters using agent reliability, confidence, parse quality, support-pattern reliability, and independence corrections. A coordinator receives only policy-permitted evidence from that belief state. On six reasoning benchmarks it improves the strongest baseline by up to 30.7% and cuts token consumption up to 6.5x versus communication-heavy baselines.

## Key points

- **Independence first, controlled exchange second.** Withholding cross-agent visibility until after independent answers prevents the error-amplification that raw response-sharing causes.
- **Belief over clusters, not raw votes.** A calibrated belief distribution (weighted by reliability, confidence, parse quality, independence corrections) replaces naive majority voting, which is what buys the accuracy gain.
- **Up to +30.7% accuracy and 6.5x fewer tokens** than communication-heavy multi-agent baselines on six reasoning benchmarks.

## Relation to prior wiki state

DarkForest is the multi-agent member of the 05-27 cost-reduction cluster, alongside CPT (share findings to search less) and AKBE (fewer redundant tool calls). The instructive contrast is with [CPT (05-27)](../inference-efficiency/2026-05-27-cpt-collaborative-parallel-thinking.md): CPT *adds* structured sharing across parallel branches to avoid redundant search, while DarkForest *limits* raw sharing across agents to avoid error propagation. Both improve the accuracy-cost frontier, which means the real variable is the *quality* of what gets shared, not the quantity. It also operationalizes the "controlled communication / governance" idea that [Scaling the Harness (05-27)](2026-05-27-scaling-the-harness.md) names as a harness bottleneck: the coordinator only sees policy-permitted evidence.

## Gaps

Reasoning benchmarks only; the belief-calibration parameters (reliability, support-pattern weights) may need per-domain tuning, and the approach assumes agent independence that genuinely diverse agents may not provide.

## Links

- [Paper](https://arxiv.org/abs/2605.25188)
- Raw: [raw/huggingface/2026-05-27-darkforest-less-talk-higher-accuracy-for-multi-agent-llms.md](../../raw/huggingface/2026-05-27-darkforest-less-talk-higher-accuracy-for-multi-agent-llms.md)
- Related: [CPT 2026-05-27](../inference-efficiency/2026-05-27-cpt-collaborative-parallel-thinking.md), [AKBE 2026-05-27](2026-05-27-akbe-knowledge-boundary-tool-use.md)
