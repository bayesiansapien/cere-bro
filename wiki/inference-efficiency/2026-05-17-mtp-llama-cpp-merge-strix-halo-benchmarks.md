# MTP support merged into llama.cpp: Strix Halo benchmarks confirm a 2x decode speedup at 27B, mixed result at 35B

**Source:** r/LocalLLaMA (multiple posts on 2026-05-16/17), score=683 + 511 + 110, tier=1
**PR:** [ggml-org/llama.cpp #22673](https://github.com/ggml-org/llama.cpp/pull/22673)
**Benchmarks post:** [Strix Halo Llama.cpp MTP Benchmarks: 27B Gets Much Faster, 35B Is Mixed](https://www.reddit.com/r/LocalLLaMA/comments/1teypb8/strix_halo_llamacpp_mtp_benchmarks_27b_gets_much/)
**Raw:** [raw/reddit/2026-05-17-r-localllama.md](../../raw/reddit/2026-05-17-r-localllama.md)
**Tier:** 1 (speculative decoding, on-device inference, KV-adjacent acceleration)
**Date:** 2026-05-16

## TL;DR

Multi-Token Prediction (MTP) decoding support has been merged into llama.cpp upstream. Strix Halo benchmarks on Qwen3.6 single-file canvases show the practical envelope: at 27B, 5-turn chat with ~28.5K context drops from 258.65s to 200.55s wall-clock (-22.46% total time, -26.51% on turns 2-5; generation +136% from 7.61 to 17.98 t/s). At 35B the picture is mixed: generation throughput rises ~17% but total wall-clock regresses ~11% because prompt-processing throughput drops ~16% in single-turn workloads. The community has now confirmed in production what the MTP papers (Speculative Decoding for Autoregressive Video Generation 04-22, and the broader speculative-decoding line) predicted: speculative drafting wins on multi-turn / long-context decoding-heavy workloads, but its prompt-processing penalty makes single-turn short-prompt wins fragile at the larger model size.

## Why this matters for the wiki

The wiki's [speculative-decoding concept page](speculative-decoding.md) tracks the speculative-decoding line of work through Orthrus (05-14, dual-view diffusion sharing a KV cache, 7.8x speedup, bit-identical output) and the speculative-decoding-for-video-generation paper (04-22). Until this week the consumer-hardware story was Mac Studio plus llama.cpp without MTP, hitting decode-throughput ceilings that papers reported on H100. MTP's merge to llama.cpp is the moment the gap closes on Strix Halo / Ryzen 395 / RTX 5090 hardware. r/LocalLLaMA reports independently that:

1. Qwen3.6-35B-A3B with the little-coder harness hit 24.6% on Terminal-Bench 2.0, exceeding Gemini 2.5 Pro on Gemini CLI (19.6%) and Qwen3-Coder-480B on Terminus 2 (23.9%). Sub-10B local models are now measurable on a hard agentic benchmark (Qwen3.5-9B at 9.2%). This is the harness-as-load-bearing thread (WildClawBench 05-15) playing out at the consumer-hardware end of the curve: choice of decoding strategy (MTP), harness (little-coder vs Gemini CLI), and quantization explain more variance than the model itself.
2. Corsair desktop PC with Ryzen 395 plus 128GB unified RAM (96GB usable as VRAM via Radeon 8060S iGPU) is now a sub-$3K workstation that runs the 35B-A3B class at usable throughput. This is the consumer-deployment continuation of the SANA-WM (05-15) "60-second 720P on RTX 5090 with NVFP4" thread.

## Connections

**Compounds with Lighthouse Attention (05-16) and Forcing-KV (05-15).** Lighthouse changes pre-training to ship a dense-attention model; MTP changes how that model decodes at inference; Forcing-KV / Make Each Token Count change what the cache stores during decoding. All three are kernel-decoupled (no custom kernel needed in the deployed model), and all three compose multiplicatively. The "5-10x throughput on the same hardware in 2026 over 2025 with no model change" projection in 2026-05-16's Big Picture is being confirmed in piece-by-piece consumer reports this week.

**MoE-muP relevance.** Multi-Token Prediction inside a MoE is a different beast from inside dense models because the draft tokens fan out across experts. Whether MoE-muP-style scale-stable hyperparameters carry over to MTP-augmented MoE training is unaddressed in the merged llama.cpp code (which uses already-trained models) but is the natural pre-training analog.

## Worth Watching

- **MTP win/loss conditions formalized.** The 27B-wins-35B-mixed split is a known property of speculative decoding (the larger target model amortizes the draft cost less), but the precise crossover depends on the draft model, the workload (single-turn vs multi-turn, prompt-heavy vs decode-heavy), and the hardware. A community-curated rule-of-thumb (likely on r/LocalLLaMA within 30-60 days) would be useful.
- **MTP plus tool-calling agent harnesses.** When the agent harness emits short tool-call outputs frequently, prompt-processing throughput dominates and MTP's regression there hurts. Whether little-coder or Claude-Code-style harnesses can selectively disable MTP per turn is an interesting integration problem.

## Links

- PR merged: [github.com/ggml-org/llama.cpp/pull/22673](https://github.com/ggml-org/llama.cpp/pull/22673)
- Strix Halo benchmark thread: [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1teypb8/strix_halo_llamacpp_mtp_benchmarks_27b_gets_much/)
- Qwen3.6 Terminal-Bench 2.0 leaderboard post: [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1temio0/qwen3635ba3b_and_9b_are_officially_on_the_public/)
- Related: [speculative-decoding concept](speculative-decoding.md), [Orthrus 2026-05-14](2026-05-14-orthrus-dual-view-diffusion-ar.md)
