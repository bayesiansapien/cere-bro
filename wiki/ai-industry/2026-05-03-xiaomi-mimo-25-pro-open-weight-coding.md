# Xiaomi MiMo-V2.5-Pro — Open-Weight Long-Horizon Coding at 40-60% Fewer Tokens

**Source:** The Decoder
**Raw:** [raw/rss/2026-05-03-the-decoder-xiaomis-open-weight-mimo-v25-pro-takes-aim-at-claude-op.md](../../raw/rss/2026-05-03-the-decoder-xiaomis-open-weight-mimo-v25-pro-takes-aim-at-claude-op.md)
**URL:** https://the-decoder.com/xiaomis-open-weight-mimo-v2-5-pro-takes-aim-at-claude-opus-with-hours-long-autonomous-coding/
**Date:** 2026-05-03
**Tier:** 1/2 — open-weight long-horizon agent + token efficiency

## TL;DR

Xiaomi released MiMo-V2.5-Pro, an open-weight model that nearly matches Claude Opus 4.6 on coding benchmarks while burning **40–60% fewer tokens per task** (per company-reported numbers). Positioned for hours-long autonomous coding tasks. The framing in the article: the Chinese open-weight competition (DeepSeek, Xiaomi, Moonshot, Qwen) is shifting from "raw benchmark scores" to "how cheaply and how long a model can run autonomously on a single task."

## Key claims

- Near-parity with Claude Opus 4.6 on coding benchmarks (specific numbers in the post; The Decoder's RSS extract is the headline only)
- 40–60% fewer tokens per task than the comparison model — *the operative metric is now per-task cost, not capability ceiling*
- Hours-long autonomous coding focus — long-horizon agent positioning
- Open-weight release

## Why this matters for cere-bro (Tier 1)

This is the biggest open-weight competitive-pressure data point of the past 72 hours, and it lands directly on three Tier-1 threads:

1. **Tokens-per-task is the new pricing axis, not benchmark score.** SemiAnalysis (05-01) argued AI lab pricing power persists because the closed-best/open-best gap is not closing on capability. Xiaomi's framing inverts this: they concede the capability ceiling and compete on per-task cost. If the 40–60% number generalizes beyond their internal evaluations, the pricing pressure on closed labs comes through *efficiency*, not ceiling. This is the structural pressure that SemiAnalysis's thesis did not anticipate.
2. **Long-horizon coding agents intersect Step-level Optimization (05-02).** A model designed for hours-long autonomy *is* a model whose tokens-per-step matters. Whether MiMo-V2.5-Pro's efficiency comes from architecture (MoE? hybrid SSM?), training (on-policy distillation à la TIP/CoPD?), or trajectory shaping (LenVM-style length value heads, 05-01) is the open empirical question. The The Decoder post does not reveal the mechanism.
3. **Open-weight onshoring + Chinese frontier labs.** Pairs directly with Moonshot/StepFun onshoring (05-01) and the broader China vs US benchmark debate (US benchmark says China is 8 months behind; Xiaomi's release is a counter-data-point on cost-efficiency). The bilateral AI sovereignty thread continues.

## Open questions

- **Mechanism of 40–60% token reduction.** No public technical detail in the headline. Candidates: MoE sparsity, length-aware reward shaping (LenVM 05-01 is open-weight reference), distillation from a stronger teacher (CoPD 05-01 paradigm), better tokenizer for code, RL-tuned chain-of-thought truncation. First independent third-party replication or technical post will resolve this.
- **Real-world long-horizon evaluation.** "Hours-long autonomous coding" deserves Claw-Eval-Live (05-01) or InteractWeb-Bench (05-01) numbers. As of 2026-05-04 none published.
- **Comparison ceiling on multi-step composability.** Lower per-step cost but higher per-step variance could blow up cumulative variance over hours. The trajectory-routing literature (Step-level Optimization 05-02) is the right framework to evaluate this.

## Connections to prior wiki pages

- **SemiAnalysis AI Value Capture (05-01)** — counterpoint. Xiaomi's release is the open-weight efficiency competition SemiAnalysis did not weight heavily.
- **LenVM token-level length value model (05-01)** — candidate mechanism for token reduction.
- **CoPD Co-Evolving Policy Distillation (05-01)** — candidate mechanism for capability transfer.
- **Step-level Optimization (05-02)** — orthogonal axis. Xiaomi's reduction is per-step; Step-level Optimization is per-trajectory. Composing them is the deeper efficiency play.
- **China AI startups onshoring (05-01)** — same week, same theme.
- **The Decoder: China is falling behind (05-03)** — direct contradiction of the US-government-benchmark framing.

## Worth Watching

- **Independent third-party benchmark in 30 days.** Aider, SWE-Bench Verified, and Claw-Eval-Live (05-01) for token-cost-per-resolved-task. If 40–60% replicates, this is a new pricing baseline; if it doesn't, the figure was task-specific.
- **Mechanism disclosure in 60 days.** A model card or technical report. The mechanism determines whether the efficiency is generalizable.
- **Closed-lab response in 90 days.** If Anthropic or OpenAI ships an explicit "tokens-per-task" pricing tier or efficiency variant, the pricing axis has shifted. Tracker: any new Anthropic or OpenAI release framed around per-task cost rather than capability.
