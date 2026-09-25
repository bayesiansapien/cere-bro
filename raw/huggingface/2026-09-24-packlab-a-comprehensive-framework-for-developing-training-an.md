---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.23784
url: https://huggingface.co/papers/2609.23784
arxiv_url: https://arxiv.org/abs/2609.23784
date: 2026-09-24
upvotes: 10
authors: ["Donghao Zhou", "Jia-Hui Pan", "Fan Zhang", "Xingyuan Bu", "Shilong Li", "Xiaojie Gao", "Yun-Hui Liu", "Chi-Wing Fu", "Pheng-Ann Heng"]
---

# PackLab: A Comprehensive Framework for Developing, Training, and Evaluating MLLMs in Robotic Bin Packing

**Authors:** Donghao Zhou, Jia-Hui Pan, Fan Zhang, Xingyuan Bu, Shilong Li, Xiaojie Gao, Yun-Hui Liu, Chi-Wing Fu, Pheng-Ann Heng

**Upvotes:** 10

**Links:** [HuggingFace](https://huggingface.co/papers/2609.23784) · [arXiv](https://arxiv.org/abs/2609.23784)

Robotic bin packing requires long-horizon sequential decision-making, as each object placement affects the available space for subsequent packing. Existing methods primarily rely on hand-crafted geometric heuristics that optimize predefined objectives or reinforcement learning policies learned through trial and error over predefined training configurations. Despite recent advances in multimodal large language models (MLLMs) for this task, their potential for closed-loop sequential decisions across heterogeneous packing configurations remains underexplored. To address this gap, we introduce PackLab, a comprehensive framework for developing, training, and evaluating MLLMs for closed-loop robotic bin packing. PackLab-Suite provides a physics-based simulation platform for scalable generation of diverse training packing trajectories and evaluation of their physical outcomes. PackLab-VLM is a packing-specialized MLLM that understands the evolving object and container states to jointly select objects and predict placements in a closed-loop manner. PackLab-Bench provides standardized packing scenarios at multiple difficulty levels for systematic evaluation. Extensive experiments demonstrate that, on average, PackLab-VLM outperforms conventional packing heuristics, traditional reinforcement learning methods, and general-purpose MLLMs across object sets and container configurations, highlighting the potential of MLLMs for long-horizon robotic packing. The code, model, dataset, and benchmark are available at https://github.com/Correr-Zhou/PackLab .
