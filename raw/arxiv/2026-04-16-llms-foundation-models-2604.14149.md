---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.14149
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.14149
published: 2026-04-16
authors: Zheyu Zhang, Ziqi Pang, Shixing Chen
---

# One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding

**arXiv:** https://arxiv.org/abs/2604.14149
**Authors:** Zheyu Zhang, Ziqi Pang, Shixing Chen

## Abstract

arXiv:2604.14149v1 Announce Type: new  Abstract: Long video understanding is inherently challenging for vision-language models (VLMs) because of the extensive number of frames. With each video frame typically expanding into tens or hundreds of tokens, the limited context length of large language models (LLMs) forces the VLMs to perceive the frames sparsely and lose temporal information. To address this, we explore extreme video token compression towards \emph{one token per frame} at the final LLM layer. Our key insight is that heuristic-based compression, widely adopted by previous methods, is prone to information loss, and this necessitates supervising LLM layers into \emph{learnable} and \emph{progressive} modules for \emph{token-level compression} (LP-Comp). Such compression enables our VLM to digest 2x-4x more frames with improved performance. To further increase the token efficiency, we investigate \emph{frame-level compression}, which selects the frames most relevant to the queries via the internal attention scores of the LLM layers, named \emph{question-conditioned compression} (QC-Comp). As a notable distinction from previous studies, we mitigate the position bias of LLM attention in long contexts, \emph{i.e.}, the over-concentration on the beginning and end of a sequence, by splitting long videos into short segments and employing local attention. Collectively, our combined \emph{token-level} and \emph{frame-level} leads to an e\textbf{x}treme compression model for long video understanding, named \textbf{\name}, achieving a significantly larger compression ratio and enabling denser frame sampling. Our \name is finetuned from VideoChat-Flash with a data-efficient \emph{supervised compression tuning} stage that only requires 2.5\% of the supervised fine-tuning data, yet boosts the accuracy from 42.9\% to 46.2\% on LVBench and enhances multiple other long video benchmarks.
