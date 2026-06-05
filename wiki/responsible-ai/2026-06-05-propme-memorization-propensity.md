# PropMe: LLMs Can Leak Training Data, But Do They Want To? A Propensity-Aware Evaluation of Memorization

**TL;DR.** Existing memorization audits mostly measure whether a model *can* be forced to reproduce training data (prefix-based capability attacks), not whether it *does* under ordinary use. PropMe separates the two: a propensity-aware framework that contrasts adversarial prefix attacks with non-adversarial prompting, plus a metric transformation that turns existing memorization functions into propensity metrics. It ships **SimpleTrace**, a lightweight infini-gram-based pipeline that deterministically attributes generations to training corpora and computes verbatim, near-verbatim, and propensity-transformed scores. On two fully-open models (Comma, DFM Decoder) across two datasets and two languages, it finds a consistent capability-propensity gap: prefix attacks elicit strong memorization, but propensity stays low, so models *can* reveal training data when directly elicited but rarely do so under common use. Memorization audits should report both worst-case extractability and ordinary leakage propensity.

**Source:** HuggingFace Daily Papers (upvotes: 5)
**arxiv:** [2606.06286](https://arxiv.org/abs/2606.06286)
**Raw:** [raw/huggingface/2026-06-05-llms-can-leak-training-data-but-do-they-want-to-a-propensity.md](../../raw/huggingface/2026-06-05-llms-can-leak-training-data-but-do-they-want-to-a-propensity.md)

## Key points

- **Capability vs propensity:** the central distinction. Worst-case extractability (can it be forced?) overstates real-world risk if ordinary-use leakage (does it happen unprompted?) is low.
- **Metric transformation:** a recipe that converts any existing memorization function into a propensity-aware version, so the field's metrics can be retrofitted rather than replaced.
- **SimpleTrace:** infini-gram-based deterministic attribution of generations to large training corpora; computes verbatim, near-verbatim, and propensity metrics.
- **Empirical gap:** prefix attacks elicit substantially stronger memorization than generic or dataset-specific prompts; propensity scores stay low overall. DFM Decoder (continually pre-trained from Comma) shows *reduced* memorization of Comma's data, evidence that later training on partially different data lowers memorization capability.

## Relation to prior wiki

A [responsible-ai](responsible-ai.md) measurement paper that sharpens how leakage risk should be reported. It rhymes with the broader 2026 theme that *how you measure* determines what you conclude, and complements [STRIDE (06-04)](../inference-efficiency/2026-06-04-stride-training-data-attribution.md), which attributes model behavior to training data via activation-space steering. PropMe and STRIDE are two angles on the same question (what did the model take from its training data); PropMe asks whether it leaks verbatim under realistic use, STRIDE asks which examples shaped a behavior. The finding that continued pre-training reduces memorization of earlier data is a useful, falsifiable mechanism for the unlearning/data-governance discussion.

## Related pages
- [responsible-ai.md](responsible-ai.md)
- [../inference-efficiency/2026-06-04-stride-training-data-attribution.md](../inference-efficiency/2026-06-04-stride-training-data-attribution.md)
