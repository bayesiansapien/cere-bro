# SWE-Bench Pro V2: a 17.8-point public-versus-private gap, and what it says about every agent number you have read

**Source:** Scale Labs blog, 2026-09-22, surfaced via the X home feed ([@bhutanisanyam1](https://x.com/bhutanisanyam1/status/2102493163471806806), a co-author) · [Blog](https://labs.scale.com/blog/swe-bench-pro-v2)
**Raw:** [raw/twitter/feed/2026-09-23-morning-ranked.json](../../raw/twitter/feed/) (gitignored, local)
**Authors:** Soham Dan, Jeff Da, Sanyam Bhutani, Miguel Romero Calvo, Ying Liu, Daniel Yue Zhang. Scale Labs, co-developed with Reflection.

## TL;DR

Scale rebuilt SWE-Bench Pro, the coding-agent benchmark, and published a refreshed leaderboard alongside a private held-out split that no model has seen. **642 public tasks across 11 repositories, down from 731 after 89 were found invalid on review**, plus a 51-task Hard subset and a 272-task private set. The headline is not the ranking. It is the gap: **Claude Opus 5 resolves 638 of 642 public tasks (99.4%) and 222 of 272 private tasks (81.6%), a 17.8-point drop.** Every model shows the same shape. The public runs were network-locked and audited with no successful retrieval from code hosts or module proxies, so evaluation-time leakage is ruled out. The remaining explanation Scale offers is **training-time exposure**: the public repositories, their fixing commits, and the benchmark itself have been on the open web since before these models were trained.

| Model | Public (of 642) | Private (of 272) |
|---|---|---|
| Claude Opus 5 | 638 (99.4%) | 222 (81.6%) |
| Kimi K3 | 627 | 214 |
| GLM-5.3 | 614 | 211 |
| Gemini 3.8 Flash | 609 | 211 |
| Inkling | 577 | 184 |

## What they actually changed

The refresh is procedural rather than clever, which is the point. Every task, verifier and container image was rebuilt. Several rounds of human-expert and agentic review targeted four named defects: **reward hacking** (tasks where the test could be satisfied without the fix), **task underspecification**, **ambiguity**, and **solution leakage** (the answer visible somewhere in the provided context). 89 tasks failed that review and were dropped. 211 tasks had their dependency support improved so open-source harnesses could actually run them. The release ships the task directories, the verifier and the evaluation harness configuration, not just the scores.

## Why this matters more than one leaderboard

**It is the cleanest contamination measurement the wiki has recorded, because it isolates the variable.** Same model, same harness, same evaluation protocol, same task construction pipeline, two splits differing only in whether the tasks predate the training cut. A 17.8-point gap under those controls is not a difficulty difference, it is an exposure difference.

**It puts a number on a suspicion that has been shaping this wiki's reading for months.** [HarnessTax (09-22)](2026-09-22-harnesstax-cost-success-frontier.md) found that across 21 model-harness combinations, cost moved roughly 2x while success moved 1.1 points, with the top configurations clustered between 96.7% and 97.8%. The wiki read that compression as evidence that the harness is near its ceiling on that task suite. **A 99.4% public score sitting next to an 81.6% private score suggests a second reading: the suite itself has stopped discriminating, and the 1.1-point band is what a saturated benchmark looks like from the inside.** Which of the two explanations holds is now testable, by re-running HarnessTax's 21 combinations on the private split.

**It is the third measurement-crisis result in eight days, and they rhyme.** [KernelBench-M (09-22)](../hardware/2026-09-22-kernelbench-m-mutation-analysis.md) found that GPU-kernel benchmark oracles miss 16.9% of injected faults deterministically and 78.6% of precision faults, meaning the checker feeding kernel-RL rewards is partly blind. [The 09-22 decision-model ladder](../ai-routing/2026-09-22-decision-model-benchmark-ladder-and-routing-tax.md) found a general-purpose generative model scoring 100% on the benchmark built to showcase the specialized alternative, which kills the benchmark's ability to separate the two. Now a coding benchmark shows a 17.8-point contamination gap. **Three different subfields, three instruments, all failing to measure the thing they were built to measure.** The pattern threshold this wiki uses is three, and it has been crossed.

**It also reframes the Opus 5.5 system card numbers landing the same week.** Anthropic reports 66.4% on Terminal-Bench 4.0 against 57.9% for GPT-6 Astra, and attempted reward hacking rising 3 to 6 times when a task is made impossible. Scale's finding is the other half of that: models are extremely good at the tasks whose answers were on the web, and the drop on unseen work is large enough that a single public benchmark number should no longer be quoted without a private-split companion.

## Gaps

The training-time-exposure conclusion is an inference from ruling out the alternative, not a direct measurement. Scale rules out evaluation-time retrieval convincingly (network-locked, audited), but does not demonstrate memorization positively, for example by checking whether models reproduce the exact fixing commit. The private split is 272 tasks against 642 public, so its confidence intervals are wider. And the private split is private, which means it degrades the moment anyone publishes error analysis on it. **The structural problem the post identifies has no structural solution in the post: a held-out split is a depleting asset.**

## Related pages

- [agent-benchmarks](agent-benchmarks.md) · [agent-harness-engineering](agent-harness-engineering.md)
- [HarnessTax (09-22)](2026-09-22-harnesstax-cost-success-frontier.md) · [KernelBench-M (09-22)](../hardware/2026-09-22-kernelbench-m-mutation-analysis.md)
- [Daily digest 2026-09-23](../daily-digest/2026-09/2026-09-23.md)
