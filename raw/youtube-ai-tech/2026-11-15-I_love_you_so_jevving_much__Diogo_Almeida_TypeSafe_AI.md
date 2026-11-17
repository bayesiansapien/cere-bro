# I love you so jevving much (Diogo Almeida, TypeSafe AI)

**Channel:** AI Engineer
**Published:** 2026-11-15
**Source:** https://www.youtube.com/watch?v=Cyt3LU8TyNc

## TL;DR
Diogo Almeida (co-creator of RLHF, InstructGPT and ChatGPT, now CEO of TypeSafe AI) argues that AI is "jagged" because 100% of today's LLMs are optimized for human-in-the-loop assistance via RLHF, not for unattended automation. His fix is Jev, a non-text model that returns typed, calibrated decisions callable from code, which he pitches as a "fourth semantic logic gate" for software. The talk is half manifesto, half call to action for "software research": real decomposition, verified stages and explicit state instead of stuffing everything into a KV cache.

## Key Takeaways
- **Jaggedness thesis:** LLMs are superhuman at tasks where a human verifies the output (deep research, chat) and useless where output must be correct unattended (accounting, drive-through ordering). Cause: the "HF" in RLHF literally bakes in a human verifier.
- **"Einstein 95%, Mr. Bean 5%":** Without knowing which mode you got, you cannot automate. Reliability and calibration matter more than peak intelligence; benchmarks do not measure this.
- **"Bitterest lesson":** Compute beats algorithms (Sutton), data beats compute, and choosing the right task beats all. Evidence cited: the InstructGPT result where a small RLHF model beat models orders of magnitude larger on instruction following.
- **Semantic logic gate:** Adding a cheap, fast, reliable semantic primitive to AND/OR/NOT is framed like the blue LED: not +33% capability but a combinatorial explosion (e.g. replace regexes with "is this a real-looking Gmail address").
- **Agent design is fighting the KV cache:** Memory is O(N), parallel agents rediscover the same codebase patterns, sub-agent routing is unreliable. All are symptoms of global-state-in-context design.
- **Slop root cause:** Unreliable AI cannot be trusted with decisions that cost the operator, so the cost is externalized onto readers. Reliable decisions shrink slop.
- **Idea list:** real-time intelligent security, semantic dependent typing in linters, "do what I mean" interfaces, encoding the spirit (not letter) of rules to reduce principal-agent losses.

## Architecture & Optimization Mechanics
- Jev is a decision model, not a generator: outputs are typed probabilistic decisions, no free text, no code, no chat. This removes autoregressive decoding cost entirely for classification-style calls, which is where the claimed latency wins come from.
- Training is synthetic-only via what Almeida calls "reinforcement learning from calibrated decisions." The optimization target is calibration on a narrow decision, not human preference.
- The architectural implication is a split stack: a generalist LLM for open-ended generation, plus a cheap calibrated decider in the inner loop of software. This is effectively a router/classifier layer promoted to a first-class primitive.
- The KV-cache critique maps onto known problems: shared prefix caching across sub-agents, memory retrieval that is O(log N) or O(1) via learned map-reduce over history, and state passing between agents instead of re-reading context.

## Grounded Context (Web Enrichment)
TypeSafe AI exited stealth in mid-September 2026 with a $40M seed round. Jev launched as a "System One" model returning structured decisions, with the company claiming up to 444x lower cost and 193x faster responses than frontier LLMs on certain tasks, and 70 to 500 ms end-to-end latency. Target uses are high-volume decisions: ticket classification, invoice evaluation, security alert triage and reviewing agent outputs. Developer reception was strong (TechCrunch framed it as "thrilling developers"), which matches Almeida's "ChatGPT moment for developers" remark.

Treat the numbers skeptically. All performance figures are company-reported and benchmarked against general LLMs doing classification, which is a soft target. Engineers have noted the speedup comes largely from existing techniques: a small specialized model, no decoding, structured outputs. The "RLHF causes jaggedness" claim is a useful framing but overstated. RLVR-trained models have measurably improved unattended agentic reliability through 2025 and 2026, and Almeida himself concedes RLVR models still need RLHF to be usable. Calibration, not the training paradigm alone, is the real differentiator.

## Real-World Application / Actionable Step
- **Routing:** Treat Jev-style calibrated deciders as the router itself. Benchmark your current LLM router against a small, calibrated classifier with abstention: measure Expected Calibration Error and the accuracy of high-confidence decisions, not just top-1 accuracy. Route to the frontier model only when confidence falls below a threshold.
- **Distillation target:** When distilling a big model into a router or judge, optimize for calibrated probabilities (temperature scaling, proper scoring rules like Brier) rather than matching generated text. Drop the decoder head where outputs are discrete.
- **Agent memory and KV cache:** Prototype shared prefix caching across parallel sub-agents in vLLM (automatic prefix caching) plus a persistent codebase-facts store, so agents stop re-discovering repo structure on every call.
- **Evaluate Jev directly:** Request early access and test it as a cheap first-stage router/verifier on a held-out set of your own routing decisions before trusting the 444x claim.
