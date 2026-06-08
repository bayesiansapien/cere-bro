---
source: farmer/huggingface
farmed: 2026-06-08T09:23:13Z
arxiv_id: 2606.06891
url: https://huggingface.co/papers/2606.06891
arxiv_url: https://arxiv.org/abs/2606.06891
date: 2026-06-08
---

# Stream3D-VLM: Online 3D Spatial Understanding with Incremental Geometry Priors

Despite advances in 3D scene understanding, existing 3D Large Multimodal Models operate in offline settings, requiring complete scene observations or predefined video clips. In this paper, we present an online 3D vision-language model that enables real-time spatial understanding from streaming video. Our approach adopts an autoregressive streaming control modeling based on the LLM's next-token prediction objective to learn when to respond, and employs a lightweight Visual-Spatial Feature Integration (VSFI) module to incrementally inject temporally aligned geometry priors into the visual stream. To alleviate long-context decoding overhead, we propose a plug-and-play Geometry-Adaptive Voxel Compression (GAVC) module for efficient visual token compression. To address the scarcity of streaming 3D-language data, we further develop a scalable data generation pipeline that curates over 1M online spatio-temporal 3D QA pairs and establishes a comprehensive benchmark spanning 29 tasks. Extensive experiments show that our approach significantly outperforms both proprietary and open-source models across online and offline 3D spatial understanding, reasoning, and grounding tasks. The project page is available at https://stream3d-vlm.github.io/
