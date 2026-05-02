---
source: farmer/huggingface
farmed: 2026-05-02T00:00:00Z
arxiv_id: "2604.28157"
url: https://huggingface.co/papers/2604.28157
arxiv_url: https://arxiv.org/abs/2604.28157
date: 2026-05-02
---

# FlashRT: Towards Computationally and Memory Efficient Red-Teaming for Prompt Injection and Knowledge Corruption

Long-context large language models like Gemini-3.1-Pro and Qwen-3.5 power applications including retrieval-augmented generation and autonomous agents. However, security threats from prompt injection and knowledge corruption remain significant concerns. While optimization-based red-teaming methods produce stronger attacks than heuristic approaches, they demand substantial computational resources and GPU memory—particularly problematic for long-context scenarios and academic researchers.

FlashRT addresses this by being the first framework to improve the efficiency (in terms of both computation and memory) for optimization-based prompt injection and knowledge corruption attacks. The framework achieves 2x-7x speedup and reduces GPU memory consumption by 2x-4x compared to nanoGCG, with practical examples showing runtime reduction from one hour to under ten minutes and memory reduction from 264.1 GB to 65.7 GB for 32K token contexts. The approach applies broadly to black-box optimization methods like TAP and AutoDAN, with code made publicly available.
