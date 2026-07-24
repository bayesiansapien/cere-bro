---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.21553
url: https://huggingface.co/papers/2607.21553
arxiv_url: https://arxiv.org/abs/2607.21553
date: 2026-07-24
---

# SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation

We introduce SANA-Video 2.0, a hybrid video diffusion transformer instantiated at 5B and 14B scales under a unified architecture. Designed to generate high-quality video up to 720p on a single GPU, SANA-Video 2.0 matches full-softmax video DiTs in quality while retaining the favorable long-sequence scaling of linear attention. To avoid quadratic attention throughout, Hybrid Linear-Softmax Attention combines gated linear attention for O(N)-dominated mixing with periodic gated-softmax anchors at a 3:1 ratio, restoring the full-rank token interactions that pure linear attention lacks. To propagate these refreshed representations across depth, Block Attention Residuals (AttnRes) route completed block summaries into later linear layers, enabling anchor-feature reuse and boosting deep-layer effective rank by ~12%. Through from-scratch training, SANA-Video 2.0 learns the complete hybrid directly rather than linearizing pretrained models, with reduced-resolution proxy studies establishing 25% softmax as the optimal quality-efficiency trade-off. With 40-step sampling, SANA-Video 2.0 achieves a VBench score of 84.30 in 13.2s at 480p on a single H100, remaining competitive with far larger softmax video DiTs at a fraction of the latency. Its compiled DiT forward pass is 3.2x faster than a matched full-softmax baseline at 720p/60s, a gap that expands with video duration. Furthermore, full-stack Sol-Engine optimization (kernel fusion, caching, and sparse attention) accelerates this hardware-friendly backbone by a further 3.58x, bringing the 5B pipeline to 13.06s at 720p/5s and making it 120x faster than Wan 2.2-A14B on one H100. Overall, our hybrid design recovers softmax-level expressiveness at substantially reduced cost, unlocking scalable long, high resolution video generation.
