# Why Humans Can't Keep Up With AI-Written Code (Tariq Shaukat, Sonar)

**Channel:** AI Engineer
**Published:** 2026-10-29
**Source:** https://www.youtube.com/watch?v=LQW_Wvqhp04

## TL;DR
Sonar's CEO argues that agentic coding has made code abundant and confidence scarce, and that the fix is a Toyota-style "build quality in" factory rather than humans in the loop. He lists five hard limits (human review does not scale, agents degrade on large codebases, errors compound over long tasks, LLM judges are unreliable, time-to-exploit is near zero) and proposes a multiplicative "code confidence formula": Intent x Guide rails x Verification x Evidence, where any zero zeroes the whole. The problem diagnosis is well sourced and useful. The solution half is a SonarQube/Sonar Vortex pitch backed by self-reported customer numbers.

## Key Takeaways
- **Volume without shipping:** a recent study of async coding agents found +2,450% lines of code and +240% commits but only +30% releases. Production scaled, delivery did not.
- **Software factories:** 5% of developers run agentic factories today; 34% expect to within a year (39% in financial services). Same Sonar State of Code preview cited in the Kapur/Osmani talk.
- **Limit 1, cognitive surrender:** humans agree with AI 93% of the time when it is right and about 4 in 5 times when it is wrong. Human-in-the-loop is not a control.
- **Limit 2, codebase size:** one code-translation study saw 91% accuracy at 10k LOC collapse by 50k LOC. Token cost for the same task on a large repo varied 30x, mostly spent on navigation.
- **Limit 3, error compounding:** METR puts Claude Mythos Preview at a 16-hour 50%-success horizon, but the curve flattens sharply at 80%. 0.95^20 = 36% success over 20 steps.
- **Limit 4, LLM judges:** PayPal AI research found 7-17% of verdicts flip across identical replications; Meta research found a simple "are you sure?" flips 7-34% of answers.
- **Limit 5:** time to exploit is near zero, so prevention must be designed in, not bolted on.
- **Sonar claims:** Sonar Vortex (intent context plus in-loop guide rails) cut token cost 36% and issues per commit 92% on large codebases. SonarQube users report being 81% more likely to see a very positive AI security impact, 34% for time to market, 76% for outage frequency.

## Architecture & Optimization Mechanics
- **Navigation is the token sink.** The 30x token variance and the 36% saving from "starting near White Plains" both say the same thing: pre-computed codebase structure (symbol graphs, dependency maps, architectural summaries) is a cheap substitute for expensive agent exploration. It is retrieval as compute reduction.
- **Hybrid verification is a cost cascade.** "Use CPUs when you can, GPUs when you need GPUs": deterministic analyzers first, agentic review only for what rules cannot express. Same structure as an LLM router, applied to verification.
- **Judge variance is a statistics problem.** A judge that flips 7-17% of the time on identical inputs should be run as an ensemble (self-consistency, majority vote) or replaced by deterministic checks for anything gating. Single-sample LLM judges are not evidence.
- **Weak spots:** the multiplicative formula is a rhetorical device, not a model. The customer stats are correlational survey responses ("X% more likely to believe") from Sonar's own users, which says nothing about causation. The 36%/92% Vortex figures have no published methodology.

## Grounded Context (Web Enrichment)
The third-party research holds up, with caveats. METR assessed an early Mythos Preview snapshot (March 2026) at a 50% time horizon of at least 16 hours, at the ceiling of what its suite can measure; at 80% success METR and Anthropic only state the horizon is more than 2x the next-best model, without disclosing an absolute number. So "the curve flattens substantially" is directionally right, but the specific 80% figure he implies was never published. METR itself cautions that a 50% horizon is not hours of unsupervised work.

"Cognitive surrender" comes from Shaw and Nave's Wharton preprint (January 2026, three experiments, 1,372 participants on CRT-style problems). Accuracy rose about 25 points when the AI was right and fell about 15 when it was wrong; acceptance of wrong AI answers was roughly 73-80% depending on the subset, with confidence rising regardless. A published commentary has questioned its statistical power, and the effect varies with domain expertise and time pressure. These are reasoning puzzles, not code review, so extrapolating to PR review is plausible but untested. The arithmetic on compounding error (0.95^20 = 0.358) is correct.

## Real-World Application / Actionable Step
- **Never gate on a single LLM-judge sample.** For any router-quality or compression eval using an LLM judge, run 3-5 samples, report flip rate alongside the score, and compare against an exact-match or programmatic metric where one exists. If flip rate exceeds 10%, the eval cannot detect small quantization regressions.
- **Give agents a map.** For Amit's large research repos, keep an auto-generated architecture summary (module graph, key entry points, where kernels and configs live) in CLAUDE.md. That attacks the 30x navigation variance directly.
- **Research angle:** judge flip rate likely increases under quantization of the judge model. Measuring judge self-consistency as a function of bit width is a cheap, novel compression benchmark.
