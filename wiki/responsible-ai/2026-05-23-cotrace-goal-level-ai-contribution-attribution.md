# CoTrace: Measuring Goal-Level AI Contributions in Collaboration

**Source:** HuggingFace daily papers, 2026-05-23. Title: "I didn't Make the Micro Decisions".
**arxiv:** [2605.21363](https://arxiv.org/abs/2605.21363)

## TL;DR

As LLMs increasingly shape how users form, refine, and extend their goals, attribution becomes critical — for users calibrating reliance and for evaluators assessing AI-assisted work. Existing methods focus on final artifacts and miss the process by which goals are jointly shaped. CoTrace decomposes explicit goals into verifiable requirements and traces direct contributions and indirect influences across dialogue turns. Applied to 638 real-world collaboration logs, the framework finds:
- Models account for only **11-26% of goal-shaping contribution** overall.
- Models contribute substantially more on lower-level concrete requirements (operational decisions), not high-level goal shaping.
- Various indirect contributions are pervasive (e.g. the model influencing which requirements get surfaced).
- Interaction design choices significantly affect model goal-shaping behavior in controlled simulations.
- Exposing participants to goal-level analyses shifts their perceived contributions by nearly 2 points on a 5-point scale, revealing systematic miscalibration.

## Why this matters

The wiki has tracked the AI contribution / agency question since the SemiAnalysis economics framing (cache hit rates dominate unit economics) and the Beijing summit policy thread (US-China AI dialogue, classified networks, governance). Both are macro framings. CoTrace is the micro: in a single user-LLM session, who is actually steering. The 11-26% headline number is the cleanest empirical answer the field has had to "how much of an AI-assisted work product is actually from the AI."

The 2-point shift in perceived contribution when participants see goal-level analyses is the responsible-AI implication. Users systematically miscalibrate their own contribution upward when they cannot see how the model influenced lower-level requirements. This is the same shape as the calibration crisis in non-AI human collaboration (overestimating one's own contribution), but with a specific intervention (goal-level analyses) that demonstrably corrects it.

## Connections to prior wiki state

- The 05-22 Eigenism paper (CAIS, on agent memory as an alignment rationale) said that giving agents memory provides a reason to align them; CoTrace says that *measuring* what agents contribute is the precondition for that alignment to be evaluable.
- The 04-17 ASGuard / interpretability cluster — CoTrace is a behavioral interpretability move at the collaboration level, not the model level.
- The [Kurate cs.LG #15 LLMs Know They're Wrong and Agree Anyway (the shared sycophancy-lying circuit)](../) lines up with CoTrace's "indirect influences" finding: models influence which requirements get surfaced, which is exactly the mechanism by which sycophancy distorts goal-shaping.

## Gaps

638 collaboration logs is a real corpus but small relative to the population of human-AI work products in flight. The 11-26% range is reported as an aggregate; per-domain decomposition (code vs writing vs research) would change which sectors are most exposed to the calibration gap. The user-study sample size is not in the abstract.

## Research angle

If CoTrace measurements correlate with downstream artifact quality (or with user task satisfaction), the framework becomes a practical evaluation tool, not just a measurement instrument. The cleanest follow-up: do work products with low model goal-shaping contribution (high human steering) outperform those with high model goal-shaping contribution on independent quality measures? If yes, the 11-26% range becomes prescriptive ("aim for less than 30% model contribution at the goal level"). If no, the framework is descriptive only.

## Raw source

[raw/huggingface/2026-05-23-i-didnt-make-the-micro-decisions-measuring-inducing-and-expo.md](../../raw/huggingface/2026-05-23-i-didnt-make-the-micro-decisions-measuring-inducing-and-expo.md)
