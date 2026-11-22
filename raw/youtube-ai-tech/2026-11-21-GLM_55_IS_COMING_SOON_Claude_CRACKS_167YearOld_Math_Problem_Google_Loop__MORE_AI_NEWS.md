# GLM 5.5 IS COMING SOON! Claude CRACKS 167-Year-Old Math Problem?! Google Loop & MORE

**Channel:** WorldofAI
**Published:** 2026-11-21
**Source:** https://www.youtube.com/watch?v=a36atq-Dy8A

*Secondary domain: deep-science (Riemann hypothesis).*

## TL;DR
The headline: Anthropic mathematician **Levent Alpöge claims a Claude-assisted proof of the Riemann Hypothesis and the Generalized RH**, built in about 6 weeks as about 17M lines of Lean 4 (more than 250,000 pages). It is unverified. Other items: Zhipu teasing **GLM 5.5** before December, with speculation that the stealth model Gestalt is GLM 5.5 (98 days since GLM 5.3 against a 61-day average cycle); **Google "Loop"** (codename Jitro, Jules v2), a goal-driven agent that runs continuously against product metrics; Thinking Machines' **Inkling 2 Mini**, a 26.4B-total / 3.4B-active **looped transformer** (24 layers, middle 12 repeated 3×); plus Antigravity thread forking, Grok Build 2.0 merging with Cursor CLI, ChatGPT Spaces for Plus, OpenAI Rosalind MedChem benchmark, six OpenAI departures (three to Anthropic), and Neuralink GTA 6.

## Key Takeaways
- **RH claim:** a Lean archive with no human-readable paper or independent review yet. Formal verification moves the open question to whether the Lean *statement* of RH is encoded correctly and which axioms are used.
- **GLM 5.5 / Gestalt link:** circumstantial. Zhipu pre-tested GLM 5 as "Pony Alpha" five days before launch, so the stealth-release pattern exists.
- **Google Loop:** connect a repo, set a long-term objective (security, engagement, performance). It generates its own skills, chooses metrics, splits work into tasks, ships via Gemini, monitors post-deploy metrics, and iterates. 100+ integrations, custom MCP. Expected in 2027.
- **Inkling 2 Mini (as reported):** 26.4B total / 3.4B active. The 6 first and 6 last layers run once and the middle 12 loop 3×, giving more compute per token without more parameters. Chain-of-thought gets shorter as loops increase but stays monitorable. A variable-loop research model is also released. Reported AA index 20.1. Runs on a 32 GB Mac. Apache 2.0.
- **Antigravity /btw:** now forks side threads and can promote them into the main workflow (Claude Code-style).
- **Gemini API:** voice-editing transcription (Rambler tech). Gemini Omni 1.2 Flash makes GIFs.
- **OpenAI Rosalind:** neurodegeneration research partnerships plus a MedChem reasoning benchmark.

## Architecture & Optimization Mechanics
- **Looped transformers are compression via weight tying across depth.** Twelve middle layers reused 3× give an effective depth of 48 from 24 layers' worth of weights. Combined with MoE sparsity (3.4B active of 26.4B), this attacks both memory (fewer unique parameters) and quality (more sequential compute). For inference, weight reuse means better cache locality per loop. But latency grows with loop count, and KV cache handling per loop iteration is non-trivial. Expect serving engines (vLLM) to need loop-aware scheduling.
- **Variable loop count = adaptive compute knob.** This is a natural **routing target inside one model**: easy tokens or queries get 1 loop, hard ones get 3. It is an alternative to routing between separate small and large models.
- **The monitorability result matters for safety-constrained deployment.** More latent compute did not erase CoT legibility in their tests. Verify that independently before relying on it.
- **Google Loop is Warp's closed-loop factory idea (see Zach Lloyd entry, 2026-11-20) applied to product metrics** rather than SDLC metrics. Without guardrails it is a Goodhart risk.

## Grounded Context (Web Enrichment)
The RH claim is real but **unverified**. Alpöge released a 14-part Lean 4 archive (reports say about 175,000 files) claiming RH and GRH. As of 2026-11-20 there is no written argument, no independent expert review, and no official Anthropic announcement. Experts stress that the Lean statement encoding still has to be audited ([Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/), [SiliconANGLE](https://siliconangle.com/2026/11/20/anthropic-researcher-claims-to-have-proven-riemann-hypothesis-using-claude/), [phys.org](https://phys.org/news/2026-11-anthropic-claude-math-greatest-riddle.html), [CASRAI](https://casrai.org/news/anthropic-levent-alpoge-claude-lean-riemann-hypothesis-claim-2026)). Within hours, Stanford researchers posted a competing, all-human draft proof ([The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/), [DataCamp](https://www.datacamp.com/blog/ai-solved-riemann-hypothesis)). Context: in August Claude raised the proven fraction of zeta zeros on the critical line to 67.2%, a genuine but partial result. The video's line "it seems like it is verified" is wrong. Lean checks the proof against the stated theorem, not whether that theorem is RH.

I could **not verify Inkling 2 Mini**. Indexed Thinking Machines releases are Inkling (975B/41B active), Inkling-Small (276B/12B), and Inkling 2 Small (594B/17B active), and none of them is looped ([Thinking Machines](https://thinkingmachines.ai/news/inkling-2-small/), [Raschka](https://www.sebastianraschka.com/blog/2026/inkling-architecture-benchmark-notes.html)). The closest looped-LM precedent is ByteDance's Ouro ([arXiv](https://arxiv.org/abs/2510.25741)). Treat the 26B/3.4B looped specs as unconfirmed until there is a model card. GLM 5.5 = Gestalt is speculation.

## Real-World Application / Actionable Step
- **Prototype loop-count routing.** Take an open looped LM (Ouro, or Inkling 2 Mini if it is real) and measure quality vs loops per task class. Then train a lightweight classifier to choose the loop count per query. This is intra-model adaptive compute, and it is directly publishable next to your routing work.
- **Pruning angle:** test whether looped middle blocks tolerate more aggressive quantization (e.g. INT4) than the once-run edge layers, since errors may compound across loops. Measure per-loop error accumulation.
- **On the RH claim:** wait for independent Lean statement audits (e.g. Mathlib maintainers, Tao's commentary) before citing it. If it holds, AI-for-formal-math becomes a serious inference workload, with long-horizon, verifier-in-the-loop agents and heavy test-time compute. That is a good stress case for your serving optimization.
