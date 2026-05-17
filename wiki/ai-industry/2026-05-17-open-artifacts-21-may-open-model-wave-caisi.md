# Open Artifacts #21: The May 2026 Open-Model Wave and the CAISI / ECI Gap

**Source:** Interconnects by Nathan Lambert (Gmail-starred 2026-05-16, [raw/gmail/2026-05-17-starred.md item 1](../../raw/gmail/2026-05-17-starred.md))
**Original:** [interconnects.ai/p/latest-open-artifacts-21-open-model](https://www.interconnects.ai/p/latest-open-artifacts-21-open-model)
**Tier:** 2 (industry, open-model strategy, evaluation methodology)
**Date:** 2026-05-16

## TL;DR

May 2026 was the most concentrated open-frontier model release month since Mixtral 8x7B in late 2023. Six labs shipped frontier-tier MoE weights inside roughly two weeks: Gemma 4 (Google, Apache 2.0, 4B / 9B / 31B dense plus 26B-A4B MoE), Kimi K2.6 (moonshotai, long-horizon focused), GLM-5.1, Qwen3.6 (35B-A3B variant open, Plus closed), Laguna XS.2 (poolside, 33B-A3B coding-focused), MiMo-V2.5-Pro (XiaomiMiMo, Apache 2.0), and DeepSeek V4 (Pro 1.6T-A49B, Flash 284B-13B). In parallel, the US Center for AI Standards and Innovation (CAISI) published an Item-Response-Theory-based Elo comparison showing that open models are falling behind US closed frontiers and the gap is widening. Lambert and his co-author Florian disagree on the interpretation: Florian argues the Elo gap is partly an artifact of evaluating open models without their preferred harness (so the comparison runs models in a strict bash-plus-token-budget setup rather than inside Claude Code or OpenCode); Nathan thinks the benchmarks are imperfect but the gap is real.

## Key signals

1. **CAISI's evaluation methodology.** Item Response Theory is used to roll a model's performance across nine benchmarks (CTF-Archive-Diamond run on a subset, PortBench private, ARC-AGI-2 with non-public scoring) into an Elo score. The choice of benchmarks and the IRT extrapolation drive the headline gap. The same methodology applied to closed-frontier coding tasks evaluated without the model's preferred harness reproduces the gap. The 1M-LOC Bun port from Zig to Rust (reported in the original post) is the existence proof that real-world capability is being underestimated by the harness-naive evaluation.
2. **Epoch AI's ECI (Epoch Capabilities Index) tells a softer story.** ECI also uses IRT over a set of different benchmarks and reports the gap roughly stays between 3-7 months since DeepSeek R1's release in early 2025. Two IRT-based methodologies giving different headline numbers is the signal that the methodology itself, not the underlying capability, drives the conclusion.
3. **Six labs' picks.**
   - **MiMo-V2.5-Pro** (Xiaomi, Apache 2.0): neck and neck with Kimi K2.6 and GLM-5.1 on benchmarks and real-world usage.
   - **Gemma 4 26B-A4B** (Google, Apache 2.0): KV-sharing plus per-layer embeddings, 31B dense variant is the post-training-friendly option (see Raschka 05-16 deep dive).
   - **Kimi K2.6** (moonshotai): long-horizon-task focus, can run hours of autonomous work, important for autoresearch-class systems.
   - **Laguna XS.2** (poolside, 33B-A3B): first public release, coding-focused, blog post catalogs reward hacking observed during coding evaluations.
   - **DeepSeek-V4-Flash** (DeepSeek, 284B-13B): the surprise of the release. Pro (1.6T-A49B) is reported to underdeliver relative to its size; Flash is the model practitioners are actually using.
4. **Fireworks training-platform updates (Gmail item 2).** Kimi K2.6 full-parameter tuning with 256K context now available; GLM 5.1 LoRA RL live; Qwen3.6 27B fully enabled (128K and 256K); Gemma 4 Dense Full-Param + LoRA RL with SFT/DPO/RL on 256K. The training-platform layer is now keeping pace with the model-release cadence at 1-2 week lag.

## Connections to the wiki

**Industry strategy thread.** Anthropic crossing $900B on 05-15, Microsoft pulling Claude Code internally on 05-15, and the open-frontier wave landing at the same time form one coherent story: the closed-model API is a commodity, the value capture sits in the agent harness (Microsoft's bet) and in the integrated training stack (Anthropic's bet, Fireworks' bet on a third platform layer). The Gurley "Open Source Strategy" essay (retweeted via @bayesiansapien on 05-16) predicts Chinese open models become the global default by 2030; the May 2026 wave is the supply-side evidence the prediction is on track.

**Architecture thread.** All six new MoEs use architectural innovations that the wiki's Raschka summary (05-17) catalogs: KV sharing (Gemma 4), layer-wise attention budgeting (Laguna XS.2), compressed convolutional attention (ZAYA1-8B in the same wave but not in Interconnects' picks), mHC plus compressed attention (DeepSeek V4). The same week saw MoE-muP land on Kurate (cs.LG #13, ai_rating 9.0): the theoretical recipe for scaling these architectures is being published exactly as the empirical evidence accumulates.

**Evaluation methodology thread.** WildClawBench's 18-point harness spread (05-15) is now the canonical example of why benchmark Elo rankings can underestimate real-world capability for models trained against specific harnesses. CAISI's IRT-Elo approach is one specific instance of the failure mode. The wiki should treat any cross-lab capability comparison that does not control for harness as suspect.

## Worth Watching

- **CAISI re-evaluation with preferred-harness control.** 60 days. Falsifiable: a published re-run of CAISI's IRT-Elo with each model evaluated in its preferred harness (Claude Code for Claude, OpenCode for OpenAI, Qwen-CLI for Qwen, Codex CLI for Codex). The expectation, based on WildClawBench's 18-point spread, is that the open-closed gap compresses by 5-10 Elo points or roughly half the reported gap.
- **DeepSeek V4 Flash vs Pro adoption curve.** 30 days. If practitioners continue to pick Flash over Pro, the wiki should treat this as the first empirical evidence that the "scale beats recipe" prior is breaking even within one lab's release.
- **Fireworks Training Platform RLVR throughput.** 60 days. Full-param RLVR on Kimi K2.6 256K context is a substantial commodification of the agentic post-training stack the wiki has been tracking (Orchard, SDAR, EvoEnv from 05-15). Watch for whether labs producing the new MoE wave standardize on Fireworks as the training surface vs maintaining their own pipelines.

## Links

- Original post: [interconnects.ai](https://www.interconnects.ai/p/latest-open-artifacts-21-open-model)
- Raw: [raw/gmail/2026-05-17-starred.md](../../raw/gmail/2026-05-17-starred.md)
- Related wiki: [Raschka architecture deep dive 05-17](../inference-efficiency/2026-05-17-raschka-llm-architecture-kv-sharing-mhc-compressed-attention.md), [MoE-muP 05-17](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md), [WildClawBench 05-15](../agentic-systems/2026-05-15-wildclawbench-native-runtime-agent-benchmark.md)
