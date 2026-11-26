---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.31752
url: https://huggingface.co/papers/2611.31752
arxiv_url: https://arxiv.org/abs/2611.31752
date: 2026-11-25
---

# Separating Measurement Failures from Defence Failures in Split Language-Model Privacy

Split-training privacy evaluations fail through distinct mechanisms. Evaluators can overlook an exposed gradient channel, align reconstructions against shifted labels, or deploy uncalibrated probes before testing a candidate defence, while calibrated attacks can also refute real defences. Separating these failure modes alters which claims survive. We conduct a retrospective evidentiary reanalysis across four split-LLM campaigns and two cross-cutting scope checks covering host key custody and variational mutual-information bounds, mapping every recorded claim to one of five admissibility states (breach, non-detection, undetermined coverage, invalid measurement, or out-of-scope inference). Across a 19-configuration exploration, only four of 24 required probes qualified, yet those four calibrated probes still established qualified privacy breaches in 13 configurations, while utility or learning-gain failures eliminated the remaining 6. In a seven-cell defence-redesign pilot, 2 quantised configurations failed utility gates, calibrated next-byte structure probes breached the 0.02 gate on all 7 cells (0.097 to 0.112), and qualified punctuation-property probes reached 0.79 to 0.89, yielding 4 failed and 3 undetermined composite privacy assessments (the latter from marginal null-band excursions on punctuation bindings). Negative evidence against both defence families remains intact. Scope checks further show that shared-key orthogonal wrappers protect passive network captures without hiding activations from a compromised restoring host, and why near-zero variational lower bounds leave worst-case leakage unconstrained. Rerunnable scripts verify 1,522 checks across 122 SHA-256-pinned artifacts while preserving each campaign's native seed intervals and retrospective boundaries.
