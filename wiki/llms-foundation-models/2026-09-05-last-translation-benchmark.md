# Last Translation Benchmark

**arxiv:** [2609.04173](https://arxiv.org/abs/2609.04173) · **Source:** [HuggingFace Daily Papers 2026-09-05](../../raw/huggingface/2026-09-05-last-translation-benchmark.md)

## TL;DR

Machine translation has a measurement problem with three layers, and this benchmark attacks all three at once. Standard MT benchmarks are approaching saturation, so they no longer discriminate between strong models. Automatic metrics are unreliable and **vulnerable to reward hacking**, and when they do report a low score they do not say what went wrong. Gold human evaluation, the usual fallback, lacks reproducibility, objectivity and scale.

The Last Translation Benchmark is a collection of **human-authored and peer-reviewed examples across text, images, audio and video that break leading translation models**. The design decision that matters is not the difficulty of the examples but what ships alongside each one: **handcrafted verification rules describing concrete failure cases on that specific example.** That converts evaluation from "what score did the output get" into "did the output commit this named error," which is reproducible, objective at the item level, and directly actionable, because a failed rule tells you what to fix.

It is a **live dataset accepting ongoing contributions**. LTBv1 contains accepted contributions submitted before 1 September 2026, with further releases planned as data accumulates.

## Key findings

- **Per-example verification rules replace scalar metrics.** Each item carries handcrafted rules naming concrete failure cases, so a result is a list of violated obligations rather than a number.
- **Multimodal by construction**, spanning text, images, audio and video, which matters because translation failures that only appear when the source is spoken or rendered are invisible to text-only benchmarks.
- **Adversarial by selection**: every example is one that breaks a leading model, so saturation is deferred by construction rather than by scaling the test set.
- **Live rather than frozen.** Ongoing contribution with versioned releases, which is a maintenance commitment most benchmarks do not make.

## Relation to prior wiki state

**This is one of four papers on 2026-09-05 that independently replace a scalar score with a structured verdict**, and the convergence is the story rather than any single paper. [VeriPhy (09-05)](../vision-audio-video/2026-09-05-veriphy-physical-verification.md) compiles a video prompt into typed physical obligations and returns provenance-carrying evidence records with a three-valued supported/contradicted/unknown verdict. [OVMI (09-05)](../vision-audio-video/2026-09-05-ovmi-speech-bci-common-measure.md) shows word error rate computed only over the vocabulary a speech interface supports overstates communicated information, and replaces it with an information-theoretic quantity defined against a reference distribution. [Select, Compress, Reinvest (09-05)](../inference-efficiency/2026-09-05-select-compress-reinvest-visual-tokens.md) measures a **0.07 to 3.74 point harness artifact** on identical published rules at identical budgets, which is larger than most published margins in its area.

That is the general form the [agent benchmarks](../agentic-systems/agent-benchmarks.md) page arrived at on 09-04, stated there as: **any benchmark reporting one number is conditioning on something it has not stated.** LTB names the conditioning variable for MT explicitly, which is the metric's own hackability, and removes it by making the failure condition part of the item rather than part of the scorer.

**It also connects to the reward-hacking thread on the judge side.** [More Convincing, Not More Correct (07-26)](2026-07-26-self-play-reward-hacking-llm-judges.md) found self-play drove an LLM judge's pass rate from 0.72 to 0.94 while true accuracy stayed pinned at 0.20, and [J-Zero (08-31)](../agentic-systems/2026-08-31-j-zero-challenger-solver-judge.md) fixed it by training the judge only on preference pairs whose ordering is fixed by the generation procedure rather than the judge's own scores. LTB's per-example rules are the non-learned version of the same defence: **a rule written by a human before the output existed cannot be earned by writing more convincing prose.**

## Gaps

Handcrafted per-example rules do not scale the way an automatic metric does, and the paper's answer is community contribution, which makes coverage a function of who volunteers. Adversarial selection means the benchmark measures the tail rather than the distribution, so a model that improves on LTB has not necessarily improved on typical translation. Peer review of contributions is a quality gate whose criteria and inter-rater agreement are not the sort of thing a benchmark paper usually reports, and here it is load-bearing. And a live dataset with rolling releases makes cross-paper comparison version-dependent, which is the failure mode this benchmark exists to fix, arriving from a different direction.

## Related pages

- [Agent Evaluation & Benchmarks](../agentic-systems/agent-benchmarks.md)
- [Daily digest 2026-09-05](../daily-digest/2026-09/2026-09-05.md)
