---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.05833
url: https://huggingface.co/papers/2606.05833
arxiv_url: https://arxiv.org/abs/2606.05833
date: 2026-06-06
---

# Learning Geometric Representations from Videos for Spatial Intelligent Multimodal Large Language Models

Multimodal Large Language Models (MLLMs) excel at 2D semantic understanding but lack intrinsic 3D awareness, resulting in representations that fail to maintain geometric and spatial consistency across video frames. Given the scarcity of large-scale 3D data, we present GeoVR, a novel framework that learns geometric representations using purely 2D video sequences. This approach effectively restructures the semantic latent space within MLLMs to unlock spatial intelligence. Rather than employing superficial feature mixing, GeoVR reshapes the internal representations of the MLLM by distilling geometry knowledge from pre-trained 3D foundation models. This is accomplished through a multi-objective learning strategy driven by four complementary geometric targets: (1) estimating inter-frame camera poses to embed varying viewpoint dynamics, (2) regressing dense depth maps to anchor physical distances, (3) predicting a metric scale factor for real-world calibration, and (4) distilling multi-scale 3D features to align the intermediate feature space. Guided by these explicit physical and geometric constraints, the model's internal representations naturally develop strong 3D awareness. Extensive experiments on spatial reasoning benchmarks demonstrate that GeoVR achieves state-of-the-art performance, establishing a new paradigm for endowing foundation models with spatial intelligence.
