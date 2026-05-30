---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.23235
url: https://huggingface.co/papers/2605.23235
arxiv_url: https://arxiv.org/abs/2605.23235
date: 2026-05-30
---

# Convex Low-resource Accent-Robust Language Detection in Speech Recognition

Globalization and multiculturalism continue to produce increasingly diverse speech varieties. Yet current spoken dialogue systems frequently fail on under-represented dialects and accents, often misidentifying the input language and causing cascading failures in downstream dialogue tasks. Addressing this dialectal variance under low-resource constraints remains an open challenge, as standard fine-tuning is computationally expensive and prone to overfitting on high-dimensional speech data. We propose Convex Language Detection (CLD), a novel framework that integrates theoretically grounded convex optimization techniques into the spoken dialogue systems pipeline. Our method is efficiently implemented via multi-GPU Alternating Direction Method of Multipliers (ADMM) in JAX, thus providing global optimality guarantees and fast training in polynomial time. Theoretically, we prove that our convex objective induces certified margin stability and provide guarantees against feature perturbations. Empirically, we demonstrate sample efficiency and robustness to input dialectical variation, achieving 97-98% accuracy in challenging low-resource regimes. Our open-source package is available at https://pypi.org/project/jaxcld/
