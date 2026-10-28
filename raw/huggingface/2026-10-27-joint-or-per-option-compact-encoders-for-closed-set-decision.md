---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.30970
url: https://huggingface.co/papers/2610.30970
arxiv_url: https://arxiv.org/abs/2610.30970
date: 2026-10-27
---

# Joint or Per-Option? Compact Encoders for Closed-Set Decisions from 17 Million to 1 Billion Parameters

Many language-model pipelines end in a closed-set decision, such as selecting a tool. Prompting a large language model for it is slow and order-sensitive. We ask how small an encoder for such decisions can be and whether it should read the options jointly or separately. In a three-seed study at 32 million parameters, per-option scoring beats joint scoring on a held-out sample of a 37-benchmark decision suite by 5.8 points of chance-corrected skill at matched optimizer steps and by 2.8 at approximately matched training compute; two external benchmarks agree, though not significantly on their unseen tasks. Crossing reader with initialisation shows that the advantage requires a reranker initialisation, whose query-candidate pair input matches per-option reading; from the raw encoder the two readers are indistinguishable. Per-option scoring needs 5 to 13 times more encoder passes: at most twice the median latency, but more than four times the mean. Of six released joint encoders (17 million to 1 billion parameters), the 68- and 150-million-parameter models exceed a 435-million-parameter DeBERTa-v3 zero-shot classifier by 4.9 and 5.9 accuracy points on 209 overlap-audited System1-Arena tasks and are at least on par with it on the 145 tasks unseen in training. The smallest answers a median request in 14 milliseconds on 16 processor threads, against 728 for the classifier. Reordering options changes 12 to 23% of the joint models' answers (per-option scoring: none). Up to 68 million parameters, they lead their size range on a public leaderboard's private, mainly in-distribution tests.
