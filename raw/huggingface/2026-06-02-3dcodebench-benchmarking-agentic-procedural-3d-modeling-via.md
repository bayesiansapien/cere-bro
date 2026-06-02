---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2606.01057
url: https://huggingface.co/papers/2606.01057
arxiv_url: https://arxiv.org/abs/2606.01057
date: 2026-06-02
---

# 3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code

Procedural 3D modeling through code is emerging as a versatile paradigm, offering deterministic, engine-ready, and precisely editable assets that neural 3D generators inherently lack. Authoring such procedural content, however, demands deep expertise in 3D software APIs, parametric design, and code-level geometric reasoning. In this paper, we propose 3DCodeBench, a systematic benchmark for evaluating vision-language model (VLM) agents for procedural 3D generation in 3D modeling software. Specifically, 3DCodeBench evaluates how effectively 12 advanced VLMs can serve as procedural 3D modelers by translating text and image references into procedural code for 3D modeling software. Recognizing that automated metrics may not fully capture the perceptual quality of 3D shapes, we build 3DCodeArena, a ranking platform based on pairwise human preferences over generated 3D outputs. From extensive evaluations and results, we observe that: (1) Failures mostly arise from API mismatches, while successful renders still suffer from disconnected or floating 3D geometric components. (2) Test-time scaling, such as higher thinking budgets and multi-turn refinement, improves performance overall. Our findings highlight a critical need for high-quality procedural coding data to advance commercial VLMs. Furthermore, effective procedural 3D modeling requires a robust execution environment that provides high-fidelity feedback for iterative refinement. We release 3DCodeBench, including the curated large-scale dataset of multimodal (text/image) prompts, procedural code, 3D object triplets, evaluation protocol, and the public 3DCodeArena platform as a foundational toolkit for exploring VLM-based procedural 3D modelers.
