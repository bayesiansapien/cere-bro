---
source: farmer/huggingface
farmed: 2026-08-07T06:50:52.124211+00:00
arxiv_id: 2608.05137
url: https://huggingface.co/papers/2608.05137
arxiv_url: https://arxiv.org/abs/2608.05137
date: 2026-08-07
---

# SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding

Understanding 3D scenes is fundamental to embodied intelligence, requiring joint reasoning over heterogeneous information from multiple modalities, including visual and geometric cues. However, the relevance of these modalities often varies across queries. Existing Multimodal Large Language Models (MLLMs) typically rely on fixed modality combinations, overlooking query-dependent modality needs. Such a rigid design can introduce semantic noise from irrelevant modalities while underutilizing more informative ones, leading to wasted computation and diluted reasoning. To address these challenges, this paper proposes SmartMage, a unified MLLM that dynamically orchestrates heterogeneous modalities for semantic-aware 3D scene understanding. Specifically, SmartMage incorporates: (1) a Semantic-guided Modality Adaptive RouTng (SMART) module that selects task-relevant modalities using semantic priors, text-modality alignment, and modality quality; and (2) a Modality-Aware Gating Expert (MAGE) module that leverages modality priors to guide expert activation, fostering adaptive specialization in multimodal reasoning. Empirically, SmartMage achieves state-of-the-art performance across five 3D scene understanding benchmarks, and attains competitive results on RGB-only video understanding benchmarks. In our diagnostic benchmark ScanFacet, tasks are divided into fine-grained semantic categories, enabling analysis of modality combinations preferred by each semantic type. The observed modality-semantic patterns provide further evidence of SmartMage's effectiveness. Project page: https://yuecheong.github.io/SmartMage/.
