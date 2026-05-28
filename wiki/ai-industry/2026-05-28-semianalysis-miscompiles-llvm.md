# SemiAnalysis: Finding Miscompiles for Fun, Not Profit

**Date ingested:** 2026-05-28
**Source:** SemiAnalysis (via RSS and starred Gmail)
**Author:** Justin Lebar
**Links:** [Post](https://newsletter.semianalysis.com/p/finding-miscompiles-for-fun-not-profit) · [raw](../../raw/rss/2026-05-28-semianalysis-finding-miscompiles-for-fun-not-profit.md) · [Gmail raw](../../raw/gmail/2026-05-28-starred.md)

## TL;DR

A compiler engineer with a decade of ML compiler experience (Google, Waymo, OpenAI) spent $10K of API credits in an afternoon and uncovered hundreds of plausible LLVM bugs including many miscompiles, with at least one "Quite Serious." The fuzzer was vibe-coded with ChatGPT 5.5: the LLM wrote the fuzzer, modified it after each found bug to avoid re-finding the same one, and minimized test cases. In three days the ptxas fuzzer (closed-source NVIDIA compiler) found 40 miscompiling programs; a week later, 80. He then asked Claude to read LLVM directly with 50 subagents looking for bugs and got one new bug every four minutes for the AMDGPU backend, and almost two per minute on x86. One agent-found example: LLVM downgrading an atomic store to two non-atomic stores. AMD has already fixed five of the open-source-backend bugs.

## Key findings

- Vibe-coded fuzzer in days, no manual code review by the author.
- 80 ptxas miscompilations found within a week of fuzzer work.
- Agent direct-read of LLVM source produces bugs faster than the fuzzer: one every 4 minutes (AMDGPU) and nearly two per minute (x86).
- At least one critical agent-discovered bug: LLVM downgrading an atomic store into two non-atomic stores, which would be hard to find by fuzzing and catastrophic when triggered.
- AMD has fixed five bugs already; closed-source ptxas can only be worked around in the fuzzer.
- Cost: vibe-coding the fuzzer was relatively cheap ($200/mo ChatGPT Pro plus contractor account); the bug-finding agent runs were the expensive part.

## How this fits prior wiki state

Today's pair from r/CUDA and r/MachineLearning shows AI generating speed-of-light kernels (doubleAI) and AI-generated kernels silently breaking training (the bf16 embedding-grad bug). SemiAnalysis adds a third leg: AI agents finding latent bugs in human-written compilers at industrial rates. The combined picture this week is that AI is now competitive in three roles in the low-level compute stack, author, auditor, breaker, and the audit role is the most surprising piece.

The atomic-store-to-non-atomic-store bug is the kind of latent issue that fuzzing usually misses, because fuzzing atomics is hard. Agent-driven static analysis closes that gap. The wider implication: production compilers' bug surface is much larger than the bugs that the compiler community has the bandwidth to surface manually.

## Related pages

- [[2026-05-28-doubleai-blackwell-sol-execbench]], AI-written speed-of-light kernels
- [[2026-05-28-ai-kernels-silently-break]], AI-written kernels silently breaking training
- [[gpu-kernels]], concept page

## Research angle

The economics of $10K/afternoon for hundreds of compiler bugs is a clean number to track. If that rate holds, then bug-discovery has moved from "expensive expert time" to "moderate compute spend." The risk is asymmetric: open-source compilers benefit (AMD already fixed five), closed-source compilers (ptxas) are exposed in a way they cannot defend by fixing, only by adversarial fuzzers and selective disclosure. NVIDIA's position on this matters. The next year's interesting paper would track whether bug-fix rates in open compilers keep up with the discovery rate from AI agents, or whether the gap grows.
