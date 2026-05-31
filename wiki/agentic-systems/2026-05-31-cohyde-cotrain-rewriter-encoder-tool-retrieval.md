# CoHyDE: Iterative Co-Training of LLM Rewriter and Dense Encoder for Tool Retrieval

**arXiv:** [2605.29271](https://arxiv.org/abs/2605.29271) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.29271) · **Date:** 2026-05-31
**Raw:** [farmer file](../../raw/huggingface/2026-05-31-cohyde-iterative-co-training-of-llm-rewriter-dense-encoder-f.md)

## TL;DR

Tool retrieval (picking the right API from a large catalog for an agent's query) fails at a vocabulary mismatch: users write colloquial, underspecified queries while the catalog speaks technical API language. The two standard fixes break in opposite directions. A contrastively fine-tuned dense encoder nails queries whose surface form already matches the catalog but collapses when it does not. HyDE-style query expansion (have a frozen LLM hallucinate a hypothetical API description, then retrieve against that) is robust to vague queries but, because the LLM is catalog-unaware, generates descriptions that hurt retrieval when the query was already well-formed. CoHyDE trains the encoder and the rewriter as a single co-evolving system: the encoder is retrained with InfoNCE on the rewriter's catalog-style hypothetical descriptions, while the rewriter is preference-aligned via DPO against the encoder's own retrieval scores, both warm-started on the catalog first. On a ~10k-tool ToolBench subset, three co-training rounds beat the strongest single-component baseline by +2.5 pp NDCG@5 on standard queries and +6.3 pp on held-out vague queries (up to +8 pp on the hardest vague tier). Ablations confirm co-training is the load-bearing ingredient: either component alone loses by up to 8 pp on vague queries.

## The mechanism

```
Standard encoder fine-tune : great on surface-matching queries, COLLAPSES on vague ones
Frozen-LLM HyDE expansion  : robust to vague queries, HURTS well-formed ones (catalog-unaware)

CoHyDE (co-evolving loop, both warm-started on the catalog):
   ┌──────────────────────────────────────────────┐
   │  rewriter ──► catalog-style hypothetical desc  │
   │      ▲                     │                   │
   │ DPO against                ▼                   │
   │ retrieval scores    encoder retrains (InfoNCE  │
   │      │               on the rewriter's output) │
   │      └─────────── retrieval scores ◄───────────┘
   └──────────── repeat × 3 rounds ─────────────────┘
```

## What problem it solves

As agent tool catalogs grow into the thousands of APIs, retrieval becomes the bottleneck that decides whether the agent even sees the right tool. The colloquial-query-versus-technical-catalog gap is exactly where retrievers fail, and the field's two tools for it (encoder fine-tuning, HyDE expansion) each fix one half of the query distribution while breaking the other. CoHyDE makes the two halves cooperate instead of trading off.

## Core novelty

Treating the rewriter and the encoder as one jointly-trained system with a closed feedback loop, rather than bolting a frozen LLM onto a fixed encoder. The encoder learns to embed the *kind* of catalog-style hypotheticals the rewriter produces; the rewriter learns, via DPO against the encoder's retrieval scores, to produce hypotheticals the encoder can actually use. Warm-starting both on the catalog before the loop begins is what keeps the co-evolution from drifting.

## Key takeaways

- Co-training closes the encoder-vs-HyDE tradeoff: **+2.5 pp NDCG@5 on standard queries, +6.3 pp on held-out vague queries** over the strongest single-component baseline.
- Up to **+8 pp on the hardest vague tier**, the regime where both base methods are weakest.
- Ablations: either component in isolation loses by up to 8 pp on vague queries, so **co-training, not the parts, is the ingredient**.
- Mechanism: encoder retrained with InfoNCE on rewriter output; rewriter DPO-aligned against encoder retrieval scores; three rounds on a ~10k ToolBench subset.

## Gaps in the study

Evaluated on one ~10k-tool ToolBench subset; whether the co-training stability holds on catalogs an order of magnitude larger (where the rewriter's hypotheticals could drift faster than the encoder adapts) is untested. The loop runs three rounds, with no analysis of when or whether it converges versus oscillates. Latency and training cost of the co-evolution versus a one-shot encoder fine-tune are not reported, which matters for whether this is deployable or just an offline accuracy win.

## Relation to prior wiki state

CoHyDE sits in the tool-calling thread (see the [tool-calling concept page](tool-calling.md)) and is a retrieval-side complement to the wiki's agent-efficiency work. It shares a structural shape with several recent papers: a cheap component and an expensive component trained to cooperate rather than stacked. PANDO (05-30) routed across an online-distilled skill library; CollectionLoRA (today) distills many teacher LoRAs into one via dual-stream routing; CoHyDE co-trains a rewriter and an encoder. All three reject the "freeze one, tune the other" default in favor of joint adaptation. The vague-query robustness gain is also the retrieval analog of the recurring theme that the hard cases (underspecified queries, rare entities, sub-threshold tokens) are where the real signal-design work lives, the same instinct behind CorVer's focus on rare-entity facts and the LoRA Parametric Memory Law's focus on sub-threshold tokens.

## Research angle

The open question is whether the co-trained rewriter generalizes its catalog-awareness across catalogs, or overfits to the one it trained on. If a CoHyDE rewriter trained on ToolBench transfers zero-shot to a fresh API catalog, the loop has learned a general "how to write catalog-style hypotheticals" skill and tool retrieval becomes a solved-once problem; if it must be re-run per catalog, the training cost (unreported here) becomes the deciding factor for production use. A second angle: the DPO-against-retrieval-scores signal is a self-generated reward, which inherits the reward-hacking risk the RL pages flag, the rewriter could learn to produce hypotheticals that game the encoder's scores without improving true retrieval, and an adversarial probe of that failure mode is the natural robustness check.

## Links

- [arXiv 2605.29271](https://arxiv.org/abs/2605.29271)
- [Tool-calling concept page](tool-calling.md)
- [PANDO online skill distillation (05-30)](2026-05-30-pando-online-skill-distillation.md)
