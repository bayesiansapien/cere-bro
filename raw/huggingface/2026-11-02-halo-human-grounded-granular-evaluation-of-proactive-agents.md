---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.499336+05:30
arxiv_id: 2610.39086
url: https://huggingface.co/papers/2610.39086
arxiv_url: https://arxiv.org/abs/2610.39086
date: 2026-11-02
---

# HALO: Human-Grounded Granular Evaluation of Proactive Agents

Proactive agents must decide whether, when, and how far to assist without an explicit request. Existing evaluations often rely on automated scores or binary verdicts, offering limited human diagnosis of evidence use and intervention quality. To address these gaps, we introduce HALO, Human-Grounded GrAnular EvaLuation of PrOactive Agents. HALO-Arena covers 4 proactive need types, Dependency, Blockage, Risk, and Opportunity, across 10 everyday domains and 50 personal environments. Scenarios require agents to retrieve evidence from structured databases or unstructured documents before judging whether assistance is warranted and choosing its scope. On HALO-Arena, we construct HALO-8K, a dataset of 8,000 responses from 10 models across 400 scenarios, annotated by 20 experts for action level, acceptability verdicts, and human diagnosis. For rejected responses, human diagnosis covers timing, intensity, and other issues. Recorded reasoning tokens and retrieval rounds measure the effort behind these responses. The best proprietary and open-source models achieve 72.88% and 56.63% acceptability, respectively. Our central finding is that over-proactivity is the dominant observed failure mode, with Premature timing or Excessive intensity accounting for 61.20% of rejected responses. Further analyses yield complementary findings on the balance between intervention and restraint, evidence acquisition, and the calibration of timing and intensity.
