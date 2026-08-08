---
source: farmer/huggingface
farmed: 2026-08-08T23:44:03.927649
arxiv_id: 2608.05802
url: https://huggingface.co/papers/2608.05802
arxiv_url: https://arxiv.org/abs/2608.05802
date: 2026-08-08
---

# On-Policy Delta Distillation for Multilingual Math Reasoning

On-Policy Distillation (OPD) is emerging as a promising alternative to reinforcement learning for LLM post-training, yet its effectiveness in multilingual settings remains underexplored. We study OPD and its advanced variant, On-Policy Delta Distillation (OPD^2), for mathematical reasoning in English, Korean, and Japanese. OPD^2 improves OPD by using the probability gap between a post-trained teacher and its base model as the learning signal. Experiments with Qwen3 show that OPD^2 consistently outperforms the original OPD, with particularly strong improvements in Korean and Japanese, and generally narrows the English-Korean performance gap. We further find that English-only OPD can also increase performance for Korean and Japanese, but often shifts the responses toward English, highlighting the importance of multilingual data to preserving target-language responses.
