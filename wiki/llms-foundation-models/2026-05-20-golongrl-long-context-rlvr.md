# GoLongRL: Capability-Oriented Long-Context Reinforcement Learning

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.19577](https://arxiv.org/abs/2605.19577) · [raw](../../raw/huggingface/2026-05-20-golongrl-capability-oriented-long-context-reinforcement-lear.md)

## TL;DR

A fully open-source, capability-oriented post-training recipe for long-context RLVR. Existing long-context RL methods treat data construction as designing complex retrieval paths, which leads to homogeneous task coverage and reward formulations that don't reflect real long-context needs. GoLongRL contributes two pieces. (1) **Capability-oriented data construction with full open release:** 23K RLVR samples plus the construction pipeline and training code. Guided by a taxonomy of long-context capabilities, the dataset spans 9 task types each paired with its natural evaluation metric. Under identical vanilla GRPO, the GoLongRL dataset alone outperforms the closed-source QwenLong-L1.5 dataset. A Qwen3-30B-A3B trained on this data delivers long-context performance comparable to DeepSeek-R1-0528 and Qwen3-235B-A22B-Thinking-2507. (2) **TMN-Reweight** for heterogeneous multitask optimization: task-level mean normalization for cross-task reward scale alignment plus difficulty-adaptive weighting. Improves average performance over vanilla GRPO without degrading general capabilities.

## Why it matters

Long-context performance has been mostly driven by data and continued pretrain. GoLongRL shows post-training RLVR on the right data can deliver 30B performance comparable to 235B thinking models. The dataset's full open release is the substantive contribution; the technique (TMN-Reweight) is a reasonable engineering refinement of GRPO.

## Connections

- **FocuSFT (2026-05-13)** and **MMProLong (2026-05-14)** worked on training-side long-context behavior at the SFT and continued-pretrain levels. GoLongRL is the RLVR analog at the post-training level. The three together form a complete training-side long-context recipe.
- **EndPrompt (2026-05-19)** extended context window via short-sequence training. GoLongRL trains at long context for capability. Different points on the long-context training surface.
