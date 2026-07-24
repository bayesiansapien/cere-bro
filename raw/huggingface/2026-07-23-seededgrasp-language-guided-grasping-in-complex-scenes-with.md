---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.20207
url: https://huggingface.co/papers/2607.20207
arxiv_url: https://arxiv.org/abs/2607.20207
date: 2026-07-23
---

# SeededGrasp: Language-Guided Grasping in Complex Scenes with Multiple Embodiments

Practical robotic grasping in complex scenes requires both 3D spatial reasoning and alignment with task-specific requirements. Vision-language models (VLMs) offer a natural way to specify these requirements using language, but existing approaches either use a VLM to predict the grasp directly with limited spatial awareness, or train the VLM together with the grasping model, which requires significantly more data and compute. These limitations impede performance and have prevented scaling to multiple embodiments in complex scenes. We address this by proposing SeededGrasp, a novel data-efficient framework that enables a VLM to predict a seed point to be used as conditioning for a subsequent lightweight grasp-generation model. Our architecture decouples high-level semantic reasoning from low-level geometric execution, enabling multi-embodiment support while bypassing the need for expensive end-to-end training. To enable training such models, we release the first multi-embodiment tabletop grasping dataset comprising over 2.5M grasps in cluttered scenes. Experimental results demonstrate that our approach outperforms existing baselines, achieving 72% success in simulation and 78% in real-world grasping experiments. See our project site for data and code: https://uoft-isl.github.io/seeded-grasp/
