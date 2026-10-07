---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.06679
url: https://huggingface.co/papers/2610.06679
arxiv_url: https://arxiv.org/abs/2610.06679
date: 2026-10-06
---

# Closing the Context Gap: Activation Alignment for Tabular In-Context Learning

Tabular foundation models perform in-context learning (ICL) by conditioning predictions on labeled training examples provided as context. Unlike traditional models that separate training from inference, these models must process all training examples in every forward pass, making each prediction expensive. Restricting the number of training examples reduces this cost but substantially degrades performance. Instead of discarding context, we propose activation alignment, a method that leverages the full context to teach a model how to behave when seeing only a subset. This is achieved by training a lightweight linear transformation on synthetic unlabeled data to map the intermediate activations of a data-constrained "student" (using partial context) toward those of a full-context "teacher" (using all data). Training the aligner requires no GPU and converges in seconds to minutes on commodity hardware. We evaluate on 38 classification datasets from the TabArena benchmark using the leading two tabular foundation models, TabPFN-3 and TabFM. Across all context budgets, the aligned student yields broad, statistically significant improvements over the unaligned baseline for both models. In low-data regimes, alignment recovers nearly half of the teacher's predictive advantage. The method provides a practical, low-overhead approach to achieving the inference speed of compact contexts while closing a significant fraction of the performance gap to the full-context teacher.
