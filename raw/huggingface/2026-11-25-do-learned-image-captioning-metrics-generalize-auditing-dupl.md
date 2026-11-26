---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.30488
url: https://huggingface.co/papers/2611.30488
arxiv_url: https://arxiv.org/abs/2611.30488
date: 2026-11-25
---

# Do learned image captioning metrics generalize? Auditing duplicated samples in human-judgment benchmarks

Learned image captioning metrics are trained and tested on human judgments, so their reported correlation is a claim about generalization. We audit this claim for the three most recent collections of such judgments, Polaris, Nebula, and Spica, matching images at the pixel level. First, test samples reappear in training sets: the Spica training set contains about two-thirds of the Polaris test set, with identical human ratings. Second, controlled retraining shows that duplicates can inflate a metric: for Pearl, the gain is confined to the duplicated samples and grows with every epoch; for DENEB, it stays below one point. The gain depends on the learner and on how often a training set repeats a sample. Third, Kendall's τ over all samples is the sum of two terms, detecting captions with the lowest human score and ranking the others; the first supplies most of the reported correlation and is nearly saturated. The recent test sets cannot order Polos, DENEB and Pearl consistently, and a ridge regression on frozen features matches or exceeds all three. Fourth, we propose a protocol that ranks a learned metric only with a model trained without test samples, reports both terms, and compares metrics by paired tests. Under it, zero-shot vision--language judges rank first on the three recent test sets, and a fine-tuned judge ranks first on the three earlier benchmarks. The same analysis applies to any evaluator learned from human judgments; filter lists and code are released at https://github.com/morninghut/ic-dataset-audit .
