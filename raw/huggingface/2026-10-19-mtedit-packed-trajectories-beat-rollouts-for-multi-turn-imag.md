---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23751
url: https://huggingface.co/papers/2610.23751
arxiv_url: https://arxiv.org/abs/2610.23751
date: 2026-10-19
---

# MTEdit: Packed Trajectories Beat Rollouts for Multi-Turn Image Editing

Multi-turn image editing aims to modify an image according to a sequence of instructions, making it better aligned with human-AI collaborative creation than single-turn editing. However, constructing high-quality multi-turn training data remains challenging, as conventional sequential rollout accumulates errors and introduces visual-quality drift across editing turns. To address this challenge, we introduce MTEdit, a multi-turn image editing dataset built through a pipeline centered on packed trajectory canvas (PTC) generation. By jointly generating multiple editing states within a unified visual context, this pipeline reduces visual-quality drift across turns. Covering both step-wise and context-aware editing scenarios, MTEdit comprises 500K multi-turn image editing trajectories, with up to 8 turns and an average of 5.38 turns per trajectory, making it one of the most extensive datasets for multi-turn image editing. We further introduce MTEdit-Bench, a benchmark designed to evaluate both scenarios by assessing models' ability to follow editing instructions, maintain content consistency, resist visual-quality drift, and effectively use historical context across turns. Using MTEdit, we fine-tune Qwen-Image-Edit-Causal to obtain Qwen-Image-MTEdit. On MTEdit-Bench, we evaluate a broad range of closed-source and open-source image editing models, including Qwen-Image-MTEdit. Experimental results show that Qwen-Image-MTEdit achieves the best performance among the evaluated open-source models, demonstrating the effectiveness of MTEdit in improving models' multi-turn image editing capabilities.
