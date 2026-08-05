---
source: farmer/huggingface
farmed: 2026-08-05T09:04:08.705882+00:00
arxiv_id: 2608.03812
url: https://huggingface.co/papers/2608.03812
arxiv_url: https://arxiv.org/abs/2608.03812
date: 2026-08-05
---

# OmniPack: Unified Token Compression for Efficient Omni-modal Large Language Models

Omni-modal large language models (Omni-LLMs) have achieved remarkable performance on audio-visual understanding tasks, but processing long and highly redundant visual and audio token sequences incurs substantial computational overhead, demanding aggressive token compression for efficient deployment. Existing methods often degrade at low token budgets: pre-LLM compression may discard structurally important and globally distributed evidence, whereas inner-LLM compression often underexploits query-conditioned audio-visual collaboration. To address these limitations, we propose OmniPack, a training-free framework that coordinates structural compression before the LLM with task-relevant semantic refinement within the LLM. Before the LLM, OmniPack removes structural redundancy through modality-specific importance, global coverage, and similarity-aware merging. After sufficient multimodal interaction, it further consolidates diverse, task-relevant representations through textual guidance and audio-visual collaboration. Extensive experiments on five benchmarks with three Omni-LLM backbones demonstrate that OmniPack consistently achieves the best performance-efficiency trade-off across diverse retention ratios, outperforming all existing methods. Notably, on Qwen2.5-Omni-7B, OmniPack preserves 98.0% of the original performance while reducing FLOPs to 16.7%, and still retains 92.9% of the original performance with only 6.8% of the original FLOPs.
