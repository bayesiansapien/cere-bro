# Parametric Context Internalization

**Concept.** Instead of supplying a model's context as tokens in the prompt (retrieved documents, video frames, repository snippets), *internalize* that context into the model's weights, and do it cheaply by **predicting** a small adapter (typically a LoRA) with a hypernetwork in a single forward pass rather than training one with gradient descent. At query time the context lives in the adapter, so the prompt carries zero (or near-zero) context tokens. This trades a one-time hypernetwork pass for the per-query token cost that RAG and long-context inference pay forever.

This page tracks the emergence of this idea as a distinct efficiency axis, separate from compressing context (fewer/cheaper tokens) or caching it (smaller KV cache).

## Why it is a distinct axis

The wiki already tracks two ways to make context cheap:

1. **Compress the tokens.** Feed less per item: AdaCodec (predictive video coding), token pruning/merging, sparse attention.
2. **Cache smarter.** Store less of the attention state: KV-cache eviction ([kv-cache.md](kv-cache.md)), low-rank latent caches (VideoMLA).

Parametric internalization is a third move: **do not put the context in the prompt at all.** Encode it into weights ahead of time. The key enabler is that the adapter is *predicted*, not *trained*. A hypernetwork maps the raw context (a document, a video, a repo) to adapter weights in one pass, so you avoid the per-item fine-tuning cost that made "just train a LoRA per item" impractical at scale.

The cost model flips. RAG and long context pay `O(context tokens) per query`. Internalization pays `O(1) hypernetwork pass per item`, then `O(0) context tokens per query`. It wins whenever an item is queried many times; it can lose for one-shot queries where the generation pass is not amortized.

## The lineage

- **Doc-to-LoRA** (prior work) — maps a *text document* into a LoRA via a feedforward hypernetwork; the LLM answers about the document with no text in context. The template the 2026-06 papers extend.
- **[Code2LoRA](2026-06-06-code2lora-hypernetwork-repo-adapters.md)** (2026-06-06) — generates a *repository-specific* adapter from a code snapshot (static) or updates it per commit diff via a GRU hidden state (evolution). Matches the per-repo LoRA upper bound on assertion completion (63.8% cross-repo EM) with zero query-time tokens.
- **[Video2LoRA](2026-06-06-video2lora-parametric-video-internalization.md)** (2026-06-06) — a perceiver hypernetwork reads a frozen VLM's layer-by-layer activations on a *video* and predicts a LoRA in one pass. Statistically non-inferior to video-in-context at up to 1,500x fewer answer-time visual tokens and 6-80x faster TTFT; segment adapters compose in rank space.

Two independent groups shipping the same mechanism (predict-an-adapter-from-context) for two different modalities on the same day is the signal that this has crystallized into a named approach rather than a one-off trick.

## Connection to parametric-memory theory

This axis is the deployment face of the wiki's parametric-memory thread. [How LoRA Remembers](2026-05-29-how-lora-remembers-parametric-memory-law.md) (05-29) characterized *how much* a low-rank adapter can store and at what rank. Parametric internalization is the operational question that follows: if a rank-`r` adapter can hold this context, **generate that adapter cheaply and keep it current**. The composition-in-rank-space result from Video2LoRA also touches the additive-adapter / merge line (MergePipe), suggesting internalized chunks can be summed.

## Open questions

- **Break-even query count.** For each modality, how many queries against one item before the hypernetwork pass pays for itself versus just feeding the context once?
- **Drift and freshness.** Code2LoRA's per-diff GRU update tracks an evolving repo, but does the adapter accumulate error over thousands of commits and need periodic full regeneration?
- **Composition ceiling.** Video2LoRA shows segment adapters add in rank space; how many before interference degrades the answer?
- **Frontier-scale transfer.** All current results are on small backbones (SmolVLM2 500M/2.2B, mid-size code LMs). Does predicting an adapter for a frontier model still match in-context performance?
- **Cross-modal generality.** Doc, code, video done. Audio, tabular, tool-call histories next?

## Related pages

- [2026-06-06-code2lora-hypernetwork-repo-adapters.md](2026-06-06-code2lora-hypernetwork-repo-adapters.md)
- [2026-06-06-video2lora-parametric-video-internalization.md](2026-06-06-video2lora-parametric-video-internalization.md)
- [2026-05-29-how-lora-remembers-parametric-memory-law.md](2026-05-29-how-lora-remembers-parametric-memory-law.md)
- [2026-05-14-mint-million-scale-lora-serving.md](2026-05-14-mint-million-scale-lora-serving.md)
- [kv-cache.md](kv-cache.md) · [knowledge-distillation.md](knowledge-distillation.md)
