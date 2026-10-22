---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.647472
arxiv_id: 2610.24452
url: https://huggingface.co/papers/2610.24452
arxiv_url: https://arxiv.org/abs/2610.24452
date: 2026-10-21
---

# HumanSkill-4D: Training-Free Language Querying of Animatable Gaussian Avatars in Space and Time

We introduce avatar referring segmentation, which selects regions of animatable Gaussian avatars from language queries. A query can also specify a pose or motion to select matching intervals. This lets users interact with avatars for local editing and motion inspection. However, making these selections with existing language Gaussian splatting methods poses two challenges: adjacent parts and garments are hard to separate and may be referred to indirectly (region ambiguity), while fine-grained motions can look alike in RGB (motion ambiguity). We address these challenges with HumanSkill-4D, a training-free framework that shares a multimodal large language model (MLLM) and geometric operators across avatars. For each avatar, a semantic memory links body-part and garment categories to persistent Gaussian regions and appearance descriptions. The MLLM uses category names and descriptions to select categories by appearance, relation, or function. To find matching intervals, it composes operators into programs that check query conditions on driving joint trajectories stored in a motion memory. These category choices and operator outputs make selections traceable, while composing or adding operators supports new motion conditions. To evaluate this task, we introduce three human-annotated benchmarks and show that HumanSkill-4D outperforms the baselines in part segmentation and 3D and 4D referring segmentation, with compact memories and only minutes of setup per avatar.
