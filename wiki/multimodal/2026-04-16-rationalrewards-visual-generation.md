---
date: 2026-04-16
source: huggingface
arxiv: 2604.11626
---

# RationalRewards: Reasoning Rewards Scale Visual Generation at Training and Test Time

**TL;DR:** Teaching reward models to produce explicit multi-dimensional critiques before scoring (via PARROT — Preference-Anchored Rationalization) turns them into active optimization tools. At training time they provide structured RL rewards; at test time a Generate-Critique-Refine loop improves outputs without any parameter updates, matching or exceeding RL fine-tuning on several benchmarks.

## Key Findings

- Standard reward models collapse human preference to a single scalar — discarding the reasoning that drives the preference.
- **PARROT**: recovers high-quality rationales from preference data without rationale annotations via anchored generation, consistency filtering, and distillation.
- **RationalRewards (8B)**: state-of-the-art among open-source reward models, competitive with Gemini-2.5-Pro, using 10–20× less training data.
- **Training time**: structured rationales provide fine-grained RL rewards — outperforms scalar alternatives.
- **Test time**: Generate-Critique-Refine loop matches or exceeds RL fine-tuning on several benchmarks — no parameter updates needed.
- Key insight: structured reasoning can unlock latent capabilities in existing generators that suboptimal prompts fail to elicit.

## Related Pages

- [Video Generation](video-generation.md)
- [Seedance 2.0](2026-04-16-seedance-2-video-generation.md)
- [../llms-foundation-models/rl-for-llms.md](../llms-foundation-models/rl-for-llms.md)

**Raw source:** [../../raw/huggingface/2026-04-16-rationalrewards-reasoning-rewards-scale-visual-generation-bo.md](../../raw/huggingface/2026-04-16-rationalrewards-reasoning-rewards-scale-visual-generation-bo.md)
