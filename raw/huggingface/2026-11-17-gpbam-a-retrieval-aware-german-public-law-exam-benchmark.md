---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.117241+00:00
arxiv_id: 2611.18981
url: https://huggingface.co/papers/2611.18981
arxiv_url: https://arxiv.org/abs/2611.18981
date: 2026-11-17
---

# GPBam: A Retrieval-Aware German Public Law Exam Benchmark

Legal reasoning in civil-law systems is not rule-lookup: the German state examination asks for a structured opinion (Gutachten) that names the governing norms, applies them to the facts, and argues to a conclusion. We introduce GPBam (German Public Law Bar-style Exam), 81 public-law examination cases with reference solutions, paired with a recitation task over 200 statutory provisions. Drawn from state examination preparation, the cases are broad and rarely repeat, and are not publicly available - we find no evidence of exact-solution memorisation in the models we evaluate, and keeping them private limits contamination. Because each reference solution's cited norms form a retrieval gold set over the very instances the essays are graded on, GPBam scores retrieval and long-form generation jointly, which makes it a benchmark for legal retrieval as well as for legal writing and lets us ask how much retrieval quality a legal opinion actually needs. Across 32 open-weight and proprietary models evaluated without retrieval, scores span 4.81-76.42 out of 100. Supplying the law helps modestly: across seven models and eight retrieval configurations, retrieval performance varies nearly threefold and buys at most 4.1 essay points, and nothing significant for three of the seven, while an oracle with 91% gold-norm recall improves scores by 2-6 points. Essay quality strongly tracks prior knowledge: verbatim statute recall, measured in a separate task, correlates at ρ= 0.92 over 32 models.
