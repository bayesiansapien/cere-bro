---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349640+05:30
arxiv_id: 2609.39827
url: https://huggingface.co/papers/2609.39827
arxiv_url: https://arxiv.org/abs/2609.39827
date: 2026-10-01
---

# Synthetic Pre-pretraining Survives Scale, but Not as a Grammatical Prior

Pre-pretraining (PPT) on synthetic non-natural language data improves token efficiency during language model pre-training (PT). Prior work attributes this gain to a grammatical prior, i.e., a structural inductive bias learned during PPT that transfers to natural language grammar. However, PPT has only been tested on models of at most 1B parameters and PT budgets below 2B tokens on predominantly web text. It is unknown whether PPT is effective at larger scales and under more realistic PT data mixtures that combine diverse sources (e.g., code and math). We therefore present a comprehensive study on PPT spanning five PPT tasks, four PT data mixtures, four parameter scales (500M to 7B), and PT budgets of up to 100B tokens. Our results demonstrate that the downstream performance and token efficiency gains of PPT persist at scale, e.g., saving at least 21B PT tokens at the 3B scale. However, in contrast to prior work, we find no consistent evidence that these gains stem from a grammatical prior. Downstream performance does not consistently align with grammatical acceptability across model sizes. Instead, we find that downstream gains arise from PPT tasks that improve long-range retrieval. Finally, PPT performance gains are robust to how PT data mixtures are composed and diminish only when web text is absent. Overall, PPT is a low-cost addition to PT, and future PPT task design should target long-range retrieval rather than natural language grammar.
