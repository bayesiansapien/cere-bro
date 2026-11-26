---
title: "Where evals break: Eugene Yan's 12-eval audit, SemiAnalysis GDPx results, OWE-Bench's deployment gap"
date: 2026-11-26
source: https://newsletter.semianalysis.com/p/evaluating-recent-model-releases
raw: ../../raw/gmail/2026-11-26-newsletters.md
raw2: ../../raw/rss/2026-11-26-semianalysis-evaluating-recent-model-releases-on-gdpx.md
raw3: ../../raw/huggingface/2026-11-25-owe-bench-a-long-horizon-benchmark-for-measuring-real-world.md
tags: [benchmarks, evals, reliability, graders, deployment-gap, agent-cost, gdpx]
signal: Eugene Yan newsletter (essay), SemiAnalysis (essay), HuggingFace 11-25 (OWE-Bench, SpecEngineeringBench, CUA-SEE)
---

# Where evals break

**TL;DR.** Two essays and three benchmark papers in one window, all arguing that today's agent scores measure the wrong thing. Eugene Yan audits 12 public evals and finds graders failing correct work in 8 of them. SemiAnalysis's GDPx update says OpenAI's GPT-6.2 Astra leads on hard frontier domains while the public preferred Gemini 4 Neon's personality. OWE-Bench finds every model scores about 18 points lower on hidden cases than on the cases it could test against.

## Eugene Yan: "Lessons from 12 Evals"

- **Grader failures are common:** in 8 of 12 public evals there is evidence the grader failed work that should have passed.
- **Shared design principles:** deterministic checks over LLM judges (DeepSWE and AutomationBench use none); grade the outcome, not the steps (Terminal Bench inspects final container state); all-pass scoring is common because partial work is often unusable ("a report that flags eight of ten risks is incomplete, not 80% useful"); tasks mined for difficulty to slow saturation.
- **Two dominant failure modes:** skipping verification or stopping early, and dropping stated requirements. On AutomationBench models declared success on 72-91% of the failures analyzed.
- **The argument that matters for cost work:** cost per task is misleading because agents fail cheaply. On Agents' Last Exam 17% of failures were stopping early; on FrontierSWE one model submitted within 8 hours of a 20-hour budget in 169 of 170 trials. "The scarce resource is human attention, not token cost": if you cannot tell which tasks failed, you review all of them. He would pay 2x for a model that finishes every time.
- Evals are maintained like software now (Agents' Last Exam v1.1 retired 30 tasks and revised 57), which also makes scores incomparable across versions.

## SemiAnalysis: "Evaluating Recent Model Releases on GDPx"

- GDPx: 206 tasks built with 14 data partners across 11 frontier-value domains (chip design, hardware design, cyber, bio, finance, legal, quant trading, RSI, materials, alignment, software engineering).
- Main board: **GPT-6.2 Astra 19.3%, Fable 5.2 16.4%**, best non-OpenAI/Anthropic Gemini 4 Carbon 10.9%, Gemini 4 Neon 10.1%. The cost-performance Pareto frontier is entirely OpenAI, with DeepSeek v4.1 Flash at the low end.
- **Fable 5.2 leads chip design, software engineering and quant trading**; Astra leads RSI, materials science and hardware design, and is first above 0% on legal. Astra scores half of Fable on software engineering, which SemiAnalysis says explains its poor public reception.
- Safety classifiers sandbag scores in cyber, bio and alignment; an alternate board excludes them.
- Their read: Neon's popularity is behavior ("a pleasant model to talk to"), not intelligence. Tiers: Anthropic and OpenAI, then Google, then everyone else.

## Benchmark papers (HuggingFace 11-25)

- **OWE-Bench** ([2611.30017](https://arxiv.org/abs/2611.30017)): 26 expert-written long-horizon engineering tasks (optimizing kernels, designing an aircraft, finding earthquake faults), scored on speed, cost and accuracy. Best: Claude Fable 5.2 at 54.6%, averaging **211 million tokens per task**. More time means more test-time compute and higher scores, but models scale differently: GPT-6 Astra wins at short limits and equal tokens, Fable wins at long limits by spending more. Every model scores lower on hidden cases than provided ones, **18 points on average: the deployment gap**.
- **SpecEngineeringBench** ([2611.32973](https://arxiv.org/abs/2611.32973)): 100 instances from 78 repos. Agents reach 91.47% head pass rate and 80.48% change-focused coverage but only **26.36% fail-to-pass**: tests that run and cover code still miss the defects.
- **CUA-SEE** ([2611.30962](https://arxiv.org/abs/2611.30962)): a computer-use eval that co-evolves tasks and executable verifiers from rollout evidence, so difficulty and verifier precision track agent progress.

## Relation to prior wiki pages

- **Confirms** the [agent benchmarks](agent-benchmarks.md) page's 11-25 SWE-Gym audit (74% of never-solved tasks had a test rejecting correct fixes) from the essay side: grader error is the norm, not an edge case.
- **Same lesson as** Anthropic's Rust migration (same window): 98% of tests passed while production parity was ~25%. SpecEngineeringBench's coverage-without-detection is the benchmark version.
- **Tension with the cost papers.** Delegent and effort escalation report dollar savings at equal accuracy. Yan's critique says report repeated-run reliability and silent-failure rate too. OWE-Bench's deployment gap is the number that would expose a cheap agent overfitting the visible tests.
- **Hardware angle:** GDPx's split (Fable ahead on chip design, Astra on hardware design) is the first frontier-model benchmark carrying domain splits that matter to the semiconductor reader.

## Gaps

- GDPx is 206 tasks; per-domain splits are ~20 tasks each.
- Yan's "vibes" section is labeled as opinion by the author.

Raw: [Gmail (Eugene Yan, SemiAnalysis)](../../raw/gmail/2026-11-26-newsletters.md) (private) · [SemiAnalysis RSS](../../raw/rss/2026-11-26-semianalysis-evaluating-recent-model-releases-on-gdpx.md) · [OWE-Bench](../../raw/huggingface/2026-11-25-owe-bench-a-long-horizon-benchmark-for-measuring-real-world.md)
