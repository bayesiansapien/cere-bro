---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.148278+00:00
arxiv_id: 2611.24161
url: https://huggingface.co/papers/2611.24161
arxiv_url: https://arxiv.org/abs/2611.24161
date: 2026-11-19
---

# AVTR: Adaptive Multimodal Reasoning with Visual Imagination

Vision-Language Models increasingly rely on textual reasoning to solve advanced multimodal tasks. Despite its effectiveness, this paradigm faces two fundamental limitations. First, relying on textual reasoning alone can limit perceptual ability in vision-centric questions, where accurate answers depend on interpreting task-relevant visual evidence. Second, applying textual reasoning uniformly across inputs overlooks question-dependent variation in both reasoning modality and depth, often producing verbose and unnecessary traces when little logical inference is required. To this end, we propose Adaptive Visual-Textual Reasoning (AVTR), which introduces visual imagination as a complementary reasoning modality to textual thinking, enabling the model to revisit its visual observations and distill the salient evidence through generative visual reflection. Furthermore, we formulate reasoning-modality selection as a learned routing problem, allowing a single policy to adaptively harness the complementary strengths of visual reflection and textual reasoning in response to the perceptual and inferential demands of the input. Across 16 benchmarks, AVTR improves the average score by 4.5 points over Qwen3.5 baseline, while reducing inference latency by 33\%. It also scales effectively into a smaller size backbone, outperforming the evaluated 2B-scale baselines.
