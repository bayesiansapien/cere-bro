---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.15178"
url: "https://huggingface.co/papers/2605.15178"
arxiv_url: "https://arxiv.org/abs/2605.15178"
date: 2026-05-17
---

# SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer

We introduce SANA-WM, an efficient 2.6B-parameter open-source world model natively trained for one-minute generation, synthesizing high-fidelity, 720p, minute-scale videos with precise camera control. SANA-WM achieves visual quality comparable to large-scale industrial baselines such as LingBot-World and HY-WorldPlay, while significantly improving efficiency. Four core designs drive our architecture: (1) Hybrid Linear Attention combines frame-wise Gated DeltaNet (GDN) with softmax attention for memory-efficient long-context modeling. (2) Dual-Branch Camera Control ensures precise 6-DoF trajectory adherence. (3) Two-Stage Generation Pipeline applies a long-video refiner to stage-1 outputs, improving quality and consistency across sequences. (4) Robust Annotation Pipeline extracts accurate metric-scale 6-DoF camera poses from public videos to yield high-quality, spatiotemporally consistent action labels. Driven by these designs, SANA-WM demonstrates remarkable efficiency across data, training compute, and inference hardware: it uses only ~213K public video clips with metric-scale pose supervision, completes training in 15 days on 64 H100s, and generates each 60s clip on a single GPU; its distilled variant can be deployed on a single RTX 5090 with NVFP4 quantization to denoise a 60s 720p clip in 34s. On our one-minute world-model benchmark, SANA-WM demonstrates stronger action-following accuracy than prior open-source baselines and achieves comparable visual quality at 36x higher throughput for scalable world modeling.
