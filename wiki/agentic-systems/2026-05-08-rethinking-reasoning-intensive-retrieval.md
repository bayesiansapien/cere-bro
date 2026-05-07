# Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems

**arXiv:** [2605.04018](https://arxiv.org/abs/2605.04018)
**Authors:** Yilun Zhao, Jinbiao Wei, Tingyu Song, Arman Cohan (Yale NLP Lab); Siyue Zhang (NUS); Chen Zhao (NYU Shanghai)
**Tier:** 2 — agentic-systems / retrieval

## TL;DR

Argues that current retriever benchmarks (BRIGHT) evaluate retrievers in isolation rather than within the agentic-search loop they actually serve. Existing synthetic training corpora pair queries with single positive passages plus hard negatives, which encourages models to prioritize individual relevant passages over building a balanced "evidence portfolio" covering multiple reasoning aspects. Net argument: the retriever-vs-agent distinction is the wrong frame for benchmark and training design.

## The two gaps the paper identifies

```
1. Evaluation gap
   ─────────────
   Current benchmarks (BRIGHT) provide limited "gold standard" evidence sets
   (1-2 sources) and evaluate retrievers in isolation.
   They cannot assess:
     - whether the retriever gathers complementary evidence across reasoning aspects
     - whether the retriever is useful within a dynamic, iterative agentic workflow

2. Training gap
   ─────────────
   Current synthetic corpora pair queries with one positive + hard negatives.
   This encourages:
     - prioritizing individual relevant passages
     - NOT developing a balanced "evidence portfolio"
   Result: retrievers look effective on single-passage metrics but fail to
   meet the comprehensive evidence needs of an LLM agent.
```

## How this relates to prior wiki work

- **Companion** to today's [OpenSearch-VL](2026-05-08-opensearch-vl-multimodal-search.md). Different geography (Yale vs Tencent/CUHK/HKU), similar critique. Both argue retrievers should be evaluated within the agent loop, not in isolation.
- **Lateral** to [BRIGHT-Pro Retriever](2026-05-07-bright-pro-rtriever-reasoning-retrieval.md) (05-07, just yesterday). BRIGHT-Pro extends BRIGHT, this paper argues BRIGHT itself is the wrong benchmark frame. Direct intellectual tension worth tracking.
- **Connects** to [agent-benchmarks concept page](agent-benchmarks.md) for the meta-claim that benchmarks need to follow the agent paradigm rather than persist from the pre-agent retrieval era.

## What's surprising

The "evidence portfolio" framing. Most retrieval research treats relevance as a per-passage property, but the paper argues that for agentic search the right unit is a *set* of complementary passages that together support multi-aspect reasoning. The implication is that the loss function used to train retrievers needs to change, not just the benchmark.

## Open questions

1. **What does the "evidence portfolio" loss look like in practice?** The paper proposes the framing but the operational training-loss form is the next step.
2. **Does this generalize to multi-modal retrieval?** OpenSearch-VL today addresses multi-modal search but doesn't use the evidence-portfolio framing. Cross-pollination would be productive.
3. **Cost of multi-passage relevance evaluation.** Single-passage relevance is cheap to label. Multi-passage portfolio relevance requires evaluators to assess complementarity, which is harder. The paper's own evaluation methodology is a falsifiable test.

## Why it matters

Plus today's [OpenSearch-VL](2026-05-08-opensearch-vl-multimodal-search.md) and [ResRL](../llms-foundation-models/2026-05-08-resrl-negative-sample-projection-rl.md), three papers in one day argue that 2026 agentic-systems work is data-and-recipe-bound rather than algorithm-bound. Different sub-areas (retrieval, multimodal search, RL training) but same structural claim.
