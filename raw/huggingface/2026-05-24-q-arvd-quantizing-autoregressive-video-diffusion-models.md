---
source: farmer/huggingface
farmed: 2026-05-24T05:07:38.368292+00:00
arxiv_id: 2605.21072
url: https://huggingface.co/papers/2605.21072
arxiv_url: https://arxiv.org/abs/2605.21072
date: 2026-05-24
---

# Q-ARVD: Quantizing Autoregressive Video Diffusion Models

Autoregressive video diffusion models (ARVDs) have emerged as a promising architecture for streaming video generation, paving the way for real-time interactive video generation and world modeling. Despite their potential, the substantial inference cost of ARVDs remains a major obstacle to practical deployment, making model quantization a natural direction for improving efficiency. However, quantization for ARVDs remains largely unexplored. Our empirical analysis shows that directly applying existing quantization schemes developed for standard diffusion transformers to ARVDs leads to suboptimal performance, revealing quantization behaviors that differ from those observed in bidirectional diffusion models. In this paper, we identify two critical challenges in quantizing ARVDs: (C1) Highly unbalanced frame-wise quantization sensitivity. Error accumulation during autoregressive generation can induce severely skewed quantization sensitivity across frames, following an exponential-like decay pattern. (C2) Prominent and heterogeneous outlier patterns in weights. Weight distributions exhibit pronounced outlier channels, whose patterns vary substantially across layer types and block depths. To address these issues, we propose Q-ARVD, a novel framework for accurate ARVD quantization. (S1) To tackle the highly unbalanced frame-wise sensitivity, Q-ARVD incorporates a final-quality aware frame-weighting mechanism into the quantization objective. (S2) To prevent heterogeneous outliers from degrading performance, Q-ARVD introduces an outlier-aware adaptive dual-scale quantization, which automatically detects the presence and quantity of outlier channels for an arbitrary layer, and isolates them to protect normal channels. Extensive experiments demonstrate the superiority of Q-ARVD.
