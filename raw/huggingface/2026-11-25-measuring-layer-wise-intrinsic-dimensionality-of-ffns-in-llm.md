---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32782
url: https://huggingface.co/papers/2611.32782
arxiv_url: https://arxiv.org/abs/2611.32782
date: 2026-11-25
---

# Measuring Layer-wise Intrinsic Dimensionality of FFNs in LLMs via PCA

Modern large language models (LLMs) keep the feed-forward network (FFN) intermediate width identical across every layer, a convention inherited from the original Transformer. Yet mechanistic work suggests layers at different depths do qualitatively different work, raising a natural question: are their capacity demands also non-uniform, and if so, can a fixed parameter budget be allocated more wisely than uniformly? To probe this, we apply principal component analysis (PCA) to the input of each FFN down-projection and measure, for every layer, its intrinsic dimensionality as the smallest number of principal components needed to reconstruct the activation up to a fixed cosine similarity. Scanning 58 open-weight LLMs spanning 14 families and 70M to 72B parameters, we find a recurring middle-heavy profile in which middle layers carry higher intrinsic dimensionality than edge layers; the profile is robust to the calibration corpus, even across English and Chinese, and is largely preserved through post-training fine-tuning. As a direct test that this signal is structurally meaningful, we use it to guide width pruning in a knowledge-distilled student under a matched parameter budget: the PCA-guided allocation outperforms the uniform-width convention by +2.3 points on Qwen3-8B and +2.5 on Qwen2.5-3B, while lower-dispersion teachers show smaller gaps (+0.9 on Gemma-3-4B, +0.5 on LLaMA-3-8B), and a budget-matched inverted control does worst on all four teachers. Across these four teachers, the size of the gap tracks how unevenly the teacher's intrinsic dimensionality is distributed across layers (a single-number summary we call σ_{99}), and the advantage persists through downstream supervised fine-tuning. Code is available at https://github.com/naver-ai/lidf.
