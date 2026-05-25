# DeepSeek-V4: interleaved compressed attention with manifold-constrained hyper-connections

**Source:** AI Papers Academy summary via Gmail starred email, 2026-05-24. Original paper page: [aipapersacademy.com/deepseek-v4](https://aipapersacademy.com/deepseek-v4/).
**Raw:** [farmed](../../raw/gmail/2026-05-25-starred.md)

## TL;DR

DeepSeek-V4 replaces standard full attention with an interleaved system of three specialized attention mechanisms, supported by a widened residual stream. The three are Manifold-Constrained Hyper-Connections (mHC) that widen the residual stream into a higher-dimensional space and compress back down per layer; Heavily Compressed Attention (HCA) that crushes groups of 128 tokens into one entry via a learned token compressor and concatenates the global summary with a sliding window of recent tokens; and Compressed Sparse Attention (CSA) that compresses tokens in blocks of 4, then filters down to the most important entries via an indexer-attention component running over a lower-dimensional compressed space. The result is reported competitive performance versus top proprietary models with dramatic reduction in compute and memory.

## Why this matters

This is the most aggressive published attempt to make million-token context economically tractable. Standard attention is quadratic in the sequence; agentic workflows and test-time scaling have forced contexts past the point where that scales. DeepSeek-V4 says the question is no longer how to compress one cache but how to interleave different compression regimes across layers, so the network's attention behavior is itself a routed schedule. The mHC trick is independently interesting because it widens the residual stream temporarily and then compresses back, restoring the high-bandwidth path between layers that the original Transformer's residual stream provides but that pre-norm stacks (with their forward magnitude inflation) erode.

The HCA-CSA pair is the load-bearing idea. HCA collapses by 128 with a learned compressor so the global view is cheap. CSA compresses by 4 then filters via a learned indexer attention over a lower-dimensional projection of the compressed entries, so the local view is selective. The 128-block global summary plus the indexed 4-block selective view plus the uncompressed recent window is a three-tier memory hierarchy inside a single layer. This is what the KV cache concept page has been converging toward across the four KV-cache papers from 2026-05-24 ([2026-05-24-kvserve-service-aware-kv-compression.md](2026-05-24-kvserve-service-aware-kv-compression.md), [2026-05-24-gated-deltanet-2-decoupled-erase-write.md](2026-05-24-gated-deltanet-2-decoupled-erase-write.md), [2026-05-24-worldkv-video-world-memory.md](2026-05-24-worldkv-video-world-memory.md), [2026-05-24-rtpurbo-full-to-sparse-attention.md](2026-05-24-rtpurbo-full-to-sparse-attention.md)). DeepSeek shipped a foundation model that internalizes the same pattern.

## Connection to RTPurbo

RTPurbo on 2026-05-24 (the paper that found 16-dimensional retrieval subspace inside full-attention LLMs and converted full to sparse in a few hundred steps) made the *post hoc* case: full-attention training produces a low-dimensional retrieval geometry that can be extracted. DeepSeek-V4 is the *prior* case: train the model from scratch with the low-dimensional indexer baked into the attention layer itself. If RTPurbo's claim is right, DeepSeek-V4 should outperform a hundred-step RTPurbo conversion of a same-sized full-attention base. Empirical comparison is the open question.

## Where this fits

DeepSeek-V4 is the first production-scale model to interleave more than two attention regimes per layer. Prior hybrids (Mamba+attention, linear+full) typically pick a fixed ratio. DeepSeek-V4 picks three regimes and routes between them inside each block. Combined with the LLMs-as-noisy-channels Shannon scaling law paper from today ([2026-05-25-shannon-scaling-law-noisy-channel.md](../llms-foundation-models/2026-05-25-shannon-scaling-law-noisy-channel.md)), which models LLM training as transmission over a noisy channel where parameters are bandwidth and tokens are signal power, the picture becomes: scale up bandwidth (parameters) and signal power (tokens) while making the attention layer match the bandwidth profile of the actual signal. DeepSeek-V4 is a signal-shaped attention.

## Open research angles

- Whether HCA's learned 128-to-1 compressor preserves rare information (named entities far back, single-occurrence code identifiers) is the failure mode worth probing.
- The CSA indexer attention runs over a learned low-dimensional projection. If the projection is fixed across layers, it cannot adapt to layer-specific selection criteria. If it is learned per-layer, the parameter count expands. The paper's choice is not yet clear from the summary.
- mHC widens the residual stream — by how much, and is the widening factor constant across depth or scheduled? DAR (the diffusion routing paper from today, [2026-05-25-dar-diffusion-adaptive-routing.md](../ai-routing/2026-05-25-dar-diffusion-adaptive-routing.md)) finds that timestep-adaptive aggregation matters; whether mHC needs a depth-adaptive widening factor is the analogous question for LLMs.

## Industrial implication

If DeepSeek-V4 delivers million-token reasoning at the claimed compute reduction, every production stack with long-context workloads (coding agents, document-QA, multi-turn agent loops) has a new baseline to beat. The Mythos / Opus 4.7 / Gemini 3 Pro tier will have to either match the architecture or beat it on capability at higher cost. Pricing on long-context inference probably collapses further in Q3-Q4 2026 if independent reproduction holds.
