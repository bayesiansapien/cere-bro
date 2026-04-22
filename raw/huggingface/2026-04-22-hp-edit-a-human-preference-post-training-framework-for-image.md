---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.19406
url: https://huggingface.co/papers/2604.19406
arxiv_url: https://arxiv.org/abs/2604.19406
date: 2026-04-22
---

# HP-Edit: A Human-Preference Post-Training Framework for Image Editing

Common image editing tasks typically adopt powerful generative diffusion models as the leading paradigm for real-world content editing. Meanwhile, although reinforcement learning (RL) methods such as Diffusion-DPO and Flow-GRPO have further improved generation quality, efficiently applying Reinforcement Learning from Human Feedback (RLHF) to diffusion-based editing remains largely unexplored, due to a lack of scalable human-preference datasets and frameworks tailored to diverse editing needs. To fill this gap, we propose HP-Edit, a post-training framework for Human Preference-aligned Editing, and introduce RealPref-50K, a real-world dataset across eight common tasks and balancing common object editing. Specifically, HP-Edit leverages a small amount of human-preference scoring data and a pretrained visual large language model (VLM) to develop HP-Scorer—an automatic, human preference-aligned evaluator. We then use HP-Scorer both to efficiently build a scalable preference dataset and to serve as the reward function for post-training the editing model.
