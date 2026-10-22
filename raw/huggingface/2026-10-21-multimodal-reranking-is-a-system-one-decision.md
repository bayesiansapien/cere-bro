---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.646681
arxiv_id: 2610.28435
url: https://huggingface.co/papers/2610.28435
arxiv_url: https://arxiv.org/abs/2610.28435
date: 2026-10-21
---

# Multimodal Reranking Is a System One Decision

Multimodal rerankers are usually dedicated models: a vision-language model (VLM) is trained on retrieval data to score the candidates of a query. Scoring options is not specific to reranking. System One decision models such as Jev map a state and a typed question to one probability per option without generating text, and general models can make such decisions with little or no training. Reranking is one such decision, with the query and its candidates as the state and the candidates as the options. We therefore argue that a general VLM can serve as a multimodal reranker through System One decisions, and that decision tuning can improve its reranking. We ask a VLM one choice question over the top 16 candidates of a first-stage retriever and rank the candidates by the probabilities of their labels, read from one forward pass. On MMEB-V2 image retrieval, this choice scores 5.4 to 7.3 hit@1 above a yes/no question per candidate, and the yes/no question falls below the first stage. With the choice, zero-shot Qwen3.8-27B beats the supervised Qwen3-VL-Reranker-2B on all three benchmarks and comes within 1.6 points of Reranker-8B on each. It matches Reranker-8B on MMEB-V2 visual documents (84.79 vs. 84.78 nDCG@5), at 1.1 to 1.5 times its latency. JEV-27B-VL, the same backbone tuned on text decisions only, improves page reranking by 0.6 to 1.1 points, with gains on most tasks (sign test, p <= 0.017), and leaves natural images unchanged. The zero-shot model is larger than the supervised rerankers and of a newer generation, so these comparisons are confounded; we discuss this and other alternative views, and the experiments that would test the position.
