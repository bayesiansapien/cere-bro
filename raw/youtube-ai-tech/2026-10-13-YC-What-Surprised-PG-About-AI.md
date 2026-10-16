# What Surprised PG About AI

**Channel:** Y Combinator
**Published:** 2026-10-13
**Source:** https://www.youtube.com/watch?v=cp7mBZJkaCs

## TL;DR
Paul Graham studied symbolic AI in the 1980s, which he now calls "a joke" that never would have worked. The expected path was bottom-up competence: a perfect fly, then a mouse, then a cat, then a monkey, then a human, flawless at every stage within its scope. What arrived instead was the reverse: human-level breadth with low reliability, "a bullshitting undergraduate." Progress since then has been from broad-but-sloppy toward perfect, not from narrow-but-perfect toward broad. He adds that he still cannot get AI to reliably tell him when restaurants are open, even as it solves famous open math problems. The clip is short and the observation is sharp.

## Key Takeaways
- **The quality that got optimized first was plausibility, not correctness.** Next-token pretraining on human text gets you human-like breadth before it gets you reliability.
- **The jagged frontier is still here.** Solving open math problems and getting simple factual lookups wrong coexist in the same model.
- **The fix is reliability engineering** (verifiers, tools, retrieval), not more breadth.

## Architecture & Optimization Mechanics
- The "start at human, work toward perfect" path is a direct result of the training objective. Imitation gives broad coverage, and RL with verifiers (RLVR) is what drives the move toward correctness, one checkable domain at a time. That is why math and code improved first and "is this restaurant open" (stale, unverifiable, retrieval-bound) did not.
- The restaurant failure is mostly a grounding and tool-use problem, not a reasoning one. A model with no live retrieval or a weak places API will produce a plausible answer, which is exactly the undergraduate failure he describes.

## Grounded Context (Web Enrichment)
"Jagged frontier" comes from the 2023 Harvard/BCG field study (Dell'Acqua, Mollick et al.), not from this conversation. The math claim is real: OpenAI said in August 2026 that an internal version of Astra solved ten previously open problems in math and theoretical CS, and Epoch's FrontierMath Open Problems set now tracks this directly. Subbarao Kambhampati made the same jaggedness point this week with a Gemini answer that "becoming 5 ft tall" means wearing one-foot heels. His explanation is that jaggedness tracks the training distribution, not problem hardness (see [[2026-10-14-Kambhampati-Mythos-Of-LLM-Thinking-Traces]]). The "slot machine" interjection echoes [[2026-10-11-MLST-Jeremy-Howard-AI-Coding-Slot-Machine]].

## Real-World Application / Actionable Step
- **For routing:** do not use apparent query difficulty as a proxy for which model to call. Route by verifiability and grounding needs. Send live-fact queries to a cheap model with tools/retrieval, and save frontier reasoning for problems that can be checked.
- **For evals:** keep a "dumb but real" slice (lookups, unit arithmetic, trick questions) next to hard benchmarks. Compression or quantization often breaks reliability on easy OOD items before it shows up on headline scores.
