---
source: farmer/huggingface
farmed: 2026-07-29T08:14:21.288961+00:00
arxiv_id: 2607.25572
url: https://huggingface.co/papers/2607.25572
arxiv_url: https://arxiv.org/abs/2607.25572
date: 2026-07-29
---

# Mapping CVEs to MITRE ATT&CK Techniques: A Curated Gold-Set Classifier and the Limits of LLM-Assisted Label Expansion

We present a reproducible pipeline for mapping Common Vulnerabilities and Exposures (CVEs) to MITRE ATT&CK Enterprise techniques from free-text vulnerability descriptions. Rather than relying on the CWE->CAPEC->ATT&CK derivation chain, whose table-expansion artifacts we quantify, we train a multi-label classifier on a curated gold dataset of 1,207 CVEs from expert MITRE Center for Threat-Informed Defense mappings. The resulting model approximately doubles recall@5 compared with a zero-shot embedding-similarity baseline and improves every ranking metric. We then investigate whether LLM-assisted labeling can extend the gold dataset. Initial experiments suggest contradictory conclusions: a single run indicates degraded performance, while averaging over five random seeds suggests a small gain. However, an independent replication and an expansion-size study (100--984 additional CVEs) show that the apparent improvement is an evaluation artifact. LLM-generated labels, with approximately 0.39 agreement with expert annotations, provide no reliable improvement at any expansion size and reduce rare-technique coverage at around 1,000 added CVEs (macro-F1 decreases by 0.04). The root cause is evaluation noise. Selecting checkpoints on a small test split effectively maximizes over many noisy evaluations, producing recall@5 differences of up to 0.05 between otherwise identical runs. Using a corrected protocol based on validation-split checkpoint selection, the gold-only model achieves recall@5 of (0.673 \pm 0.019), and repeating the decisive experiment confirms the null result for LLM expansion. A final scaling study shows that additional expert-curated data consistently improves performance, whereas LLM-labeled data does not, indicating that the classifier is limited by label quality rather than dataset size. All datasets, models, code, and training logs are publicly released.
