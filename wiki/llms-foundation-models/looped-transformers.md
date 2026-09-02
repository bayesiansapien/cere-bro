# Looped Transformers / Iterative Latent Depth

Looped (or "universal") transformers add computation by applying the *same* shared block repeatedly, rather than stacking many distinct layers. The promise is parameter efficiency (one block, reused) and adaptive depth (loop more on hard inputs). The recurring cost is that naive sequential looping inflates latency and KV cache linearly with loop count, and that more loops do not monotonically help.

## Current state (as of 2026-09-02)

**The loop-count question is settled to two, by a second paper that got there independently and brought a mechanism.** [SMELT (09-02)](2026-09-02-smelt-moe-looped-transformers.md) (arxiv 2609.01343, Tsinghua / ByteDance Seed / M-A-P / TokenWave.AI) is the first study to compare looped against unlooped models while matching **three budgets simultaneously**: per-token FLOPs, total non-embedding parameters, and KV cache. MoE is what makes that feasible, because it decouples total parameters from per-token FLOPs, so you can narrow the hidden dimension to hold FLOPs fixed and then raise the expert count to recover capacity. The surviving recipe is **loop the middle half of the layers twice**, leaving early and late layers single-pass. Scaled across four sizes to 54B non-embedding parameters with a separate Chinchilla-style law fit per architecture, it saves **6.8 to 18.0% of training FLOPs on the compute-optimal frontier**, with the advantage largest on Code and *growing* with sequence length and in-context example count.

**Why this is the important entry on this page.** The page's headline finding since 06-17 has been LoopCoder-v2's empirical result that **two loops is optimal and three-plus regress**, with a diagnosis (later loops give oscillatory low-diversity updates while the positional-mismatch cost keeps accruing) but no account of why the *second* loop is productive. SMELT supplies one: the second visit **reduces the attention sink**, the pile-up of attention mass onto a few early or delimiter tokens carrying almost no information, and redirects that mass toward content-relevant tokens. Two papers, two and a half months apart, different scales, dense versus MoE, loose versus strict budget control, same loop count, and now one mechanism. **This crosses from "an empirical ceiling somebody found" to "a property of the architecture."** It also explains the shape of the gains: attention sinks cost most when there is a lot of context to discriminate among, which is why the advantage grows with sample length and in-context examples rather than being a fixed offset.

**Two of this page's three open tensions move.**

- **"Saturation vs adaptivity" is now half-resolved and better posed.** SMELT lands hard on the fixed-depth side and adds a dimension the tension did not have: loop depth should vary by **layer position**, not by input. LoopWM's claim for *adaptive per-step* depth is untouched but now looks like the minority position. The sharpened open question: nobody has ablated adaptive-per-input against fixed-middle-half looping on the same task under matched budgets, and until someone does, "loop the middle twice" is the default and adaptivity is the burden of proof.
- **"KV cost is the gating constraint" is superseded by a stronger framing.** The page recorded that looping was only practical because LoopCoder-v2 shared KV across loops via gated sliding-window attention. SMELT does not need a KV-sharing trick, because it treats KV cache as a **budget to hold constant** rather than a cost to mitigate. That reframing matters beyond looping: KV size bounds the longest servable context, so a looped model that quietly needs a larger cache is not a drop-in replacement at serving time regardless of its loss curve. **Matching KV is a precondition for the loop's benefit being a well-defined quantity at all.**

**The unresolved axis is now latency, not loss.** Looping serializes computation, so matched FLOPs is not matched wall-clock, and SMELT reports the frontier saving in training FLOPs without addressing serving latency. Concurrent MoE-looping work (MoEUT, LoopMoE) matched **wall-clock time** instead. Those two literatures are optimizing different objectives and no head-to-head exists, which is the cleanest experiment anyone could run on this page right now.

**It also puts a claim on [scaling-laws.md](scaling-laws.md).** SMELT's frontier saving is only legible because it fits a *separate* law per architecture; one law across both would average the effect away. That is a third kind of failure of the received law, distinct from Skaling's misspecified additive form (08-10) and LLaDA's cross-objective transfer failure (08-05): a claim that **architecture belongs inside the law**.

---

## Prior state (as of 2026-06-17)

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
