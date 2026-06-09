---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.09809
url: https://huggingface.co/papers/2606.09809
arxiv_url: https://arxiv.org/abs/2606.09809
date: 2026-06-09
---

# Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting

AI evaluation results are produced at scale but reported inconsistently across leaderboards, model cards, benchmark papers, and company blogs. The cost is interpretive: readers cannot reliably compare results across sources, identify what a report omits, or trace an aggregate claim to its underlying evidence. Recent efforts address isolated components but leave three gaps: they cover only narrow slices of the evaluation lifecycle and do not compose into a single interpretable record; they specify static representations that do not differentiate the questions different stakeholders bring to the same evidence; and they remain proposals on paper, lacking the extraction infrastructure required for adoption at scale. We present , an operational reporting layer that composes benchmark metadata, evaluation run data, and model metadata into a unified record. We (1) derive a reporting schema from a structured review of 52 papers and 10 stakeholder interviews, (2) implement four interpretive signals (reproducibility, documentation completeness, provenance and risk, and score comparability), rendered through reader modes calibrated to research and non-research audiences, and (3) deploy a monitoring tool that applies  across 5,816 models, 635 benchmarks, and 101,843 results, surfacing systematic gaps in current reporting practice.
