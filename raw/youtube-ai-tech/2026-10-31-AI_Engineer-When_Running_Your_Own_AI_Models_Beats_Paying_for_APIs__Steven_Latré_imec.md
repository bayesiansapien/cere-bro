# When Running Your Own AI Models Beats Paying for APIs (Steven Latré, imec)

**Channel:** AI Engineer
**Published:** 2026-10-31
**Source:** https://www.youtube.com/watch?v=9-Y_oS9OBLc

## TL;DR
imec (the Belgian semiconductor R&D lab) ran 1,000+ agentic coding runs on SWE-bench Pro across three harnesses (Codex, Claude Code and a third), API baselines and open-weight models (Qwen, DeepSeek, GLM, Kimi K3), each mapped to its smallest viable GPU config. Main findings: (1) the cost curve against accuracy is a **step function**, since model choice decides the hardware tier. (2) **Concurrency, not accuracy, decides self-hosting viability.** Kimi K3 gave ~86% resolve but only ~4 comfortable concurrent users per node at ~3x API latency. (3) Break-even GPU utilization is **~89% on low-tier hardware** (infeasible) versus **~15% on 8×B200** (realistic), with GLM-class models the sweet spot and **~25% TCO savings** for coding assistance. (4) The harness doesn't change accuracy but **Codex halved token generation and GPU wall time** with GLM. Once you pay for GPU-hours, harness choice is a cost lever.

## Key Takeaways
- **AI-maturity path:** frontier APIs, then cost optimization and routing, then self-hosted open weights on leased GPUs, then owned infrastructure. Routing is the "low-hanging fruit" phase. Owning the stack blows up the design space (model trust, CPU:GPU balance, KV-cache, inference engine).
- **Accuracy tiers (SWE-bench Pro, resolve rate):** Qwen and DeepSeek ~32-40%. GLM about Opus-level. Kimi K3 ~86%, which the speaker flags as likely training-set contamination.
- **Hardware non-linearity:** Qwen vs DeepSeek is about equal accuracy for **4x** the GPU rental cost. GLM to Kimi K3 is **+20% accuracy for +15% rental cost**. Choosing a slightly smaller model can drop you a whole hardware tier.
- **Concurrency wall:** KV-cache for long-horizon agent trajectories dominates memory. Big models on big nodes still support very few users at worse latency than the Claude Code API baseline.
- **Break-even utilization:** low-tier systems need ~89% GPU utilization to beat API pricing, 8×B200 only ~15%. GLM-class is where self-hosting starts to win, ~24.5% TCO savings for this workload.
- **Harness efficiency:** same resolve rate across harnesses, but Codex + GLM produced ~50% of the tokens and ~50% of the GPU wall time of the others.
- **Not covered yet:** quantization, speculative decoding (applied but not studied), mixed enterprise workloads. imec plans a public benchmark dataset and a hardware-software alliance.

## Architecture & Optimization Mechanics
- **KV-cache is the binding constraint for agentic workloads.** Long-horizon coding sessions hold 50-200k-token contexts per user. Capacity = (HBM − weights) / (per-user KV size). This is why MoE models with huge total parameters (Kimi K3, DeepSeek) can't serve many users: weights eat HBM even when active parameters are small. MLA/GQA, KV quantization (FP8/INT4 KV) and prefix sharing across a team's repo are the direct levers.
- **Step-function cost:** the cost-optimal model sits just under a hardware-tier boundary. Compression that moves a model down one tier (e.g. INT4 weights to fit on 4 GPUs instead of 8, or one node instead of two) is worth far more than its percent-accuracy cost suggests.
- **Utilization economics:** big nodes break even at low utilization because per-token cost falls superlinearly with batch size up to the KV limit. Small nodes can't batch enough. Routing that concentrates traffic onto one well-batched model beats spreading it across many small endpoints.
- **Harness as a decode-cost multiplier:** tokens generated per task varies ~2x by harness. For self-hosted decode-bound serving, that is a 2x throughput difference with no model change. Measure tokens per resolved task, not tokens per second.

## Grounded Context (Web Enrichment)
A republished copy of imec's write-up (originally on its aistack site, 23 July 2026) gives different concurrency figures from the talk: **Kimi K3 at 16 concurrent sessions vs GLM-5.2 at 24**, with K3 throughput ~30% lower (122 vs 170 tok/s at 16 users) and median task time ~50% longer (38 vs 26 min). The talk's "4 comfortable users" likely uses a stricter latency SLO. Treat the absolute numbers as configuration-dependent and the ranking as the robust finding. imec itself warns about K3 contamination on SWE-bench Pro, and no official K3 SWE-bench Pro score could be confirmed (aggregators list K3 at ~93% on plain SWE-bench). Moonshot shipped Kimi K3.1 Pro in October 2026, so the model frontier has already moved past the study.

Independent analyses agree on the direction. One estimates an 8×B200 node must sustain ~814 tok/s around the clock to match Kimi K3's API price. Another finds single-node hardware at $11-16k/month vs ~$30k Anthropic list price for a team, but much higher at frontier-class concurrency. The consensus caveat: "is self-hosting cheaper" has no general answer without workload, peak and latency tolerance. imec's 25% savings is real but narrow, for one workload with high sustained use.

## Real-World Application / Actionable Step
- **Add hardware tier to the routing objective.** For each candidate model, record minimum GPU config, max concurrency at a target p95 latency, and tokens per resolved task. Route on cost per resolved task at the needed concurrency, not $/Mtok.
- **Target compression at tier boundaries.** Find models sitting just above a node-size threshold (e.g. GLM-class at FP8 needing 8 GPUs). Test INT4 weights (GPTQ/AWQ) plus FP8 KV-cache in vLLM to drop a tier, and measure SWE-bench Pro resolve delta against the concurrency gain.
- **Benchmark KV compression for agent traces.** Long-horizon agent contexts are an underexplored setting for KV eviction and quantization (SnapKV/H2O-style, KV-FP8/INT4). imec says it hasn't studied it, so it's a publishable gap.
- **Count harness tokens.** If self-hosting, run your agent harness against Codex-style concise harnesses on the same model and track generated tokens per task. A 2x reduction beats most kernel work.
- Watch for imec's public benchmark dataset and alliance as a possible collaboration venue on hardware-aware routing.
