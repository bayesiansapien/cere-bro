---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.08614
url: https://huggingface.co/papers/2605.08614
arxiv_url: https://arxiv.org/abs/2605.08614
date: 2026-05-18
---

# DiagnosticIQ: A Benchmark for LLM-Based Industrial Maintenance Action Recommendation from Symbolic Rules

Monitoring complex industrial assets relies on engineer-authored symbolic rules that trigger based on sensor conditions and prompt technicians to perform corrective actions. The bottleneck is not detection but response: translating rules into maintenance steps requires asset-specific knowledge gained through years of practice. We investigate whether LLMs can serve as decision support for this rule-to-action step and introduce DiagnosticIQ, a benchmark of 6,690 expert-validated multiple-choice questions from 118 rule-action pairs across 16 asset types. We contribute (i) a symbolic-to-MCQA pipeline normalizing rules to Disjunctive Normal Form with embedding-based distractor sampling, (ii) five variants probing distinct failure modes (Pro, Pert, Verbose, Aug, Rationale), and (iii) a benchmark of 29 LLMs and 4 embedding baselines. A human evaluation (9 practitioners, mean 45.0%) confirms DiagnosticIQ requires specialist knowledge beyond operational experience. Three findings stand out. The frontier has closed: the top three LLMs lie within one Macro point. DiagnosticIQ Pro exposes brittleness, with every model losing 13-60% relative accuracy under distractor expansion. DiagnosticIQ Aug exposes pattern-matching: under condition inversion, frontier models still select the original answer 49-63% of the time. The deployment bottleneck is not capability but calibration: frontier models handle template-style fault detection but break under structural perturbation.
