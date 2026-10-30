# Stop Guessing Your vLLM Config: Benchmarking LLMs on Runpod (Chris Vela, Runpod)

**Channel:** AI Engineer
**Published:** 2026-10-28
**Source:** https://www.youtube.com/watch?v=P_0_Th_ZzIg

## TL;DR
A Runpod forward-deployed engineer pitches BenchPod, an unreleased Docker template that wraps vLLM's OpenAI server with a FastAPI control plane, a metrics dashboard, a self-healing watchdog and hot config swaps so you can A/B serving configs without a full cold start. The useful message is methodological: vLLM recipes are a proven starting point but not production configs, so sweep the knobs against your real concurrency and target metric (TTFT, ITL, TPOT) before shipping. The demo itself is thin: one knob (`max_num_batched_tokens`) on Kimi K3 on a B300, and its headline finding runs against vLLM's own tuning guidance.

## Key Takeaways
- **Common failure modes seen at customers:** wrong vLLM version (new models like Kimi K3 do not run on 0.27, need nightly), wrong CUDA (K3 failed on CUDA 12.8, worked on 13.0), oversized context windows, and picking the smallest/cheapest GPU while ignoring KV-cache needs under concurrency.
- **Start from the use case.** Coding agent vs summarization, and number of concurrent users, decide model size, context length and GPU. A 1M context model is often unnecessary.
- **Do not ship day-0 models.** Expect hallucinations and immature kernels for the first days after release.
- **BenchPod features:** prebuilt image per vLLM version, model selection, watchdog auto-restart (survived a GPU failure on a 4-node internal K3 deployment), ~9 min K3 cold start, live metrics persisted to storage, all exposed via FastAPI so an agent can drive experiments. Promised release end of the month.
- **Demo result:** sweeping concurrency 1, 8, 64, 192 while raising `max_num_batched_tokens` barely moved TTFT but cut inter-token latency noticeably, so long jobs finished faster than with the recipe default.
- **K3 on one B300 node:** cannot reach the full 1M context, roughly half fits. Still enough for long coding-agent tasks.
- **Right-size the model:** a B200 node runs about $40k/month on Runpod. DeepSeek on 4x H200 handles most of their work; K3 is reserved for long, detailed tasks. Internal team of ~50 users largely moved off hosted Claude to self-hosted K3, GLM, DeepSeek and Qwen, and is eyeing smart routers next.

## Architecture & Optimization Mechanics
- **`max_num_batched_tokens` is the chunked-prefill token budget per scheduler step.** vLLM's docs state the textbook tradeoff: smaller budgets (around 2048) improve ITL because fewer prefill tokens stall decodes; larger budgets improve TTFT and throughput (>8192 recommended for throughput). The demo shows the opposite pattern (ITL improves, TTFT flat). Plausible explanations: the budget was not binding at low concurrency, prompts were short, or at high concurrency the larger budget let more decodes batch per step. Without the prompt/output length distribution, the result does not generalize.
- **Hot reload is the real productivity win.** For multi-hundred-GB MoE checkpoints, weight download plus load dominates experiment time (30 min first time, 9 min cold start). Keeping weights on a persistent volume and restarting only the engine makes config sweeps practical.
- **Concurrency sweep is the right axis.** KV-cache pressure, preemption and batch shape only show up at 64-192 concurrent requests. Single-user benchmarks say nothing about production cost per token.
- **What is missing:** no goodput or SLO-constrained throughput, no prefix-cache hit rates, no comparison of TP/EP/DP layouts or quantization formats, which are the knobs that matter most for a 2.8T MoE.

## Grounded Context (Web Enrichment)
vLLM shipped day-zero Kimi K3 support around late July 2026, with its own recipe starting at 8x GB300, and a September 2026 vLLM post reported 2.2-2.8x higher B300 throughput versus v0.27.1, which matches the speaker's warning that older versions are not viable. SemiAnalysis InferenceX measures K3 (2.8T MoE) on B300 with vLLM FP4 at about 6,083 tok/s/GPU at 50 tok/s/user, peaking near 12.6k tok/s/GPU. NVIDIA's Dynamo recipe confirms the 1M-token context and targets GB200/GB300 racks, consistent with a single B300 node only fitting about half. A mid-October vLLM post reportedly showed 8x AMD MI355X beating an HGX B300 on an agentic workload, so the "rent the newest NVIDIA box" default is already being challenged on price/performance.

The vLLM optimization guide directly contradicts the generalizable reading of the demo: lower `max_num_batched_tokens` is the documented lever for ITL, higher for TTFT. Treat the talk's result as workload-specific, which ironically is the talk's own argument for benchmarking rather than trusting folklore. BenchPod itself was not yet public at recording time, and vLLM already ships `vllm bench serve` plus parameter sweep tooling, so the novelty is the dashboard and hot-swap, not the measurements.

## Real-World Application / Actionable Step
- **Build a sweep harness, not a dashboard.** For every model Amit serves, run `vllm bench serve` with his real prompt/output length histogram at concurrency 1/8/64/192, sweeping `max_num_batched_tokens` (2048, 8192, 16384), `max_num_seqs`, KV dtype (FP8 vs BF16) and quantization (FP8, INT4/GPTQ, FP4 on Blackwell). Optimize for SLO goodput (e.g., p95 TTFT < 1s and ITL < 50ms), not mean throughput.
- **Pin versions per model.** Store (vLLM version, CUDA, driver, config YAML) alongside every benchmark result. Half the failures in this talk are version drift.
- **Routing angle:** the team's ad hoc policy (DeepSeek on 4x H200 by default, K3 for long hard tasks) is a manual router. A difficulty classifier that sends only long-horizon tasks to the 2.8T model could cut a $40k/month node to a fraction of its load. This is a ready-made case study for Amit's routing work.
