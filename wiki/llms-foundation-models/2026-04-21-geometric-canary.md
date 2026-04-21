# Geometric Canary: Steerability and Drift Detection from Representational Geometry

**Date:** 2026-04-21  
**Source:** HuggingFace Daily Papers  
**Paper:** [arxiv 2604.17698](https://arxiv.org/abs/2604.17698)  
**Raw:** (HuggingFace Daily Papers feed)

---

## TL;DR

Geometric stability — how consistently a model's pairwise representation distances hold across inputs — predicts two distinct deployment properties depending on how supervision is applied. Task-aligned (supervised) stability predicts linear steerability with ρ=0.89–0.97. Unsupervised stability fails at steerability prediction but detects post-training drift earlier and with 6x fewer false alarms than CKA. A single metric, two lifecycle phases, two completely different applications.

---

## Key Findings

**The core measurement:** Geometric stability measures whether the pairwise distance structure of a model's representation space stays consistent. If two inputs that were "far apart" in the representation space yesterday are still far apart today after fine-tuning, the geometry is stable. If they've moved relative to each other, the geometry has shifted.

**Supervised stability → steerability prediction (pre-deployment):**
- Task-aligned Shesha variants achieve ρ=0.89–0.97 correlation with linear steerability
- Tested across 35–69 embedding models and three NLP tasks
- A model with stable task-aligned geometry can be controlled by linear probes (affine transformations of its hidden states)
- Practical use: run this before deploying to check whether the model will accept behavioral control at inference time

**Unsupervised stability → drift detection (post-deployment):**
- ρ~0.10 for steerability prediction — unsupervised stability tells you nothing about steerability
- But detects ~2x more geometric change than CKA (centered kernel alignment) during post-training alignment
- Provides earlier warning in 73% of models tested
- 6x lower false alarm rate than CKA for the same detection sensitivity
- Practical use: monitor this continuously post-deployment to catch alignment drift early

**The dissociation is the key finding.** The same underlying mathematical concept (geometric stability) has radically different predictive value depending on supervision. This is not a continuous spectrum — it is a genuine fork. Supervised: steerability signal. Unsupervised: drift signal.

---

## Relation to Prior Wiki Pages

- Connects to the broader theme of model deployment diagnostics. No prior wiki page specifically covers representation geometry as a monitoring tool.
- The steerability finding is relevant to ASGuard (04-19) — which identified specific attention heads as the locus of jailbreak vulnerability. If geometric stability predicts linear steerability, it may also predict susceptibility to activation-scaling interventions like ASGuard's.
- Drift detection use case connects to the safety monitoring discussion in llm deployment literature. A lightweight geometric metric that fires early warning is directly useful for production systems where model versions are updated frequently.

---

## Why It Matters

Production ML needs lifecycle tools that scale. Geometric stability delivers pre-deployment controllability assessment and post-deployment drift monitoring from a single lightweight metric family. No expensive benchmark runs at either phase — just geometric computation on the model's hidden states.

The 2x improvement over CKA in drift sensitivity, at 6x lower false alarms, is a strong practical result. CKA has been the field's standard for representation similarity measurement. If Shesha-unsupervised beats it on drift detection, it should become the default for alignment monitoring pipelines.

---

## Open Questions

- Does supervised geometric stability predict steerability for *instruction-following* behaviors beyond the three NLP tasks tested? The probe-based framing assumes linear relationships between representation geometry and behavioral outputs — which may break down for complex multi-turn behaviors.
- Can unsupervised geometric stability detect *targeted* alignment drift (e.g., a specific jailbreak variant emerging) or only global distributional shift?
- Is the ρ=0.89–0.97 correlation consistent across architecture families (encoder-only, decoder-only, MoE) or specific to the 35–69 embedding models tested?

---

## Related Pages

- [ASGuard: Activation-Scaling Jailbreak Defense](2026-04-19-asguard-activation-jailbreak-defense.md)
- [RL for LLMs](rl-for-llms.md)
