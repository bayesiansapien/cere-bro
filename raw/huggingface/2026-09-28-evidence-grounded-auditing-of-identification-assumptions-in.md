---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.600608+00:00
arxiv_id: 2609.30867
url: https://huggingface.co/papers/2609.30867
arxiv_url: https://arxiv.org/abs/2609.30867
date: 2026-09-28
---

# Evidence-Grounded Auditing of Identification Assumptions in Climate-Policy Causal Evaluations

Difference-in-differences (DID) studies are widely used to evaluate climate policy, but assessing the evidence supporting their identification assumptions remains challenging. We introduce ARGUS, a structured language-model pipeline that audits reported evidence against an eleven-dimension assumption-implication-evidence rubric and abstains when relevant evidence cannot be retrieved. We evaluate ARGUS using injected flaws, economics papers, and a small pilot with reconciled labels. On the 11-flaw benchmark, ARGUS detects 73% of planted flaws, compared with 18% for a keyword-based pipeline. Across 26 economics papers, ARGUS abstains on about 40% of paper-dimension assessments for lack of retrievable evidence. In a five-paper pilot with labels reconciled by two annotators, it assigns a higher risk level than the labels on 25 of the 33 assessments it completes. A rule fixed before the labels arrived removes most of this in-sample; weighted agreement stays low. ARGUS provides evidence-linked risk reports that localize potential weaknesses for expert review, without adjudicating causal claims. Code and data: https://github.com/yonghongzhang-io/ARGUS
