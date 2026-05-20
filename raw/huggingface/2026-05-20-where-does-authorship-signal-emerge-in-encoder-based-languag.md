---
source: farmer/huggingface
farmed: 2026-05-20T09:55:01.245641+00:00
arxiv_id: 2605.19908
url: https://huggingface.co/papers/2605.19908
arxiv_url: https://arxiv.org/abs/2605.19908
date: 2026-05-20
---

# Where Does Authorship Signal Emerge in Encoder-Based Language Models?

Authorship attribution models fine-tuned with the same pretrained encoder, data, and loss can differ four-fold in performance depending only on their scoring mechanism. We use mechanistic interpretability tools to explain this gap. Stylistic features such as word length, punctuation density, and function-word frequency are equally available at every layer in every model, including in an off-the-shelf control encoder, hence the gap not coming from representation quality. Instead, causal intervention shows that the scorer determines where the encoder consolidates authorship signal. Mean pooling forces consolidation by early to mid layers, while late interaction defers it to later layers. We further derive this difference from the gradient structure of each scorer, and training dynamics reveal distinct learning trajectories that follow from that difference.
