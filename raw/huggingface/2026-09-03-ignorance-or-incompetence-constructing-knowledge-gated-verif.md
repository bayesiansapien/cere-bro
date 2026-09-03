---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2608.30322
url: https://huggingface.co/papers/2608.30322
arxiv_url: https://arxiv.org/abs/2608.30322
date: 2026-09-03
---

# Ignorance or Incompetence? Constructing Knowledge-Gated, Verifiable Tasks for LLM Agents

Professional agent tasks often depend on conventions that are absent from public corpora, yet benchmarks rarely control whether an agent has access to those conventions. We introduce a knowledge-gated task-construction protocol that separates a task instruction from a compact artefact containing private conventions, reference tables, and utility operators. Construction-time provenance, byte-identical task instructions across the provided- and withheld-artefact conditions, leak audits, and executable witnesses make dependence on the artefact explicit and testable. Across fifteen calibration tasks, one frontier agent configuration achieves a 68.0% pass rate with the artefact and 0% without it; on one task, a plausible but incorrect artefact also yields 0% across five trials. Deterministic solvers and rule corpora provide exact ground truth for structured tasks, while named criterion-level rubrics support outputs that cannot be checked by a single executable oracle. A configuration-relative calibration screen retains seven tasks satisfying our five-trial empirical knowledge-gating screen. These experiments validate the behavior of the construction protocol; they do not establish that the retained tasks improve post-training. We publicly release part of the task suite and supporting tooling at https://github.com/DatagridsAI/Knowledge-Gated-Task-Construction.
