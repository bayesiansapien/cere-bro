# GPT-6.2 Astra Is INSANE! Gemini 4 Neon, OpenAI AGI CONFIRMED?!, Claude Code UPGRADES & MORE! AI NEWS

**Channel:** WorldofAI
**Published:** 2026-11-17
**Source:** https://www.youtube.com/watch?v=WRdgKyOTPXA

## TL;DR
A rumor-heavy weekly roundup. The signal: Tencent's **Hy4 Flash** (224B MoE, 12B active, 1M context, $0.07/$0.28 per M tokens) is the week's most important release for cost-optimized routing. OpenAI signed **embedded safety assessments** with METR, Apollo, Transluce and Goodfire. Codex fixed capacity errors. Anthropic described its Claude Code verification workflow. The noise: GPT-6.2 Astra "leaks" via Chinese API relays and a hidden chart row, Gemini 4 "Neon/Oxygen" log strings, and an unsourced "Altman: we didn't have AGI, now we do" quote that I could not verify.

## Key Takeaways
- **GPT-6.2 Astra (unconfirmed):** ~75 days since GPT-6 Astra, the long end of OpenAI's 28 to 77 day cadence. Relay-service "access" since ~Nov 11 produced impressive single-prompt 3D game demos. A leaked Bio Basics Bench row (89% vs 67% for GPT-6 Astra) was found via devtools and is unverified. Delay attributed to safety/alignment work.
- **Tencent Hy4 Flash:** blind test of 85 users and 259 tasks rated it 2.79 vs 2.81 for Claude Haiku 5.5 (highest thinking). Average task cost $0.04 vs $0.71, ~18x cheaper. Fastest tested at ~6.7 min/task, >150 tok/s. 50% off until Nov 30. Open weights promised.
- **Gemini 4 family:** Carbon, Argon and Hydrogen are live in Antigravity, with context doubled from 256k to 512k. "Oxygen" looks like a stronger Flash. "Neon" appears as both a model and an Ultra-adjacent subscription tier.
- **Codex reliability:** capacity errors fell from 6.89% of DAU (peak) to 0.085% by Nov 12 after better retries, backoff and WebSocket handling. That is overload handling, not added compute.
- **Claude Code verification:** Claude now writes and reviews ~90% of the Claude Code team's code. A `/verify` skill runs the app and tests inputs, and escalates to a human after 3 failed attempts. There are 39 regression-derived checks, with the relevant ones selected per change.
- **Other:** Hugging Face models routable through OpenRouter (auto provider selection plus failover, traces saved to HF). Microsoft MAI Code 2 Flash expected at Ignite. OpenAI self-reported ~2x researcher productivity (n≈1,800) and healthcare computer-use plugins. Open Code Browser rewritten in Rust (25x less memory, Playwright dependency dropped). An Anthropic researcher gave a "1.3 years to broadly superhuman AI" timeline. ~1,000 people in 6 countries marched for an AI treaty.

## Architecture & Optimization Mechanics
- **Hy4 Flash is the routing story.** At 224B total and 12B active, it is extremely sparse (~5% active). Reporting says 64B of the parameters are "Engram" parameters, i.e. a conditional memory/lookup component separate from the experts. That points to decoupling knowledge storage (cheap lookup) from compute (active experts), a direct lever on MoE memory/compute trade-offs. Per-token decode cost tracks 12B active, while HBM footprint tracks 224B, unless the Engram tables can be offloaded to host memory or CXL.
- **Quality-per-dollar frontier:** near-Haiku-5.5 satisfaction at ~1/18 the cost makes it a strong default tier for a cascade router, with escalation on verifier failure.
- **Verification as the scaling bottleneck:** Anthropic's 39-check, select-relevant-subset pattern is a learned/heuristic router over test suites. Applying the same idea to eval suites in compression work (choose the eval subset most sensitive to the change) cuts iteration time.
- **Context growth plus less compaction** (512k, "3.5x fewer compactions" claimed) makes KV-cache compression and offload the binding inference constraint for agent workloads.

## Grounded Context (Web Enrichment)
Verified: Tencent launched Hy4 Flash on Nov 16, 2026, with list pricing of $0.070 input, $0.281 output and $0.003 cached per M tokens. The model is a 224B MoE (incl. 64B Engram parameters) with 12B active, 1M context, and text plus vision input. Tencent claims average cost per task is 1/20 of full Hy4. That is a per-task, not per-token, ratio. Its Haiku comparison is Tencent-internal and not independently reproduced. The safety story is also real: OpenAI announced "embedded assessments" (Nov 13 to 16). Six Apollo evaluators embed for four months on covert goal pursuit, METR examines OpenAI's largest RL run to date, Transluce audits post-training alignment eval coverage, and Goodfire does interpretability on training. METR and Transluce take no cash compensation, and OpenAI reserves the right to request disclosure delays.

Unverified or weak: I found no source for the "we didn't have AGI, now we do" quote. Altman's documented stance through 2025 was that "AGI" is not a useful term and that it may have "whooshed by". Treat the video's AGI and RSI framing as speculation. The GPT-6.2 Astra relay "access" is not a credible evaluation channel, since relays routinely misreport model identity. The "board won't reinstate Jensen" item is confirmed (see the DOAC Nvidia page).

## Real-World Application / Actionable Step
- **Benchmark Hy4 Flash this week while it is 50% off (until Nov 30):** run your router's held-out task set through it as the cheapest tier and measure the escalation rate vs Haiku 5.5. If the open weights ship, profile Engram-table offload (HBM vs host) on vLLM.
- **Read Tencent's Engram description** for a compute/memory disaggregation idea transferable to your MoE memory work.
- **Adopt the "select relevant checks" pattern** for compression regression suites.
- **Discount relay "leaks"** entirely. Wait for official GPT-6.2 numbers.
