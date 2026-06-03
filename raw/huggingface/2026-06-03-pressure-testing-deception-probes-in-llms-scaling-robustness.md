---
source: farmer/huggingface
farmed: 2026-06-03T06:14:02Z
arxiv_id: 2605.27958
url: https://huggingface.co/papers/2605.27958
arxiv_url: https://arxiv.org/abs/2605.27958
date: 2026-06-03
---

# Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations

Linear probes trained on LLM activations are increasingly proposed as deception-detection metrics, yet report AUROC exceeding 0.96 on clean benchmarks while collapsing under distributional shift. This paper systematically pressure-tests probe-based metrics across the Gemma 3 model family (1B-27B parameters), diagnosing why they fail rather than merely documenting that they fail. We test four hypotheses about deception encoding: (1) single linear direction, (2) multi-dimensional subspace, (3) convex conic hull, (4) entropy proxy. Our design includes cross-domain transfer matrices, multi-dimensional probe analysis with permutation null baselines, entropy-residualization tests, and distractor evaluations across 8 stylistic shifts. We find that: (a) probes achieve near-perfect AUROC (>=0.998) on clean data but collapse under stylistic shifts; style-augmented probes recover near-perfect detection (mean AUROC 0.979-0.983) on unseen styles; (b) the single-direction hypothesis is rejected (k=1 captures only 0.61-0.80 AUROC), with cross-domain transfer failure confirmed as geometric rather than layer-mismatch-driven; (c) the entropy-proxy hypothesis is rejected (max |rho|=0.454, max Delta-AUROC after residualization=0.004); and (d) deception does not form a significant linear subspace (per-domain k*=0), yet multi-dimensional probes (k>=5) recover the signal through distributed sub-threshold features. Probe fragility reflects distributional narrowness rather than an architectural limitation: style-augmented probes recover near-perfect detection at both 4B and 27B, establishing that the inverse scaling pattern is a training-distribution artifact rather than a genuine scale-dependent phenomenon.
