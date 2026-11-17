---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.000791+00:00
arxiv_id: 2611.16378
url: https://huggingface.co/papers/2611.16378
arxiv_url: https://arxiv.org/abs/2611.16378
date: 2026-11-16
---

# Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents

Autonomous agents modify prompts, memories, tools, workflows, and policies using interaction histories. Yet a plausible modification is not necessarily suitable for persistent adoption: candidate selection is adaptive, evaluators may be imperfect, and local gains can hide degradation against an earlier baseline. We introduce Evidence-Governed Evolution (EGE), a framework for governing adoption of self-generated agent modifications. EGE separates candidate generation from confirmatory adoption, evaluates frozen candidates on fresh paired audits, requires meaningful improvement on a prespecified primary objective, protects declared capabilities through reference-relative non-inferiority tests, and applies governance constraints before bounded canary deployment. We establish an evaluator-calibrated simultaneous lower-bound construction for a countable sequence of adaptively generated candidates. It combines candidate-wise Hoeffding bounds with independent calibration samples comparing the operational evaluator with a prespecified reference procedure. We also formalise reference replacement through bridge tests, derive a cumulative degradation bound along a versioned reference lineage, and provide an audit-planning condition relating effect-size margin, sample sizes, and acceptance probability. A Monte Carlo stress test illustrates calibration under candidate-dependent evaluator optimism; it is a stylised statistical experiment, not an evaluation of a deployed agent. The guarantees are conditional on bounded paired scores, fresh sampling, a valid reference-evaluation construct, and declared evaluation distributions; they do not establish universal agent safety or robustness to arbitrary distribution shift.
