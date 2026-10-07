---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04047
url: https://huggingface.co/papers/2610.04047
arxiv_url: https://arxiv.org/abs/2610.04047
date: 2026-10-06
---

# Periscope: Extending Frozen Language Models Beyond Their Context Window

A language model reads long text in one quadratic forward pass, stops at the context window, and loses accuracy with length before reaching it. We ask whether the read can be factorized when deciding over a finite set: which document is relevant, which option is supported, which passage is the evidence. Periscope, a training-free inference method, arranges the N chunks of a text on a K{times}K grid with K{=}lceilNrceil and asks a frozen model the same question about K local spans of consecutive chunks and K strided spans that sample the whole text, reading the log-odds of every answer at one token. Each answer takes its best local and strided score, and scoring every chunk by its two spans gives an evidence map at no further cost, whose peak is the chunk behind the answer. Every probe is about sc tokens for a text of s tokens and chunk size c, so a window of W tokens reaches W^{2}/c tokens at s^{1.5} cost. The map replaces the long read. On LongBench v2, reading only the K chunks the map ranks highest, 9k tokens, matches the same model's best window read across windows from 32k to 1M tokens, and on InfiniteBench, where the median context is 150k tokens, it leads the best window read by 5 points. The same map ranks BRIGHT's long-document corpora with the best NDCG@10 of six methods. Each call caches only one probe, so a 27B model reads 4.5M-token contexts on one 80GB GPU, where a single pass would need 296GB of cache. A long read then needs a GPU that holds the model, not one that holds the text.
