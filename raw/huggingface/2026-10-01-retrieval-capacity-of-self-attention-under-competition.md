---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.353321+05:30
arxiv_id: 2609.37879
url: https://huggingface.co/papers/2609.37879
arxiv_url: https://arxiv.org/abs/2609.37879
date: 2026-10-01
---

# Retrieval Capacity of Self-Attention Under Competition

How many tokens from its context does a language model actually use, and what determines that number? We study this question through self-attention. Without retraining, we retain only the tokens with the highest attention weights at each head, layer, and query, keeping their original weights unchanged. By varying the selected set size and measuring the increase in negative log-likelihood (NLL), we estimate the effective attention set size needed to stay within a chosen loss tolerance. Relatively small selected sets can keep NLL close to the full-attention baseline, although the required size varies across models. Attention-based selection substantially outperforms random selection. Selected sets exhibit geometric structure, although geometric separation alone does not establish that model loss is preserved. Extending context while evaluating the same prediction targets increases the required set size, while its fraction of context decreases over the tested range. Experiments with a fixed supporting fact show that additional background pushes its tokens down the attention ranking and reduces their attention mass. Renormalizing the retained weights can substantially reduce the required set size, showing that it also depends on how selected representations are combined. Conditional theoretical models explain how competition and attention-mass retention can produce growing set sizes without more distinct information to retrieve. These results provide a way to measure effective attention set size in language models and investigate its dependence on context, competition, and aggregation.
