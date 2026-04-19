# ASGuard: Mechanistic Defense Against Targeted Jailbreaking

**Date:** 2026-04-19  
**Source:** HuggingFace Daily Papers  
**Paper:** [arxiv 2509.25843](https://arxiv.org/abs/2509.25843)  
**Raw:** [raw/huggingface/2026-04-19-asguard-activation-scaling-guard-mitigate-targeted-jailbreaking.md](../../raw/huggingface/2026-04-19-asguard-activation-scaling-guard-mitigate-targeted-jailbreaking.md)

---

## TL;DR

ASGuard uses circuit analysis to identify specific attention heads responsible for refusal behavior, then trains a channel-wise activation scaling vector to harden those heads against targeted jailbreaks (e.g. tense-changing attacks that rephrase harmful requests in past tense). Preventative fine-tuning with this vector achieves Pareto-optimal safety/utility tradeoff across four LLMs.

---

## Key Findings

- **Tense-changing jailbreak**: models that refuse harmful requests in present tense often comply when the same request is rephrased in past tense — a surprisingly simple and effective attack
- **Mechanistic root cause**: adversarial suffixes suppress propagation of refusal-mediating activation directions in specific attention heads
- **Circuit analysis**: ASGuard identifies the exact attention heads causally responsible for the tense-vulnerable refusal path
- **Activation scaling**: a channel-wise scaling vector is trained to recalibrate those specific heads without touching the rest of the model
- **Preventative fine-tuning**: the scaling is applied as a fine-tuning signal, forcing the model to learn a more robust refusal mechanism
- **Results**: attack success rate drops across four LLMs; general capabilities and "helpfulness" preserved; less over-refusal than prior defenses

---

## Why It Matters

Most safety defenses work at the input level (filtering) or output level (classifier). ASGuard works at the mechanism level — it finds the exact circuit responsible for a vulnerability and repairs it surgically. This is the mechanistic interpretability approach applied to alignment, not just to understanding.

The tense-changing attack is a good stress test because it's a minimal transformation — the semantic content is identical, only the grammatical tense changes. A model that is truly aligned on the *concept* of harm should be robust to this. Models that aren't are revealing that their refusal is surface-pattern-matching, not semantic.

---

## Related Pages

- [RL for LLMs](rl-for-llms.md)
- [C2: Rubric-Augmented Reward Modeling](2026-04-18-c2-rubric-reward-modeling.md)
