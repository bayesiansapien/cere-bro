# dMoE: dLLMs with Learnable Block Experts

Diffusion LLMs (dLLMs, models that decode many tokens in parallel per forward pass instead of one token at a time like autoregressive models) increasingly bolt on Mixture-of-Experts (MoE, where each token routes to a small subset of specialized sub-networks). But the two designs fight each other. Block-parallel decoding processes a whole block of tokens with bidirectional dependencies in one pass, while conventional MoE routes each token to its own experts independently. The mismatch blows up the number of uniquely activated experts per pass, and since every activated expert's weights must be loaded, inference becomes memory-bound. dMoE fixes this by aggregating the per-token expert distributions inside a block into one unified block-level expert distribution that routes the whole block coherently. The result: uniquely activated experts drop from 69.5 to 14.6 on average, performance is retained at 99.11% of the original, memory usage falls 76.64% to 79.84%, and end-to-end latency speeds up 1.14x to 1.66x.

```
Token-level routing (baseline):
  tok1 ►exp A,F     ┐
  tok2 ►exp C,K     ├─► union = many unique experts loaded (≈69.5)
  tok3 ►exp B,M     ┘    → memory-bound: load all their weights

Block-level routing (dMoE):
  tok1 ┐
  tok2 ├─► aggregate token distributions ►block dist ►few shared experts (≈14.6)
  tok3 ┘                                                → 76-80% less memory
```

## Key points

- **The problem is structural, not a tuning issue.** Block-parallel decode and per-token routing pull in opposite directions. More tokens per pass means more independent routing decisions means more distinct experts to load.
- **The fix is a routing aggregation, not a new architecture.** dMoE collapses the token-level expert distributions within a block into a single block-level distribution, so the block activates a small, shared set of experts coherently.
- **Uniquely activated experts: 69.5 down to 14.6 on average.** That is the core mechanism payoff and the direct cause of the memory savings.
- **Performance retention 99.11%.** The block-level aggregation is close to free in quality terms, which is what makes it deployable rather than a tradeoff knob.
- **Memory down 76.64% to 79.84%, latency 1.14x to 1.66x faster end-to-end.** Memory is the headline win because MoE serving is memory-bound; the latency win follows from loading far fewer expert weights.

## Gaps in the study

Tested on dLLM benchmarks only. There is no analysis of routing-quality loss on very long blocks, where forcing a single shared expert set across many bidirectionally-dependent tokens may start to hurt. It also does not characterize whether block aggregation degrades on heterogeneous blocks, where tokens genuinely want different experts and collapsing them is lossy.

## How it relates to prior wiki pages

- **MISA (tracked in kv-cache.md)** routes on a head axis, learning per-head sparse expert-like selection inside the DeepSeek Sparse Attention indexer. dMoE is the diffusion-LLM analogue of the same instinct: make expert activation sparse and coherent rather than letting every unit pick independently. MISA does it across attention heads; dMoE does it across the tokens of a decode block. Both treat uncontrolled independent routing as the waste to eliminate.
- **Nemotron 3 Super hybrid MoE (2026-04-21, [summary](2026-04-21-nemotron3-super-hybrid-moe.md))** established the prior MoE-efficiency baseline in the wiki, where the lever was the hybrid layer mix and expert granularity. dMoE adds a new lever specific to parallel decoding: control how many experts a parallel block is allowed to touch at once. It extends the MoE-efficiency thread into the dLLM serving regime, which the Nemotron work did not cover.

## Industrial implication

Memory bandwidth and capacity, not compute, are the binding constraint for MoE serving. As the dLLM-plus-MoE stack matures, block-coherent routing is close to a free win: it cuts the expert weights you must stream per pass by roughly 4x to 5x with under 1% quality loss. Expect block-level routing to become a default in any production dLLM-MoE serving path, the same way grouped or shared experts became default in autoregressive MoE serving.

## Links

- Paper: [arXiv 2605.30876](https://arxiv.org/abs/2605.30876)
- Related concept page: [KV cache](kv-cache.md)
- Related concept page: [Knowledge distillation](knowledge-distillation.md)

Raw source: [raw/huggingface/2026-06-01-dmoe-dllms-with-learnable-block-experts.md](../../raw/huggingface/2026-06-01-dmoe-dllms-with-learnable-block-experts.md)
