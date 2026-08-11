# SWE-Bench ProMax: Multilingual Large-Scale Refactoring, and an Audit of SWE-bench Verified

**Source:** HuggingFace Daily Papers · [arXiv 2608.09802](https://arxiv.org/abs/2608.09802) · [dataset](https://huggingface.co/datasets/swe-bench-promax/SWE-Bench-ProMax)
**Raw:** [raw/huggingface/2026-08-11-swe-bench-promax-benchmarking-agents-on-large-scale-multilin.md](../../raw/huggingface/2026-08-11-swe-bench-promax-benchmarking-agents-on-large-scale-multilin.md)
**Date:** 2026-08-11

## TL;DR

The headline is a new benchmark; the more consequential content is the audit it cites. **Nearly 60% of unsolved SWE-bench Verified instances contain flawed tests**, either overly narrow tests that reject correct solutions or overly broad tests that check unstated requirements, and frontier models can **verbatim reproduce gold patches from training data**. SWE-Bench ProMax responds by moving to a task type that resists both problems: **behavior-preserving refactoring coordinated across many files**. 170 expert-curated instances from real commits across seven languages (Python, Java, TypeScript, Go, C, C++, Rust), averaging **11.4 modified files and 261.6 lines changed** per instance. Issue descriptions are rewritten from scratch for unambiguous specification and test suites are manually reviewed to remove both failure modes. Best frontier model under two agent scaffolds: **41.2% resolve rate**.

## Why refactoring is the right task choice

Refactoring is behavior-preserving, so correctness has a sharp definition (the existing tests still pass and the structure changed as specified) that does not depend on a hidden-requirements judgment call. It is also inherently cross-file, which is what makes the 11.4-files-per-instance figure the load-bearing number: it forces the agent to hold a coordinated plan across a codebase rather than localize a fix. And because the target is a real commit's structural change rather than a bug fix with a canonical patch, verbatim recall from training data helps much less.

## How this relates to prior wiki pages

**This is the third paper in one day arguing that current agent benchmarks do not measure what they are trusted to measure.** [A²E (08-11)](2026-08-11-harness-evolution-cluster.md) argues correctness alone is too coarse for comparing harnesses and adds execution efficiency, tool use, planning and error recovery as separate dimensions. [Evo-Bench (08-11)](2026-08-11-harness-evolution-cluster.md) builds sensitivity-aware stratified splitting specifically to prevent task-specific overfitting and to isolate harness improvement from base model strength. SWE-Bench ProMax audits the incumbent and finds 60% of its hard instances broken. **[agent-benchmarks.md](agent-benchmarks.md) should now treat measurement validity as the page's central problem rather than as a caveat.**

**It confirms the pattern this wiki named on 08-10 from a different direction.** [StreamArena (08-10)](2026-08-10-streamarena-streammind.md) reported that on old streaming-video benchmarks, reading only the last four frames matches complex streaming models, meaning the benchmark was measuring recency rather than streaming comprehension. Same shape: a widely trusted benchmark whose scores were partly an artifact of its construction. Two in two days, in unrelated subfields.

**41.2% is the number to carry forward.** It sits against Ouroboros's same-day **86.74% on Terminal-Bench 2.1** and **90.69% on OSWorld-Verified**, both reported as best-known results. Those three numbers on one board are the cleanest available evidence that **agent capability is benchmark-shaped**: near-saturation on interactive terminal and OS tasks, and under half on coordinated multi-file refactoring.

## Gaps

- **170 instances is small** for a benchmark meant to be the successor to a saturating standard, and the paper does not report per-language breakdowns in the abstract, so whether the 41.2% is uniform across seven languages or dominated by Python is unknown.
- **Manual curation is the quality guarantee and also the scaling limit.** The audit's finding was that automated curation produced 60% flawed tests; hand review fixes that at a cost that does not scale, so this benchmark will saturate without an obvious refresh path.
- **Two agent scaffolds is a narrow harness sample**, and A²E's same-day finding is precisely that model-harness combinations vary substantially by task type. The 41.2% ceiling may be a scaffold ceiling.
- **No contamination test is reported for ProMax itself.** The instances come from real commits, which are public.

## Industrial implication

Refactoring is where enterprise coding-agent value actually sits, and it is where the tooling is weakest: a 41.2% resolve rate on 11-file behavior-preserving changes is not a number anyone ships against without human review. Read alongside the [08-10 finding that AI-written C++ consumes 5 to 8% more compute in production](../ai-industry/2026-08-10-ai-generated-cpp-production-quality.md) across 3.52 million changes, the picture is that agents are strong at adding code and weak at restructuring it, which is the direction that accumulates cost. Expect the coding-agent vendors to start reporting refactoring benchmarks separately, and expect the gap to be the main argument for keeping humans in the review loop.

## Related

- [agent-benchmarks.md](agent-benchmarks.md) concept page
- [harness evolution cluster (08-11)](2026-08-11-harness-evolution-cluster.md), [StreamArena (08-10)](2026-08-10-streamarena-streammind.md)
- [AI-generated C++ in production (08-10)](../ai-industry/2026-08-10-ai-generated-cpp-production-quality.md)
