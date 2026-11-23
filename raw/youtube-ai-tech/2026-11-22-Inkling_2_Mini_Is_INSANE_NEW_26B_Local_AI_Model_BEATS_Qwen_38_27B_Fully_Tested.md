# Inkling 2 Mini Is INSANE! NEW 26B Local AI Model BEATS Qwen 3.8 27B! (Fully Tested)

**Channel:** WorldofAI
**Published:** 2026-11-22
**Source:** https://www.youtube.com/watch?v=cUuVObUqbn0

## TL;DR
Thinking Machines released Inkling 2 Mini (Nov 20, 2026): a 26.4B-total-parameter open-weight (Apache 2.0) looped mixture-of-experts transformer that reruns its middle layers for extra reasoning passes. It matches Qwen 3.8 27B on the Artificial Analysis Intelligence Index (20) with roughly 5x fewer active parameters. It runs on 32 GB Macs and DGX Spark, and it wins on agentic coding, tool use and token efficiency. Qwen still leads on multi-turn chat, complex instruction following and knowledge-heavy tasks. The video's own tests are vibe-heavy front-end demos; the architecture is the real story.

## Key Takeaways
- **Specs:** 26.4B total, 3.4B unique active weights per token, 5.4B "weight activations" per token once 3 loop passes are counted. 1M context, text + image input, Apache 2.0.
- **Benchmarks (as quoted):** AA Intelligence Index 20, on the Pareto frontier vs active params. Claimed SWE-Bench Pro 77.9%, BrowseComp 79%, "DeepSWE" 48.2%. Parallel ranked it #1 among open-weight models for efficiency, with $25.80 cost per correct answer. Web search gave its biggest accuracy lift of any model tested, compensating for small knowledge capacity.
- **Local speed (claimed):** 210 tok/s decode on M5 Ultra, 125 tok/s on M5 Max MacBook Pro, ~200 tok/s on RTX 5090. Prefill 3,620 and 1,750 tok/s on the two Macs.
- **Quantization robustness:** community quants at 5.4 GB and 8.9 GB reportedly retain 91.2% and 96.8% of full-precision performance.
- **Weaknesses:** trails Qwen 3.8 27B on multi-turn conversation and complex instruction following. Larger models still win hard reasoning.
- **Ecosystem:** weights on Hugging Face, fine-tuning/inference via Thinking Machines' Tinker. A variable-loop research model was also released to study how loop count affects accuracy and transparency.
- **Video tests:** WorldofAI's harness showed Inkling faster and using fewer output tokens than Qwen on most coding/web tasks. Front-end taste was split between the two. Sponsor: Decision Node.

## Architecture & Optimization Mechanics
- **Looping = compute without parameters.** Reusing a block of middle layers N times multiplies effective depth while holding memory constant. On bandwidth-bound devices (Macs, laptops), the weight footprint sets decode speed, so looping converts spare compute into reasoning at no memory cost.
- **Looping x MoE.** Each pass routes tokens through experts again, so "active params" becomes ambiguous (3.4B unique vs 5.4B counted with loops). This matters for any cost model or router that uses active params as a proxy for FLOPs or latency.
- **Variable loop count is an adaptive-compute knob.** It is effectively depth-wise early exit. The released variable-loop research model lets you trade passes for accuracy per query, which maps directly onto routing ("spend more loops on hard prompts").
- **Quantization tolerance.** ~97% retention at ~9 GB suggests loop-shared weights are well conditioned. The open question is whether quant error compounds across passes, which makes it worth testing per-loop activation drift.

## Grounded Context (Web Enrichment)
Artificial Analysis confirms the core claims: Inkling 2 Mini scores 20 on its Intelligence Index, matching Qwen3.8 27B (xhigh) and Nanbeige4.3-33B with about 5x and 6x fewer active parameters, and sits on the Pareto frontier for both total and active parameters. AA counts 5.4B active (three passes over looped layers) on 3.1B unique weights per text token. Thinking Machines says 3.4B active, 5.4B with looping. The video calls the model "26B" and says "5.4B active," which is the loop-counted figure. It is a sibling of Inkling 2 Small (594B total, 17B active MoE, launched Nov 5, 2026) and follows the original 975B/41B Inkling from July 2026. The video's "best open-weight model from a US lab since Llama" framing is fair. The SWE-Bench Pro, BrowseComp and "Stanford energy-efficiency" numbers come from the creator and were not independently confirmed in my search. Treat them as vendor or creator claims until AA or lab model cards corroborate them.

## Real-World Application / Actionable Step
- **Benchmark loop count as a routing dimension.** Using the variable-loop research model, measure accuracy vs loop count on your routing eval set. Build a router that picks (model, loop count) instead of only picking a model.
- **Fix your cost model.** If your router or MoE capacity planner uses "active params," split it into unique-weight bytes (memory/bandwidth) and loop-multiplied FLOPs (compute).
- **Quantization study:** run GPTQ/AWQ at 4-bit and track error accumulation per loop pass. Looped models are a fresh testbed for whether shared-weight quant error compounds.
- **Local agent default:** for on-laptop coding agents with web search, try Inkling 2 Mini at 8-bit against Qwen 3.8 27B. Keep Qwen for instruction-heavy, multi-turn flows.
