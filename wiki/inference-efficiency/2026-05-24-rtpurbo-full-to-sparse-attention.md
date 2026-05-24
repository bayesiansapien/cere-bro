# Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps (RTPurbo)

**Source:** HuggingFace daily papers, [arXiv 2605.16928](https://arxiv.org/abs/2605.16928). Nanjing University, Alibaba Group.
**Date:** 2026-05-24
**Tier:** 1 (sparse attention, long-context)

## TL;DR

RTPurbo argues that full-attention LLMs are already intrinsically sparse, and the transformation into highly sparse models needs only a few hundred training steps rather than expensive native sparse pretraining. Three observations carry the paper. First, only a small subset of attention heads truly requires full long-context processing; the rest can operate on a restricted window. Second, long-range retrieval is governed primarily by a low-dimensional subspace, so relevant tokens can be retrieved with a 16-dimensional indexer rather than a full-rank similarity check. Third, the useful token budget is strongly query-dependent, which makes dynamic top-p selection a strictly better fit than fixed top-k. The implementation retains the full KV cache only for retrieval heads and adds a lightweight token indexer for sparse attention. The result is up to 9.36x prefill speedup at 1M context and roughly 2.01x decode speedup, with near-lossless accuracy on long-context benchmarks and reasoning tasks.

## Key findings

- Full attention models are already sparse; the question is how to expose that sparsity cheaply at inference time.
- Head-level differentiation is real. A small fraction of heads carry the long-range retrieval load; the rest are local. A method that does not exploit this is leaving compute on the floor.
- A 16-dimensional indexer suffices for long-range token retrieval. This is the strongest claim of the paper because it implies the long-context retrieval problem is fundamentally low-dimensional inside the trained weights.
- Dynamic top-p outperforms fixed top-k because the useful token budget varies per query. Static budgets either over-allocate or starve.
- A hundred training steps is enough adaptation. The model is doing the work; the post-training is just exposing it.

## Why this matters

This paper is the strongest statement yet that the trade-off between full-attention pretraining and sparse-attention efficiency is illusory. The wiki has tracked two camps for months: native sparse pretraining (Kimi Delta Attention, DeepSeek Sparse Attention) and inference-time eviction or sparsification (Minference, Quest, SnapKV, RazorAttention, Make-Each-Token-Count). The shared assumption was that you choose one. RTPurbo says you can pretrain full and convert to sparse in hundred-steps post-training, which dominates both endpoints: the pretraining recipe stays standard, the inference cost matches native-sparse.

The 16-dimensional retrieval-subspace finding is the load-bearing claim for downstream research. It says the geometry of long-context retrieval, learned implicitly during full-attention pretraining, lives in a tiny subspace of the key embeddings. That subspace is the right object to study. If it generalizes across model families, the indexer can be shipped as a standalone artifact reusable across many models.

This is also the paper that most directly couples to the optimizer-spectral story from yesterday's digest. The spectral paper (2026-05-23 Same Architecture, Different Capacity, the paper that showed Muon achieves linear hard-rank scaling β=1.02 versus AdamW's β=0.44 on rare-token representations) argued that optimizer choice determines how much representational capacity gets used. RTPurbo argues that the capacity that gets used is itself low-dimensional. Together: capacity is a function of optimizer, and useful capacity sits in a small subspace. The two findings constrain each other.

## Research angle

The most direct follow-up is to study whether the 16-dimensional retrieval subspace is shared across full-attention models from different families (Llama, Qwen, DeepSeek). If yes, the indexer is a portable artifact: train it once on any full-attention model, reuse it on any other. If the subspace is model-specific, RTPurbo's hundred-step recipe still works but the savings do not amortize across deployments.

A second question: does the head-level head-of-heads selection survive the optimizer-spectral lens? If Muon-trained models have larger usable spectral capacity, the fraction of heads needed for long-range retrieval might shift. If RTPurbo's "small subset of heads" is universal across optimizers, the optimizer-spectral effect lives outside this dimension; if not, it constrains how RTPurbo's recipe should be tuned per training run.

## Related

- [KV Cache](kv-cache.md) — concept page; native-sparse vs full-attention conversion is now a tracked axis.
- [MISA (2026-05-11)](kv-cache.md#key-papers) — head-axis sparse routing; RTPurbo's "small subset of heads needs full context" is the closest precedent.
- [Make-Each-Token-Count (2026-05-12)](2026-05-12-make-each-token-count-kv-eviction.md) — learned KV eviction that surpasses full-cache; same flavor of "sparse can beat dense".
- [Same Architecture Different Capacity (2026-05-23)](../llms-foundation-models/2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md) — optimizer-spectral paper that constrains RTPurbo's "intrinsic sparsity" claim.

## Raw source

[`raw/huggingface/2026-05-24-full-attention-strikes-back-transferring-full-attention-into.md`](../../raw/huggingface/2026-05-24-full-attention-strikes-back-transferring-full-attention-into.md)
