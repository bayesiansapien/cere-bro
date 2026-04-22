---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.19550
url: https://huggingface.co/papers/2604.19550
arxiv_url: https://arxiv.org/abs/2604.19550
date: 2026-04-22
---

# LoopCTR: Unlocking the Loop Scaling Power for Click-Through Rate Prediction

Scaling Transformer-based click-through rate (CTR) models by stacking more parameters brings growing computational and storage overhead, creating a widening gap between scaling ambitions and the stringent industrial deployment constraints. We propose LoopCTR, which introduces a loop scaling paradigm that increases training-time computation through recursive reuse of shared model layers, decoupling computation from parameter growth. LoopCTR adopts a sandwich architecture enhanced with Hyper-Connected Residuals and Mixture-of-Experts, and employs process supervision at every loop depth to encode multi-loop benefits into the shared parameters. This enables a train-multi-loop, infer-zero-loop strategy where a single forward pass without any loop already outperforms all baselines. Experiments on three public benchmarks and one industrial dataset demonstrate state-of-the-art performance.
