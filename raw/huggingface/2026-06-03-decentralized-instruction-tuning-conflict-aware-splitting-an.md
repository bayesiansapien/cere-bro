---
source: farmer/huggingface
farmed: 2026-06-03T06:14:02Z
arxiv_id: 2606.01717
url: https://huggingface.co/papers/2606.01717
arxiv_url: https://arxiv.org/abs/2606.01717
date: 2026-06-03
---

# Decentralized Instruction Tuning: Conflict-Aware Splitting and Weight Merging

Instruction tuning aligns large language models, including multimodal ones, with diverse user intents, but scaling to heterogeneous mixtures is hindered by gradient interference and bandwidth-heavy synchronization. We ask whether these two bottlenecks can be addressed jointly by training parts of the mixture independently and reconciling them once in parameter space. We develop a local quadratic theory inside a shared flat basin that yields three results: weight merging produces a curvature-weighted variance reduction; PCA-aligned conflict splitting maximizes this gain along high-curvature directions; and merging additionally acts as spectral filtering with implicit norm regularization. These results directly motivate MERIT, a decentralized merge-ready instruction-tuning pipeline that estimates dataset-level gradient conflicts, partitions the mixture along the top PCA conflict axes, fine-tunes each partition independently with no inter-partition communication, and merges once via token-weighted averaging. On Qwen2.5-VL-3B with 136 Vision-FLAN tasks, MERIT improves the 8-benchmark average from 54.3 (joint training) to 57.0. The same recipe scales to a 7B model on a 1.6M-example, 176-source mixture -- matching or exceeding centralized joint training with minimal cost overhead -- and transfers to text-only FLAN. Our code is available at https://github.com/naver-ai/merit.
