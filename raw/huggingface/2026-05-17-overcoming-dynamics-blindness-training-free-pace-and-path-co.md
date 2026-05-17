---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.11459"
url: "https://huggingface.co/papers/2605.11459"
arxiv_url: "https://arxiv.org/abs/2605.11459"
date: 2026-05-17
---

# Overcoming Dynamics-Blindness: Training-Free Pace-and-Path Correction for VLA Models

Vision-Language-Action (VLA) models achieve remarkable flexibility and generalization beyond classical control paradigms. However, most prevailing VLAs are trained under a single-frame observation paradigm, which leaves them structurally blind to temporal dynamics. Consequently, these models degrade severely in non-stationary scenarios, even when trained or finetuned on dynamic datasets. Existing approaches either require expensive retraining or suffer from latency bottlenecks and poor temporal consistency across action chunks. We propose Pace-and-Path Correction, a training-free, closed-form inference-time operator that wraps any chunked-action VLA. From a single quadratic cost, joint minimization yields a unified solution that decomposes orthogonally into two distinct channels. The pace channel compresses execution along the planned direction, while the path channel applies an orthogonal spatial offset, jointly absorbing the perceived dynamics within the chunk window.
