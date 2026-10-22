# Drafters under load: EAGLE-4, Liquid's DSpark drafter, Ling-3 UBTree, and the TPU engines

**Sources:** AI lab watcher (`raw/labs/2026-10-2*-labs.md`): [LiquidAI/LFM2.5-24B-A2B-DSpark](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-DSpark) (+ [GGUF](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-DSpark-GGUF)); [inclusionAI/Ling-3.0-tiny-UBTree](https://huggingface.co/inclusionAI/Ling-3.0-tiny-UBTree) (paper arXiv 2609.39972); [Google: vLLM and SGLang inference engines on TPU](https://developers.googleblog.com/announcing-new-vllm-and-sglang-inference-engines-on-tpu/). X feed: [EAGLE-4 load table via @theomlondhe](https://x.com/theomlondhe/status/2113162304900747772); [Red Hat on suffix decay](https://x.com/RedHat_AI/status/2112622163203154198). YouTube: [Hugging Face "Local AI 202: speculative decoding"](https://www.youtube.com/watch?v=H4azmWcqO5g).

## TL;DR

- **Speculation can make you slower under load.** EAGLE-4's table (Qwen3.8-27B on 4x B300): DSpark and DFlash 2 are 2.6-2.8x faster than vanilla decoding at 1 request but fall **below vanilla at 512 requests** (14.2K and 16.6K vs 21.2K tok/s). EAGLE-4 resizes its draft tree as load changes: 3.59x at low load, 1.34x at high load. Batched GPUs are already compute-busy, so verification work that was free at batch 1 now competes.
- **Liquid LFM2.5-24B-A2B-DSpark**: a 327.7M drafter (5 attention layers, rank-256 Markov head, confidence head, block 9). On one B300 with FP8 target in SGLang: **2.38x at concurrency 1, 2.69x at 32, 1.71x at 256**; mean 5.16 tokens per step. The card warns batched verification can change outputs even under greedy decoding.
- **Ling-3.0-tiny-UBTree**: a 183M drafter where a DFlash backbone proposes candidates per position and a learned bigram selector builds a 64-node tree. Acceptance length 7.5-10 and **2.8-3.5x end-to-end**, beating DSpark by roughly 0.3-0.7x on every benchmark (e.g. MATH-500 3.52x vs 2.83x). MIT.
- **Google's TPU engines** ship MTP, EAGLE-3, DFlash, DSpark and n-gram drafters natively, plus a Pallas megakernel that runs Kimi K3's (2.8T) full decode step as one kernel at 700+ tok/s per user.
- **Red Hat**: acceptance falls from 87.5% at token 1 to 39.5% by token 6 ("suffix decay"), which is why Meta's Muse Spark Open speculator drafts exactly 7 tokens.

## How this relates to prior wiki pages

- **Answers a gap flagged repeatedly on [speculative-decoding](speculative-decoding.md):** most drafter papers report batch-1 speedups. The EAGLE-4 table is the first clear crossover number in the wiki: somewhere between 32 and 512 concurrent requests, fixed-length drafting stops paying. Liquid's own 1.71x at 256 is consistent with the decline.
- **DScout (today)** makes the same argument from the training side: mean accepted tokens is not throughput.
- **Tree drafting vs block drafting:** UBTree's lead over DSpark suggests the 10-20 tension (DLite drops drafter history, ReaDy adds compact history) has a third axis, the shape of the draft.

## Gaps

- The EAGLE-4 numbers come from a tweet of the paper's table; the paper itself was not in this window.
- UBTree serving support in SGLang is "coming soon"; all its numbers are concurrency 1.

## Research angle

A load-aware draft-length controller (EAGLE-4's adaptive tree) is a routing problem: choose draft depth per batch from live utilization, the same shape as ATEST choosing sample count from live GPU cost.
