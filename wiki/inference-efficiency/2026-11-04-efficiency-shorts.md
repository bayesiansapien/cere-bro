# Efficiency shorts, 2026-11-04

**Sources:** HuggingFace 2026-11-03, Kurate cs.AI/cs.LG (week opening), Ken Huang (Gmail/RSS), The Decoder, X Following feed · raw: `raw/huggingface/2026-11-03-*.md`, `raw/kurate/2026-11-04-cs-*.md`, `raw/gmail/2026-11-04-newsletters.md`, `raw/rss/2026-11-03-*.md`, `raw/twitter/feed/2026-11-03-evening-210222-ranked.json`

## LEMS + KFAC-SVD: better rank allocation for low-rank compression ([2610.32878](https://arxiv.org/abs/2610.32878))

SVD compression replaces each weight matrix with a low-rank product. It has two weak points. The first is how to split a global rank budget across layers: per-layer error proxies miss how errors propagate downstream. The second is decomposition quality: Fisher-weighted SVD suffers rank collapse. LEMS builds a layer-wise error surrogate that combines local importance, global importance and a propagation bias, then allocates ranks with an integer linear program. KFAC-SVD uses token-wise statistics to avoid the rank deficiency. Up to +4.8 points zero-shot over prior search methods across Mistral, Qwen3 and Llama 3, holding to 70B. KFAC-SVD averages 15% better perplexity. Fits the [pruning/sparsity](model-pruning-sparsity.md) thread where allocation, not the decomposition, is the lever (TWIG on 10-27 treated pruning, quantization and low-rank as branches of one decision tree).

## DeepSeek-V4.1-Flash at 1-bit on one DGX Spark (Ken Huang)

A practitioner deployment on one GB10 (128 GB unified memory). The model pairs a 552B-parameter MoE at 1-bit with a 196B-parameter Engram memory table (sparse n-gram lookup for recall). It holds 116.8 GB of weights resident and decodes at 18.10 tok/s. Prefill latency ranges from 77.8 ms to 52.9 s. 2-bit formats run out of memory; 1-bit leaves 5.6 GB of headroom. The KV cache is 4-bit MLA (multi-head latent attention, which stores a compressed latent per token). Splitting the model across a DGX Spark and a Mac over LAN tensor parallelism drops decode below 4 tok/s, so interconnect, not compute, sets the multi-box ceiling. Claims of preserved AIME/GPQA accuracy at 1-bit are paywalled and unverified. Links to [conditional memory embeddings](conditional-memory-embeddings.md) and [quantization](quantization.md). ([post](https://kenhuangus.substack.com/p/deploying-deepseek-v41-flash-on-nvidia))

## Anthropic Message Threads: send only the diff

The Messages API now lets agents send only what changed in a conversation instead of the whole history each turn. For 500K-1M-token requests, time to first token drops about 35%. This is the API-level form of prefix caching. It cuts upload and parse time, not only recompute. ([The Decoder](https://the-decoder.com/anthropics-message-threads-cut-time-to-first-token-by-35-percent-for-long-conversations/))

## Cache hits are now the price of an agent run

A practitioner ran the same one-line game-build prompt in their own harness. LongCat-2.5 (Meituan, 1.6T total / ~48B active parameters) finished for $0.28 in 34 minutes and 53 turns, versus $0.82 for Qwen3.8-Max. 4.7M of its 4.8M input tokens were cache hits, billed at $0.006/M versus $0.30/M uncached. In long agent loops, the cached-input price dominates the bill, more than the headline per-token price. ([@omarsar0](https://x.com/omarsar0/status/2117625533794332885))

## Serving benchmarks and quantized serving

- **MAServeBench ([2610.40293](https://arxiv.org/abs/2610.40293)).** Multi-agent systems make serving workloads with dependencies. Calls become ready at different times and carry growing shared context. The benchmark makes the collaboration pattern a configurable workload dimension and records it as replayable traces. Its key finding: serving efficiency (tokens/s) does not always translate into faster task completion.
- **"Twice as Fast, Until It Isn't" ([2611.04380](https://arxiv.org/abs/2611.04380), Kurate cs.AI list).** Quantized serving of mid-size open LLMs, where the speedup erodes under some conditions. Listed in Kurate's week-opening cs.AI set before ranking began.
- **MatMoE ([2611.01704](https://arxiv.org/abs/2611.01704), Kurate cs.LG list).** Matryoshka MoE with dynamic mixed-precision quantization for inference. Same caveat: listed before the week's tournament had scored anything.
- **Multi-Agent Relay Thinking ([2610.35219](https://arxiv.org/abs/2610.35219)).** Reasoning ownership passes between agents by confidence bidding. It matches multi-agent baselines at 6.0x lower token overhead on HallusionBench and MMStar.

## Hardware-side signals

- SK hynix took 9% of Penguin Solutions (SSD/CXL KV-cache offload) for $377M. SambaNova SN50 decode chips go into Supermicro disaggregated racks next to NVIDIA GPUs. Details in [SpaceX and the compute squeeze](../hardware/2026-11-04-spacex-ai-cloud-and-china-memory-loophole.md).
