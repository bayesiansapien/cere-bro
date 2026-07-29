---
source: farmer/huggingface
farmed: 2026-07-29T08:14:21.288961+00:00
arxiv_id: 2607.25669
url: https://huggingface.co/papers/2607.25669
arxiv_url: https://arxiv.org/abs/2607.25669
date: 2026-07-29
---

# OmniDelta: Skill-Driven Budget Allocation for Token Compression in OmniLLMs

Emerging Omni-modal Large Language Models (OmniLLMs) enable unified understanding of text, audio, and video, but their long audio-video token sequences introduce substantial memory and inference costs. Existing compression methods mainly focus on selecting important tokens under fixed budgets, leaving the preceding budget-allocation problem underexplored. We show that direct query-to-audio/video similarity is unreliable for inter-modal budget allocation, and that uniform intra-modal budgets can miss key evidence while retaining redundant content. To address these limitations, we propose OmniDelta, a training-free, skill-driven framework that couples intent-aware inter-modal allocation with content-aware intra-modal allocation. OmniDelta first constructs audio and video skill pools to shift the fixed retained-token budget according to query demand, then reallocates modality budgets over audio segments and video frames using local complexity and temporal redundancy. The resulting local budgets can be combined with existing pruning strategies, preserving the total retained-token ratio while changing where the budget is spent. Experiments on four audio-video benchmarks with two Qwen2.5-Omni models show that OmniDelta establishes a new accuracy-efficiency Pareto frontier across pruning ratios. At 25% token retention on Qwen2.5-Omni-7B, OmniDelta reduces GPU memory by 22.0% and achieves a 1.64x end-to-end speedup over full-token inference.
