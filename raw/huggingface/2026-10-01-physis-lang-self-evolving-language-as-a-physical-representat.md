---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349727+05:30
arxiv_id: 2609.40358
url: https://huggingface.co/papers/2609.40358
arxiv_url: https://arxiv.org/abs/2609.40358
date: 2026-10-01
---

# Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model

Video world models are expected to predict how the physical world evolves, yet they often produce visually plausible videos that violate basic physical principles. Existing approaches commonly assume that natural language is insufficient to represent the physical knowledge required for reliable generation, and therefore introduce additional visual, latent, numerical, or planning-based signals. We revisit this assumption and introduce Physis-Lang, a self-evolving framework that treats physical language as a shared and optimizable representation across data curation, model training, and video generation. Physis-Lang represents physical processes through language that describes their relevant entities, causes, interactions, governing principles, temporal evolution, and effects. To improve this representation, we construct PhysCapBench, which decomposes physical processes into atomic assertions and evaluates captions using recall and precision. An agentic loop iteratively analyzes assertion-level errors and refines the instruction used to produce physical captions. Physis-Lang further converts model deficiencies into textual descriptions and uses language-guided retrieval to identify visually diverse videos that cover missing physical processes. Experiments on four widely used physical video benchmarks with Wan and Cosmos backbones demonstrate consistent improvements in physical plausibility. Notably, starting from open-source Cosmos3-Nano backbones, our Physis-Lang-enhanced models surpass the leading proprietary Veo 3.1 model.
