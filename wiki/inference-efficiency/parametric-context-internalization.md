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

- **Doc-to-LoRA** (prior work): maps a *text document* into a LoRA via a feedforward hypernetwork, so the LLM answers about the document with no text in context. The template the 2026-06 papers extend.
- **[Code2LoRA](2026-06-06-code2lora-hypernetwork-repo-adapters.md)** (2026-06-06): generates a *repository-specific* adapter from a code snapshot (static) or updates it per commit diff via a GRU hidden state (evolution). Matches the per-repo LoRA upper bound on assertion completion (63.8% cross-repo EM) with zero query-time tokens.
- **[Video2LoRA](2026-06-06-video2lora-parametric-video-internalization.md)** (2026-06-06): a perceiver hypernetwork reads a frozen VLM's layer-by-layer activations on a *video* and predicts a LoRA in one pass. Statistically non-inferior to video-in-context at up to 1,500x fewer answer-time visual tokens and 6-80x faster TTFT; segment adapters compose in rank space.

Two independent groups shipping the same mechanism (predict-an-adapter-from-context) for two different modalities on the same day is the signal that this has crystallized into a named approach rather than a one-off trick.

## Connection to parametric-memory theory

This axis is the deployment face of the wiki's parametric-memory thread. [How LoRA Remembers](2026-05-29-how-lora-remembers-parametric-memory-law.md) (05-29) characterized *how much* a low-rank adapter can store and at what rank. Parametric internalization is the operational question that follows: if a rank-`r` adapter can hold this context, **generate that adapter cheaply and keep it current**. The composition-in-rank-space result from Video2LoRA also touches the additive-adapter / merge line (MergePipe), suggesting internalized chunks can be summed.

## The tool-call-history modality arrives (2026-07-25)

The open questions below asked, after doc, code, and video: "Audio, tabular, **tool-call histories** next?" [Experience Distillation](../agentic-systems/2026-07-25-experience-distillation-sample-efficient-agent-learning.md) (2607.21051, Monash + ByteDance Seed) is tool-call histories, arriving by a different mechanism but on the identical cost model.

The mechanism differs in a way worth naming. Code2LoRA and Video2LoRA *predict* an adapter from context in one hypernetwork pass. Experience Distillation *trains* a student to reproduce the behavior of a teacher that read the context, which is classic context distillation. What makes it belong on this axis is the cost model, which flips exactly the same way: pay once to move the context into weights, then pay zero context tokens per query forever. Its specific contribution is that the distillation phase touches the environment **zero times**, unlike prior in-context-learning-plus-context-distillation attempts for agents, which re-ran the experience-conditioned teacher inside the environment and thereby spent the very resource the exercise was conserving.

The number that matters for this page is the gap between distillation and naive internalization: **64.8% of the in-context gain retained versus 3.8% for supervised fine-tuning on the same transcripts.** That is a strong argument that *what* you internalize matters more than *how*. Fine-tuning internalizes the record (mostly failure); distillation internalizes the behavior of a model that has read the record. Whether the hypernetwork branch has a comparable failure mode, predicting an adapter that encodes the document rather than the competence the document confers, is not something Code2LoRA or Video2LoRA tested, and this result suggests it should be.

It also supplies a partial answer to the **break-even query count** question below. Experience Distillation matches classical RL baselines at 9.6x fewer environment samples, so the break-even is not measured in queries against one item but in avoided environment interactions, which for agents is the expensive unit.

## The corpus scale arrives, and it is a parameter-allocation argument (2026-07-31)

Everything above internalizes **one item at a time**: a document, a repo, a video, a set of tool-call transcripts. [Memory Decoder at Scale](2026-07-31-memory-decoder-at-scale.md) (2607.27919) internalizes a **corpus**, and it does so as a separate model rather than an adapter on the base one. A memory model of up to 6.9B parameters is pretrained on 300B tokens to predict the next-token distribution a kNN retriever would have produced, then run alongside a frozen base model with the two output distributions interpolated. No index and no retrieved documents at query time.

The cost model is this page's cost model, run at a different granularity. Pay once, up front, to move context into weights; pay zero context tokens per query afterwards. What changes is the unit of amortization. Code2LoRA and Video2LoRA amortize a hypernetwork pass over queries against **one item**, which is why this page's first open question below asks for a break-even query count. Memory Decoder amortizes a pretraining run over queries against **an entire domain**, which makes break-even a non-question and replaces it with a different one: is the memory worth its parameters compared to spending them on the base model?

**The answer is yes, and it is the reason this entry matters.** A 6.9B general memory paired with Pythia-410M averages **37.34 across 17 benchmarks against Pythia-12B's 37.24, at 39% fewer total parameters**, lifting the base model's own 29.86 by roughly 7.5 points. More striking, a **1.7B domain memory adds more than 9 points to the three-domain average at every Qwen3 Base size from 0.6B to 14B**. If memory and reasoning were substitutes you would expect a 14B base to need less external memory than a 0.6B one, and it does not.

**This is a partial answer to the frontier-scale transfer question below.** That question asked whether predicted-adapter results on small backbones survive when the base model is large. Memory Decoder tests a neighbouring version, whether the *value* of internalized context survives base-model scaling, and finds it does across a 23-fold range. It does not answer the hypernetwork branch's version, since Memory Decoder pretrains its memory rather than predicting it, and the two mechanisms could scale differently.

