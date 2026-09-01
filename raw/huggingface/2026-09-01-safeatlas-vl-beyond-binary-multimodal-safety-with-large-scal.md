---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.29098
url: https://huggingface.co/papers/2608.29098
arxiv_url: https://arxiv.org/abs/2608.29098
date: 2026-09-01
---

# SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Models

Multimodal safety moderation requires distinguishing risks arising from visual content, user intent, and assistant behavior. Existing safeguards, however, are typically trained for a single judgment target and reduce safety assessment to a binary decision. Consequently, risk becomes difficult to compare across a multimodal interaction, and ambiguous cases are obscured. We introduce SafeAtlas-VL, a dataset of 1.5M training instances that places image-, request-, and response-level judgments on a five-level ordered scale. We curate a broad collection of safety-relevant data from both real-world and synthetic sources and apply a disagreement-aware annotation procedure. The resulting dataset spans 15 harm categories and 55 fine-grained subcategories, covering a broad range of multimodal safety scenarios. We also construct SafeAtlas-Bench, a held-out set of 5,000 instances for evaluating five-level predictions and continuous risk scores. Upon this dataset, we train the SafeAtlas Guard series of models via target-conditioned tuning for multimodal safety detection. Our models not only perform five-way classification of safety levels but also map safety to continuous scores through a soft cumulative ordinal head. Experimental results demonstrate that guard models trained on our dataset exhibit strong generalization: even without using the training sets of other benchmarks, they achieve competitive performance on the corresponding test sets. Notably, our 8B model attains the overall best performance, outperforming the previous SOTA by approximately 4% in F1 score. Code, data, and models are released to support further research. Warning: this paper contains example data that may be offensive, harmful, graphic, or disturbing.
