---
source: raw/huggingface/2026-05-02-safety-drift-after-fine-tuning-evidence-high-stakes-domains.md
date: 2026-05-02
arxiv: https://arxiv.org/abs/2604.24902
---

# Safety Drift After Fine-Tuning: Evidence from High-Stakes Domains

## TL;DR

100 models analyzed — including deployed medical and legal models. Benign domain-specific fine-tuning causes large, heterogeneous, often *contradictory* changes in safety. A model frequently improves on some safety benchmarks while degrading on others simultaneously. Base-model safety evaluations don't predict post-fine-tuning safety. Current evaluation and accountability practices fail to capture downstream harms.

## Key findings

- Benign fine-tuning (no adversarial intent) induces substantial, unpredictable safety changes.
- Safety changes are **heterogeneous**: a model can improve on toxicity benchmarks while degrading on robustness benchmarks for the same fine-tuning run.
- Changes are often **contradictory**: improvement on one safety metric ≠ safety improvement overall.
- **Base-model safety assessment is inadequate** for managing risk in deployed high-stakes applications.
- Analysis spans 100 models including publicly available medical and legal domain variants.

## Implication

The current accountability assumption — "evaluate the base model, approve derivatives" — is broken. Fine-tuned variants in healthcare, legal, and financial domains carry safety profiles that are unpredictable from the base. Regulators and deployers who rely on base-model evals are flying blind.

## Relation to prior wiki knowledge

This is the first paper in the wiki to directly characterize safety as an *unstable property under benign fine-tuning*. Prior safety papers tracked adversarial attacks; this paper shows benign adaptation is enough to break the safety profile.

**Connects to Claude Security** (May 1, Industry Pulse): Anthropic launched Claude Security to give defenders the same offensive capabilities attackers have. The context matters: if fine-tuning degrades safety in unpredictable ways, every organization fine-tuning Claude for a domain is implicitly introducing new attack surface. Claude Security's "defenders need the same tools" pitch takes on more weight if fine-tuned variants are systematically less safe than the base.

**Connects to GPT-5.5 cyber tests** (May 1): frontier models matched in offensive capability evaluation. The safety-lifecycle problem is: train safe base → distribute → fine-tune → unknown safety profile at deployment. This paper is the empirical evidence that the unknown is large and contradictory.

## Open questions

1. Is the safety heterogeneity driven by dataset composition, learning rate, number of steps, or something structural about the domain?
2. Can post-fine-tuning safety be predicted from fine-tuning data statistics alone (without running full evaluations)?
3. What is the minimum "safety-maintenance" intervention during domain fine-tuning? Simple safety-objective regularization? Checkpoint mixing?

## Links

- Raw: [raw/huggingface/2026-05-02-safety-drift-after-fine-tuning-evidence-high-stakes-domains.md](../../../raw/huggingface/2026-05-02-safety-drift-after-fine-tuning-evidence-high-stakes-domains.md)
