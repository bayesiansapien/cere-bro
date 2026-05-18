---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.15824
url: https://huggingface.co/papers/2605.15824
arxiv_url: https://arxiv.org/abs/2605.15824
date: 2026-05-18
---

# FashionChameleon: Towards Real-Time and Interactive Human-Garment Video Customization

FashionChameleon is a real-time and interactive framework that enables human-garment customization in autoregressive video generation, allowing users to interactively switch garments during generation while maintaining coherent human motion. The framework consists of three key technical contributions: (1) Teacher Model with In-Context Learning that trains on reference images paired with garment images, enabling the model to implicitly preserve coherence during single-garment switching; (2) Streaming Distillation with In-Context Learning that introduces in-context teacher forcing to eliminate data-intensive ODE initialization and employs gradient-reweighted distribution matching distillation to improve consistency in long-video extrapolation; and (3) Training-Free KV Cache Rescheduling that enables interactive multi-garment video customization through garment KV refresh, historical KV withdraw, and reference KV disentangle mechanisms while preserving coherent human motion. The method achieves real-time 720p video generation at 23.8 FPS on a single H200 GPU and is evaluated on a newly proposed HGC-Bench benchmark, demonstrating superior performance over existing baselines.
