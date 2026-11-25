---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.918319+00:00
arxiv_id: 2611.29338
url: https://huggingface.co/papers/2611.29338
arxiv_url: https://arxiv.org/abs/2611.29338
date: 2026-11-24
---

# A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation

Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced. We introduce nanoAstra, an approach to training vision-language models (VLMs) for generalizable manipulation that combines semantic action modeling with capability-preserving supervised fine-tuning (CP-SFT). nanoAstra represents robot behavior as semantic steps composed of reusable, parameterized action primitives, guided by explicit progress descriptions. Meanwhile, CP-SFT uses an explicit robot-specific system prompt to constrain manipulation outputs to a structured action space, aiming to focus adaptation on robot-specific contexts and promote specialization while minimizing interference with broader pretrained capabilities. With this formulation, we train nanoAstra on more than 5,000 hours of robot data together with general VQA data. On RoboTwin 2.0's randomized benchmark, nanoAstra-9B achieves a 17.8% zero-shot success rate, substantially outperforming advanced VLA and WAM baselines as well as similarly sized VLMs. With inference faster than the corresponding motion execution on a single H20 GPU, our model supports action-chunk-like streaming execution that overlaps inference with motion, reducing the robot's idle time from 35.0% to 6.9%.
