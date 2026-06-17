# Looped Transformers / Iterative Latent Depth

Looped (or "universal") transformers add computation by applying the *same* shared block repeatedly, rather than stacking many distinct layers. The promise is parameter efficiency (one block, reused) and adaptive depth (loop more on hard inputs). The recurring cost is that naive sequential looping inflates latency and KV cache linearly with loop count, and that more loops do not monotonically help.

## Current state (as of 2026-06-17)

**The loop became a first-class scaling axis this week — three papers, three domains, one shared claim: iterative latent depth is orthogonal to width and data.**

- [LoopCoder-v2](../inference-efficiency/2026-06-17-loopcoder-v2-parallel-loop-transformer.md) (arxiv 2606.18023) — a 7B Parallel Loop Transformer (PLT) coder trained from scratch on 18T tokens. PLT makes loop count cheap via cross-loop position offsets (CLP) and **shared-KV gated sliding-window attention** (the KV is reused across loops, so the cache does not grow linearly). The headline empirical result: **two loops is optimal** (SWE-bench Verified 43.0→64.4, Multi-SWE 14.0→31.0), and **three-plus loops regress**. Diagnosis: loop 2 supplies the productive refinement; later loops give oscillatory, low-diversity updates while the fixed CLP positional-mismatch cost keeps accruing.
- [Looped World Models](2026-06-17-looped-world-models.md) (LoopWM, arxiv 2606.18208) — the first looped architecture for world simulation. One shared block iteratively refines the latent environment state, claiming up to **100x parameter efficiency** with *adaptive* loop depth scaled to each prediction step's complexity.
- *Solve the Loop: Attractor Models for Language and Reasoning* (Fein-Ashley & Rashidinejad, Kurate cs.LG #6, ai_rating 7.5) — frames reasoning as convergence to an attractor of a looped/recurrent dynamic, the theoretical sibling of the two architecture papers.

This crosses the wiki's ≥3-papers threshold for declaring a pattern.

## Open tensions

- **Saturation vs adaptivity.** LoopCoder finds *fixed* deep looping saturates hard at two loops for code. LoopWM claims *adaptive per-step* loop depth is a feature. The unresolved question: does adaptive depth dodge the oscillatory regression LoopCoder hits past loop 2, or just hide it? No paper yet ablates adaptive vs fixed looping on the same task.
- **KV cost is the gating constraint.** Looping is only practical because LoopCoder shares KV across loops (gated SWA). This ties the loop line to the wiki's KV-sharing thread ([Raschka's MHC/compressed-attention survey](../inference-efficiency/2026-05-17-raschka-llm-architecture-kv-sharing-mhc-compressed-attention.md), 05-17): sharing KV across loops is the same instinct as sharing it across heads/layers.
- **Test-time-compute framing.** Looping is a form of test-time compute that does not lengthen the output. That makes it a different lever from chain-of-thought; the LoopCoder result (a hard ceiling on useful loops) parallels the broader finding that scaling inference compute is non-monotonic, echoing the [Extrapolation Cliff](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md) (05-14, a closed-form threshold past which on-policy distillation collapses).

## Related concepts

- [attention-mechanisms](attention-mechanisms.md) — shared-KV gated SWA is the enabling attention design.
- [kv-cache](../inference-efficiency/kv-cache.md) — KV-across-loops sharing is what keeps looping affordable.
- [Variable-Width Transformers](../inference-efficiency/2026-06-17-variable-width-transformers.md) — the width-allocation efficiency axis, orthogonal to looped depth.
