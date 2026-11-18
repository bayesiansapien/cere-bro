# "Where is all the automation?" Diogo Almeida, TypeSafe AI

**Channel:** AI Engineer
**Published:** 2026-11-15
**Source:** https://www.youtube.com/watch?v=Cyt3LU8TyNc

## TL;DR
Diogo Almeida (InstructGPT/RLHF co-author, now founder of TypeSafe AI) argues that AI looks superhuman on benchmarks yet barely automates real work because every frontier LLM is optimized for *assistance*: RLHF literally bakes a human verifier into the loop. Automation needs the opposite property, narrow and boringly reliable judgment that code can call without supervision. His pitch: treat a cheap, fast, reliable "semantic decision" model (TypeSafe's Jev) as a fourth logic gate inside ordinary software, and rebuild agents around real engineering (decomposition, verified stages, explicit state) instead of one giant KV cache. The talk is also an infomercial for Jev, so the diagnosis is stronger than the product evidence.

## Key Takeaways
- **Jaggedness explained by objective, not capability.** Models are superhuman where a human checks the output (deep research, chat, coding with review) and useless where nobody does (accounting, drive-through ordering). "Einstein 95% of the time, Mr. Bean 5% of the time, and you can't tell which" kills automation.
- **RLHF is the cause.** 100% of shipping LLMs are tuned for assistance; RLVR-only models are pleasant to nobody, so they get RLHF'd too. You get what you optimize for.
- **"Bitterest lesson" ladder:** compute > algorithms (Sutton), data > compute, and *choosing the right task* > data. Next-token prediction beat masked LM not because it was a better objective but because it enabled generation; RLHF's instruction-following gain dwarfed years of pretraining scale.
- **Fourth logic gate.** AND/OR/NOT built all of software; a reliable semantic primitive ("is this a real-looking Gmail address?") should expand software like the blue LED expanded LEDs from indicators to displays and white lighting.
- **Tyranny of the KV cache.** Agent designs that should work (shared state across parallel agents, map-reduce over full history, smarter sub-agent routing, sub-linear memory lookup) are abandoned because they break prefix caching, not because they are bad ideas.
- **Idea list for "software research":** real-time semantic security monitors, semantic dependent types in linters, encoding the *spirit* of rules to shrink principal-agent loopholes, anti-slop filters, do-what-I-mean interfaces.
- **Slop thesis:** slop exists because unreliable AI cannot be trusted with decisions that cost *you*, so its cost gets externalized onto readers.

## Architecture & Optimization Mechanics
- **Decision models vs generators.** Jev is non-generative: it returns typed, schema-constrained answers with probabilities instead of prose. Functionally it is a calibrated classifier/router exposed as an API. For a router this is exactly the right shape: no decoding cost, output space known in advance, confidence directly usable for thresholding and fallback.
- **Reliability as the target metric.** The claim is that narrow, calibrated reliability is what unlocks automation, and it does not show up on leaderboards. For routing work this maps to *selective prediction*: optimize coverage at fixed error rate, not mean accuracy.
- **KV-cache-aware agent design.** Cache-friendliness constrains architecture. Patterns he names as blocked:
  - parallel agents re-discovering the same codebase facts (no shared state)
  - O(N) memory instead of map-reduce over all past sessions
  - sub-agent routing that fails even when naive
  The opportunity is to pay prefill once and route/compress across cached segments (shared-prefix trees, cache-aware schedulers like SGLang RadixAttention) rather than abandon the pattern.
- **RLHF data efficiency anchor.** Original InstructGPT result: humans preferred a 1.3B RLHF model over 175B GPT-3 on OpenAI's prompt distribution, roughly a 100x parameter gap closed by changing the task. His "GPT-2 sized model matches GPT-7 to 9" line is rhetorical extrapolation, not a measured number.

## Grounded Context (Web Enrichment)
TypeSafe launched Jev on 15 Sep 2026 as a "System One" model: typed outputs with probabilities, aimed at machine-to-machine decisions (automation, real-time checks, map-reduce classification over large corpora, verifying AI inputs, model harnesses). The startup has about $40M in funding. Access is closed, hosted and waitlisted with no open weights; current stable is `jev-1.13.0`. All performance numbers are TypeSafe's own evaluations, and independent coverage flags that bias. So the talk's "people love Jev for reliability" is unverified marketing.

The RLHF anchor holds up: Ouyang et al. (2022) report the 1.3B PPO-ptx InstructGPT preferred over 175B GPT-3, and 175B InstructGPT preferred about 85% of the time over 175B GPT-3. The broader diagnosis (assistant-tuned models are miscalibrated for unattended use) is widely shared. But "nobody can automate accounting" is overstated: production document-extraction and reconciliation agents exist. They just wrap LLMs in verification layers, which is his point, restated.

## Real-World Application / Actionable Step
- **Reframe your router as a decision model.** Benchmark it on risk-coverage curves (error at 80/90/95% coverage), not average accuracy. Escalate to the large model only below a calibrated confidence threshold.
- **Test a non-generative classifier head as the router.** Use a small distilled encoder or a constrained-decoding single-token head. Compare latency and calibration against an LLM-as-router prompt. Jev itself is waitlisted, so build the open equivalent.
- **Audit your agent stack for KV-cache-driven compromises.** Find places where you dropped shared state or sub-agents purely for cache hit rate. Prototype a shared radix-prefix cache across parallel agents and measure prefill savings.
- **Distillation angle:** distill assistant-tuned teachers into *narrow, reliability-optimized* students (one schema, calibrated logits) rather than general chat students. That is where compression buys automation value.
