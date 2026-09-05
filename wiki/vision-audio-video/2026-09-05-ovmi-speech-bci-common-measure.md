# OVMI: A Common Measure of Communication for Speech Brain-Computer Interfaces

**arxiv:** [2609.02887](https://arxiv.org/abs/2609.02887) · **Source:** [HuggingFace Daily Papers 2026-09-05](../../raw/huggingface/2026-09-05-a-common-measure-of-communication-for-speech-brain-computer.md)

## TL;DR

Speech brain-computer interfaces translate neural activity into language, and the field cannot tell whether it is making progress, because every system uses a different dataset, recording method, speech type and vocabulary. Reported scores are not comparable. Underneath that lie two questions nobody had answered: **what distribution of words should such a system let a user say**, and **how much of that distribution does a given decoder actually convey**.

The paper derives **open-vocabulary mutual information (OVMI)**, an information-theoretic quantity measuring the information a decoder conveys *relative to a reference distribution over the words the user may wish to communicate*. Because the reference is external to the system, capabilities measured under different vocabularies land on one common communication scale.

The finding with teeth is a measurement critique that generalises well beyond BCIs. **Accuracy, word error rate and every other metric computed only over the words a system supports can overstate how much of a user's intended speech it can communicate.** A decoder with a 50-word vocabulary and perfect accuracy scores better on WER than one with a 5,000-word vocabulary and mediocre accuracy, while conveying far less. OVMI exposes the trade-off between how much of the user's language a system supports and how accurately it decodes those words, and shows the comparison depends on what the user is expected to say. Optimising vocabulary choice for OVMI yields up to **16.3 percent relative improvement in accuracy across three speech domains**, so the measure is not only diagnostic, it is an objective worth designing against.

## Key findings

- **Metrics computed over the supported vocabulary systematically overstate communicated information.** Restricting the vocabulary improves the reported number while reducing what the user can actually say.
- **OVMI puts heterogeneous systems on one scale** by scoring against an external reference distribution rather than the system's own word list.
- **Vocabulary selection is a design variable, not a given.** Choosing the vocabulary to maximise OVMI gives up to 16.3 percent relative accuracy improvement across three speech domains.
- **Which system is better depends on what the user is expected to communicate**, and OVMI makes that dependence explicit instead of hiding it in the vocabulary choice.

## Relation to prior wiki state

**This is the fourth paper on 2026-09-05 replacing a scalar score with something conditioned explicitly**, alongside the [Last Translation Benchmark](../llms-foundation-models/2026-09-05-last-translation-benchmark.md) (per-example verification rules instead of automatic MT metrics), [VeriPhy](2026-09-05-veriphy-physical-verification.md) (typed physical obligations with provenance-carrying evidence records instead of a quality score), and [Select, Compress, Reinvest](../inference-efficiency/2026-09-05-select-compress-reinvest-visual-tokens.md) (a measured 0.07 to 3.74 point harness artifact on identical published rules).

OVMI is the sharpest statement of the shared claim, because it names the mechanism precisely: **the metric is computed over a support set that the system itself chose, so shrinking the support improves the score.** That is the exact structure of the unstated conditioning variable the [agent benchmarks](../agentic-systems/agent-benchmarks.md) page has been cataloguing, where RealSWE (09-04) found that benchmark prompts are 7 percent of the real request distribution and realistic inputs cost 6.4 points and can flip rankings. **A benchmark's prompt set is its support set, and RealSWE's finding is OVMI's critique applied to coding agents.** Neither paper cites the other and they are in unrelated fields.

## Gaps

OVMI requires a reference distribution over the words a user may wish to communicate, and that reference is a modelling choice with real consequences: different references reorder systems, which the paper acknowledges as a feature but which also means "best under OVMI" is only meaningful once the reference is agreed. Three speech domains for the vocabulary-optimisation result. And the measure scores words, so it says nothing about whether the communicated content is the *intended* content at the sentence level.

## Related pages

- [Agent Evaluation & Benchmarks](../agentic-systems/agent-benchmarks.md)
- [Daily digest 2026-09-05](../daily-digest/2026-09/2026-09-05.md)
