---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.995068+05:30
arxiv_id: 2602.10657
url: https://huggingface.co/papers/2602.10657
arxiv_url: https://arxiv.org/abs/2602.10657
date: 2026-10-28
---

# The Lexical Imprint of Pre-training Data

How much of zero-shot benchmark accuracy is captured by word-level alignment between a pre-training corpus and the benchmark target? We study this question through word-level unigram cross-entropy (UCE), a tokenizer-agnostic, model-free measure of lexical alignment between a reference corpus and a target benchmark. Likelihood training shapes the model's predictive distribution from the pre-training corpus, and zero-shot scores under likelihood-based evaluation depend in part on the lexical alignment between that corpus and the benchmark target. Cleanly tracing how the lexical imprint of pre-training data scales with corpus--benchmark alignment requires controlled from-scratch pre-training that varies corpus identity while holding the training recipe fixed. Across this controlled sweep, spanning 10 zero-shot benchmarks, 4 pre-training corpora, and 3 model scales, we find that corpus--benchmark lexical alignment, UCE, consistently tracks zero-shot accuracy on every benchmark, with corpora more aligned with the benchmark (lower UCE) achieving higher accuracy. The same signal extends from measurement to control at finer scopes. At the document level, strengthening the imprint by selecting training documents to maximize lexical alignment with the benchmark produces the accuracy gains predicted by the mechanism. At the prompt level, matching the imprint per prompt by routing each prompt to the drafter whose domain corpus is most lexically aligned with it produces measurable throughput gains over a generalist-drafter baseline. Taken together, pre-training corpora leave a measurable lexical imprint on base-model zero-shot behavior, and UCE provides a model-free probe of lexical alignment between reference and target data.
