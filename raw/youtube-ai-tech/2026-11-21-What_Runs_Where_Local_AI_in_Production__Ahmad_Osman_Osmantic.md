# What Runs Where? Local AI in Production (Ahmad Osman, Osmantic)

**Channel:** AI Engineer
**Published:** 2026-11-21
**Source:** https://www.youtube.com/watch?v=GKSQYbELDzw

## TL;DR
Ahmad Osman (Osmantic, maker of the ODS local inference stack and "Portal" harness) argues that open-source AI is an optimization problem and local AI is a UX problem. His thesis: frontier intelligence is not needed at most agent steps; small specialized models plus per-model, per-chip, per-workflow inference engines beat generic stacks like llama.cpp. He bets continual learning will only work locally, built from n-gram/Engram-style memory tables, small decision models and weight edits. The talk is dense and directionally right, but several numbers are garbled and should not be quoted without checking.

## Key Takeaways
- **Agents now dominate token volume.** OpenRouter data (Oct 2026): agents passed humans as token producers in Feb 2026. Token volume skews open-weight (DeepSeek V4.1 Flash leads by tokens); spend skews closed (Opus 5.5 leads by dollars).
- **Agent latency is tool-bound, not decode-bound.** Most wall-clock is waiting on shell commands and tool results, so even a single RTX 3090 is useful for agentic work.
- **Eval crisis.** Open-vs-closed gap ranges from "open ahead by 2 points" (Terminal-Bench) to ">50% behind" (HLE). Artificial Analysis v5 ranking Haiku 5.5 above DeepSeek V4.1 Flash is cited as evidence benchmarks are broken.
- **Quantization is per-layer, not uniform.** Calibration-based mixed precision (keep hot layers at 16/8-bit, crush rarely used ones to very low bits) is what Unsloth-style dynamic quants do. Blanket 4-bit "nukes the model." Claimed: GLM 5.3 at 4-bit retains ~94% accuracy vs DeepSeek V3.1 at ~76% a year earlier.
- **Hardware choice follows workload.** Prefill is compute-bound, decode is bandwidth-bound. Dense 27B on a DGX Spark (273 GB/s) is slow; MoE fits it better. Two DGX Sparks reportedly beat an M5 Ultra (~1.2 TB/s) because Apple's AI software stack lags CUDA.
- **Batching is where GPUs win.** At 50 concurrent requests, an RTX Pro 6000 hit ~1,300 tok/s on Qwen 3.6 27B while Mac/Spark/Strix Halo stacks effectively ran sequentially. He frames this as a software gap, not a silicon one.
- **Amdahl's law in LLM pipelines.** A 100x faster tokenizer gave only a 1.1% end-to-end speedup. Optimize the whole system.
- **Density of intelligence.** Qwen 3.6 27B dense beat the Qwen 397B MoE (17B active) one month after release, at 1/15 the memory. GPT-4o-class capability now runs on phones.
- **Small specialized models at 1% cost.** Cites Airbnb matching frontier quality on a production task with a ~2B fine-tuned model. Opus 5.5 is described as a distilled, coding-RL'd "student" of larger Fable models: great executor, weak out-of-distribution reasoner.
- **Cheap API providers may silently substitute models.** A "$0.30/M" frontier endpoint may actually route to a smaller MoE. Verify what you are served.
- **Local agents need search.** A local model failed a GPU-RGB task until given web search; tool docs post-date training cutoffs.
- **Continual learning recipe (his bet):** Engram/n-gram lookup tables on SSD/RAM + small decision models + weight edits, replacing the "markdown bloat" of skill files in current harnesses.

## Architecture & Optimization Mechanics
- **Per-layer sensitivity is the core of good quantization.** Run calibration, measure each layer's activation usage and loss sensitivity, assign bits accordingly. This is the same signal used for structured pruning, so one profiling pass can feed both.
- **Bottleneck mapping:** long context and KV cache building shift work to compute-bound prefill; interactive single-stream is bandwidth-bound decode; multi-agent fan-out is a batching/scheduler problem. Pick hardware and kernels per regime.
- **Agent-aware scheduling.** He cites a Nov 9 paper ("FlashData," name uncertain) that records turn boundaries so vLLM stops guessing, claiming 1.5x to 3.14x more tokens per minute. Treat this as unverified.
- **DeepSeek V4.1 Flash memory.** Combines KV compression with an Engram conditional-memory module (196B parameters, deterministically addressed, prefetchable from host memory).
- **Specialization via distillation.** Collect frontier traces, build evals, generate synthetic data, then SFT + RL a 1 to 2B model. This is the route Osman says delivers "frontier at 1% cost."

## Grounded Context (Web Enrichment)
The DeepSeek-V4.1-Flash technical report (arXiv 2609.19969) confirms the KV story, but credits the savings to CSA2 cross-layer KV reuse with sparse attention, FP4 KV caching and bounded SWA replay. Secondary write-ups report a global KV footprint of ~890 bytes/token, about 1/4 of V4-Flash. Engram is separate: it splits memorization from computation, not KV. SemiAnalysis found that moving the ~189 GiB Engram table into HBM barely helps and steals KV capacity. Engram keeping for prefill matters more than for decode. Osman's own figures ("13 GB for 400K tokens to 29 MB for 1K tokens") work out to roughly the same per-token cost, so the "437x" claim cannot be read off his slide. Quote the paper instead. Airbnb's engineering blog does have a post titled "Frontier quality at 1% of the cost: a production benchmark" (fine-tuned E2B-class model on a classification task), and Airbnb's CTO has described post-training small models "beyond the frontier" for narrow tasks. I could not find a "FlashData" paper. Adjacent, verifiable work covers the same idea: MARS (arXiv 2604.26963, exports agent execution boundaries to a vLLM control plane), NVIDIA Dynamo's ThunderAgent scheduler (pause/resume at tool boundaries), Continuum (KV TTL across agent turns, arXiv 2511.02230) and SAGA (workflow-level scheduling, 1.64x lower task completion time vs vLLM 0.15.1).

Opinion: the strongest content is the systems framing (tool-bound agents, batching gaps, Amdahl). The weakest is benchmark-dismissal used to justify a sales pitch. "1B model beats Opus 5.5 in 3 years" is a tweet-grade prediction, not an argument.

## Real-World Application / Actionable Step
- **Routing:** profile your agent traces and measure what fraction of wall-clock is tool wait vs decode. If tool wait dominates, route more steps to small local models. Latency cost is near zero.
- **Quantization:** replace uniform 4-bit with a per-layer sensitivity sweep and bit allocation. Reuse the same sensitivity map as a pruning prior.
- **Distillation pipeline:** pick one narrow, high-volume classification or extraction step, harvest frontier traces, and fine-tune a 1 to 3B model. Benchmark it against the frontier on your own eval, following the Airbnb template.
- **Serving:** evaluate MARS/ThunderAgent-style turn-aware scheduling in vLLM for multi-agent workloads before buying more GPUs.
- **Provider hygiene:** spot-check cheap endpoints with fingerprinting prompts to detect silent model substitution.
- Read DeepSeek V4.1 Flash §KV (CSA2 + FP4 KV) for a KV-compression baseline to compare against your own MoE memory work.
