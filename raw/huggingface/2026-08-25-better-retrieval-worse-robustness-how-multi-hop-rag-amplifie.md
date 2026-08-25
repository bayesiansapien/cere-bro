---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.22872
url: https://huggingface.co/papers/2608.22872
arxiv_url: https://arxiv.org/abs/2608.22872
date: 2026-08-25
upvotes: 3
authors: ["Zhenghua Bao"]
---

# Better Retrieval, Worse Robustness:How Multi-hop RAG Amplifies Upstream ASR Errors

**Upvotes:** 3
**Authors:** Zhenghua Bao

Speech-based applications pass spoken queries through automatic speech recognition (ASR) before any retrieval module, so ASR errors enter the pipeline as a fixed upstream constraint. We empirically test whether two extensions to standard retrieval-augmented generation (RAG), entity-graph linking and iterative reformulation, absorb or amplify these errors. Using four English accents synthesized through neural TTS, we evaluate four RAG configurations on three multi-hop QA benchmarks (HotpotQA, 2WikiMultiHopQA and MuSiQue) against a clean-text oracle. Although the structurally richer configurations generally retain higher absolute F1 under ASR input, both extensions amplify the error: the F1 gap from clean text to the highest-WER accent is 36-67% larger under their combination than under naive dense retrieval, on all three benchmarks. The dominant failure mode is corruption of one or more query entities, accounting for 87-96% of degradation cases on 2WikiMultiHopQA across all four methods. Two lightweight surface-form mitigations leave most of the gap intact, indicating that downstream retrieval structure amplifies remaining entity errors. We release code and data at https://github.com/ZhenghuaBao/spoken-multihop-rag .
