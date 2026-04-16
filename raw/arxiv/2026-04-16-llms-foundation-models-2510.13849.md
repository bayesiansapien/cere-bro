---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.13849
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.13849
published: 2026-04-16
authors: Andrey Goncharov, Nikolai Kondusov, Alexey Zaytsev
---

# Language steering in latent space to mitigate unintended code-switching

**arXiv:** https://arxiv.org/abs/2510.13849
**Authors:** Andrey Goncharov, Nikolai Kondusov, Alexey Zaytsev

## Abstract

arXiv:2510.13849v3 Announce Type: replace-cross  Abstract: Multilingual Large Language Models (LLMs) often exhibit hallucinations such as unintended code-switching, reducing reliability in downstream tasks. We propose latent-space language steering, a lightweight inference-time method that identifies language directions via Principal Component Analysis (PCA) on parallel translations and steers token embeddings along these axes to control language identity. Our approach mitigates code-switching while preserving semantics with negligible computational overhead and requires only minimal parallel data for calibration. Empirically, we achieve 95-99\% language classification accuracy using a single principal component and reduce next-token distributional divergence by up to 55\% across multiple language pairs on Qwen2.5 and Llama-3.2 models. Generation-based evaluation on Llama-3.2 further demonstrates 63--99\% reduction in Code-Switching Index across four language pairs ($p < 0.001$). We further analyze the layer-wise evolution of language representations, revealing that language identity concentrates in final layers with near-perfect linear separability.
