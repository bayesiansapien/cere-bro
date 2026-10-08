---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.08463
url: https://huggingface.co/papers/2610.08463
arxiv_url: https://arxiv.org/abs/2610.08463
date: 2026-10-07
---

# UNREAL: Unifying Retrieval and Long-Context with a Single Model

Long-context inference and Retrieval-Augmented Generation (RAG) handle evidence selection at vastly different scales, from a single long prompt to an entire corpus. We ask whether a single model-internal mechanism can select evidence across this range. We introduce UNifying REtrieval And Long-Context with a Single Model (UNREAL), a model-native evidence selection framework to span corpus retrieval and long-context inference. UNREAL encodes chunks and derives retrieval queries directly from the frozen LLM's internal representations. It adds fewer than 500K trainable parameters and leaves the backbone unchanged. On a 3B-token, 21M-chunk Wikipedia index, all four dense and hybrid UNREAL backbones outperform state-of-the-art retriever-reranker systems. The best model raises recall from 49.1% to 73.2% on HotpotQA, from 31.7% to 60.1% on 2WikiMultiHopQA, and from 8.8% to 14.4% on MuSiQue. Applied to long-context tasks, the same selection mechanism removes distractors before generation, raising NoLiMa accuracy from 1.0% to 24.83% at its maximum context length of 128K tokens, and LV-Eval's F1 score from 49.97% to 54.66% at 256K. UNREAL also reduces FLOPs and time-to-first-token relative to full-context inference from roughly 32K tokens onward, with larger gains as context grows. Together, these results establish model-internal evidence selection as a common foundation for corpus retrieval and evidence-sparse long-context inference.
