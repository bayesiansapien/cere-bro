---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819301+00:00
arxiv_id: 2610.00812
url: https://huggingface.co/papers/2610.00812
arxiv_url: https://arxiv.org/abs/2610.00812
date: 2026-10-02
---

# Video Generation Models: A Survey of Post-Training and Alignment

Video generation has rapidly progressed from short, low-quality clips to high-resolution, long-duration sequences with complex spatiotemporal dynamics. Despite strong generative priors learned through large-scale pretraining, pretrained video models often fail to reliably follow human intent, maintain temporal coherence, or satisfy physical and safety constraints. Compared with image and text generation, alignment in video generation presents unique challenges, including error accumulation over time, motion-appearance coupling, multi-objective trade-offs, and limited supervision for temporal properties. These challenges motivate systematic post-training strategies that adapt pretrained models without retraining them from scratch. In this survey, we present the first comprehensive review of post-training and alignment in video generation models. We frame post-training as a unifying framework and distinguish between implicit alignment and explicit alignment based on how alignment signals are enforced. From this perspective, we organize existing approaches into four broad categories: supervised fine-tuning methods, self-training and distillation methods, preference- and reward-based methods, and inference-time methods. This taxonomy provides a coherent view of how alignment signals shape model behavior across both training and deployment. Beyond methodological advances, we review commonly used datasets, benchmarks, and evaluation practices, and discuss open challenges such as scalable reward design, long-horizon temporal consistency, stability-expressiveness trade-offs, and safety-aware generation. This survey aims to provide a structured conceptual foundation and practical guidance for advancing controllable and reliable video generation models.
