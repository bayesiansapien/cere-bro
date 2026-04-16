---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13453
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13453
published: 2026-04-16
authors: Xinjin Li, Jinghan Cao, Mengyue Wang
---

# FAST: A Synergistic Framework of Attention and State-space Models for Spatiotemporal Traffic Prediction

**arXiv:** https://arxiv.org/abs/2604.13453
**Authors:** Xinjin Li, Jinghan Cao, Mengyue Wang

## Abstract

arXiv:2604.13453v1 Announce Type: new  Abstract: Traffic forecasting requires modeling complex temporal dynamics and long-range spatial dependencies over large sensor networks. Existing methods typically face a trade-off between expressiveness and efficiency: Transformer-based models capture global dependencies well but suffer from quadratic complexity, while recent selective state-space models are computationally efficient yet less effective at modeling spatial interactions in graph-structured traffic data. We propose FAST, a unified framework that combines attention and state-space modeling for scalable spatiotemporal traffic forecasting. FAST adopts a Temporal-Spatial-Temporal architecture, where temporal attention modules capture both short- and long-term temporal patterns, and a Mamba-based spatial module models long-range inter-sensor dependencies with linear complexity. To better represent heterogeneous traffic contexts, FAST further introduces a learnable multi-source spatiotemporal embedding that integrates historical traffic flow, temporal context, and node-level information, together with a multi-level skip prediction mechanism for hierarchical feature fusion. Experiments on PeMS04, PeMS07, and PeMS08 show that FAST consistently outperforms strong baselines from Transformer-, GNN-, attention-, and Mamba-based families. In particular, FAST achieves the best MAE and RMSE on all three benchmarks, with up to 4.3\% lower RMSE and 2.8\% lower MAE than the strongest baseline, demonstrating a favorable balance between accuracy, scalability, and generalization.
