---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.21783
url: https://huggingface.co/papers/2610.21783
arxiv_url: https://arxiv.org/abs/2610.21783
date: 2026-10-19
---

# Learning to Think and Explore in 3D World

We study how vision-language models (VLMs) can learn to think and actively explore in 3D space. Instead of providing multi-view images, videos, or 3D representations to the model, we preserve the native visual encoding of VLMs, i.e., a single image, one at a time, just like humans, and treat the 3D representation only as an environment with which the model can interact through actions (e.g., move left) and observations (rendered images). Each rollout begins from an initial first-person view and a visual question. The model can then iteratively reason, navigate, and reorient its viewpoint before committing to a final answer. Following an initial trajectory-supervised finetuning, we apply reinforcement learning (RL) with rewards driven primarily by final-answer correctness. Crucially, RL provides no direct supervision over which viewpoints the model should visit or which exploration actions it should take. Instead, the model must learn an effective exploration policy solely from the extent to which its interactions improve performance. Across six 3D benchmarks, our model ACT3D achieves an average accuracy of 53.2% that improves its base Qwen model by 22.0% and surpasses proprietary Gemini 3.6 Flash. ACT3D also outperforms existing open-source 3D methods while using 50-70% fewer input frames, and generalizes to unseen domains with an average improvement of 5.9% over its supervised initialization. Further analysis reveals adaptive, question-conditioned exploration. Performance gains over the base model increase from 0.6% on questions answerable from the initial view to 16.3% on those requiring extensive exploration. ACT3D searches for occluded targets, avoids unnecessary exploration, and acquires complementary viewpoints for spatial comparisons. These findings demonstrate that outcome-based RL enables VLMs not only to reason over visual evidence, but also to learn when and how to acquire it.
