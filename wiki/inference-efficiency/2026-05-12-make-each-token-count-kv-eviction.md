# Make Each Token Count: Improving Long-Context Performance with Learned KV Eviction

**Date:** 2026-05-12
**Source:** HuggingFace Daily Papers
**arXiv:** [2605.09649](https://arxiv.org/abs/2605.09649)
**Tier:** 1 — KV cache / inference efficiency / long-context reasoning

## TL;DR

A learned, globally calibrated KV-cache eviction policy that does not just compress the cache, it *improves* long-context generation over the full-cache baseline. The framing flip is the load-bearing claim: in long contexts, full-cache attention is not optimal because irrelevant tokens dilute attention away from useful evidence. Lightweight retention gates assign per-token utility scores, a shared final scoring projection calibrates those scores across every layer and head, and one global memory budget lets tokens from different layers, heads, and modalities compete directly for cache capacity. Across long-context language, vision-language reasoning, and multi-turn dialogue, the method substantially reduces KV memory while matching or surpassing the full cache.

## Why it matters

Every prior KV-eviction paper in the wiki (TurboQuant, MISA, Stream-T1) framed eviction as a compression-quality tradeoff: how close can you stay to the full cache. This paper argues the full cache is not the ceiling. Once context is long enough, the full cache is a noisier oracle than a selective one because attention dilution from irrelevant tokens is a real cost. That turns eviction from a memory-saving trick into a reasoning-quality intervention. It is the same shift that LongAct (04-18) made on the training side: identify the small set of locations doing real work, concentrate the budget there. Now the same shift happens at the cache layer.

## Mechanism

Three pieces compose the design.

1. **Retention gates per cached entry.** A lightweight gate over each KV slot produces a utility score. Geometric retention serves as the query-agnostic proxy for future utility, which gives the gate a closed-form prior to learn against.
2. **A shared final scoring projection.** This is the global-calibration trick. Without it, layer-local and head-local scoring scales are incomparable, and a global budget cannot allocate tokens across layers. The shared projection puts every gate output on the same axis, so the eviction decision is genuinely global.
3. **A single unified budget across all layers, heads, and modalities.** Token candidates from different layers and heads compete directly for the same cache slots. The paper provides theoretical analysis showing that preferentially retaining useful tokens reduces attention dilution, which is the formal version of the framing flip in the TL;DR.

## How it relates to prior wiki state

- **LongAct (2026-04-18).** Both papers identify small subsets of locations that carry the real signal in long contexts. LongAct sparsifies *gradient updates*, this paper sparsifies *cached state*. Different optimization layers, same architectural intuition. The cross-paradigm transfer (saliency-in-quantization to saliency-in-training to saliency-in-eviction) is now three steps deep.
- **TurboQuant (2026-04-22).** TurboQuant gives a quantization-side path to KV memory reduction. This paper is the eviction-side path. They stack. Quantize the cache at low bits, then evict learned-useless tokens from the quantized cache, then run on a hybrid architecture that pulls KV across datacenters via PrfaaS.
- **Stream-T1 (2026-05-07).** Stream-T1 introduced the first content-aware KV eviction policy in the wiki, but for streaming video diffusion, and the routing signal was reward feedback. This paper is the language-model analogue with a learned utility gate, and the eviction policy is global rather than per-stream. Stream-T1 and this paper now bracket content-aware eviction: video-side reward routing, text-side learned utility.
- **MISA (2026-05-11).** MISA sparsifies the indexer-head axis of DeepSeek Sparse Attention. This paper sparsifies the cached-token axis with a global calibrator. Both reduce dilution. Composing them inside a long-context production stack is the natural next step: MISA selects the candidate token set, then the learned eviction policy decides which candidates persist across decoding steps.
- **KV Packet (2026-04-17).** KV Packet eliminates recomputation on cache reuse. This paper changes the structure of the cache itself before reuse. The two are orthogonal: KV Packet treats the cache as immutable and adapts the context to it, this paper treats the cache as a budgeted resource and lets utility decide.

## Research angle

The strong claim is that selective eviction beats the full cache. That implies a curve: at some context length, the selective policy crosses the full-cache baseline. Where is the crossover, and how does it move with task type? A second open question is whether the global calibrator generalizes across architectures. The shared final scoring projection is trained per model, but the structural argument (layers and heads have heterogeneous utility scales that need a common axis) does not depend on architecture. A third question, the most actionable one: does the learned eviction policy compose with KV-cache quantization (TurboQuant) without retraining the gates? If yes, the production cost floor for long-context inference drops by another integer factor.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2605.09649)
- [HuggingFace page](https://huggingface.co/papers/2605.09649)
- Raw source: [raw/huggingface/2026-05-12-make-each-token-count-towards-improving-long-context-perform.md](../../raw/huggingface/2026-05-12-make-each-token-count-towards-improving-long-context-perform.md)

## Related wiki pages

- [KV Cache concept page](kv-cache.md)
- [LongAct: saliency-guided sparse RL updates](2026-04-18-longact-saliency-sparse-rl.md)
- [Stream-T1: content-aware KV eviction in streaming video](2026-05-07-stream-t1-test-time-scaling-streaming-video.md)
- [MISA: indexer-head sparsification](2026-05-11-misa-mixture-of-indexer-sparse-attention.md)
- [TurboQuant: ultra-low-bit KV quantization](kv-cache.md#key-papers)
