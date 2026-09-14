# Route by Task, Not by Model: the 2026 open-versus-frontier cost picture

**Source:** HackerNoon, "How Close Are Open-Source Models to GPT-5-Class Performance? The 2026 State of Play" (published 2026-09-09, surfaced via the X home feed on 09-14). [Article](https://hackernoon.com/how-close-are-open-source-models-to-gpt-5-class-performance-the-2026-state-of-play) · [Tweet](https://x.com/hackernoon/status/2097742136972361741)
**Date:** 2026-09-14
**Raw:** [feed capture](../../raw/twitter/feed/2026-09-14-morning-ranked.json)

## TL;DR

The recurring question "have open models caught up to the frontier" is the wrong question, and this piece is useful mainly because it replaces it with a better one. On a neutral composite (the Artificial Analysis Intelligence Index, which blends nine evaluations including Humanity's Last Exam, GPQA Diamond, Terminal-Bench and long-context reasoning), the best open-weight models sit **about six points behind the best proprietary model**: Claude Fable 5.1 at 66, Kimi K3 and GLM-5.3 at 60, Qwen3.8 at 58. But that average hides a shape. Open models are **at or above parity on retrieval, embeddings, reranking, structured extraction, classification and OCR**, within a few points on general coding and reasoning, and still clearly behind on the hardest math and science reasoning, on multimodal breadth, and on long-horizon agentic work. The decision-relevant consequence is that model choice is not a procurement decision made once, it is a **per-step routing decision inside a single agent run**, and the axis you route on is task type, not vendor.

## The three claims worth keeping

**1. The cheap parts of the stack are already free.** Retrieval is the clearest case. The Qwen3 embedding family ships Apache 2.0 with a real 32,768-token context, its 8B model entered the MTEB multilingual leaderboard at number one, and Qwen3-Embedding-0.6B costs roughly **$0.011 per million tokens** to serve. If your agent does retrieval-augmented generation, there is no remaining argument for paying per token for the retrieval layer. Narrow generation is the second case: Qwen3.8-27B scores 52 on the composite, quantizes to about 14-17GB, and runs on one 24GB GPU doing classification, extraction, routing and routine drafting.

**2. Free weights are not free inference, and the crossover variable is utilization.** Most top open models are mixture-of-experts and their weights sit in VRAM. The footprint table is the useful part: gpt-oss-20b at 16GB runs on consumer hardware; Qwen3.8-27B at 14-17GB in 4-bit on a single 24GB card; gpt-oss-120b at roughly 80GB needs an H100-class GPU; **Kimi K3 at 2.8T parameters needs roughly 1.4TB of VRAM, an 8x B200 node, about $32K per month.** Plus headroom for the KV cache, which grows with context. The choice is not cheap-open versus expensive-API, it is a **per-token bill versus a GPU bill plus operational overhead**, and only utilization decides which is smaller.

**3. Nearly every open-model benchmark number is vendor self-reported.** Citing an August 2026 Morph analysis, the piece notes that none of the SWE-bench Verified entries tracked at the time were independently verified. The instruction is to treat any "we beat GPT-5.x" release claim as a hypothesis to test on your own data.

## How this relates to what the wiki already knows

**It is the commercial statement of a result this folder established as a research finding.** The [LLM routing page](llm-routing.md) has tracked the same claim from the research side for months: [TRACER (04-17)](2026-04-17-tracer-llm-routing.md) and the [Netflix state-of-routing survey (05-08)](2026-05-08-netflix-state-of-routing-model-serving.md) both argued that the right granularity for model selection is the request, not the deployment. What is new here is the **specific task taxonomy with a price attached**, which is what a routing policy actually needs and what most routing papers do not supply.

**It confirms the cloud-device thread from a third angle.** [Cloud-device hybrid agents (05-29)](2026-05-29-cloud-device-hybrid-agents.md) and [Perplexity's hybrid local-cloud deployment (06-04)](2026-06-04-perplexity-hybrid-local-cloud.md) both concluded that the durable pattern is a local model absorbing the high-volume, low-difficulty share of traffic with escalation to a frontier model on the rest. This piece says the same thing with 2026 prices and adds the boundary: escalate on hardest-reasoning, multimodal and long-horizon agentic steps, keep everything else local.

**The tension with the day's other cost signal.** The article's own routing advice assumes you can cheaply switch models per step. [SemiAnalysis's 4-hi HBM analysis (09-14)](../hardware/2026-09-14-semianalysis-4hi-hbm-bandwidth-over-capacity.md) points out that serving economics are dominated by amortizing one read of the weights across a large batch. **Routing across many small models fragments batches**, which is exactly how you lose the amortization that makes a GPU bill competitive with a per-token bill in the first place. Neither source prices that interaction, and it is the missing number for anyone actually building a self-hosted router: the throughput cost of model-switching granularity.

## Gaps

It is a survey post, not a measurement. The Artificial Analysis numbers are a snapshot of a leaderboard the author explicitly warns changes frequently. The self-host footprints are approximate 4-bit figures from public deployment notes. And it offers no routing *mechanism*, only a taxonomy: no confidence threshold, no escalation policy, no measured accuracy loss from routing wrong.

## Related pages

- [LLM routing](llm-routing.md)
- [Compute economics](../hardware/compute-economics.md)
- [Quantization](../inference-efficiency/quantization.md)
