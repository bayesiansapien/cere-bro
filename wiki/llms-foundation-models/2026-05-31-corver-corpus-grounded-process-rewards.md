# CorVer: Verifiable Rewards Beyond Math and Code via Corpus-Grounded Process Supervision

**arXiv:** [2605.29648](https://arxiv.org/abs/2605.29648) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.29648) · **Date:** 2026-05-31
**Raw:** [farmer file](../../raw/huggingface/2026-05-31-verifiable-rewards-beyond-math-and-code-lightweight-corpus-g.md)

## TL;DR

RLVR (reinforcement learning with verifiable rewards) works beautifully on math and code because correctness is mechanically checkable, but factual question answering has no such checker. Response-level rewards are too coarse to tell which sentence in a reasoning trace is wrong, and sentence-level alternatives lean on NLI models, LLM judges, or knowledge-verification pipelines that are expensive to run at RL scale and especially unreliable for rare-entity facts, which is exactly where you need the signal most. CorVer (Corpus Verify) replaces the neural verifier with a corpus-grounded statistic: it scores each generated sentence using Wikipedia co-occurrence statistics, assigns sentence-level credit, and maps that to token-level advantages through a simple alignment. It needs only a 0.5B extractor plus one corpus lookup per sentence. Across 30 (model, benchmark) cells spanning six instruction-tuned models from 3B to 14B and five QA benchmarks, CorVer improves over the raw baseline in every cell (average +4.1 pp on TriviaQA) and beats four neural-verifier baselines in 18 of 20 feasible cells while training 4.8 to 8.4x faster.

## The mechanism

```
Prior fine-grained reward (expensive):
  reasoning trace ─► [NLI verifier / LLM judge / KB pipeline] ─► sentence rewards
                      └ slow, unreliable on rare entities, costly at RL scale ┘

CorVer (corpus-grounded, cheap):
  reasoning trace
     │  split into sentences
     ▼
  0.5B extractor pulls entities/facts per sentence
     │
     ▼
  Wikipedia co-occurrence lookup ─► sentence-level credit score
     │  (one corpus lookup per sentence, no neural verifier)
     ▼
  simple alignment ─► token-level advantages ─► RL update
```

## What problem it solves

Extending RLVR past the math/code island is the open frontier of verifiable-reward RL, and the blocker has been the verifier: anything accurate enough to grade factual claims (an NLI model, an LLM judge, a retrieval-and-check pipeline) is too slow and too costly to call on every sentence of every rollout, and these verifiers degrade precisely on rare-entity facts where ground truth is sparse. CorVer removes the neural verifier from the hot loop entirely, replacing it with a corpus-statistics lookup that is cheap, deterministic, and does not itself need to be trained or trusted as a model.

## Core novelty

The reward signal is a corpus co-occurrence statistic rather than a learned model. Co-occurrence in Wikipedia is a proxy for "this combination of entities and claims is consistent with the world's recorded facts," and it is computable with a single lookup. The pipeline is deliberately lightweight (a 0.5B extractor plus the lookup), which is what makes per-sentence process supervision affordable at RL scale. The sentence-to-token advantage alignment then lets a coarse, sentence-level signal drive standard token-level policy optimization.

## Key takeaways

- Corpus co-occurrence replaces neural verifiers for sentence-level factual reward; only a **0.5B extractor + one lookup per sentence** is needed.
- Improves over the raw baseline in **all 30 (model, benchmark) cells**; average **+4.1 pp on TriviaQA**.
- Beats four neural-verifier baselines in **18 of 20** feasible cells while training **4.8–8.4x faster**.
- Targets the rare-entity regime where NLI/LLM-judge verifiers are least reliable.

## Gaps in the study

Wikipedia co-occurrence is a popularity-and-coverage signal, so it should be weakest exactly on the long-tail and very recent facts that fall outside the dump, the same blind spot The Decoder's LiveBrowseComp coverage (05-31) flagged when it found search agents fall back on training-time memory once asked about events from the last 90 days. Co-occurrence rewards correlation, not truth, so a fluent but subtly wrong claim that pairs commonly-co-occurring entities could be over-rewarded (a reward-hacking surface the paper does not stress-test). Evaluation is on five QA benchmarks; whether the signal transfers to multi-hop reasoning or open-ended long-form factual generation is untested.

## Relation to prior wiki state

CorVer is the latest move in the "push RLVR past math and code" program the rl-for-llms page has been tracking, and it attacks the cost axis specifically. The verifier-cost problem is a recurring theme: NeMo-RL speculative decoding (04-30) attacked the rollout-generation cost of RL; CorVer attacks the reward-evaluation cost. It is also the factual-domain counterpart to RUBRIC-ARROW (today), which builds cheap pointwise rewards for *non-verifiable* subjective domains by training a rubric generator and judge from pairwise data: the two papers split the post-math/code reward-design space into "factually checkable against a corpus" (CorVer) and "subjective, judged against rubrics" (RUBRIC-ARROW). The reward-hacking caveat connects directly to Kurate cs.LG #12 this week, "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking," and to the wiki's 05-13 Reward-Hacking-in-Rubrics finding: any cheap proxy reward invites the policy to optimize the proxy rather than the target, and a co-occurrence statistic is a particularly gameable proxy.

## Research angle

The decisive test is adversarial: construct factual claims that maximize Wikipedia co-occurrence while being false (plausible entity pairings, common-but-wrong attributions) and measure how fast a policy trained under CorVer learns to exploit them. If the co-occurrence reward is robust to this, it is a genuinely cheap verifier for the head of the factual distribution; if it collapses, CorVer needs a truthfulness correction layered on top, and the interesting design question becomes how to combine a cheap corpus prior with an occasional expensive verifier call (a routing problem: spend the costly NLI judge only on sentences where the cheap co-occurrence signal is ambiguous). That hybrid, cheap-prior-plus-selective-expensive-check, is the natural next paper and mirrors the cache-budget and confidence-routing patterns appearing across the efficiency literature.

## Links

- [arXiv 2605.29648](https://arxiv.org/abs/2605.29648)
- [RL for LLMs concept page](rl-for-llms.md)
- [Speculative decoding for RL rollouts (04-30)](../inference-efficiency/2026-04-30-speculative-decoding-rl-rollouts.md)