**Two caveats worth carrying.** Every base model reported is Pythia or Qwen3 Base, so nothing instruction-tuned appears, and interpolating a memory distribution into a model whose post-training shaped its output distribution deliberately is a different proposition. And this axis now costs **two forward passes per token**, which the parameter count hides and which is the opposite of the serving-cost story that made adapter prediction attractive.

**The sibling paper is on a different branch.** [Metis](../agentic-systems/2026-07-31-metis-memory-foundation-model.md), same day, also deletes the external store but keeps memory as an **activation state inside the backbone** updated gradient-free by a forward pass. That is closer to this page's spirit (no second model, no second forward pass) and further from its mechanism (no adapter at all). Whether "internalized context" should be parameters, adapters, or persistent activations is now a live three-way question rather than the two-way one this page was set up to track.

## 2026-09-04: three arrivals in one day, and the page's cost model needs a middle row plus a new column

**Three papers on one HuggingFace board occupy three different positions relative to this page's frame, and the frame has to widen to hold them.**

**[LatentPress (09-04)](2026-09-04-latentpress-latent-context-compression.md)** (arxiv 2609.01507) writes conversational history and long documents into **continuous memory tokens a frozen decoder reads directly through its input-embedding interface**, with no text reconstruction at inference. A reader-matched writer compresses **4-16x** while training only an adapter of **4.2M-26.2M parameters, about 0.1% of the decoder**. On LongMemEval it reaches **0.504 accuracy at 7.70x compression against 0.490 for uncompressed evidence**, beating text summaries (0.184) and OCR-based compression (0.426 falling to 0.312). Writing takes **43ms per conversation** and reading is **5-9x faster** than raw context.

**This is the intermediate cost position the page did not have.** Code2LoRA, Video2LoRA and Experience Distillation all pay `O(1)` per item and then `O(0)` context tokens per query, which is why the page's framing has been that internalization wins whenever an item is queried many times. LatentPress pays `O(1)` per item and then a **small but nonzero** per-query cost, because memory tokens still occupy input positions. It is cheaper to produce than an adapter (a 43ms forward pass, no hypernetwork over layer activations) and cheaper to swap and compose than weights. **The page needs a middle row: soft tokens win at low reuse counts where adapter prediction has not amortized, which is also a partial answer to the break-even question below.**

**It also retires a live option.** Rendering context as an image and letting a vision-language model read it has circulated as a compression trick on the argument that a page of text costs fewer visual tokens than text tokens. LatentPress measures it at 0.426 degrading to 0.312 against 0.504, plus a decode cost. As a machine-facing context interface it is dominated on both axes.

**[LatentStream (09-04)](2026-09-04-latentstream-progressive-latent-memory.md)** (arxiv 2609.04131) does the same thing for streaming video and names the shift precisely: **store-and-retrieve becomes retrieve-and-internalize**. Query-agnostic hierarchical streaming memory organizes history into short, mid and long-term levels under a fixed budget; groups of latent memory tokens with progressively expanding receptive fields then pull evidence from their own scopes and fold it into a compact **fixed-length** latent memory, refined by a progression reward built from group-wise predictive entropy. **The fixed-length read is the property worth taking: retrieval-augmented systems budget the store and not the read, so per-query context cost depends on what the user asked. Here it is a constant.**

**Together they are the page's clearest confirmation of its own strongest lesson.** The Experience Distillation entry found a large gap between distilling *behavior* (64.8% of the in-context gain retained) and fine-tuning on raw transcripts (3.8%), concluded that *what* you internalize matters more than *how*, and asked whether the hypernetwork branch shares the failure mode of encoding the document rather than the competence. LatentPress answers on the near side: a compressor trained to preserve **answerability** beats the reconstruct-the-text baseline by 32 points. **Optimizing for the reconstruction is the failure; optimizing for the downstream read is the fix. Three mechanisms, one rule, and it is now the most reliable finding on this page.**

**[Compile by Training (09-04)](2026-09-04-compile-by-training-neural-functions.md)** (arxiv 2609.04199) is the new column. It compiles a **natural-language specification** into a reusable neural function: teachers generate examples at compile time, those train a small adapter for a compact interpreter, and the artifact runs with no teacher. **83.6% semantic accuracy on FuzzyBench-Hard, where the prior Program-as-Weights fast compiler produced no exact matches, for roughly a minute of compile time instead of seconds.** Every prior entry on this page internalizes an *artifact* (a repository, a video, a transcript) to stop paying context tokens. This internalizes a *behavior* to stop paying **API calls**. There is no context to compress because there never was any, only a recurring inference bill. **That makes it a fourth mechanism on this axis and the first whose input is a specification rather than data**, and it inherits the page's software-artifact properties in the strongest form yet: storable, versionable, composable.

**New open question the day creates: portability across models.** Every result here is contingent on the writer being reader-matched or the adapter being backbone-specific. Soft tokens are arguably the worst case, since a continuous embedding tuned to one decoder's input space has no reason to mean anything in another's, and this is the same model-keyed boundary [cross-model KV sharing (09-02)](2026-09-02-cross-model-kv-sharing.md) attacked for KV state. **Whether memory tokens are portable across models decides whether this axis is a serving primitive or a single-model optimization, and nobody has run the experiment.**

**And one governance note this page has not carried before.** A continuous, non-human-readable representation sitting in the context window is not inspectable by any prompt-auditing tool that assumes text. None of the three papers discusses it, and it cuts against the monitorability arguments in [responsible-ai](../responsible-ai/).

## Open questions

- **Portability across models.** Are soft memory tokens or predicted adapters transferable to a different decoder, or is every result on this page model-keyed? (Added 09-04.)
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
