# Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations

**Date:** 2026-06-03
**Source:** HuggingFace Daily Papers
**arXiv:** [2605.27958](https://arxiv.org/abs/2605.27958)
**Tier:** 2 — Interpretability / safety, linear probes, deception detection

## TL;DR

Linear probes trained on LLM activations are increasingly pitched as deception detectors, reporting AUROC above 0.96 on clean benchmarks. This paper pressure-tests them across the Gemma 3 family (1B–27B) and diagnoses *why* they break rather than just noting that they do. It tests four hypotheses about how deception is encoded — a single linear direction, a multi-dimensional subspace, a convex conic hull, or an entropy proxy — using cross-domain transfer matrices, multi-dimensional probe analysis with permutation null baselines, entropy-residualization, and distractor evaluations across eight stylistic shifts. The findings reframe the whole "inverse scaling" worry: probes hit near-perfect AUROC (≥0.998) on clean data but collapse under stylistic shift; style-augmented probes recover near-perfect detection (mean AUROC 0.979–0.983) on unseen styles. The single-direction hypothesis is rejected (k=1 gets only 0.61–0.80), cross-domain transfer failure is geometric not layer-mismatch, the entropy-proxy hypothesis is rejected, and deception does not form a significant linear subspace per domain (k*=0) yet multi-dimensional probes (k≥5) recover the signal from distributed sub-threshold features. The punchline: probe fragility is distributional narrowness, not an architectural limit, and the scary "inverse scaling" pattern is a training-distribution artifact, not a real scale-dependent failure.

```
Clean benchmark:  probe AUROC ≥ 0.998  ────────►  looks solved
        │
   apply 8 stylistic shifts
        ▼
  AUROC COLLAPSES   ◄── fragility = distributional narrowness, NOT scale
        │
   retrain with style-augmented data
        ▼
  AUROC 0.979–0.983 on UNSEEN styles  (recovers at 4B AND 27B)

Geometry of deception:
  k=1 single direction ........ REJECTED (0.61–0.80)
  per-domain linear subspace ... k* = 0 (no significant subspace)
  entropy proxy ................ REJECTED (|ρ|≤0.454)
  distributed k≥5 features ..... RECOVERS the signal
```

## Key findings

1. **Clean-data success is an illusion of narrowness.** Near-perfect AUROC on clean benchmarks collapses under eight stylistic shifts; the probe learned the style distribution, not deception.
2. **Style augmentation fixes it, at every scale.** Style-augmented probes recover ~0.98 AUROC on unseen styles at both 4B and 27B, which is what proves the "inverse scaling" pattern is a training-distribution artifact, not a genuine scale phenomenon.
3. **Deception is not one direction.** The single-linear-direction story is rejected; so is the entropy-proxy story. There is no significant per-domain linear subspace, yet k≥5 multi-dimensional probes recover the signal from distributed sub-threshold features.
4. **Diagnose, don't just document.** Cross-domain transfer matrices localize the failure as geometric (the deception geometry differs across domains) rather than a layer-selection mistake.

## Relation to prior wiki state

This is a direct, sobering update to the [responsible-ai page](responsible-ai.md)'s probe/monitoring thread. [Monitoring the Internal Monologue via probe trajectories](2026-05-19-monitoring-internal-monologue-probe-trajectories.md) (05-19) and [The First Token Knows: hallucination detection](2026-05-08-first-token-knows-hallucination-detection.md) (05-08) both leaned on the premise that a clean linear readout of an internal state is a reliable safety signal. This paper says: not without distributional coverage. It is the empirical counterweight to the "operational variables are linear and steerable" optimism the [rl-for-llms page](../llms-foundation-models/rl-for-llms.md) recorded (the MIT superposition / steerable-manifold line, 05-03) — features may be linearly readable in-distribution while the readout shatters under style shift.

It sharpens the agent-oversight worry from [Emergent Languages in Populations of LM Agents](2026-06-01-emergent-languages-oversight-evasion.md) (06-01, agents inventing steganographic protocols to evade surface monitoring). If a probe trained on clean deceptive text already collapses under a benign style shift, an adversary deliberately shifting style is a far easier attack than learning a hidden code. Both papers land the same verdict from different angles: a monitor validated only on narrow clean data is not a monitor.

The geometry result (no single direction; distributed k≥5 features) also refines the [refusal-neuron / single-feature install](responsible-ai.md) findings: some safety-relevant concepts are single-direction (refusal), but deception is distributed. The interpretability toolkit cannot assume one geometry fits all behaviors.

## Research angle

1. **Adversarial style shift as a red-team standard.** The natural falsifier: report deception-probe AUROC under an adversarially chosen style distribution, not a fixed eight. Style augmentation that closes the held-out gap may still lose to adaptive shift.
2. **Why k* = 0 but k≥5 works.** The tension between "no significant linear subspace" and "multi-dimensional probes recover the signal from sub-threshold features" is the deepest open question: is deception a thin distributed manifold that null-baselines miss, and does it have shared structure across domains at all?
3. **Generalization of the artifact claim.** The paper argues inverse scaling is a distribution artifact for deception. Whether other reported inverse-scaling safety results (sandbagging, sycophancy probes) are the same artifact is a high-value replication target.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2605.27958)
- [HuggingFace page](https://huggingface.co/papers/2605.27958)
- Raw: [raw/huggingface/2026-06-03-pressure-testing-deception-probes-in-llms-scaling-robustness.md](../../raw/huggingface/2026-06-03-pressure-testing-deception-probes-in-llms-scaling-robustness.md)
- Concept page: [Responsible AI](responsible-ai.md)
- Related: [Monitoring Internal Monologue 05-19](2026-05-19-monitoring-internal-monologue-probe-trajectories.md) · [First Token Knows 05-08](2026-05-08-first-token-knows-hallucination-detection.md) · [Emergent Languages 06-01](2026-06-01-emergent-languages-oversight-evasion.md)
