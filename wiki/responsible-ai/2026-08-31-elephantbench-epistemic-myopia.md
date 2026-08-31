# Blind Men and the Elephant: ElephantBench and the Epistemic Myopia of LLMs

**Source:** [arXiv 2608.28478](https://arxiv.org/abs/2608.28478) · [HuggingFace](https://huggingface.co/papers/2608.28478) · Tencent · code at [github.com/Tencent/ElephantBench](https://github.com/Tencent/ElephantBench)
**Raw:** [raw/huggingface/2026-08-31-blind-men-and-the-elephant-probing-the-epistemic-myopia-of-l.md](../../raw/huggingface/2026-08-31-blind-men-and-the-elephant-probing-the-epistemic-myopia-of-l.md)
**Date ingested:** 2026-08-31

## TL;DR

Factual QA benchmarks almost all assume one canonical answer per question, which quietly makes an entire class of failure unmeasurable: what a model does when the world genuinely contains two credible, conflicting accounts of the same long-tail fact. ElephantBench measures it. The construction is the part worth copying. An auditable graph-based pipeline retrieves related documents from a **low-exposure** web corpus, finds naturally occurring disagreements between them, and converts those into multi-account QA records; every answer is verified against its originating documents and against authoritative public sources, then reviewed by human annotators. The result across 32 models: the strongest one recovers **both** accounts on only **52.4%** of questions, and on nearly all the rest it confidently produces one account and simply omits the other. Scaling model size and adding inference-time reasoning both improve recall and neither eliminates the incompleteness. Corpus analysis gives the mechanism: exposure imbalance in pretraining favours the dominant account, and greater minority-side exposure correlates with more complete recall.

## What makes it more than another benchmark

The failure mode is not hallucination and it is not a knowledge gap, which is why existing evals miss it. The model **has** the minority account somewhere, or at least had exposure to it, and produces a fluent, well-calibrated-sounding single answer anyway. There is no uncertainty signal on the output, because from the model's perspective there is no conflict, only the account that dominated its training distribution. That makes it invisible to confidence-based abstention, which is the standard mitigation for the adjacent problems.

The pipeline generalizes past this paper. Turning a long-tail corpus into source-traceable knowledge probes by mining naturally-occurring disagreement is a reusable recipe, and it produces benchmarks where every item carries its provenance, which is rare.

## Relation to prior wiki state

**It is a specific counterexample to the abstention direction the wiki recorded on 08-30, and the two should be held together.** Yesterday's digest identified three papers on one leaderboard all replacing a forced dense decision with a sparse one plus an explicit way to say "no answer", with [FedCC](../inference-efficiency/2026-08-30-fedcc-label-skew-distillation.md) letting the teacher decline rather than emit a confident wrong label under label-distribution skew. Abstention is a good default and ElephantBench shows its boundary. Abstention helps when the model knows it does not know. Epistemic myopia is the case where the model has no internal signal that anything is missing, so an abstention mechanism has nothing to fire on. **These are different failures needing different instruments**, and conflating them is how a system ships with a calibration story that does not cover its actual gap.

**The exposure-imbalance finding also connects to the data-pruning thread in a way neither literature has noticed.** [MCL (08-30)](../inference-efficiency/2026-08-30-mcl-concept-landscape-data-pruning.md) argued that scoring training samples in embedding space is mechanically wrong, because an embedding is a lossy summary produced by a model trained to discard detail, and that detail is exactly the rare concepts pruning was supposed to preserve; it built an explicit entity-event-attribute graph and selected greedily by concept coverage instead. ElephantBench measures the downstream symptom of exactly that loss: minority accounts of long-tail facts vanishing under exposure imbalance. **MCL is a candidate intervention for the failure ElephantBench measures, and ElephantBench is a candidate evaluation for the property MCL claims to preserve.** Neither paper knows about the other. That pairing is a clean, cheap experiment: prune a pretraining corpus with MCL's coverage objective, train, and score minority-account recall on ElephantBench against a random-pruning control.

## Gaps

1,094 questions is a small probe, and the construction deliberately targets a low-exposure corpus, so the absolute 52.4% figure describes a hard slice rather than general factual behaviour. Recovering "both accounts" treats disagreement as binary; real long-tail disagreement often has three or more positions with unequal support, and the metric would need rethinking there. The exposure analysis is correlational, run over corpus statistics rather than through a controlled intervention, so the causal claim that exposure imbalance produces the omission remains an inference.

## Related pages

- [responsible-ai](responsible-ai.md)
- [agent-benchmarks](../agentic-systems/agent-benchmarks.md)
- [MCL: concept-landscape data pruning (08-30)](../inference-efficiency/2026-08-30-mcl-concept-landscape-data-pruning.md)
- [Daily digest 2026-08-31](../daily-digest/2026-08/2026-08-31.md)
