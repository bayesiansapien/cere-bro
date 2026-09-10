---
source: farmer/huggingface
farmed: 2026-09-10T08:36:11.637058+00:00
arxiv_id: 2609.07103
url: https://huggingface.co/papers/2609.07103
arxiv_url: https://arxiv.org/abs/2609.07103
upvotes: 6
date: 2026-09-10
---

# Revisiting Complete Reasoning Traces for Post-Training

Large language models (LLMs) are often post-trained on pre-collected reasoning trajectories to improve their reasoning capability. Such trajectories tend to be long due to complex, interwoven paths, which often include detours on the path toward the answer. However, it has been underexplored whether LLMs indeed benefit from learning complete trajectories in post-training, such as supervised fine-tuning (SFT). Starting from our pilot study, we find that full trajectories provide only limited benefit, while partial trajectories are effective even under heavy truncation. We analyze redundancy in reasoning trajectories through attention-based analyses and controlled token-removal studies, both of which show that intermediate tokens contribute minimally to final reasoning quality. This suggests that avoiding redundant information may allow LLMs to internally infer coherent alternatives by inferring missing steps from their internal knowledge, given known trajectory endpoints. Furthermore, we show that training LLMs using endpoints leads to consistent changes in reasoning behavior, and that it also benefits post-training methods based on reinforcement learning or on-policy distillation, highlighting the need to revisit complete reasoning traces. Code is available at https://github.com/naver-ai/revisiting-trace.
