---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.14663
url: https://huggingface.co/papers/2604.14663
arxiv_url: https://arxiv.org/abs/2604.14663
date: 2026-04-20
---

# EdgeDetect: Importance-Aware Gradient Compression with Homomorphic Aggregation for Federated Intrusion Detection

Federated learning (FL) enables collaborative intrusion detection without raw data exchange, but conventional FL incurs high communication overhead from full-precision gradient transmission and remains vulnerable to gradient inference attacks. This paper presents EdgeDetect, a communication-efficient and privacy-aware federated IDS for bandwidth-constrained 6G-IoT environments. EdgeDetect introduces gradient smartification, a median-based statistical binarization that compresses local updates to {+1, -1} representations, reducing uplink payload by 32x while preserving convergence. We further integrate Paillier homomorphic encryption over binarized gradients, protecting against honest-but-curious servers without exposing individual updates. Experiments on CIC-IDS2017 (2.8M flows, 7 attack classes) demonstrate 98.0% multi-class accuracy and 97.9% macro F1-score, matching centralized baselines, while reducing per-round communication from 450 MB to 14 MB (96.9% reduction).
