# Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and Lexical Diversity

**Source:** HuggingFace Daily Papers · arXiv [2608.13430](https://arxiv.org/abs/2608.13430)
**Raw:** [raw/huggingface/2026-08-16-are-you-sure-youre-sure-on-the-impact-of-instruction-tuning.md](../../raw/huggingface/2026-08-16-are-you-sure-youre-sure-on-the-impact-of-instruction-tuning.md)
**Topic:** calibration, instruction tuning, interpretability

## TL;DR

Instruction-tuned models are known to be verbally overconfident, meaning they say "I am certain" more often than they should. This paper asks whether that confidence shift comes with a matching change in the *rationales* the model writes to support its answers, and evaluates three matched base and instruction-tuned model pairs across question-answering benchmarks. Three findings. Instruction tuning **consistently alters answer confidence** while producing **limited changes in predictive accuracy** and **decreasing likelihood-based calibration**. Its effect on rationale diversity is **non-uniform**: cross-rationale diversity (how much two independently sampled explanations differ from each other) consistently *decreases*, while surface-level lexical diversity moves in both directions depending on the model and the benchmark. And both effects persist after controlling for answer selection and rationale length, so confidence and rationale diversity are measuring genuinely distinct consequences of instruction tuning rather than one artifact seen twice.

## Why it matters here

The clean version of the result is uncomfortable: the post-training step that makes a base model usable makes it **more confident, no more correct, and worse calibrated**. Confidence and accuracy are decoupled by the procedure, not by the data.

The rationale finding is the more interesting half and the less discussed one. Cross-rationale diversity collapsing means the instruction-tuned model converges on one way of explaining itself. Any method that treats agreement across sampled rationales as a proxy for correctness, which includes self-consistency voting and most rationale-based confidence estimation, is reading a signal that instruction tuning has quietly compressed. The traces agree more because the model has fewer ways of speaking, not because the answer got more reliable.

## Relation to prior wiki pages

**It puts a mechanism under a problem [CaRL (08-16)](../inference-efficiency/2026-08-16-carl-knowing-when-to-quit.md) has to solve.** CaRL, today's paper on aborting futile reasoning, finds universal capability overreach and systematic miscalibration between what a model can do and what it attempts, and spends an RL stage training the overconfidence back out. This paper identifies where a large part of that overconfidence was installed. One paper creates the debt in post-training, the other pays it down in post-post-training, and neither cites the other.

**It complicates self-consistency, which was already under attack this week.** [When Self-Consistency Backfires](http://arxiv.org/abs/2608.11403) sits at #1 on this week's Kurate cs.AI board, reporting that majority vote *hurts* on the majority of hard science problems for small LLMs. Two independent results, one measuring the aggregation rule and one measuring the diversity of the things being aggregated, both landing on the same conclusion that voting over sampled rationales is a weaker instrument than the field treats it as.

## Gaps

Three model pairs is a small sample for a claim about instruction tuning in general, and the paper does not report whether the effect scales with the size of the instruction-tuning corpus or with its composition. Nothing here separates preference optimization from supervised instruction tuning, which are usually stacked in practice and which plausibly contribute the confidence shift in different proportions.

## Related pages

- [Responsible AI](responsible-ai.md)
- [CaRL: Knowing When to Quit (08-16)](../inference-efficiency/2026-08-16-carl-knowing-when-to-quit.md)
- [RL for LLMs](../llms-foundation-models/rl-for-llms.md)
