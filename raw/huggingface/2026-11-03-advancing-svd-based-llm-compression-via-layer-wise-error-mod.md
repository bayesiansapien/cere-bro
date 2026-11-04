---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.32878
url: https://huggingface.co/papers/2610.32878
arxiv_url: https://arxiv.org/abs/2610.32878
date: 2026-11-03
---

# Advancing SVD-based LLM Compression via Layer-Wise Error Model Search

Low-rank SVD-based compression offers a powerful strategy to reduce the computational costs of LLMs. However, existing methods face two key limitations: (i) global rank allocation, where uncalibrated error proxies fail to capture complex error propagation, and (ii) decomposition quality, where Fisher-based estimators suffer from severe rank collapse. In this work, we address these limitations by introducing Layer-wise Error Modeling Search (LEMS) and KFAC-SVD. LEMS advances rank allocation by introducing a layer-wise error surrogate that integrates local and global layer importance alongside a propagation bias, enabling effective global rank allocation via an ILP formulation. KFAC-SVD improves decomposition quality by utilizing token-wise statistics, mitigating the rank deficiency observed in prior Fisher-based SVD approaches. Across Mistral, Qwen3, and Llama 3 model families, we show that LEMS consistently outperforms existing search strategies, delivering significant zero-shot accuracy gains of up to 4.8 p.p. that generalize to model sizes of 70B parameters, while KFAC-SVD achieves an average perplexity improvement of 15%. Project page and code: https://lems-svd.github.io
